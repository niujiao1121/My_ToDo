# Tag Configuration

This directory contains the centralized tag configuration file for the My_ToDo project.

## Files

### tags-config.json

This is the central configuration file that defines all tags used in the project. It provides:

1. **Tag Definitions**: All available tags organized by category
   - Task Types (project, epic, task-with-deadline, task-open, subtask, ai-todo-inbox)
   - Priorities (critical, high, medium, low)
   - Statuses (planning, in-progress, blocked, review, testing)
   - Types (feature, enhancement, bug, refactoring, documentation, research)
   - Other labels (help-wanted, good-first-issue, duplicate, wontfix, archived)

2. **System Labels List**: A flat list of all system-defined labels used by workflows to distinguish between system and custom project labels

## Usage

### For Workflows

Workflows should reference the `systemLabels` array in `tags-config.json` to determine which labels are system-defined vs. custom project labels.

Example:
```javascript
// Load system labels from tags config
const systemLabels = [
  'project', 'epic', 'task-with-deadline', 'task-open', 'subtask', 'ai-todo-inbox',
  'priority:critical', 'priority:high', 'priority:medium', 'priority:low',
  // ... etc
];

// Identify custom project labels
const customLabels = allLabels.filter(label => !systemLabels.includes(label));
```

### For Label Management

The `labels.yml` file is synchronized with `tags-config.json` to ensure consistency. When updating tags:

1. Update `tags-config.json` with the new tag definition
2. Update `labels.yml` with the corresponding label
3. Update the `systemLabels` array in `tags-config.json` if adding a new system label

## Tag Inheritance

Subtasks automatically inherit project-related tags from their parent tasks:

1. **From Parent Body**: Tags specified in the "项目标签" (Project Labels) field of the parent task
2. **From Parent Labels**: Custom labels (non-system) attached to parent project issues

This allows for easy categorization and filtering of tasks by:
- Sprint (e.g., `sprint-1`, `sprint-2`)
- Team (e.g., `team-frontend`, `team-backend`)
- Version (e.g., `v1.0`, `v2.0`)
- Custom categories

## Modifying Tags

To add or modify tags:

1. Edit `tags-config.json`:
   - Add the new tag definition in the appropriate category
   - Update the `systemLabels` array if it's a system label
   - Update the tag color and description

2. Edit `.github/labels.yml`:
   - Add the corresponding label entry

3. Update workflows if needed:
   - If the tag affects workflow behavior, update the relevant workflow files

4. Sync labels to GitHub:
   - GitHub Actions will automatically sync labels based on `labels.yml`
   - Or manually sync using the GitHub CLI: `gh label sync -f .github/labels.yml`
