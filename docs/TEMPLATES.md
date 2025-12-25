# Issue模板使用指南

本文档说明如何使用各种Issue模板创建和管理TODO任务。

## 📝 可用模板

### 1. 项目/大型任务模板 (Project Template)

**用途**: 创建大型项目或主要任务线

**适用场景**:
- 启动新的产品开发
- 大规模重构计划
- 季度/年度目标
- 跨部门协作项目

**使用方法**:
1. 点击 "New Issue"
2. 选择 "项目/大型任务" 模板
3. 填写项目概述、时间规划、关键里程碑
4. 添加 `project` 标签和适当的优先级标签

**示例**:
```markdown
标题: [PROJECT] 电商平台V2.0升级
标签: project, priority:high
Milestone: 2024 Q1
```

---

### 2. 有截止日期的任务模板 (Task with Deadline)

**用途**: 创建有明确截止日期的任务

**适用场景**:
- 版本发布前必须完成的功能
- 有时间约束的需求
- 计划在特定时间点完成的工作
- 关键路径上的任务

**使用方法**:
1. 选择 "有截止日期的任务" 模板
2. **必填**: 设置截止日期
3. **必填**: 关联到相应的Milestone
4. 填写验收标准和任务清单
5. 添加 `task-with-deadline` 标签和优先级标签

**示例**:
```markdown
标题: [TASK] 实现用户认证API
标签: task-with-deadline, priority:high
截止日期: 2024-02-15
Milestone: MVP版本
```

**最佳实践**:
- ✅ 设置合理的缓冲时间
- ✅ 明确具体的验收标准
- ✅ 如果任务复杂，分解为多个子任务
- ❌ 避免设置过于激进的截止日期

---

### 3. 开放性任务模板 (Open Task)

**用途**: 创建没有固定截止日期的任务

**适用场景**:
- 技术债务
- 代码优化
- 性能改进
- 文档完善
- 探索性研究
- "有时间就做"的任务

**使用方法**:
1. 选择 "开放性任务" 模板
2. 说明任务动机和预期价值
3. 评估重要性和紧急性
4. 建议合适的开始时机
5. 添加 `task-open` 标签

**示例**:
```markdown
标题: [OPEN] 优化数据库查询性能
标签: task-open, priority:medium
重要性: 高
紧急性: 低
建议时机: 下次版本发布后，有空闲时间时处理
```

**最佳实践**:
- ✅ 说明为什么这个任务值得做
- ✅ 给出优先级建议
- ✅ 定期（如每月）回顾开放性任务
- ❌ 避免创建过多低价值的开放性任务

---

### 4. 子任务模板 (Subtask)

**用途**: 创建隶属于父任务的子任务

**适用场景**:
- 将大任务分解为小任务
- 并行开发的模块
- 独立可交付的工作单元
- 需要单独跟踪的步骤

**使用方法**:
1. 选择 "子任务" 模板
2. **必填**: 在"Parent Issue"字段填写父任务编号
3. 描述子任务的具体目标
4. 添加 `subtask` 标签
5. 在父Issue中添加子任务清单

**示例**:
```markdown
标题: [SUBTASK] 实现JWT token生成
标签: subtask
Parent Issue: #123 (用户认证系统)
```

**父子关系管理**:

在子任务中：
```markdown
## 🔗 父任务
**Parent Issue**: #123
```

在父任务中：
```markdown
## 📝 子任务列表
- [ ] #124 实现JWT token生成
- [ ] #125 实现token验证中间件
- [ ] #126 实现token刷新机制
```

**最佳实践**:
- ✅ 子任务应该是1-5天可完成
- ✅ 子任务可以独立交付和验证
- ✅ 完成子任务后，更新父任务清单
- ❌ 避免子任务嵌套超过3层

---

## 🎨 模板自定义

### 修改现有模板

1. 编辑 `.github/ISSUE_TEMPLATE/*.md` 文件
2. 修改模板内容
3. 提交并推送更改

### 创建新模板

1. 在 `.github/ISSUE_TEMPLATE/` 创建新的 `.md` 文件
2. 添加YAML front matter：
```yaml
---
name: 模板名称
about: 模板描述
title: '[PREFIX] '
labels: ['label1', 'label2']
assignees: ''
---
```
3. 添加模板内容

