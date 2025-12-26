# 常见问题解答 (FAQ)

## 基础概念

### Q1: 为什么选择GitHub作为TODO管理工具？

**A**: GitHub提供了完整的项目管理功能：
- ✅ **Issues**: 天然的任务跟踪系统
- ✅ **Labels**: 灵活的分类和标记
- ✅ **Milestones**: 时间和目标管理
- ✅ **Projects**: 可视化看板
- ✅ **关联性**: 代码、文档、任务统一管理
- ✅ **免费**: 个人使用完全免费
- ✅ **跨平台**: Web、移动端、CLI全支持

### Q2: 这个系统和传统TODO工具（如Todoist、Notion）有什么区别？

**A**: 主要区别：
| 特性 | GitHub系统 | 传统工具 |
|------|-----------|---------|
| 树状结构 | ✅ 支持无限层级 | ⚠️ 有限支持 |
| 代码集成 | ✅ 原生支持 | ❌ 不支持 |
| 版本控制 | ✅ 完整历史 | ⚠️ 有限 |
| 协作 | ✅ PR、Review | ⚠️ 基础协作 |
| 自动化 | ✅ Actions | ⚠️ 有限 |
| 成本 | ✅ 免费 | ⚠️ 部分付费 |

最大优势：开发者友好，任务与代码紧密结合。

### Q3: 树状TODO结构最多可以有多少层？

**A**: 技术上没有限制，但建议：
- **推荐深度**: 3-4层
- **最佳实践**: 
  ```
  Level 1: Project (项目)
  Level 2: Epic (大功能)
  Level 3: Task (任务)
  Level 4: Subtask (子任务)
  ```
- **避免**: 超过5层，会导致管理复杂度过高

## 使用问题

### Q4: 如何选择使用"有截止日期的任务"还是"开放性任务"？

**A**: 决策流程：
```
问自己：这个任务有明确的时间要求吗？
├─ 是 → 使用"有截止日期的任务"
│   例子：版本发布前必须完成的功能
│   
└─ 否 → 使用"开放性任务"
    例子：代码优化、文档完善、技术债务
```

**经验法则**:
- 40% 有截止日期的任务（关键路径）
- 60% 开放性任务（持续改进）

### Q5: Issue标题应该如何命名？

**A**: 推荐格式：
```
[类型] 简短描述

示例：
✅ [PROJECT] 电商平台V2.0升级
✅ [TASK] 实现用户认证API
✅ [SUBTASK] 编写单元测试
✅ [OPEN] 优化数据库查询性能

❌ 实现用户认证（缺少类型）
❌ [TASK] 实现用户认证API，包括JWT生成、验证、刷新等功能（太长）
```

**最佳实践**:
- 包含类型前缀
- 简洁明了（<50字符）
- 动词开头（实现、优化、修复）
- 具体但不详细（细节放在描述中）

### Q6: 什么时候应该创建新的Issue，什么时候在已有Issue中添加清单？

**A**: 
| 创建新Issue | 添加清单项 |
|-----------|----------|
| 需要独立跟踪进度 | 简单的步骤 |
| 需要分配给不同人 | 不需要独立讨论 |
| 工作量>1天 | 工作量<2小时 |
| 需要独立讨论和文档 | 机械性的步骤 |

**示例**:
```markdown
创建新Issue:
- [ ] #123 实现OAuth2.0认证（3天工作量）
- [ ] #124 实现RBAC权限系统（5天工作量）

添加清单:
任务: 部署到生产环境
- [ ] 备份数据库
- [ ] 停止服务
- [ ] 更新代码
- [ ] 启动服务
- [ ] 验证功能
```

### Q7: 如何处理任务优先级变化？

**A**: 
1. **更新标签**
   ```bash
   gh issue edit 123 --remove-label "priority:medium"
   gh issue edit 123 --add-label "priority:high"
   ```

