# AI TODO 自动创建系统 - 配置指南

本文档详细说明如何配置 AI TODO 自动创建功能。

## 📋 前置要求

- GitHub 仓库管理员权限（用于配置 Secrets）
- OpenAI API Key（用于调用 GPT-4o-mini 模型）

## 🔑 步骤 1：获取 OpenAI API Key

### 1.1 注册 OpenAI 账户

1. 访问 [OpenAI Platform](https://platform.openai.com/)
2. 如果没有账户，点击 "Sign up" 注册
3. 如果已有账户，点击 "Log in" 登录

### 1.2 创建 API Key

1. 登录后，点击右上角头像
2. 选择 "View API keys" 或直接访问 https://platform.openai.com/api-keys
3. 点击 "Create new secret key"
4. 给 Key 起个名字（如 "My_ToDo_AI"）
5. **重要**：立即复制生成的 API Key，关闭窗口后将无法再次查看
6. 将 API Key 保存在安全的地方

### 1.3 费用说明

- 本系统使用 `gpt-4o-mini` 模型，成本非常低
- 参考价格（2024年）：
  - 输入：$0.15 / 1M tokens
  - 输出：$0.60 / 1M tokens
- 平均每次 TODO 创建约消耗 500-1000 tokens
- **估算**：创建 1000 个 TODO 约花费 $0.50-1.00

## ⚙️ 步骤 2：配置 GitHub Secrets

### 2.1 进入仓库设置

1. 打开你的 GitHub 仓库
2. 点击顶部的 "Settings"（设置）标签
3. 在左侧菜单中找到 "Secrets and variables"
4. 点击展开，选择 "Actions"

### 2.2 添加 OPENAI_API_KEY

1. 点击右上角的 "New repository secret" 按钮
2. 在 "Name" 字段输入：`OPENAI_API_KEY`（必须完全一致）
3. 在 "Secret" 字段粘贴你在步骤 1 中获取的 OpenAI API Key
4. 点击 "Add secret" 保存

### 2.3 配置示意图

```
仓库 → Settings → Secrets and variables → Actions → New repository secret

Name: OPENAI_API_KEY
Secret: sk-proj-xxxxxxxxxxxxx...
```

## 🔐 步骤 3：配置工作流权限

### 3.1 检查 Actions 权限

1. 在仓库的 "Settings" 页面
2. 在左侧菜单找到 "Actions" → "General"
3. 滚动到 "Workflow permissions" 部分
4. 选择 "Read and write permissions"
5. 勾选 "Allow GitHub Actions to create and approve pull requests"
6. 点击 "Save" 保存

### 3.2 权限说明

AI TODO 工作流需要以下权限：
- **issues: write** - 创建和更新 Issues
- **contents: read** - 读取仓库内容

这些权限已在工作流文件中声明，但需要仓库级别的权限支持。

## ✅ 步骤 4：验证配置

### 4.1 测试 AI TODO 创建

1. **方式一：使用 AI 快速创建模板**
   - 进入仓库的 Issues 页面
   - 点击 "New issue"
   - 选择 "🤖 AI 快速创建 TODO" 模板
   - 在 "我要做的事" 下方输入：
     ```
     明天前完成测试任务，验证 AI TODO 系统是否正常工作
     ```
   - 点击 "Submit new issue"
   - 等待几秒钟，查看评论区是否出现 AI 创建的成功消息

2. **方式二：使用命令行**
   - 在任何 Issue 下评论：
     ```
     /todo 测试 AI TODO 功能是否正常
     ```
   - 等待几秒钟，查看是否自动创建新 Issue

### 4.2 预期结果

成功配置后，你应该会看到：

1. 在原 Issue 的评论区看到类似这样的消息：
   ```
   ✅ AI 已成功创建 TODO!
   
   📌 新 Issue: #X
   📝 标题: 完成测试任务
   ⏰ 截止日期: 2024-XX-XX
   🏷️ 优先级: medium
   
   [查看详情 →]
   ```

2. 自动创建的新 Issue 包含：
   - 结构化的任务描述
   - 验收标准清单
   - 任务步骤清单
   - 适当的标签（任务类型、优先级、模块）
   - 自动分配给创建者

## 🔍 故障排除

### 问题 1：工作流没有触发

**可能原因**：
- Issue 没有添加 `ai-todo-inbox` 标签
- 评论不是以 `/todo` 开头

**解决方法**：
- 使用 AI 快速创建模板（自动添加标签）
- 或手动给 Issue 添加 `ai-todo-inbox` 标签
- 确保评论格式正确：`/todo 任务内容`

### 问题 2：提示 "OpenAI API Key 未配置"

**可能原因**：
- GitHub Secrets 中没有添加 `OPENAI_API_KEY`
- Secret 名称拼写错误（必须完全一致）

**解决方法**：
1. 检查 Settings → Secrets and variables → Actions
2. 确认存在名为 `OPENAI_API_KEY` 的 Secret
3. 如果不存在或名称错误，重新添加

### 问题 3：提示权限不足

**可能原因**：
- 不是仓库成员或协作者
- Actions 权限配置不正确

**解决方法**：
1. 确认你是仓库的所有者、管理员或协作者
2. 检查 Actions 权限设置（见步骤 3）
3. 如果是私有仓库，确保 Actions 已启用

### 问题 4：AI 解析失败

**可能原因**：
- OpenAI API Key 无效或过期
- OpenAI 账户余额不足
- 网络连接问题

**解决方法**：
1. 验证 API Key 是否有效：
   - 访问 https://platform.openai.com/api-keys
   - 检查 Key 状态
2. 检查 OpenAI 账户余额：
   - 访问 https://platform.openai.com/account/billing
   - 确保有足够余额
3. 如果持续失败，系统会创建基本的 TODO（不包含 AI 解析）

### 问题 5：创建的 Issue 格式不理想

**原因**：
- 用户输入太简单或不够明确
- AI 理解有偏差

**解决方法**：
1. 提供更详细的任务描述
2. 明确指出截止日期、优先级、模块等信息
3. AI 创建后，手动编辑补充完善信息
4. 参考 `examples/ai-todo-examples.md` 中的最佳实践

## 📊 监控和维护

### 查看工作流运行日志

1. 进入仓库的 "Actions" 标签
2. 找到 "AI 自动创建 TODO" 工作流
3. 点击具体的运行记录
4. 查看详细日志，包括：
   - OpenAI API 调用
   - AI 响应内容
   - Issue 创建过程
   - 错误信息（如果有）

### 成本控制

1. **监控 API 使用量**：
   - 访问 https://platform.openai.com/account/usage
   - 查看每日/每月的 token 使用量和费用

2. **设置用量限制**：
   - 在 OpenAI Platform 设置每月最大消费限额
   - 避免意外超支

3. **优化使用**：
   - 简单任务可以手动创建
   - 复杂或批量任务使用 AI 创建
   - 定期清理不需要的 API Keys

## 🔄 更新和升级

### 更新 API Key

如果需要更换 API Key：
1. 在 OpenAI Platform 创建新的 Key
2. 在 GitHub Secrets 中编辑 `OPENAI_API_KEY`
3. 粘贴新的 Key
4. 可选：在 OpenAI Platform 删除旧 Key

### 升级工作流

当有新版本的工作流时：
1. 查看 `.github/workflows/ai-create-todo.yml` 的更新日志
2. 测试新功能
3. 如果有新的配置要求，按照说明更新

## 🆘 获取帮助

如果以上方法都无法解决问题：

1. **查看示例**：参考 `examples/ai-todo-examples.md`
2. **查看文档**：阅读 `README.md` 和 `docs/` 目录下的其他文档
3. **提交 Issue**：在仓库中创建新 Issue 描述问题
4. **查看 Discussions**：在 GitHub Discussions 中搜索或提问

## 🎓 最佳实践

1. **安全性**：
   - 不要将 API Key 提交到代码中
   - 定期轮换 API Key
   - 只给必要的人员分配仓库权限

2. **成本优化**：
   - 提供清晰的输入，减少 AI 重试
   - 简单任务使用标准模板
   - 复杂任务使用 AI 创建

3. **使用技巧**：
   - 在输入中明确说明日期、优先级、模块
   - 创建后检查并补充 AI 生成的内容
   - 利用 `/todo` 命令快速创建临时任务

---

配置完成后，你就可以享受 AI 驱动的 TODO 管理了！🎉
