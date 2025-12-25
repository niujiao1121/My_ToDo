# 实现变更说明

## 问题描述

根据问题陈述，需要解决以下三个问题：

1. **Milestone 创建**：AI创建的TODO虽然有ddl和标签，但无法根据ddl时间筛选todo，需要创建milestone才能时间筛选
2. **子TODO默认创建**：希望在某个todo下的某个comment创建的todo，可以默认作为这个todo的子todo创建
3. **直接新建issue问题**：若直接新建一个issue的方式使用ai一句话生成，事实上并没有反应

## 实现方案

### 1. Milestone 自动创建功能

**实现位置**：`.github/workflows/ai-create-todo.yml`

**变更内容**：
- 在创建 Issue 之前，检查任务是否有截止日期（`due_date`）
- 如果有截止日期且任务类型是 `task-with-deadline`：
  - 生成 Milestone 标题格式：`YYYY-MM-DD Deadline`
  - 查找是否已存在相同日期的 Milestone
  - 如果存在，复用该 Milestone
  - 如果不存在，创建新的 Milestone，设置截止日期为 `due_date + 23:59:59`
  - 将创建的 Issue 关联到 Milestone
- 在成功消息中添加 Milestone 信息

**好处**：
- 用户可以在 Issues → Milestones 页面查看按截止日期分组的任务
- 可以使用 Milestone 过滤器快速找到特定日期的任务
- 相同截止日期的任务自动归类到同一个 Milestone
- 提高任务管理的时间维度可视化

### 2. 自动父子任务关联（/todo 命令）

**实现位置**：`.github/workflows/ai-create-todo.yml`

**变更内容**：
- 添加 `autoParentIssue` 变量来跟踪自动检测的父任务
- 当通过 `issue_comment` 事件触发（即使用 `/todo` 命令）时：
  - 自动将 `sourceIssueNumber`（评论所在的 Issue）设置为 `autoParentIssue`
- 在 AI 解析完成后，如果：
  - `autoParentIssue` 存在（从评论触发）
  - 且 AI 没有识别出明确的父任务（`parsedData.parent_issue` 为空）
  - 则使用 `autoParentIssue` 作为父任务
- 这样可以实现：用户在任何 Issue 下使用 `/todo` 命令，创建的任务自动成为该 Issue 的子任务

**好处**：
- 简化用户操作，不需要在每个 `/todo` 命令中显式指定父任务
- 更符合用户直觉：在某个任务下创建的子任务，自然应该属于这个任务
- 仍然支持显式指定父任务（如果用户在输入中指定了父任务，AI 识别的优先级更高）

### 3. 修复直接创建 Issue 的问题

**实现位置**：`.github/workflows/ai-create-todo.yml`

**变更内容**：
- 当通过 `issues` 事件触发时（直接创建新 Issue）：
  - 添加 HTML 注释清理逻辑：`userInput.replace(/<!--[\s\S]*?-->/g, '').trim()`
  - 提取 "我要做的事" 部分的内容：使用正则表达式 `/##\s*我要做的事\s*\n+([\s\S]+?)(?=\n##|\n---|$)/i`
  - 这样可以正确提取模板中用户填写的实际内容，忽略模板的说明和注释

**问题原因**：
- AI 模板包含大量 HTML 注释（`<!-- ... -->`）作为使用说明
- 如果不清理这些注释，AI 会尝试解析整个模板内容，导致解析混乱或失败
- 通过清理注释和提取目标内容，确保 AI 只处理用户输入的实际任务描述

**好处**：
- 用户可以直接使用 AI 模板创建新 Issue，工作流会正确触发
- 提取的内容更纯净，AI 解析更准确
- 保留了模板中的使用说明，不影响用户体验

## 技术实现细节

### Milestone 创建逻辑

