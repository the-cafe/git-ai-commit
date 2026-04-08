"""
测试版本号管理功能
Task 2: 验证 ConfigService 版本号管理方法
"""
import sys
import os

# 添加项目路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_set_valid_version():
    """Test 1: set_project_version("1.9.1") 成功保存"""
    from ai_commit_msg.services.config_service import ConfigService

    cs = ConfigService()
    cs.set_project_version("1.9.1")
    assert cs.get_project_version() == "1.9.1", "版本号应该被正确保存"
    print("[PASS] Test 1: set_project_version 成功保存有效版本号")

def test_set_invalid_version():
    """Test 2: set_project_version("invalid") 抛出异常"""
    from ai_commit_msg.services.config_service import ConfigService

    cs = ConfigService()
    try:
        cs.set_project_version("invalid-version")
        raise AssertionError("应该抛出异常")
    except Exception as e:
        assert "版本号格式无效" in str(e), f"错误信息应包含'版本号格式无效'，实际: {e}"
    print("[PASS] Test 2: set_project_version 拒绝无效版本号")

def test_clear_version():
    """Test 3: set_project_version("") 成功清空版本号"""
    from ai_commit_msg.services.config_service import ConfigService

    cs = ConfigService()
    cs.set_project_version("1.0.0")
    cs.set_project_version("")
    assert cs.get_project_version() == "", "版本号应该被清空"
    print("[PASS] Test 3: set_project_version 可以清空版本号")

def test_get_version():
    """Test 4: get_project_version() 返回已保存的版本号或空字符串"""
    from ai_commit_msg.services.config_service import ConfigService

    cs = ConfigService()
    cs.set_project_version("2.0.0-beta")
    version = cs.get_project_version()
    assert version == "2.0.0-beta", f"应该返回保存的版本号，实际: {version}"
    print("[PASS] Test 4: get_project_version 返回正确的版本号")

if __name__ == "__main__":
    print("Running Task 2 tests...\n")
    try:
        test_set_valid_version()
        test_set_invalid_version()
        test_clear_version()
        test_get_version()
        print("\n[SUCCESS] All tests passed!")
        sys.exit(0)
    except (AssertionError, AttributeError) as e:
        print(f"\n[FAIL] Test failed: {e}")
        sys.exit(1)
