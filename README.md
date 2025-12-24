# My_ToDo - GitHub-Based TODO Management System

基于GitHub的树状TODO管理系统，支持多项目并行、树状结构和开放/封闭性任务管理。现已支持 **AI 驱动的一句话创建 TODO**！🤖✨

## 📋 系统特点

### 1. 🤖 AI 智能创建（新功能）
- 一句话描述，AI 自动生成格式化 TODO
- 智能识别截止日期、优先级、模块分类
- 支持中文和英文输入
- 自动生成验收标准和任务清单

### 2. 多项目支持
- 使用GitHub Projects和Milestones管理不同的大任务线
- 每个项目可以独立跟踪进度
- 支持项目间的并行开发

### 3. 树状TODO结构
- 利用GitHub Issues的层级关系
- 父Issue代表大需求，子Issue代表具体问题
- 支持任意深度的任务分解
- 使用Labels标记不同模块和优先级

### 4. 开放性和封闭性TODO并存
- **封闭性TODO**：有明确截止日期的任务（使用Milestone + Due Date）
- **开放性TODO**：可随时完成的任务（使用特定Label标记）
- 两种类型可在同一项目中共存

## 🚀 快速开始

### 🎯 三种创建 TODO 的方式（按推荐顺序）

#### 方式一：🤖 AI 快速创建（推荐）⭐

**最简单、最快速的方式！** 只需一句话，AI 自动帮你创建格式化的 TODO。

**使用步骤**：
1. 点击 "New Issue"
2. 选择 "🤖 AI 快速创建 TODO" 模板
3. 在 "我要做的事" 下方输入一句话描述
4. 点击 "Submit new issue"
5. 等待几秒，AI 会自动创建详细的 TODO 并回复链接

**输入示例**：

```
示例 1 - 日常任务：
明天前完成周报，总结本周工作进展和下周计划

示例 2 - 技术任务：
紧急修复支付接口超时问题，后端优化，预计3天，下周五完成

示例 3 - 学习任务：
学习 Docker 容器化部署，包括基础概念和实践操作，预计 5 天

示例 4 - 设计任务：
设计用户个人主页的 UI 原型，包括移动端和桌面端，下周三交付
```

**AI 自动生成的效果**：
- ✅ 结构化的任务标题和描述
- ✅ 智能识别截止日期（今天、明天、下周等）
- ✅ 自动推断优先级（紧急、重要等）
- ✅ 自动判断模块类型（前端、后端、数据库等）
- ✅ 生成验收标准清单
- ✅ 生成任务步骤清单
- ✅ 自动添加适当的标签
- ✅ 自动分配给创建者

**配置说明**：
首次使用需要配置 OpenAI API Key（很简单，费用很低）：
👉 [查看详细配置步骤](./docs/AI_SETUP.md)

**命令行快速创建**：
也可以在任何 Issue 下评论：
```
/todo 完成数据库备份脚本，下周一交付
```

---

#### 方式二：📋 使用标准模板创建

适合需要精确控制所有字段的场景。

**使用步骤**：
1. 点击 "New Issue"
2. 选择对应的模板：
   - "有截止日期的任务" - 用于有明确截止日期的任务
   - "开放性任务" - 用于没有固定截止日期的任务
   - "项目/大型任务" - 用于大型项目或任务线
   - "子任务" - 用于创建子任务
3. 填写模板中的各个字段
4. 添加适当的标签
5. 提交 Issue

**适用场景**：
- 需要填写详细的技术方案
- 需要关联多个相关任务
- 需要添加大量参考资料
- 对格式有特殊要求

---

#### 方式三：✏️ 手动创建

完全自定义的方式。

**使用步骤**：
1. 点击 "New Issue"
2. 自己编写标题和内容
3. 手动选择标签：
   - 任务类型：`project`, `task-with-deadline`, `task-open`, `subtask`
   - 模块：`module:frontend`, `module:backend`, `module:database` 等
   - 优先级：`priority:critical`, `priority:high`, `priority:medium`, `priority:low`
   - 状态：`status:planning`, `status:in-progress`, `status:blocked` 等
4. 建立任务关系（如果需要）：
   - 在描述中使用 `Parent: #issue_number` 标记父任务
   - 使用 `- [ ] #issue_number` 创建子任务清单
5. 提交 Issue

**适用场景**：
- 非常简单的任务
- 特殊格式需求
- 临时记录

---

### 创建新项目

1. **创建Project**
   - 进入Repository → Projects → New Project
   - 选择模板或创建空白项目
   - 设置项目名称和描述

2. **创建Milestone（可选，用于有DDL的项目）**
   - 进入Issues → Milestones → New Milestone
   - 设置截止日期和描述

### 创建 TODO

