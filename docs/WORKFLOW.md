# 工作流程指南

本文档详细介绍如何使用本TODO管理系统进行日常工作。

## 日常工作流程

### 早晨：规划今日任务

#### 1. 查看今日关键任务

使用GitHub搜索：
```
is:open assignee:@me label:priority:high
is:open assignee:@me milestone:"本周"
```

或者访问：
- Projects → 查看"In Progress"列
- Issues → Filter by: Assignee: You, State: Open

#### 2. 选择任务并开始工作

```bash
# 通过CLI快速更新状态
gh issue edit 123 --add-label "status:in-progress"
```

或在Web界面：
- 打开Issue
- 添加 `status:in-progress` 标签
- 在评论中记录开始时间和计划

### 工作中：更新进度

#### 记录进度

在Issue评论中记录：
```markdown
## 进度更新 - 2024-01-15 14:30

✅ 已完成：
- 完成数据库schema设计
- 实现基础CRUD接口

🔄 进行中：
- 编写单元测试 (60%)

⏭️ 下一步：
- 集成到主分支
- 部署到测试环境
```

#### 遇到阻塞

1. 添加 `status:blocked` 标签
2. 在评论中说明阻塞原因
3. 如果需要其他人帮助，@mention 相关人员
4. 创建新Issue跟踪阻塞问题

```markdown
## ⚠️ 任务阻塞

**阻塞原因**：等待API文档确认

**需要**: @teammate 确认用户认证接口的返回格式

**预计解除时间**: 2024-01-16

**临时方案**: 先使用mock数据继续前端开发
```

### 晚间：总结和规划

#### 1. 更新任务状态

- 关闭已完成的Issue
- 更新未完成任务的进度
- 规划明天的工作

#### 2. 父任务进度同步

如果完成了子任务，更新父Issue的任务清单：
```markdown
## 子任务进度

- [x] #124 设计数据库schema ✅ 2024-01-15
- [x] #125 实现API接口 ✅ 2024-01-15
- [ ] #126 编写单元测试 🔄 进行中
- [ ] #127 部署到测试环境

进度: 2/4 完成 (50%)
```

## 周期性回顾

### 每周回顾（周五下午）

#### 1. 本周总结

创建一个周报Issue：
```markdown
# 周报 2024-W03 (1月15日-1月19日)

## 📊 本周统计
- 完成任务: 12个
- 新增任务: 8个
- 关闭任务: 10个

## ✅ 主要成果
- 完成用户认证系统 (#101, #102, #103)
- 优化数据库查询性能 (#204, #205)

## 🔄 进行中
- 支付系统集成 (#110) - 进度70%
- 前端界面优化 (#113) - 进度40%

## 🚧 遇到的问题
- 第三方API不稳定，影响集成进度
- 需要增加测试覆盖率

## 📅 下周计划
- [ ] 完成支付系统集成
- [ ] 开始前端性能优化
- [ ] 增加单元测试覆盖率到80%
```

#### 2. 调整优先级

根据本周情况，调整下周任务优先级：
- 将紧急任务标记为 `priority:critical`
- 延期的任务更新Milestone
- 开放性任务重新评估必要性

### 每月回顾（月末）

#### 1. 项目进度回顾

使用Milestone视图：
- 查看本月Milestone完成情况
- 统计各模块的任务分布
- 识别瓶颈和风险

#### 2. 清理和归档

```bash
# 关闭长期未活跃的Issue
gh issue list --state open --label task-open --json number,updatedAt

# 归档已完成的项目
# 为项目Issue添加 "archived" 标签并关闭
```

#### 3. 下月规划

创建下月的Milestone：
```markdown
Milestone: 2024年2月目标
截止日期: 2024-02-29

## 主要目标
1. 完成电商平台升级项目
2. 启动代码重构计划
3. 提升测试覆盖率到85%

## 关键任务
- #100 电商平台升级（续）
- #200 代码重构计划启动
- #250 测试体系完善
```

### 季度回顾（季度末）

#### 1. 总体评估

- 回顾本季度完成的主要项目
- 分析未完成任务的原因
- 总结经验教训

#### 2. 战略调整

- 调整技术栈和工具
- 优化工作流程
- 规划下季度重点

## 多项目管理策略

### 项目切换

#### 使用Projects分组

为每个大项目创建独立的GitHub Project：
```
Project A: 电商平台升级
Project B: 代码重构2024
Project C: 新产品原型
```

#### 时间分配

使用标签标记时间分配：
```
project:主线 - 60%时间
project:重构 - 30%时间
project:探索 - 10%时间
```

#### 上下文切换最小化