2. **说明原因**
   在Issue评论中记录：
   ```markdown
   ## 优先级调整
   
   从 `priority:medium` 调整为 `priority:high`
   
   **原因**: 客户提出紧急需求，需要优先处理
   **影响**: 可能延后 #124 和 #125 的执行
   ```

3. **调整计划**
   - 更新Milestone
   - 调整Project看板位置
   - 通知相关人员

### Q8: 如何管理跨项目的公共任务？

**A**: 几种方式：

**方式1: 创建独立Issue，多个项目引用**
```markdown
Issue #100: [TASK] 升级Node.js版本

关联项目:
- #1 电商平台升级
- #50 后台管理系统重构
- #80 数据分析平台

影响范围: 所有Node.js项目
```

**方式2: 使用"通用"项目**
```
Project: 基础设施改进
├─ #100 升级Node.js版本
├─ #101 配置CI/CD
└─ #102 统一日志系统
```

**方式3: 使用标签关联**
```
标签: cross-project, infra
在多个项目中搜索: label:cross-project
```

## 高级话题

### Q9: 如何处理循环依赖的任务？

**A**: 
1. **识别循环**
   ```
   #101 依赖 #102
   #102 依赖 #103
   #103 依赖 #101  ← 循环！
   ```

2. **打破循环**
   - 找到最弱的依赖关系
   - 创建接口/约定，解耦依赖
   - 分阶段实现

3. **重构任务**
   ```
   Phase 1:
   - #101-a 定义接口（不依赖#102）
   - #102-a 定义接口（不依赖#103）
   - #103-a 定义接口（不依赖#101）
   
   Phase 2:
   - #101-b 实现功能（依赖#102-a接口）
   - #102-b 实现功能（依赖#103-a接口）
   - #103-b 实现功能（依赖#101-a接口）
   ```

### Q10: 如何批量操作Issue？

**A**: 使用GitHub CLI：

```bash
# 批量添加标签
gh issue list --label "task" --state open --json number --jq '.[].number' | \
  xargs -I {} gh issue edit {} --add-label "needs-review"

# 批量关闭已完成的子任务
gh issue list --label "subtask" --search "完成" --json number --jq '.[].number' | \
  xargs -I {} gh issue close {}

# 批量更新Milestone
gh issue list --label "priority:high" --json number --jq '.[].number' | \
  xargs -I {} gh issue edit {} --milestone "Q1 Release"

# 批量分配
gh issue list --label "priority:high" --no-assignee --json number --jq '.[].number' | \
  xargs -I {} gh issue edit {} --add-assignee @backend-team
```

### Q11: 如何导出TODO数据进行分析？

**A**: 几种方式：

**方式1: GitHub CLI + jq**
```bash
# 导出所有Issue为JSON
gh issue list --state all --limit 1000 --json number,title,labels,state,createdAt,closedAt > issues.json

# 统计分析
jq '[.[] | select(.state=="CLOSED")] | length' issues.json  # 已完成数量
jq '[.[] | select(.labels[].name=="priority:high")] | length' issues.json  # 高优先级数量
```

**方式2: GitHub API**
```bash
curl -H "Authorization: token YOUR_TOKEN" \
  "https://api.github.com/repos/owner/repo/issues?state=all&per_page=100" > issues.json
```

**方式3: 使用第三方工具**
- Octobox
- GitHub Insights
- 自定义GitHub Actions导出到Google Sheets/Excel

### Q12: 如何处理长期运行的开放性任务？

**A**: 
1. **定期回顾**
   - 每月回顾一次
   - 评估是否仍然需要
   - 更新优先级

2. **设置虚拟里程碑**
   ```markdown
   ## 阶段性目标
   
   Phase 1 (Q1): 完成基础优化（预期收益20%）
   Phase 2 (Q2): 深度优化（预期收益40%）
   Phase 3 (Q3): 极致优化（预期收益60%）
   ```

3. **时间盒限制**
   ```markdown
   虽然是开放性任务，但设置时间盒：
   - 每周投入时间：4小时
   - 总时间预算：40小时
   - 如果超出预算，重新评估
   ```

