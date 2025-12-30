# My_ToDo - GitHub-Based TODO Management System

轻量化的 GitHub Issues/Projects 树状 TODO 管理方案，支持多项目并行、父子层级和标签化优先级。AI 一句话即可生成结构化任务，涵盖截止日期、模块、里程碑、父子关系与验收标准。

## 核心功能一览
- **AI 生成与修订**：`/todo` 一句话自动创建带父子关系的任务，推断截止时间、优先级、模块、里程碑、标签与验收标准；`/fix` 在原格式上智能修订。支持中英文与批量 `/todo`。
- **多项目与层级管理**：利用 GitHub Projects/Milestones 组织项目，父子 Issue 构建任意深度的任务树，父子任务清单自动同步。
- **开放/封闭任务并存**：截止期任务用 Milestone + Due Date，开放式任务用标签区分，方便在同一项目中共存。
- **标签与优先级体系**：集中配置 `.github/tags-config.json`，涵盖任务类型、优先级、状态、模块等，AI 和手动流程统一使用。
- **项目标签继承**：项目模板新增“项目标签”字段，父项目定义的标签自动继承到子任务，便于按冲刺或团队筛选。
- **可视化脚本**：`scripts/visualize.sh` / `scripts/visualize_todos.py` 输出任务树、优先级、截止日期与统计信息。

## 创建 TODO 的三种方式
1. **AI 快速创建（推荐）**：使用 Issue 模板“🤖 AI 快速创建 TODO”或在任意 Issue 评论 `/todo ...`。带有截止日期会自动创建/关联对应日期的 Milestone；在父 Issue 中评论会自动建立子任务关系。
2. **标准模板**：选择“有截止日期的任务”“开放性任务”“项目/大型任务”“子任务”模板，按需填写所有字段与标签。
3. **手动创建**：自定义标题与内容，手动选择标签（任务类型、优先级、状态、类型等），并通过 `Parent: #issue_number` 或清单 `- [ ] #issue_number` 建立层级。

### 批量与修订示例
```text
/todo 完成前端页面设计，下周三完成
/todo 实现后端API接口，预计2天
/todo 编写测试用例和文档
```
在已有 TODO 中评论 `/fix ...` 可批量调整截止日期、父子关系、描述与标签。

## 工作流与最佳实践
- 使用 Milestone 查看按日期分组的任务；Labels 过滤模块或优先级。
- 开始工作添加 `status:in-progress`，阻塞时标记 `status:blocked`，完成后关闭 Issue，父任务清单自动更新。
- 项目 Issue 的“项目标签”会自动传递给子任务，便于按冲刺或团队筛选。
- 可视化脚本展示全局任务树、优先级、模块与即将到期任务，支持快速检查进度。

## AI 配置（必需）
1. 在阿里云百炼平台获取 `DASHSCOPE_API_KEY`。
2. 仓库 Settings → Secrets → Actions 添加同名 Secret，并在 Actions 权限中开启 Read/Write。
3. 创建测试 TODO 验证 `/todo` 工作流（`ai-create-todo.yml`）和 `/fix` 工作流（`ai-fix-todo.yml`）。

## 参考文档
- [AI 配置指南](./docs/AI_SETUP.md)
- [AI 创建示例](./examples/ai-todo-examples.md)
- [AI 父任务关联示例](./examples/ai-parent-task-examples.md)
- [可视化脚本使用](./scripts/README.md)
- [工作流程指南](./docs/WORKFLOW.md)
- [TODO 结构说明](./docs/TODO_STRUCTURE.md)
