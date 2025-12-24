#!/usr/bin/env python3
"""
TODO 可视化脚本

此脚本从 GitHub API 获取所有 Issues，分析它们的父子关系，并以树状结构可视化展示。
显示每个 TODO 的：
- 标题
- 优先级
- 截止日期
- 状态
- 模块
- 从属关系

使用方法：
1. 设置环境变量 GITHUB_TOKEN（GitHub Personal Access Token）
2. 运行脚本：python visualize_todos.py [--owner OWNER] [--repo REPO]

示例：
    export GITHUB_TOKEN=your_token_here
    python visualize_todos.py --owner niujiao1121 --repo My_ToDo
    
或者直接在当前仓库运行：
    python visualize_todos.py
"""

import os
import sys
import json
import re
from collections import defaultdict
from datetime import datetime
import argparse

try:
    import requests
except ImportError:
    print("错误：需要安装 requests 库")
    print("请运行：pip install requests")
    sys.exit(1)


class TodoVisualizer:
    def __init__(self, owner, repo, token):
        self.owner = owner
        self.repo = repo
        self.token = token
        self.api_base = "https://api.github.com"
        self.headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json"
        }
        self.issues = []
        self.issue_map = {}
        self.children_map = defaultdict(list)
        
    def fetch_issues(self):
        """获取所有 Issues"""
        print(f"正在获取 {self.owner}/{self.repo} 的所有 Issues...")
        
        page = 1
        per_page = 100
        
        while True:
            url = f"{self.api_base}/repos/{self.owner}/{self.repo}/issues"
            params = {
                "state": "all",
                "per_page": per_page,
                "page": page,
                "sort": "created",
                "direction": "desc"
            }
            
            response = requests.get(url, headers=self.headers, params=params)
            
            if response.status_code != 200:
                print(f"错误：无法获取 Issues (状态码: {response.status_code})")
                print(f"响应：{response.text}")
                sys.exit(1)
            
            data = response.json()
            if not data:
                break
                
            # 过滤掉 Pull Requests（GitHub API 将 PR 也作为 Issue 返回）
            issues = [issue for issue in data if "pull_request" not in issue]
            self.issues.extend(issues)
            
            print(f"  已获取 {len(self.issues)} 个 Issues...")
            
            # 如果返回的数量少于 per_page，说明已经是最后一页
            if len(data) < per_page:
                break
                
            page += 1
        
        print(f"✓ 共获取 {len(self.issues)} 个 Issues\n")
        
    def parse_parent_issue(self, body):
        """从 Issue body 中提取父 Issue 编号"""
        if not body:
            return None
            
        # 匹配各种父任务标记格式
        patterns = [
            r'\*\*Parent Issue\*\*:\s*#(\d+)',
            r'Parent Issue:\s*#(\d+)',
            r'父任务:\s*#(\d+)',
            r'🔗 父任务\s*\n\s*\*\*Parent Issue\*\*:\s*#(\d+)',
        ]
        
        for pattern in patterns:
            match = re.search(pattern, body, re.IGNORECASE)
            if match:
                return int(match.group(1))
        
        return None
    
    def build_hierarchy(self):
        """构建父子关系层级结构"""
        print("正在分析 TODO 层级关系...")
        
        # 创建 issue_map 和解析父子关系
        for issue in self.issues:
            issue_num = issue["number"]
            self.issue_map[issue_num] = issue
            
            # 解析父任务
            parent = self.parse_parent_issue(issue.get("body", ""))
            if parent:
                self.children_map[parent].append(issue_num)
                issue["parent"] = parent
            else:
                issue["parent"] = None
        
        print(f"✓ 已分析完成\n")
    
    def get_priority(self, issue):
        """获取优先级"""
        labels = [label["name"] for label in issue.get("labels", [])]
        
        priority_map = {
            "priority:critical": ("🔴", "紧急"),
            "priority:high": ("🟠", "重要"),
            "priority:medium": ("🟡", "中等"),
            "priority:low": ("🟢", "低"),
        }
        
        for label in labels:
            if label in priority_map:
                return priority_map[label]
        
        return ("⚪", "未设置")
    
    def get_module(self, issue):
        """获取模块"""
        labels = [label["name"] for label in issue.get("labels", [])]
        
        module_map = {
            "module:frontend": "前端",
            "module:backend": "后端",
            "module:database": "数据库",
            "module:devops": "运维",
            "module:design": "设计",
            "module:docs": "文档",
            "module:testing": "测试",
        }
        
        for label in labels:
            if label in module_map:
                return module_map[label]
        
        return None
    
    def get_task_type(self, issue):
        """获取任务类型"""
        labels = [label["name"] for label in issue.get("labels", [])]
        
        if "project" in labels:
            return "📦 项目"
        elif "subtask" in labels:
            return "📌 子任务"
        elif "task-with-deadline" in labels:
            return "⏰ 有期限"
        elif "task-open" in labels:
            return "🔓 开放性"
        
        return "📋 任务"
    
    def get_due_date(self, issue):
        """获取截止日期"""
        body = issue.get("body", "")
        if not body:
            return None
        
        # 尝试从 body 中提取截止日期
        patterns = [
            r'\*\*截止日期\*\*:\s*(\d{4}-\d{2}-\d{2})',
            r'截止日期:\s*(\d{4}-\d{2}-\d{2})',
        ]
        
        for pattern in patterns:
            match = re.search(pattern, body)
            if match:
                return match.group(1)
        
        return None
    
    def format_issue(self, issue, show_details=True):
        """格式化单个 Issue 的显示"""
        number = issue["number"]
        title = issue["title"]
        state = "✓" if issue["state"] == "closed" else "◯"
        
        priority_icon, priority_text = self.get_priority(issue)
        task_type = self.get_task_type(issue)
        module = self.get_module(issue)
        due_date = self.get_due_date(issue)
        
        # 基本信息
        result = f"{state} #{number} {title}"
        
        if show_details:
            details = []
            details.append(f"{task_type}")
            details.append(f"{priority_icon}{priority_text}")
            if module:
                details.append(f"[{module}]")
            if due_date:
                details.append(f"⏰{due_date}")
            
            if details:
                result += f" ({', '.join(details)})"
        
        return result
    
    def print_tree(self, issue_num, prefix="", is_last=True, visited=None):
        """递归打印树状结构"""
        if visited is None:
            visited = set()
        
        if issue_num in visited:
            # 避免循环引用
            return
        
        visited.add(issue_num)
        
        issue = self.issue_map.get(issue_num)
        if not issue:
            return
        
        # 打印当前节点
        connector = "└── " if is_last else "├── "
        print(prefix + connector + self.format_issue(issue))
        
        # 打印子节点
        children = self.children_map.get(issue_num, [])
        children.sort()  # 按编号排序
        
        for i, child_num in enumerate(children):
            is_last_child = (i == len(children) - 1)
            extension = "    " if is_last else "│   "
            self.print_tree(child_num, prefix + extension, is_last_child, visited)
    
    def visualize(self):
        """可视化所有 TODOs"""
        print("=" * 80)
        print(f"📊 TODO 层级结构可视化 - {self.owner}/{self.repo}")
        print("=" * 80)
        print()
        
        # 找出所有根节点（没有父任务的 Issue）
        root_issues = [
            issue["number"] for issue in self.issues 
            if not issue.get("parent")
        ]
        
        if not root_issues:
            print("没有找到任何 Issue")
            return
        
        # 按任务类型分组
        projects = []
        tasks = []
        
        for issue_num in root_issues:
            issue = self.issue_map[issue_num]
            labels = [label["name"] for label in issue.get("labels", [])]
            
            if "project" in labels:
                projects.append(issue_num)
            else:
                tasks.append(issue_num)
        
        # 打印项目
        if projects:
            print("🎯 项目列表")
            print("-" * 80)
            for i, issue_num in enumerate(sorted(projects, reverse=True)):
                is_last = (i == len(projects) - 1) and not tasks
                self.print_tree(issue_num, "", is_last)
            print()
        
        # 打印独立任务
        if tasks:
            print("📋 独立任务列表")
            print("-" * 80)
            for i, issue_num in enumerate(sorted(tasks, reverse=True)):
                is_last = (i == len(tasks) - 1)
                self.print_tree(issue_num, "", is_last)
            print()
        
        # 统计信息
        self.print_statistics()
    
    def print_statistics(self):
        """打印统计信息"""
        print("=" * 80)
        print("📈 统计信息")
        print("=" * 80)
        
        total = len(self.issues)
        open_count = sum(1 for issue in self.issues if issue["state"] == "open")
        closed_count = total - open_count
        
        # 按优先级统计
        priority_stats = defaultdict(int)
        for issue in self.issues:
            if issue["state"] == "open":  # 只统计未完成的
                _, priority_text = self.get_priority(issue)
                priority_stats[priority_text] += 1
        
        # 按模块统计
        module_stats = defaultdict(int)
        for issue in self.issues:
            if issue["state"] == "open":  # 只统计未完成的
                module = self.get_module(issue)
                if module:
                    module_stats[module] += 1
        
        # 即将到期的任务
        upcoming_deadlines = []
        today = datetime.now().date()
        for issue in self.issues:
            if issue["state"] == "open":
                due_date = self.get_due_date(issue)
                if due_date:
                    try:
                        due = datetime.strptime(due_date, "%Y-%m-%d").date()
                        days_left = (due - today).days
                        if days_left >= 0 and days_left <= 7:
                            upcoming_deadlines.append((issue, due_date, days_left))
                    except:
                        pass
        
        print(f"\n总任务数: {total}")
        print(f"  - 进行中/未完成: {open_count}")
        print(f"  - 已完成: {closed_count}")
        
        if priority_stats:
            print(f"\n按优先级（未完成）:")
            for priority in ["紧急", "重要", "中等", "低", "未设置"]:
                count = priority_stats.get(priority, 0)
                if count > 0:
                    print(f"  - {priority}: {count}")
        
        if module_stats:
            print(f"\n按模块（未完成）:")
            for module, count in sorted(module_stats.items(), key=lambda x: -x[1]):
                print(f"  - {module}: {count}")
        
        if upcoming_deadlines:
            print(f"\n⚠️  即将到期的任务（7天内）:")
            upcoming_deadlines.sort(key=lambda x: x[2])
            for issue, due_date, days_left in upcoming_deadlines[:5]:  # 只显示前5个
                days_text = "今天" if days_left == 0 else f"{days_left}天后"
                print(f"  - #{issue['number']}: {issue['title']} (截止: {due_date}, {days_text})")
        
        print()


