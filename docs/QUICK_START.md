# 快速开始指南

5分钟上手GitHub TODO管理系统！

## 第一步：理解系统特点

本系统支持：
- ✅ **多项目管理** - 同时跟踪多个独立项目
- ✅ **树状结构** - 任务可以无限层级分解
- ✅ **灵活的截止日期** - 支持有DDL和无DDL的任务

## 第二步：设置标签（首次使用）

### 方式一：手动创建标签

进入 Repository → Issues → Labels → New label

参考 `.github/labels.yml` 创建以下标签：

**必需标签**:
- `project` (紫色)
- `task-with-deadline` (红色)  
- `task-open` (绿色)
- `subtask` (浅蓝色)
- `type:feature`, `type:bug` 等（蓝色系）
- `priority:high`, `priority:medium`, `priority:low` (红黄绿)

### 方式二：使用GitHub CLI批量创建

```bash
# 如果有labels.yml配置文件，可以使用工具批量导入
# 或者手动创建关键标签
gh label create "project" --color "5319E7" --description "大型项目或任务线"
gh label create "task-with-deadline" --color "D93F0B" --description "有截止日期的任务"
gh label create "task-open" --color "0E8A16" --description "开放性任务"
gh label create "subtask" --color "C5DEF5" --description "子任务"
```

## 第三步：创建第一个项目

### 使用Issue模板创建

1. 点击 **"New Issue"**
2. 选择 **"项目/大型任务"** 模板
3. 填写信息：

```markdown
标题: [PROJECT] 我的第一个项目

项目概述: 这是一个测试项目，用于熟悉系统

时间规划:
- 开始日期: 2024-01-15
- 预计完成: 2024-02-15

主要功能模块:
- [ ] 模块1: 需求分析
- [ ] 模块2: 设计开发
- [ ] 模块3: 测试部署
```

4. 添加标签：`project`, `priority:high`
5. 点击 **"Submit new issue"**

✅ 恭喜！你创建了第一个项目Issue，比如 #1

## 第四步：分解任务

### 创建子任务

1. 点击 **"New Issue"**
2. 选择 **"有截止日期的任务"** 或 **"开放性任务"** 模板
3. 填写信息：

```markdown
标题: [TASK] 完成需求文档

任务描述: 编写项目需求文档

截止日期: 2024-01-25

验收标准:
- [ ] 完成功能需求列表
- [ ] 完成非功能需求列表
- [ ] 评审通过
```

4. 添加标签：`task-with-deadline`, `priority:high`
5. 在Issue描述中添加：`Parent: #1`（关联到项目）
6. 提交Issue，假设得到 #2

### 在父Issue中添加子任务清单

回到项目Issue #1，编辑描述，添加：

```markdown
## 子任务进度

- [ ] #2 完成需求文档
- [ ] #3 设计系统架构（待创建）
- [ ] #4 实现核心功能（待创建）
```

## 第五步：创建Project看板（可选但推荐）

1. 进入 Repository → **Projects** → **New Project**
2. 选择 **"Board"** 视图
3. 命名：例如 "2024 Q1 任务看板"
4. 创建列：
   - 📋 Backlog
   - 📝 To Do
   - 🔄 In Progress
   - ✅ Done

5. 将Issue添加到看板：
   - 点击 "Add items"
   - 搜索并添加 #1, #2 等Issue
   - 拖动到合适的列

## 第六步：创建Milestone（用于有截止日期的项目）

1. 进入 Repository → **Issues** → **Milestones** → **New Milestone**
2. 填写信息：
   ```
   标题: MVP版本
   截止日期: 2024-02-28
   描述: 完成最小可用版本
   ```
3. 编辑有截止日期的Issue，关联到这个Milestone

## 第七步：开始工作

### 今天要做什么？

查看任务：
```bash
# 使用GitHub CLI
gh issue list --assignee @me --label priority:high

# 或在Web界面
# Issues → Filter: is:open assignee:@me label:priority:high
```

### 开始一个任务

1. 打开Issue，例如 #2
2. 添加标签：`status:in-progress`
3. 在评论中记录：
   ```markdown
   开始工作 - 2024-01-15 09:00
   今天计划完成功能需求列表部分
   ```

### 任务完成

1. 完成任务后，在Issue中评论：
   ```markdown
   ✅ 任务完成！
   
   完成内容：
   - ✅ 功能需求列表
   - ✅ 非功能需求列表
   - ✅ 需求评审
   
   交付物：需求文档 v1.0
   ```

2. 关闭Issue
3. 回到父Issue #1，勾选完成的子任务：
   ```markdown
   ## 子任务进度
   - [x] #2 完成需求文档 ✅ 2024-01-18
   - [ ] #3 设计系统架构
   ```

## 常用操作速查

### 查看任务

```bash
# 我的所有待办任务
gh issue list --assignee @me --state open

# 高优先级任务
gh issue list --label priority:high --state open

# 本周截止的任务
gh issue list --milestone "本周"

# 某个项目的所有任务
gh issue list --search "我的第一个项目"
```

### 快速创建任务

```bash
# 创建带标签的任务
gh issue create \
  --title "[TASK] 编写测试用例" \
  --label "task-with-deadline,priority:medium" \
  --body "为核心功能编写单元测试"

# 分配给自己
gh issue create \
  --title "[TASK] 代码review" \
  --assignee @me \
  --label "task,priority:high"
```

### 更新任务状态

```bash
# 开始工作
gh issue edit 5 --add-label "status:in-progress"

# 任务被阻塞
gh issue edit 5 --add-label "status:blocked"

# 完成任务
gh issue close 5 --comment "✅ 任务完成"
```

## 最佳实践提醒

1. **每天早晚各5分钟**
   - 早上：查看今日任务，规划优先级
   - 晚上：更新任务状态，关闭完成的任务

2. **保持任务粒度适中**
   - 单个任务：1-5天可完成
   - 太大的任务：分解为子任务
   - 太小的任务：合并或作为清单项

3. **合理使用标签**
   - 必备：类型标签 + 模块标签
   - 选配：优先级 + 状态标签

4. **定期回顾**
   - 每周五：回顾本周，规划下周
   - 每月末：回顾月度进展，调整计划

## 进阶阅读

- 📖 [详细的TODO结构说明](./TODO_STRUCTURE.md)
- 🔄 [完整的工作流程指南](./WORKFLOW.md)
- 📝 [Issue模板使用说明](./TEMPLATES.md)
- 💡 [实际项目示例](../examples/ecommerce-project.md)

## 需要帮助？

- 查看文档目录：`docs/` 文件夹
- 查看示例：`examples/` 文件夹
- 提出问题：创建一个Issue或Discussion

---

🎉 恭喜你完成快速开始！现在开始用GitHub管理你的TODO吧！
