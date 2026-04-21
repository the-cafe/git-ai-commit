"""
Git diff 解析模块

将原始 git diff 输出解析为结构化的 Python 数据，用于变更分类和提交信息生成。
"""

from unidiff import PatchSet, UnidiffParseError
from ai_commit_msg.core.prompt import NOISE_FILE_PATTERNS


def _is_noise_file(path):
    """
    检查文件路径是否匹配噪音文件模式

    Args:
        path: 文件路径字符串

    Returns:
        bool: 如果是噪音文件返回 True，否则返回 False
    """
    for pattern in NOISE_FILE_PATTERNS:
        if path.endswith(pattern):
            return True
    return False


def _get_change_type(patched_file):
    """
    获取文件的变更类型

    Args:
        patched_file: unidiff.PatchedFile 对象

    Returns:
        str: 变更类型 ("added" | "modified" | "deleted" | "renamed")
    """
    if patched_file.is_added_file:
        return "added"
    elif patched_file.is_removed_file:
        return "deleted"
    elif patched_file.is_rename:
        return "renamed"
    else:
        return "modified"


def parse_diff(raw_diff):
    """
    解析原始 git diff 输出为结构化数据

    Args:
        raw_diff: git diff 命令的原始输出字符串

    Returns:
        dict: 包含 summary 和 files 的字典
            {
                "summary": {
                    "total_files": int,
                    "added": int,
                    "modified": int,
                    "deleted": int,
                    "renamed": int,
                    "total_additions": int,
                    "total_deletions": int,
                },
                "files": [
                    {
                        "path": str,
                        "change_type": str,
                        "additions": int,
                        "deletions": int,
                        "added_lines": [str],
                        "deleted_lines": [str],
                    },
                    ...
                ]
            }
    """
    # 空结构定义
    empty_result = {
        "summary": {
            "total_files": 0,
            "added": 0,
            "modified": 0,
            "deleted": 0,
            "renamed": 0,
            "total_additions": 0,
            "total_deletions": 0,
        },
        "files": []
    }

    # 处理空输入
    if not raw_diff:
        return empty_result

    # 解析 diff
    try:
        patch_set = PatchSet(raw_diff)
    except UnidiffParseError:
        # 解析失败时返回空结构
        return empty_result

    # 提取文件信息
    files = []
    for pf in patch_set:
        # 过滤噪音文件
        if _is_noise_file(pf.path):
            continue

        # 获取变更类型
        change_type = _get_change_type(pf)

        # 提取新增和删除的行
        added_lines = []
        deleted_lines = []
        for hunk in pf:
            for line in hunk:
                if line.is_added:
                    added_lines.append(line.value.rstrip('\n').rstrip('\r'))
                elif line.is_removed:
                    deleted_lines.append(line.value.rstrip('\n').rstrip('\r'))

        # 构建文件信息
        file_info = {
            "path": pf.path,
            "change_type": change_type,
            "additions": pf.added,
            "deletions": pf.removed,
            "added_lines": added_lines,
            "deleted_lines": deleted_lines,
        }
        files.append(file_info)

    # 计算汇总信息
    summary = {
        "total_files": len(files),
        "added": sum(1 for f in files if f["change_type"] == "added"),
        "modified": sum(1 for f in files if f["change_type"] == "modified"),
        "deleted": sum(1 for f in files if f["change_type"] == "deleted"),
        "renamed": sum(1 for f in files if f["change_type"] == "renamed"),
        "total_additions": sum(f["additions"] for f in files),
        "total_deletions": sum(f["deletions"] for f in files),
    }

    return {
        "summary": summary,
        "files": files
    }