```javascript
// 如果有截止日期，创建或查找对应的 Milestone
let milestoneNumber = null;
if (parsedData.due_date && taskType === 'task-with-deadline') {
  try {
    const milestoneTitle = parsedData.due_date + ' Deadline';
    
    // 查找现有 Milestone
    const { data: existingMilestones } = await github.rest.issues.listMilestones({
      owner: context.repo.owner,
      repo: context.repo.repo,
      state: 'open'
    });
    
    const existingMilestone = existingMilestones.find(m => m.title === milestoneTitle);
    
    if (existingMilestone) {
      milestoneNumber = existingMilestone.number;
    } else {
      // 创建新 Milestone
      const { data: newMilestone } = await github.rest.issues.createMilestone({
        owner: context.repo.owner,
        repo: context.repo.repo,
        title: milestoneTitle,
        due_on: parsedData.due_date + 'T23:59:59Z',
        description: '截止日期为 ' + parsedData.due_date + ' 的任务集合'
      });
      milestoneNumber = newMilestone.number;
    }
  } catch (error) {
    // Milestone 创建失败不影响 Issue 创建
    core.warning('创建或查找 Milestone 失败：' + error.message);
  }
}
```

### 自动父任务检测逻辑

```javascript
// 获取用户输入时
let autoParentIssue = null;
if (context.eventName === 'issue_comment') {
  sourceIssueNumber = context.payload.issue.number;
  autoParentIssue = sourceIssueNumber; // 自动设置父任务
}

// AI 解析后
if (autoParentIssue && !parsedData.parent_issue) {
  parsedData.parent_issue = autoParentIssue.toString();
  core.info('自动设置父任务为: ' + autoParentIssue);
}
```

### 模板内容提取逻辑

```javascript
if (context.eventName === 'issues') {
  userInput = context.payload.issue.body || '';
  // 清理模板中的注释
  userInput = userInput.replace(/<!--[\s\S]*?-->/g, '').trim();
  // 提取"我要做的事"部分的内容
  const contentMatch = userInput.match(/##\s*我要做的事\s*\n+([\s\S]+?)(?=\n##|\n---|$)/i);
  if (contentMatch) {
    userInput = contentMatch[1].trim();
  }
}
```

## 测试建议

请参考更新后的 `TESTING_GUIDE.md`，其中包含了详细的测试用例：

1. **Milestone 测试**：
   - 创建带截止日期的任务，验证 Milestone 自动创建
   - 创建相同日期的多个任务，验证 Milestone 复用
   - 通过 Milestone 筛选任务
   
2. **自动父任务测试**：
   - 在 Issue 下使用 `/todo` 命令，验证自动父子关系
   - 显式指定父任务，验证优先级
   
3. **直接创建 Issue 测试**：
   - 使用 AI 模板直接创建新 Issue
   - 验证工作流正确触发和内容提取

## 向后兼容性

所有变更都是增量的，不会破坏现有功能：

- ✅ 原有的父任务指定方式（"属于 #X"、"是 #X 的子任务"等）仍然有效
- ✅ 不带截止日期的任务仍然正常创建（不会创建 Milestone）
- ✅ 显式指定父任务的优先级高于自动检测
- ✅ Milestone 创建失败不会影响 Issue 创建
- ✅ 现有的 Issue 模板和工作流程不受影响

## 文档更新

- ✅ 更新 `README.md`：添加新功能说明
- ✅ 更新 `TESTING_GUIDE.md`：添加详细测试用例
- ✅ 所有变更都有中文注释和说明

## 总结

此次实现完整解决了问题陈述中提出的三个问题，增强了 AI TODO 管理系统的易用性和功能性：

1. **时间维度管理**：通过自动创建 Milestone，用户可以更好地按时间筛选和管理任务
2. **层级关系简化**：通过自动父子任务关联，减少用户输入，提高效率
3. **稳定性提升**：修复了直接创建 Issue 的问题，确保所有创建方式都能正常工作

所有实现都遵循了最小化修改原则，保持了代码的可维护性和向后兼容性。
