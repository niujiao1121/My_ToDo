# Tag Inheritance and Configuration Changes

## Overview

This document describes the changes made to implement tag inheritance for subtasks and create a centralized tag configuration system.

## Changes Made

### 1. Centralized Tag Configuration

**File Created**: `.github/tags-config.json`

A new centralized configuration file that defines all tags used in the project. This file serves as the single source of truth for:
- Tag definitions (name, description, color)
- Tag categories (task types, priorities, statuses, types, other)
- System labels list (for distinguishing system vs. custom project labels)

**Benefits**:
- Easy to update tags across the project from one location
- Clear documentation of all available tags
- Helps workflows distinguish between system and custom project labels

**File Created**: `.github/README_TAGS.md`

Documentation for the tag configuration system, including:
- How to use the tag configuration
- How tag inheritance works
- How to modify tags

### 2. Tag Inheritance Implementation

**Modified File**: `.github/workflows/auto-update-subtasks.yml`

Added tag inheritance logic for manually created subtasks:
1. Extracts project labels from parent task body (from "项目标签" field)
2. Inherits custom labels from parent task if it's a project type
3. Automatically adds inherited labels to the subtask
4. Logs all tag inheritance operations for debugging

**Already Implemented**: `.github/workflows/ai-create-todo.yml`

The AI workflow already had tag inheritance logic, which continues to work:
- Extracts project labels from parent task body
- Inherits custom labels from project-type parents
- Adds inherited labels to AI-created subtasks

**How It Works**:
- When a subtask is created (either manually or via AI), the workflow checks the parent task
- If the parent has "项目标签" in its body, those labels are extracted
- If the parent is a project type, any custom (non-system) labels are also inherited
- All inherited labels are automatically added to the new subtask

### 3. Removed ai-generated Tag Dependency

The `ai-generated` tag has been removed from the project as requested:

**Modified Files**:
- `.github/labels.yml` - Removed ai-generated label definition
- `.github/workflows/auto-update-subtasks.yml` - Removed ai-generated check
- `.github/workflows/ai-create-todo.yml` - Removed ai-generated from labels (3 instances)
- `FEATURE_SUMMARY.md` - Removed ai-generated mention
- `TESTING_NEW_FEATURES.md` - Removed ai-generated mentions (2 instances)
- `examples/batch-todo-and-labels-example.md` - Removed ai-generated mention
- `WORKFLOW_DIAGRAMS.md` - Removed ai-generated mentions (3 instances)
- `IMPLEMENTATION_DETAILS.md` - Removed ai-generated from system labels list

**Rationale**:
Since most TODOs in the project are AI-generated, the tag doesn't provide useful filtering capability and was redundant.

## Usage Examples

### Creating a Project with Custom Tags

1. Create a project issue using the "项目/大型任务" template
2. In the "项目标签" field, add your custom tags:
   ```
   sprint-1, team-frontend, v2.0
   ```
3. When you create subtasks for this project, they will automatically inherit these tags

### Creating a Subtask

**Option 1: Using AI (Recommended)**
```
/todo 实现用户登录功能，属于 #123
```
The subtask will automatically:
- Be linked to parent #123
- Inherit all project tags from parent #123
- Have appropriate task type and priority labels

**Option 2: Manual Creation**
1. Create an issue using the "子任务" template
2. Set the parent issue reference: `**Parent Issue**: #123`
3. The auto-update-subtasks workflow will:
   - Add the subtask to the parent's subtask list
   - Inherit all project tags from the parent

### Filtering by Project Tags

After inheriting tags, you can easily filter issues:
- `label:sprint-1` - All tasks in sprint 1
- `label:team-frontend` - All frontend team tasks
- `label:v2.0` - All tasks for version 2.0
- `label:sprint-1 label:team-frontend` - Sprint 1 frontend tasks

## Testing

To verify the changes work correctly:

1. **Test Tag Inheritance**:
   - Create a project issue with custom tags in the "项目标签" field
   - Create a subtask referencing that project
   - Verify the subtask automatically receives all project tags

2. **Test Without ai-generated**:
   - Create an AI TODO
   - Verify it works correctly without the ai-generated label
   - Check that workflows don't reference or depend on ai-generated

3. **Test Tag Configuration**:
   - Verify `.github/tags-config.json` is valid JSON
   - Verify all workflows use the system labels list correctly

## Migration Notes

**For Existing Issues**:
- Existing issues with the `ai-generated` label can keep it (it won't cause issues)
- No migration is needed - the label simply won't be added to new issues
- The label can be removed from GitHub if desired (it's not in labels.yml)

**For Workflows**:
- All workflows now work without the ai-generated tag
- Tag inheritance is automatic for all new subtasks
- No manual intervention required

## Future Enhancements

Possible future improvements:
1. Add a script to bulk-apply project tags to existing subtasks
2. Add validation to ensure project tags follow naming conventions
3. Add support for hierarchical tag inheritance (grandparent -> parent -> subtask)
4. Create a web UI for managing the tag configuration