- 同一天内尽量只处理1-2个项目的任务
- 使用番茄工作法，每个时间块专注单一项目
- 在Issue评论中记录上下文信息，便于恢复

### 优先级矩阵

使用"重要-紧急"矩阵管理任务：

| | 紧急 | 不紧急 |
|---|---|---|
| **重要** | `priority:critical` + `task-with-deadline` | `priority:high` + `task-open` |
| **不重要** | `priority:medium` + `task-with-deadline` | `priority:low` + `task-open` |

## 协作工作流程

### 团队成员分工

#### 任务分配

```bash
# 分配任务给团队成员
gh issue edit 123 --add-assignee teammate1

# 自己认领任务
gh issue edit 123 --add-assignee @me
```

#### 代码审查流程

当任务涉及代码时：
1. 完成开发后，添加 `status:review` 标签
2. 创建Pull Request并关联Issue
3. 请求Code Review
4. Review通过后合并代码，关闭Issue

### 沟通机制

#### Issue评论

用于任务相关的具体讨论：
```markdown
@teammate1 请帮忙review一下API设计

@teammate2 FYI，这个功能可能影响你负责的模块
```

#### Discussions

用于开放性讨论和头脑风暴：
- 技术方案讨论
- 架构设计
- 最佳实践分享

## 特殊场景处理

### 场景1：紧急任务插入

```markdown
## 紧急任务处理流程

1. 创建Issue，标记 `priority:critical`
2. 评估对当前任务的影响
3. 暂停当前任务（添加评论说明）
4. 处理紧急任务
5. 完成后恢复之前的任务
```

### 场景2：长期项目管理

```markdown
## 长期项目（>3个月）

1. 分解为多个阶段性Milestone
2. 每个Milestone设置子目标
3. 定期（每2周）更新项目Issue的进度
4. 使用Project Roadmap视图追踪整体进度
```

### 场景3：探索性任务

```markdown
## 探索性/研究性任务

标签: `task-open`, `type:research`, `priority:low`

- 设置时间盒（例如：不超过2周）
- 记录研究过程和发现
- 产出技术报告或POC
- 根据结果决定是否转为正式任务
```

## 效率提升技巧

### 1. 使用快捷键和CLI

```bash
# 设置别名
alias todo="gh issue list --assignee @me --state open"
alias done="gh issue close"

# 快速查看今日任务
todo | grep "priority:high"

# 快速创建任务
gh issue create --title "任务标题" --body "任务描述" --label "task,priority:medium"
```

### 2. 模板化

创建常用的Issue描述模板：
```markdown
## 📋 任务描述
[描述任务目标]

## ✅ 验收标准
- [ ] 标准1
- [ ] 标准2

## 📎 相关资源
- 文档: [链接]
- 参考: [链接]

## 🔗 关联Issue
- Parent: #
- Related: #
```

保存为snippet或使用GitHub的Issue模板功能。

### 3. 自动化

使用GitHub Actions自动化工作流：
- 自动添加标签
- 自动关联Project
- 定期生成报告
- 提醒即将到期的任务

### 4. 专注模式

减少干扰：
- 关闭不必要的通知
- 设置专注时间段
- 使用"Do Not Disturb"模式
- 批量处理非紧急任务

## 最佳实践总结

### DO ✅

- ✅ 每天早晚更新任务状态
- ✅ 及时记录工作进度和问题
- ✅ 合理估算任务时间
- ✅ 保持Issue描述简洁明了
- ✅ 使用标签统一规范
- ✅ 定期回顾和调整

### DON'T ❌

- ❌ 不要创建过于细碎的子任务
- ❌ 不要让Issue描述过长（拆分为多个Issue）
- ❌ 不要忘记关闭已完成的Issue
- ❌ 不要让标签体系过于复杂
- ❌ 不要在多个地方维护TODO（统一使用GitHub）

## 工具整合

### IDE整合

大多数IDE支持GitHub集成：
- **VS Code**: GitHub Pull Requests and Issues插件
- **JetBrains**: 内置GitHub集成
- **Vim**: vim-fugitive + hub.vim

### 移动端

使用GitHub移动App：
- 快速查看和更新Issue
- 接收重要通知
- 进行简单的任务管理

### 浏览器扩展

推荐扩展：
- **Refined GitHub**: 增强GitHub界面
- **Octolinker**: 代码导航
- **GitHub Issue Tracker**: 任务跟踪

## 总结

高效的TODO管理需要：
1. **清晰的工作流程** - 知道什么时候做什么
2. **一致的操作习惯** - 形成肌肉记忆
3. **定期的回顾调整** - 持续优化
4. **合适的工具支持** - 提升效率

坚持执行这些流程，你的TODO管理将变得轻松高效！
