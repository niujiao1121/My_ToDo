# My_ToDo - GitHub-Based TODO Management System

基于GitHub的树状TODO管理系统，支持多项目并行、树状结构和开放/封闭性任务管理。现已支持 **AI 驱动的一句话创建 TODO**！🤖✨

## 📋 系统特点

### 1. 🤖 AI 智能创建（新功能）
- 一句话描述，AI 自动生成格式化 TODO
- 智能识别截止日期、优先级、模块分类
- **支持指定父任务**：自动建立任务从属关系
- **自动创建 Milestone**：有截止日期的任务自动关联到对应日期的 Milestone，便于按时间筛选
- **评论自动关联**：在 Issue 下使用 `/todo` 命令创建的任务自动成为该 Issue 的子任务
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

示例 5 - 带父任务关系：
实现用户登录API，属于 #123，后端开发，预计2天
```

**AI 支持的父任务表达方式**：
- `属于 #123` - 指定父任务编号
- `是 #45 的子任务` - 明确子任务关系
- `从属于 #78` - 表示从属关系
- `parent #56` - 英文表达
- `subtask of #99` - 英文子任务标记

**AI 自动生成的效果**：
- ✅ 结构化的任务标题和描述
- ✅ 智能识别截止日期（今天、明天、下周等）
- ✅ **自动创建或关联 Milestone**（有截止日期时，方便按时间筛选任务）
- ✅ 自动推断优先级（紧急、重要等）
- ✅ 自动判断模块类型（前端、后端、数据库等）
- ✅ **自动识别并关联父任务**（从属关系）
- ✅ 生成验收标准清单
- ✅ 生成任务步骤清单
- ✅ 自动添加适当的标签
- ✅ 自动分配给创建者
- ✅ **自动更新父任务的子任务列表**

**配置说明**：
首次使用需要配置阿里云千问 API Key（很简单，费用很低）：
👉 [查看详细配置步骤](./docs/AI_SETUP.md)

**命令行快速创建**：
也可以在任何 Issue 下评论：
```
/todo 完成数据库备份脚本，下周一交付
```
**注意**：使用 `/todo` 命令创建的任务会**自动关联为当前 Issue 的子任务**，无需手动指定父任务！

**批量创建 TODO（新功能）**：✨
现在支持在一个评论中使用多个 `/todo` 命令批量创建多个 TODO：
```
/todo 完成前端页面设计，下周三完成
/todo 实现后端API接口，预计2天
/todo 编写测试用例和文档
```
系统会自动识别并为每个 `/todo` 创建独立的 Issue，所有 TODO 都会自动关联为当前 Issue 的子任务。

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
   - 优先级：`priority:critical`, `priority:high`, `priority:medium`, `priority:low`
   - 状态：`status:planning`, `status:in-progress`, `status:blocked` 等
   - 类型：`type:feature`, `type:bug`, `type:documentation` 等
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

1. **创建Project Issue**
   - 使用 "项目/大型任务" 模板创建 Issue
   - 填写项目名称、目标、时间规划等信息
   - **新功能** ✨：在 **项目标签** 字段中指定自定义标签（用逗号分隔）
     - 例如：`sprint-1, team-frontend, Q1-2024`
     - 这些标签会**自动应用到该项目的所有子任务**，便于后续筛选和管理
   - 添加 `project` 标签和优先级标签

2. **创建GitHub Project看板**（可选）
   - 进入Repository → Projects → New Project
   - 选择模板或创建空白项目
   - 设置项目名称和描述

2. **创建GitHub Project看板**（可选）
   - 进入Repository → Projects → New Project
   - 选择模板或创建空白项目
   - 设置项目名称和描述

3. **创建Milestone**（可选，用于有DDL的项目）
   - 进入Issues → Milestones → New Milestone
   - 设置截止日期和描述

**项目标签使用示例**：
当你创建一个项目 Issue（如 #10）时，在项目标签字段填入：
```
sprint-1, frontend-team
```
然后使用 `/todo` 命令为该项目创建子任务时，子任务会自动继承 `sprint-1` 和 `frontend-team` 标签。这样你就可以：
- 通过标签 `sprint-1` 查看该冲刺的所有任务
- 通过标签 `frontend-team` 查看前端团队的所有任务

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

## ⚙️ 配置阿里云 AI（使用 AI 功能必需）

要使用 AI 快速创建功能，需要配置阿里云千问 API Key。

### 快速配置步骤