4. **定期更新进度**
   ```markdown
   ## 进度日志
   
   2024-01-15: 优化查询A，性能提升20%
   2024-01-30: 优化查询B，性能提升15%
   2024-02-15: 添加缓存，性能提升30%
   ```

## 团队协作

### Q13: 多人协作时如何避免冲突？

**A**: 
1. **明确分工**
   ```markdown
   ## 任务分配
   
   #101 用户认证 - @alice
   #102 权限管理 - @bob
   #103 界面优化 - @carol
   ```

2. **每日同步**
   - 每天更新任务状态
   - 遇到阻塞及时沟通
   - 使用 @mention 提醒相关人员

3. **约定规范**
   ```markdown
   团队规范:
   - 每天17:00前更新任务状态
   - 添加标签时使用统一命名
   - Issue标题遵循约定格式
   - 重要决策记录在Issue评论中
   ```

### Q14: 如何防止Issue过多导致混乱？

**A**: 
1. **定期清理**
   ```bash
   # 每月清理一次
   # 关闭超过3个月未更新的开放性任务
   gh issue list --label "task-open" --state open --json number,updatedAt
   ```

2. **分层管理**
   ```
   活跃项目（<10个）→ 每天关注
   计划项目（<20个）→ 每周回顾
   归档项目（已完成）→ 关闭并添加"archived"标签
   ```

3. **使用Project看板**
   - 只在看板中显示活跃任务
   - 已完成任务自动移出看板

4. **善用搜索和过滤**
   ```
   is:open is:issue assignee:@me label:priority:high
   ```

## 工具和集成

### Q15: 推荐的移动端使用方式？

**A**: 
1. **GitHub官方App**（推荐）
   - 查看和更新Issue
   - 添加评论
   - 更新标签和状态

2. **Web移动版**
   - 功能完整
   - 可以在浏览器中使用

3. **第三方App**
   - GitTouch (iOS/Android)
   - FastHub (Android)

**使用技巧**:
- 碎片时间：查看通知、更新状态
- 完整操作：使用桌面端

### Q16: 如何与其他工具集成？

**A**: 

**集成Slack/Discord**:
```yaml
# GitHub Actions
on:
  issues:
    types: [opened, closed]
steps:
  - name: Notify Slack
    uses: slackapi/slack-github-action@v1
```

**集成Google Calendar**:
- 使用Zapier/IFTTT
- Milestone截止日期 → 日历事件

**集成IDE**:
- VS Code: GitHub Pull Requests and Issues插件
- JetBrains: 内置GitHub集成

**导出到其他工具**:
- 使用GitHub API导出数据
- 使用GitHub Actions定期同步

## 故障排除

### Q17: Issue编号不连续，怎么办？

**A**: 这是正常的！
- GitHub的Issue和PR共享编号序列
- 创建PR会占用编号
- 删除Issue也会留下空缺

这不影响使用，不需要处理。

### Q18: 不小心关闭了Issue怎么办？

**A**: 
1. **重新打开**
   - 进入Issue页面
   - 点击"Reopen issue"

2. **使用CLI**
   ```bash
   gh issue reopen 123
   ```

3. **查看历史**
   Issue的所有操作都有记录，不用担心丢失信息

### Q19: 标签太多了，怎么管理？

**A**: 
1. **分类管理**
   ```
   类型标签（必选一个）: project, task, subtask
   优先级标签（可选）: priority:*
   状态标签（可选）: status:*
   ```

2. **定期清理**
   - 删除未使用的标签
   - 合并相似的标签

3. **标签命名规范**
   - 使用前缀分组：`status:`, `type:`
   - 简短明了
   - 避免歧义

## 还有问题？

- 📖 查看完整文档: `docs/` 目录
- 💬 参与讨论: GitHub Discussions
- 📧 联系维护者: 创建Issue

---

文档持续更新中，欢迎贡献更多FAQ！
