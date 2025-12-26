# Testing Guide for New Features

This document provides step-by-step instructions for manually testing the two new features: Batch TODO Creation and Project Label Inheritance.

## Prerequisites

1. Make sure you have the `DASHSCOPE_API_KEY` configured in repository secrets
2. Make sure workflow permissions are set to "Read and write permissions"
3. You should be a repository member or collaborator

## Test 1: Batch TODO Creation

### Test Case 1.1: Multiple /todo commands in one comment

**Steps:**
1. Create a new issue (any type)
2. Add a comment with multiple `/todo` commands:
   ```
   /todo 实现前端登录页面，明天完成
   /todo 实现后端认证API，2天完成
   /todo 编写测试用例，1天
   ```
3. Wait for the workflow to complete (usually 10-30 seconds)

**Expected Results:**
- System posts a message: "🔄 检测到 3 个 TODO，正在批量创建..."
- Three separate issues are created
- All three issues are linked as subtasks to the original issue
- System posts a summary message showing:
  - Statistics: "成功 3 个，失败 0 个"
  - List of created issues with links

**Validation:**
- Check that 3 new issues were created
- Check that each issue has appropriate labels (subtask、priority)
- Check that each issue is linked in the parent issue's subtask list
- Check that each issue body contains a link back to the original issue

### Test Case 1.2: Single /todo command (backward compatibility)

**Steps:**
1. Create or use an existing issue
2. Add a comment with a single `/todo` command:
   ```
   /todo 完成数据库备份脚本，下周一交付
   ```
3. Wait for the workflow to complete

**Expected Results:**
- One issue is created
- System posts a single TODO success message (not the batch summary)
- The message format should be the same as before the feature was added

**Validation:**
- Check that the behavior is identical to the old version
- Check that the message format is correct

### Test Case 1.3: Mixed format (should handle gracefully)

**Steps:**
1. Create an issue
2. Add a comment:
   ```
   /todo 任务1，明天完成
   一些其他文本
   /todo 任务2，后天完成
   /todo 任务3，下周完成
   ```
3. Wait for the workflow to complete

**Expected Results:**
- Three issues are created (only lines starting with `/todo`)
- Other text is ignored
- Batch summary is shown

## Test 2: Project Label Inheritance

### Test Case 2.1: Create project with custom labels

**Steps:**
1. Create a new issue using the "项目/大型任务" template
2. Fill in the project details and in the "项目标签" field, add:
   ```
   sprint-1, team-alpha, q1-2024
   ```