参见上方的 [🎯 三种创建 TODO 的方式](#🎯-三种创建-todo-的方式按推荐顺序)，推荐使用 **AI 快速创建**！

## 📖 完整使用示例

### 场景：开发一个博客系统

**第 1 步：创建项目**（使用手动方式）
- 标题：`[PROJECT] 博客系统开发`
- 标签：`project`, `priority:high`
- 创建 Milestone：设置为 3 个月后

**第 2 步：使用 AI 快速创建主要任务**

AI 输入 1：
```
实现用户认证和授权系统，包括注册、登录、JWT token，后端开发，2周内完成
```
→ AI 自动创建 Issue #2，带有详细的验收标准和任务清单

AI 输入 2：
```
设计博客文章发布和管理功能的前端页面，包括编辑器、预览、发布，下个月完成
```
→ AI 自动创建 Issue #3，自动推断为前端模块

AI 输入 3：
```
设计数据库表结构，包括用户表、文章表、评论表，5天
```
→ AI 自动创建 Issue #4，自动识别为数据库模块

**第 3 步：手动创建子任务**（如果需要更细的分解）

在 Issue #2 下评论：
```
/todo 实现用户注册 API
```
→ AI 快速创建子任务 Issue #5

**第 4 步：在父项目中关联任务**

编辑 Issue #1（博客系统开发），添加：
```markdown
## 📝 子任务列表
- [ ] #2 用户认证和授权系统
- [ ] #3 文章发布管理前端
- [ ] #4 数据库设计
```

**第 5 步：跟踪进度**
- 开始工作时：添加 `status:in-progress` 标签
- 完成任务时：关闭 Issue，父任务清单自动更新 ✓
- 查看 Project 看板可视化整体进度

---

## ⚙️ 配置 OpenAI API（使用 AI 功能必需）

要使用 AI 快速创建功能，需要配置 OpenAI API Key。

### 快速配置步骤

1. **获取 OpenAI API Key**
   - 访问 [OpenAI Platform](https://platform.openai.com/api-keys)
   - 注册/登录账户
   - 创建新的 API Key
   - 复制保存 Key（只显示一次）

2. **添加到 GitHub Secrets**
   - 进入仓库的 Settings → Secrets and variables → Actions
   - 点击 "New repository secret"
   - Name: `OPENAI_API_KEY`
   - Secret: 粘贴你的 API Key
   - 保存

3. **配置工作流权限**
   - Settings → Actions → General
   - Workflow permissions 选择 "Read and write permissions"
   - 保存

4. **验证配置**
   - 创建一个 AI TODO 测试
   - 如果成功，会自动创建新 Issue 并回复

### 费用说明

- 使用 `gpt-4o-mini` 模型，成本非常低
- 平均每次创建约 $0.001（一毛钱可以创建约 100 个 TODO）
- 可在 OpenAI 平台设置每月消费上限

### 详细配置文档

👉 [完整配置步骤和故障排除](./docs/AI_SETUP.md)

---

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

- **⭐ [AI 配置指南](./docs/AI_SETUP.md)** - OpenAI API 配置、故障排除、成本控制
- **⭐ [AI 创建示例](./examples/ai-todo-examples.md)** - 10+ 个真实场景的输入输出示例
- [TODO结构说明](./docs/TODO_STRUCTURE.md) - 详细的树状结构说明和最佳实践
- [工作流程指南](./docs/WORKFLOW.md) - 详细的工作流程和使用技巧
- [Issue模板使用](./docs/TEMPLATES.md) - Issue模板的使用说明

## 💡 最佳实践

1. **优先使用 AI 快速创建**
   - 简单和中等复杂度的任务用 AI 创建
   - 输入时尽量包含日期、优先级、模块信息
   - AI 创建后及时检查和完善信息
   - 复杂任务或需要大量技术细节的用标准模板

2. **保持任务粒度适中**
   - 大任务分解为1-5天可完成的子任务
   - 避免任务过于细碎或过于宏大

3. **合理使用标签**
   - 每个Issue至少有一个类型标签和一个模块标签
   - 根据实际情况添加优先级和状态标签
   - AI 会自动添加标签，但可以手动调整

4. **及时更新状态**
   - 任务开始时添加 `status:in-progress`
   - 遇到阻塞及时标记并说明
   - 完成后及时关闭Issue

5. **利用GitHub功能**
   - 使用Project看板可视化进度
   - 使用Milestone管理阶段性目标
   - 使用Discussions讨论长期规划

## 🔧 自定义配置

可以根据实际需求：
- 添加新的标签分类（在 `.github/labels.yml` 中配置）
- 创建新的Issue模板（在 `.github/ISSUE_TEMPLATE/` 中添加）
- 调整工作流程和最佳实践

## 📝 示例

参考 `examples/` 目录下的示例项目，了解如何组织复杂的多项目TODO结构：
- [电商项目示例](./examples/ecommerce-project.md)
- **⭐ [AI TODO 创建示例](./examples/ai-todo-examples.md)** - 推荐先看这个！

---

**开始使用**: 
1. ⭐ **推荐**：配置 OpenAI API（[配置指南](./docs/AI_SETUP.md)），体验 AI 一句话创建 TODO
2. 或直接创建你的第一个 Issue，选择合适的模板，开启高效的 TODO 管理之旅！

**需要帮助？** 查看 [AI 配置指南](./docs/AI_SETUP.md) 或在 [Discussions](https://github.com/niujiao1121/My_ToDo/discussions) 提问。