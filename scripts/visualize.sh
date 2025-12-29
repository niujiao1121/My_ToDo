#!/bin/bash
# TODO 可视化脚本的便捷启动器

export GITHUB_TOKEN=$(cat /home/niujiao/github/github_token)

# 检查是否安装了 Python
if ! command -v python3 &> /dev/null && ! command -v python &> /dev/null; then
    echo "错误：未找到 Python"
    echo "请安装 Python 3.6 或更高版本"
    exit 1
fi

# 选择 Python 命令
PYTHON_CMD="python3"
if ! command -v python3 &> /dev/null; then
    PYTHON_CMD="python"
fi

# 检查是否设置了 GITHUB_TOKEN
if [ -z "$GITHUB_TOKEN" ]; then
    echo "⚠️  警告：未设置 GITHUB_TOKEN 环境变量"
    echo ""
    echo "请先设置 GitHub Token："
    echo "  export GITHUB_TOKEN=your_token_here"
    echo ""
    echo "如何获取 Token："
    echo "  1. 访问 https://github.com/settings/tokens"
    echo "  2. 点击 'Generate new token (classic)'"
    echo "  3. 勾选 'repo' 权限"
    echo "  4. 生成并复制 token"
    echo ""
    exit 1
fi

# 获取脚本所在目录
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# 检查 requests 库是否安装
$PYTHON_CMD -c "import requests" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "⚠️  requests 库未安装"
    echo "正在安装..."
    pip install requests || pip3 install requests
    if [ $? -ne 0 ]; then
        echo "❌ 安装失败，请手动安装：pip install requests"
        exit 1
    fi
    echo "✓ 安装成功"
    echo ""
fi

# 运行可视化脚本
echo "🚀 正在启动 TODO 可视化..."
echo ""
$PYTHON_CMD "$SCRIPT_DIR/visualize_todos.py" "$@"