3. Add the `project` label
4. Submit the issue (let's say it's #100)

**Expected Results:**
- Issue #100 is created with the project template

**Validation:**
- The issue body should contain the project labels in the correct section

### Test Case 2.2: Create subtask that inherits project labels

**Steps:**
1. On the project issue created in Test Case 2.1 (e.g., #100), add a comment:
   ```
   /todo 实现用户登录功能，后端开发，3天
   ```
2. Wait for the workflow to complete

**Expected Results:**
- A new subtask issue is created (e.g., #101)
- The subtask has the following labels:
  - `subtask` (automatic)
  - `task-with-deadline` or `task-open` (based on deadline)
  - `priority:medium` (or as inferred by AI)
  - `sprint-1` (inherited from project)
  - `team-alpha` (inherited from project)
  - `q1-2024` (inherited from project)

**Validation:**
- Check that all three project labels are present on the subtask
- Check that other automatic labels are also present
- Check that the subtask is linked to the parent project

### Test Case 2.3: Multiple subtasks inherit the same labels

**Steps:**
1. On the same project issue (#100), add another comment:
   ```
   /todo 设计用户界面原型，前端开发，明天完成
   /todo 编写API文档，文档编写，2天
   ```
2. Wait for the workflow to complete

**Expected Results:**
- Two new subtask issues are created
- Both subtasks inherit all three project labels: `sprint-1`, `team-alpha`, `q1-2024`
- Each subtask also has its own priority label based on AI inference

**Validation:**
- Check that both subtasks have the project labels
- Check that they have appropriate priority labels based on content

### Test Case 2.4: Project without custom labels (backward compatibility)

**Steps:**
1. Create a project issue without filling in the "项目标签" field
2. Create a subtask using `/todo` command

**Expected Results:**
- Subtask is created normally
- Subtask does not have any extra labels beyond the automatic ones
- No errors occur

**Validation:**
- Check that the feature works gracefully when no project labels are defined

### Test Case 2.5: Invalid label format

**Steps:**
1. Create a project with labels containing spaces or special characters:
   ```
   Sprint 1, Team Alpha, Q1-2024!
   ```
2. Create a subtask

**Expected Results:**
- Labels are parsed and applied (spaces might be handled differently by GitHub)
- Subtask is created successfully even if some labels are invalid

**Validation:**
- Check which labels were successfully applied
- Check that the workflow doesn't fail

## Test 3: Combined Features Test

### Test Case 3.1: Batch create subtasks with label inheritance

**Steps:**
1. Create a project issue (#200) with labels:
   ```
   project-x, milestone-1
   ```
2. Add a comment with multiple `/todo` commands:
   ```
   /todo 任务A，前端开发，明天完成
   /todo 任务B，后端开发，2天
   /todo 任务C，测试，3天
   ```
3. Wait for the workflow to complete

**Expected Results:**
- Three subtask issues are created
- All three inherit `project-x` and `milestone-1` labels
- All three are linked to #200
- Batch summary is displayed

**Validation:**
- Check that all three subtasks have the project labels
- Check that the batch creation summary is correct
- Check that all subtasks are linked in the parent issue

## Test 4: Error Handling

### Test Case 4.1: Invalid parent issue number

**Steps:**
1. Create an issue
2. Comment:
   ```
   /todo 这是一个任务，属于 #99999
   ```
3. Wait for workflow

**Expected Results:**
- Issue is created
- Warning about failing to update parent task (issue #99999 doesn't exist)
- But the issue creation itself succeeds

### Test Case 4.2: Batch with some failures

**Steps:**
1. Test by temporarily breaking something (e.g., invalid API key)
2. Or by creating tasks with very long titles that might exceed limits

**Expected Results:**
- Failed TODOs are listed in the summary
- Successful TODOs are still created
- Summary shows both successes and failures

## Reporting Test Results

After testing, report the results using this template:

```
## Test Results

### Batch TODO Creation
- [ ] Test Case 1.1: Multiple /todo commands - PASS/FAIL
- [ ] Test Case 1.2: Single /todo (backward compat) - PASS/FAIL
- [ ] Test Case 1.3: Mixed format - PASS/FAIL

### Project Label Inheritance
- [ ] Test Case 2.1: Create project with labels - PASS/FAIL
- [ ] Test Case 2.2: Subtask inherits labels - PASS/FAIL
- [ ] Test Case 2.3: Multiple subtasks inherit labels - PASS/FAIL
- [ ] Test Case 2.4: Project without labels - PASS/FAIL
- [ ] Test Case 2.5: Invalid label format - PASS/FAIL

### Combined Features
- [ ] Test Case 3.1: Batch + label inheritance - PASS/FAIL

### Error Handling
- [ ] Test Case 4.1: Invalid parent issue - PASS/FAIL
- [ ] Test Case 4.2: Batch with failures - PASS/FAIL

### Issues Found
(List any bugs or unexpected behaviors)

### Recommendations
(List any improvements or changes needed)
```

## Manual Verification Checklist

After running all tests, verify:

- [ ] No workflow errors in Actions tab
- [ ] All created issues have correct labels
- [ ] Parent-child relationships are properly established
- [ ] Project labels are correctly inherited
- [ ] Batch creation summary messages are accurate
- [ ] Backward compatibility is maintained
- [ ] Error messages are helpful and informative
- [ ] Documentation accurately describes the features