def main():
    parser = argparse.ArgumentParser(
        description="可视化 GitHub TODO 结构",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  %(prog)s --owner niujiao1121 --repo My_ToDo
  %(prog)s  (在 git 仓库中自动检测)
        """
    )
    parser.add_argument("--owner", help="GitHub 仓库所有者")
    parser.add_argument("--repo", help="GitHub 仓库名称")
    parser.add_argument("--token", help="GitHub Personal Access Token（也可以通过 GITHUB_TOKEN 环境变量设置）")
    
    args = parser.parse_args()
    
    # 获取 token
    token = args.token or os.environ.get("GITHUB_TOKEN")
    if not token:
        print("错误：需要提供 GitHub Token")
        print("请设置环境变量 GITHUB_TOKEN 或使用 --token 参数")
        print("\n如何获取 Token:")
        print("1. 访问 https://github.com/settings/tokens")
        print("2. 点击 'Generate new token (classic)'")
        print("3. 勾选 'repo' 权限")
        print("4. 生成并复制 token")
        sys.exit(1)
    
    # 获取 owner 和 repo
    owner = args.owner
    repo = args.repo
    
    # 如果未提供，尝试从 git 仓库中检测
    if not owner or not repo:
        try:
            import subprocess
            result = subprocess.run(
                ["git", "config", "--get", "remote.origin.url"],
                capture_output=True,
                text=True,
                check=True
            )
            url = result.stdout.strip()
            
            # 解析 GitHub URL
            match = re.search(r'github\.com[:/]([^/]+)/([^/\.]+)', url)
            if match:
                owner = owner or match.group(1)
                repo = repo or match.group(2)
                print(f"自动检测到仓库: {owner}/{repo}\n")
            else:
                print("错误：无法从 git remote URL 解析仓库信息")
                print("请使用 --owner 和 --repo 参数指定")
                sys.exit(1)
        except:
            print("错误：请提供 --owner 和 --repo 参数")
            sys.exit(1)
    
    # 创建可视化器并运行
    visualizer = TodoVisualizer(owner, repo, token)
    visualizer.fetch_issues()
    visualizer.build_hierarchy()
    visualizer.visualize()


if __name__ == "__main__":
    main()
