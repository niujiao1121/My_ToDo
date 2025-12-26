"""Central tag configuration loader for project-wide logic."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, Mapping, Optional

DEFAULT_TAG_CONFIG_PATH = Path(__file__).resolve().parent.parent / ".github" / "tags-config.json"


class TagConfig:
    """Load tag names from the shared configuration file.

    The loader provides consistent access to label names used across scripts so the
    same configuration can drive GitHub label usage and logic checks without
    hardcoding tag strings in multiple places.
    """

    DEFAULT_TAGS: Mapping[str, Mapping[str, str]] = {
        "taskTypes": {
            "project": "project",
            "epic": "epic",
            "taskWithDeadline": "task-with-deadline",
            "taskOpen": "task-open",
            "subtask": "subtask",
            "aiTodoInbox": "ai-todo-inbox",
        },
        "priorities": {
            "critical": "priority:critical",
            "high": "priority:high",
            "medium": "priority:medium",
            "low": "priority:low",
        },
        "statuses": {
            "planning": "status:planning",
            "inProgress": "status:in-progress",
            "blocked": "status:blocked",
            "review": "status:review",
            "testing": "status:testing",
        },
        "types": {
            "feature": "type:feature",
            "enhancement": "type:enhancement",
            "bug": "type:bug",
            "refactoring": "type:refactoring",
            "documentation": "type:documentation",
            "research": "type:research",
        },
    }

    DEFAULT_SYSTEM_LABELS = (
        list(DEFAULT_TAGS["taskTypes"].values())
        + list(DEFAULT_TAGS["priorities"].values())
        + list(DEFAULT_TAGS["statuses"].values())
        + list(DEFAULT_TAGS["types"].values())
        + ["help-wanted", "good-first-issue", "duplicate", "wontfix", "archived"]
    )

    def __init__(self, path: Optional[Path] = None):
        self.path = Path(path) if path else DEFAULT_TAG_CONFIG_PATH
        self.data = self._load()
        self.tags = self._build_tags()
        self.system_labels = self._build_system_labels()

    def _load(self) -> Dict:
        if not self.path.exists():
            return {}

        try:
            with self.path.open("r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {}

    def _build_tags(self) -> Dict[str, Dict[str, str]]:
        tags_data = self.data.get("tags", {}) if isinstance(self.data, dict) else {}
        merged: Dict[str, Dict[str, str]] = {}

        for category, defaults in self.DEFAULT_TAGS.items():
            merged_category = dict(defaults)
            configured = tags_data.get(category, {})
            if isinstance(configured, dict):
                for key, info in configured.items():
                    if isinstance(info, dict):
                        name = info.get("name")
                        if name:
                            merged_category[key] = name
            merged[category] = merged_category

        return merged

    def _build_system_labels(self) -> list[str]:
        labels = self.data.get("systemLabels") if isinstance(self.data, dict) else None
        if isinstance(labels, list) and all(isinstance(label, str) for label in labels):
            return labels
        return list(self.DEFAULT_SYSTEM_LABELS)

    def labels_for(self, category: str) -> Dict[str, str]:
        """Return resolved label names for a category (e.g., "priorities")."""
        return self.tags.get(category, {})

    def label(self, category: str, key: str) -> Optional[str]:
        """Return a specific label name from the resolved configuration."""
        return self.tags.get(category, {}).get(key)

    @property
    def priority_labels(self) -> Dict[str, str]:
        return self.labels_for("priorities")

    @property
    def task_type_labels(self) -> Dict[str, str]:
        task_types = self.labels_for("taskTypes")
        return {
            "project": task_types.get("project"),
            "epic": task_types.get("epic"),
            "task_with_deadline": task_types.get("taskWithDeadline"),
            "task_open": task_types.get("taskOpen"),
            "subtask": task_types.get("subtask"),
            "ai_todo_inbox": task_types.get("aiTodoInbox"),
        }
