"""
测试 diff_parser 模块
验证 git diff 解析功能
"""
import sys
import os

# 添加项目路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from ai_commit_msg.utils.diff_parser import parse_diff


def test_empty_diff():
    """Test 1: 空字符串返回空结构"""
    result = parse_diff("")
    assert result["summary"]["total_files"] == 0, "空 diff 应返回 0 个文件"
    assert result["files"] == [], "空 diff 应返回空文件列表"
    print("[PASS] Test 1: 空字符串返回空结构")


def test_none_diff():
    """Test 2: None 返回空结构"""
    result = parse_diff(None)
    assert result["summary"]["total_files"] == 0, "None diff 应返回 0 个文件"
    assert result["files"] == [], "None diff 应返回空文件列表"
    print("[PASS] Test 2: None 返回空结构")


def test_single_file_modify():
    """Test 3: 单文件修改"""
    diff = """diff --git a/src/main.py b/src/main.py
index 1234567..abcdefg 100644
--- a/src/main.py
+++ b/src/main.py
@@ -1,3 +1,4 @@
 def hello():
-    print("world")
+    print("hello world")
+    return True
"""
    result = parse_diff(diff)

    assert result["summary"]["total_files"] == 1, "应有 1 个文件"
    assert result["summary"]["modified"] == 1, "应有 1 个修改文件"
    assert result["summary"]["total_additions"] == 2, "应有 2 行新增"
    assert result["summary"]["total_deletions"] == 1, "应有 1 行删除"

    assert result["files"][0]["path"] == "src/main.py", "文件路径应为 src/main.py"
    assert result["files"][0]["change_type"] == "modified", "变更类型应为 modified"
    assert result["files"][0]["additions"] == 2, "应有 2 行新增"
    assert result["files"][0]["deletions"] == 1, "应有 1 行删除"

    added_lines = result["files"][0]["added_lines"]
    assert any('print("hello world")' in line for line in added_lines), "应包含新增的 print 语句"
    assert any('return True' in line for line in added_lines), "应包含新增的 return 语句"

    deleted_lines = result["files"][0]["deleted_lines"]
    assert any('print("world")' in line for line in deleted_lines), "应包含删除的 print 语句"

    print("[PASS] Test 3: 单文件修改")


def test_multi_file_mixed():
    """Test 4: 多文件混合（新增+修改）"""
    diff = """diff --git a/new_file.py b/new_file.py
new file mode 100644
index 0000000..1234567
--- /dev/null
+++ b/new_file.py
@@ -0,0 +1,3 @@
+def new_func():
+    pass
+
diff --git a/existing.py b/existing.py
index 1234567..abcdefg 100644
--- a/existing.py
+++ b/existing.py
@@ -1,2 +1,2 @@
 def old_func():
-    return False
+    return True
"""
    result = parse_diff(diff)

    assert result["summary"]["total_files"] == 2, "应有 2 个文件"
    assert result["summary"]["added"] == 1, "应有 1 个新增文件"
    assert result["summary"]["modified"] == 1, "应有 1 个修改文件"

    paths = [f["path"] for f in result["files"]]
    assert "new_file.py" in paths, "应包含 new_file.py"
    assert "existing.py" in paths, "应包含 existing.py"

    new_file = next(f for f in result["files"] if f["path"] == "new_file.py")
    assert new_file["change_type"] == "added", "new_file.py 应为新增文件"

    existing_file = next(f for f in result["files"] if f["path"] == "existing.py")
    assert existing_file["change_type"] == "modified", "existing.py 应为修改文件"

    print("[PASS] Test 4: 多文件混合（新增+修改）")


def test_deleted_file():
    """Test 5: 删除文件"""
    diff = """diff --git a/old_file.py b/old_file.py
deleted file mode 100644
index 1234567..0000000
--- a/old_file.py
+++ /dev/null
@@ -1,2 +0,0 @@
-def deprecated():
-    pass
"""
    result = parse_diff(diff)

    assert result["summary"]["deleted"] == 1, "应有 1 个删除文件"
    assert result["files"][0]["change_type"] == "deleted", "变更类型应为 deleted"

    print("[PASS] Test 5: 删除文件")


def test_noise_file_filtered():
    """Test 6: 噪音文件被过滤"""
    diff = """diff --git a/package-lock.json b/package-lock.json
index 1234567..abcdefg 100644
--- a/package-lock.json
+++ b/package-lock.json
@@ -1,3 +1,3 @@
 {
-  "version": "1.0.0"
+  "version": "1.0.1"
 }
diff --git a/src/app.py b/src/app.py
index 1234567..abcdefg 100644
--- a/src/app.py
+++ b/src/app.py
@@ -1,2 +1,2 @@
 def run():
-    start()
+    start_app()
"""
    result = parse_diff(diff)

    assert result["summary"]["total_files"] == 1, "package-lock.json 应被过滤，只剩 1 个文件"
    assert result["files"][0]["path"] == "src/app.py", "唯一文件应为 src/app.py"

    print("[PASS] Test 6: 噪音文件被过滤")


def test_invalid_diff():
    """Test 7: 无效 diff 字符串返回空结构"""
    result = parse_diff("this is not a valid diff")
    assert result["summary"]["total_files"] == 0, "无效 diff 应返回 0 个文件"
    print("[PASS] Test 7: 无效 diff 字符串返回空结构")


def test_large_diff():
    """Test 8: 大型 diff（3 个文件，每个 20 行变更）"""
    # 构造包含 3 个文件的 diff，每个文件有 10 行新增和 10 行删除
    diff_parts = []
    for i in range(3):
        file_diff = f"""diff --git a/file{i}.py b/file{i}.py
index 1234567..abcdefg 100644
--- a/file{i}.py
+++ b/file{i}.py
@@ -1,10 +1,10 @@
"""
        for j in range(10):
            file_diff += f"-    old_line_{j}\n"
        for j in range(10):
            file_diff += f"+    new_line_{j}\n"
        diff_parts.append(file_diff)

    diff = "\n".join(diff_parts)
    result = parse_diff(diff)

    assert result["summary"]["total_files"] == 3, "应有 3 个文件"
    assert result["summary"]["total_additions"] == 30, "应有 30 行新增（3 文件 x 10 行）"
    assert result["summary"]["total_deletions"] == 30, "应有 30 行删除（3 文件 x 10 行）"

    print("[PASS] Test 8: 大型 diff（3 个文件，每个 20 行变更）")


if __name__ == "__main__":
    print("Running diff_parser tests...\n")
    try:
        test_empty_diff()
        test_none_diff()
        test_single_file_modify()
        test_multi_file_mixed()
        test_deleted_file()
        test_noise_file_filtered()
        test_invalid_diff()
        test_large_diff()
        print("\n[SUCCESS] All tests passed!")
        sys.exit(0)
    except (AssertionError, AttributeError, ImportError) as e:
        print(f"\n[FAIL] Test failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
