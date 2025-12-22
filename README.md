# My_ToDo - GitHub-Based TODO Management System

基于GitHub的树状TODO管理系统，支持多项目并行、树状结构和开放/封闭性任务管理。

## 📋 系统特点

### 1. 多项目支持
- 使用GitHub Projects和Milestones管理不同的大任务线
- 每个项目可以独立跟踪进度
- 支持项目间的并行开发

### 2. 树状TODO结构
- 利用GitHub Issues的层级关系
- 父Issue代表大需求，子Issue代表具体问题
- 支持任意深度的任务分解
- 使用Labels标记不同模块和优先级

### 3. 开放性和封闭性TODO并存
- **封闭性TODO**：有明确截止日期的任务（使用Milestone + Due Date）
- **开放性TODO**：可随时完成的任务（使用特定Label标记）
- 两种类型可在同一项目中共存

## 🚀 快速开始

### 创建新项目

1. **创建Project**
   - 进入Repository → Projects → New Project
   - 选择模板或创建空白项目
   - 设置项目名称和描述

2. **创建Milestone（可选，用于有DDL的项目）**
   - 进入Issues → Milestones → New Milestone
   - 设置截止日期和描述

### 创建TODO

#### 方式一：使用Issue模板
使用 `.github/ISSUE_TEMPLATE/` 下的模板快速创建标准化的TODO

#### 方式二：手动创建
1. 点击 "New Issue"
2. 选择合适的标签：
   - `project`: 大型项目/任务线
   - `task-with-deadline`: 有截止日期的任务
   - `task-open`: 开放性任务
   - `subtask`: 子任务
   - 模块标签：`module:frontend`, `module:backend`, `module:database` 等
   - 优先级：`priority:high`, `priority:medium`, `priority:low`

3. 建立任务关系：
   - 在Issue描述中使用 `Parent: #issue_number` 标记父任务
   - 在Issue描述中使用 `Related to #issue_number` 关联相关任务
   - 在父Issue中使用 `- [ ] #issue_number` 创建子任务清单

## 📖 工作流程

### 日常TODO管理

1. **查看今日任务**
   - 使用 Milestone 视图查看本周/本月截止的任务
   - 使用 Labels 过滤特定模块或优先级的任务

2. **更新任务状态**
   - 开始工作：添加 `status:in-progress` 标签
   - 完成任务：关闭Issue，系统自动更新父任务清单
   - 阻塞状态：添加 `status:blocked` 标签并说明原因

3. **定期回顾**
   - 每周回顾：检查本周完成的任务和下周计划
   - 每月回顾：更新项目进度，调整优先级

### 树状结构示例

```
项目: 网站重构 (#1) [project, priority:high]
├── 前端改造 (#2) [task-with-deadline, module:frontend]
│   ├── 设计新UI (#3) [subtask]
│   ├── 实现响应式布局 (#4) [subtask]
│   └── 集成新组件库 (#5) [subtask]
├── 后端优化 (#6) [task-open, module:backend]
│   ├── 数据库重构 (#7) [subtask, module:database]
│   └── API性能优化 (#8) [subtask]
└── 测试与部署 (#9) [task-with-deadline]
    ├── 编写单元测试 (#10) [subtask]
    └── 配置CI/CD (#11) [subtask]
```

## 🏷️ 标签系统

### 任务类型
- `project` - 大型项目/任务线
- `task-with-deadline` - 有截止日期的任务
- `task-open` - 开放性任务，无固定截止日期
- `subtask` - 子任务

### 模块分类
- `module:frontend` - 前端相关
- `module:backend` - 后端相关
- `module:database` - 数据库相关
- `module:devops` - 运维相关
- `module:design` - 设计相关
- `module:docs` - 文档相关

### 优先级
- `priority:critical` - 紧急且重要
- `priority:high` - 重要
- `priority:medium` - 中等
- `priority:low` - 低优先级

### 状态
- `status:planning` - 规划中
- `status:in-progress` - 进行中
- `status:blocked` - 被阻塞
- `status:review` - 待审核

## 📚 详细文档

- [TODO结构说明](./docs/TODO_STRUCTURE.md) - 详细的树状结构说明和最佳实践
- [工作流程指南](./docs/WORKFLOW.md) - 详细的工作流程和使用技巧
- [Issue模板使用](./docs/TEMPLATES.md) - Issue模板的使用说明

## 💡 最佳实践

1. **保持任务粒度适中**
   - 大任务分解为1-5天可完成的子任务
   - 避免任务过于细碎或过于宏大

2. **合理使用标签**
   - 每个Issue至少有一个类型标签和一个模块标签
   - 根据实际情况添加优先级和状态标签

3. **及时更新状态**
   - 任务开始时添加 `status:in-progress`
   - 遇到阻塞及时标记并说明
   - 完成后及时关闭Issue

4. **利用GitHub功能**
   - 使用Project看板可视化进度
   - 使用Milestone管理阶段性目标
   - 使用Discussions讨论长期规划

## 🔧 自定义配置

可以根据实际需求：
- 添加新的标签分类（在 `.github/labels.yml` 中配置）
- 创建新的Issue模板（在 `.github/ISSUE_TEMPLATE/` 中添加）
- 调整工作流程和最佳实践

## 📝 示例

参考 `examples/` 目录下的示例项目，了解如何组织复杂的多项目TODO结构。

---

**开始使用**: 创建你的第一个Issue，选择合适的模板，开启高效的TODO管理之旅！