## 🔄 工作流示例

### 示例1：新功能开发

```
步骤1: 创建项目Issue
  └─ [PROJECT] 用户系统重构 (#100)

步骤2: 分解为Epic/大功能
  ├─ [TASK] 用户认证 (#101) [task-with-deadline]
  ├─ [TASK] 权限管理 (#102) [task-with-deadline]
  └─ [OPEN] 性能优化 (#103) [task-open]

步骤3: 进一步分解为子任务
  用户认证 (#101)
  ├─ [SUBTASK] 实现JWT生成 (#104)
  ├─ [SUBTASK] 实现中间件 (#105)
  └─ [SUBTASK] 编写测试 (#106)
```

### 示例2：日常任务管理

**周一**: 规划本周任务
```bash
# 查看本周Milestone的任务
gh issue list --milestone "2024 Week 12" --label task-with-deadline

# 从开放性任务池选择2-3个任务
gh issue list --label task-open --sort updated
```

**周二-周五**: 执行任务
- 使用任务模板创建新任务
- 更新任务状态
- 记录进度

**周五**: 周回顾
- 关闭完成的任务
- 更新未完成任务
- 规划下周工作

## 🏷️ 标签使用指南

### 必须添加的标签

每个Issue至少应该有：
1. **类型标签**: `project` / `task-with-deadline` / `task-open` / `subtask`
2. **优先级标签**: `priority:*`（建议添加）

### 可选标签

根据需要添加：
- **状态**: `status:*`
- **类型**: `type:*`

### 标签组合示例

```
# 紧急任务
task-with-deadline, priority:critical, status:in-progress

# 开放性的文档改进
task-open, priority:low, type:documentation

# 阻塞的子任务
subtask, status:blocked, priority:high
```

## 📊 模板效果跟踪

### 统计模板使用情况

```bash
# 各类型任务数量
gh issue list --label project --state all
gh issue list --label task-with-deadline --state all
gh issue list --label task-open --state all
gh issue list --label subtask --state all
```

### 评估模板效果

定期回顾：
- 哪些模板使用频率高？
- 哪些模板需要改进？
- 是否需要新的模板？

## 💡 高级技巧

### 1. 模板变量

在模板中使用占位符：
```markdown
**负责人**: @{{ assignee }}
**优先级**: {{ priority }}
**截止日期**: {{ due_date }}
```

使用时替换为实际值。

### 2. 快速填充

创建常用配置的模板片段：
```markdown
<!-- 高优先级任务 -->
标签: task-with-deadline, priority:high
分配给: @myself
```

### 3. CLI快速创建

```bash
# 使用CLI和模板
gh issue create --template task-with-deadline.md \
  --title "[TASK] 实现支付接口" \
  --label "task-with-deadline,priority:high" \
  --milestone "MVP版本"
```

### 4. 批量操作

```bash
# 为所有开放性任务添加标签
gh issue list --label task-open --json number --jq '.[].number' | \
  xargs -I {} gh issue edit {} --add-label "needs-review"
```

## 🔍 常见问题

### Q: 不确定使用哪个模板？

**A**: 参考决策树：
```
是否是大型项目？
  └─ 是 → 使用"项目/大型任务"模板
  └─ 否 → 是否有明确截止日期？
      └─ 是 → 使用"有截止日期的任务"模板
      └─ 否 → 是否属于某个父任务？
          └─ 是 → 使用"子任务"模板
          └─ 否 → 使用"开放性任务"模板
```

### Q: 任务类型中途变化怎么办？

**A**: 更新标签即可：
- 移除旧标签：`task-open`
- 添加新标签：`task-with-deadline`
- 补充缺失的信息（如截止日期、Milestone）

### Q: 模板填写太复杂？

**A**: 
- 必填项：任务描述、验收标准、标签
- 选填项：根据实际需要填写
- 可以简化模板，保留核心字段

## 📚 更多资源

- [TODO结构说明](./TODO_STRUCTURE.md)
- [工作流程指南](./WORKFLOW.md)
- [GitHub Issue文档](https://docs.github.com/en/issues)

---

选择合适的模板，规范化创建Issue，让TODO管理更高效！