1. **获取阿里云 API Key**
   - 访问 [阿里云百炼平台](https://dashscope.aliyun.com/)
   - 注册/登录阿里云账户
   - 开通百炼服务和通义千问模型
   - 创建新的 API Key
   - 复制保存 Key

2. **添加到 GitHub Secrets**
   - 进入仓库的 Settings → Secrets and variables → Actions
   - 点击 "New repository secret"
   - Name: `DASHSCOPE_API_KEY`
   - Secret: 粘贴你的阿里云 API Key
   - 保存

3. **配置工作流权限**
   - Settings → Actions → General
   - Workflow permissions 选择 "Read and write permissions"
   - 保存

4. **验证配置**
   - 创建一个 AI TODO 测试
   - 如果成功，会自动创建新 Issue 并回复

### 费用说明

- 使用 `qwen-plus` 模型，成本非常低且实惠
- **新用户福利**：注册即获大量免费调用额度 🎁
- 平均每次创建约 ¥0.005-0.01（一千元可以创建约 10-20万 个 TODO）
- 相比 OpenAI，价格更低、无需翻墙、中文理解更好
- 可在阿里云控制台设置每月消费预警

### 为什么选择阿里云千问？

- ✅ **中文理解出色**：专为中文优化，理解更准确
- ✅ **价格实惠**：比 OpenAI 更经济
- ✅ **访问稳定**：国内访问无障碍
- ✅ **新用户福利**：大量免费额度
- ✅ **支付便捷**：支持支付宝、微信支付

### 详细配置文档

👉 [完整配置步骤和故障排除](./docs/AI_SETUP.md)

---

## 📖 工作流程

### 日常TODO管理

1. **查看今日任务**
   - **使用 Milestone 视图查看截止日期任务**：AI 自动为有截止日期的任务创建 Milestone，可以按时间筛选
     - 进入 Issues → Milestones 查看所有截止日期分组
     - 点击具体 Milestone 查看该日期的所有任务
     - 在 Issues 页面使用 Milestone 过滤器快速定位
   - 使用 Labels 过滤特定模块或优先级的任务
   - **使用可视化脚本查看整体结构** 👇

2. **更新任务状态**
   - 开始工作：添加 `status:in-progress` 标签
   - 完成任务：关闭Issue，系统自动更新父任务清单
   - 阻塞状态：添加 `status:blocked` 标签并说明原因

3. **定期回顾**
   - 每周回顾：检查本周完成的任务和下周计划
   - 每月回顾：更新项目进度，调整优先级

### 📊 可视化 TODO 结构（新功能）

使用可视化脚本查看所有 TODO 的树状结构、优先级、截止日期等信息：

```bash
# 设置 GitHub Token（首次使用）
export GITHUB_TOKEN=your_token_here

# 运行可视化脚本（推荐使用便捷脚本）
./scripts/visualize.sh

# 或直接运行 Python 脚本
python scripts/visualize_todos.py
```

**功能特性**：
- 🌳 树状结构展示项目和任务的层级关系
- 🏷️ 彩色标记不同优先级（紧急、重要、中等、低）
- ⏰ 显示截止日期，标记即将到期的任务
- 📦 显示任务所属模块
- ✅ 区分已完成和未完成的任务
- 📈 提供详细的统计信息

**详细使用说明**：👉 [查看脚本文档](./scripts/README.md)

### 树状结构示例

```
项目: 网站重构 (#1) [project, priority:high]
├── 前端改造 (#2) [task-with-deadline]
│   ├── 设计新UI (#3) [subtask]
│   ├── 实现响应式布局 (#4) [subtask]
│   └── 集成新组件库 (#5) [subtask]
├── 后端优化 (#6) [task-open]
│   ├── 数据库重构 (#7) [subtask]
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
- **⭐ [AI 父任务关联示例](./examples/ai-parent-task-examples.md)** - 如何使用 AI 创建带父子关系的 TODO
- **⭐ [可视化脚本使用](./scripts/README.md)** - 查看 TODO 树状结构的可视化工具
- [TODO结构说明](./docs/TODO_STRUCTURE.md) - 详细的树状结构说明和最佳实践
- [工作流程指南](./docs/WORKFLOW.md) - 详细的工作流程和使用技巧
- [Issue模板使用](./docs/TEMPLATES.md) - Issue模板的使用说明

## 💡 最佳实践

1. **优先使用 AI 快速创建**
   - 简单和中等复杂度的任务用 AI 创建
   - 输入时尽量包含日期、优先级、模块信息
   - **创建子任务时指定父任务编号**（如："属于 #123"）
   - **使用批量创建功能**：一条评论中使用多个 `/todo` 命令快速分解任务
   - AI 创建后及时检查和完善信息
   - 复杂任务或需要大量技术细节的用标准模板

2. **保持任务粒度适中**
   - 大任务分解为1-5天可完成的子任务
   - 避免任务过于细碎或过于宏大

3. **合理使用标签**
   - 每个Issue至少有一个类型标签和一个模块标签
   - 根据实际情况添加优先级和状态标签
   - AI 会自动添加标签，但可以手动调整
   - **使用项目标签功能**：为项目定义自定义标签，子任务自动继承

4. **利用项目标签进行分类管理**
   - 为不同的冲刺、团队、版本创建项目标签
   - 子任务自动继承项目标签，便于筛选和跟踪
   - 使用标签组合筛选，快速定位特定任务

4. **利用项目标签进行分类管理**
   - 为不同的冲刺、团队、版本创建项目标签
   - 子任务自动继承项目标签，便于筛选和跟踪
   - 使用标签组合筛选，快速定位特定任务

5. **及时更新状态**
   - 任务开始时添加 `status:in-progress`
   - 遇到阻塞及时标记并说明
   - 完成后及时关闭Issue

6. **利用GitHub功能**
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
- **✨ [批量创建 TODO 和项目标签使用示例](./examples/batch-todo-and-labels-example.md)** - 新功能详细教程！

---

**开始使用**: 
1. ⭐ **推荐**：配置 OpenAI API（[配置指南](./docs/AI_SETUP.md)），体验 AI 一句话创建 TODO
2. 或直接创建你的第一个 Issue，选择合适的模板，开启高效的 TODO 管理之旅！

**需要帮助？** 查看 [AI 配置指南](./docs/AI_SETUP.md) 或在 [Discussions](https://github.com/niujiao1121/My_ToDo/discussions) 提问。
