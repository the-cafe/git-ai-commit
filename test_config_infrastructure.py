"""
测试配置基础设施扩展
Task 1: 验证 ConfigKeysEnum 和 default_db 扩展
"""
import sys
import os

# 添加项目路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_config_keys_enum():
    """Test 1: ConfigKeysEnum 包含 PROJECT_VERSION 和 TEMP_TASK_COUNTER"""
    from ai_commit_msg.services.local_db_service import ConfigKeysEnum

    assert hasattr(ConfigKeysEnum, 'PROJECT_VERSION'), "ConfigKeysEnum 缺少 PROJECT_VERSION"
    assert hasattr(ConfigKeysEnum, 'TEMP_TASK_COUNTER'), "ConfigKeysEnum 缺少 TEMP_TASK_COUNTER"
    assert ConfigKeysEnum.PROJECT_VERSION.value == "project_version"
    assert ConfigKeysEnum.TEMP_TASK_COUNTER.value == "temp_task_counter"
    print("[PASS] Test 1: ConfigKeysEnum 包含新的枚举值")

def test_default_db():
    """Test 2: default_db 包含 project_version="" 和 temp_task_counter=1"""
    from ai_commit_msg.services.local_db_service import default_db, CONFIG_COLLECTION_KEY, ConfigKeysEnum

    config = default_db[CONFIG_COLLECTION_KEY]
    assert ConfigKeysEnum.PROJECT_VERSION.value in config, "default_db 缺少 project_version"
    assert ConfigKeysEnum.TEMP_TASK_COUNTER.value in config, "default_db 缺少 temp_task_counter"
    assert config[ConfigKeysEnum.PROJECT_VERSION.value] == "", "project_version 默认值应为空字符串"
    assert config[ConfigKeysEnum.TEMP_TASK_COUNTER.value] == 1, "temp_task_counter 默认值应为 1"
    print("[PASS] Test 2: default_db 包含正确的默认值")

def test_semver_import():
    """Test 3: semver 库可以成功导入"""
    try:
        import semver
        print("[PASS] Test 3: semver 库可以成功导入")
    except ImportError:
        raise AssertionError("semver 库未安装")

if __name__ == "__main__":
    print("Running Task 1 tests...\n")
    try:
        test_config_keys_enum()
        test_default_db()
        test_semver_import()
        print("\n[SUCCESS] All tests passed!")
        sys.exit(0)
    except (AssertionError, AttributeError, ImportError) as e:
        print(f"\n[FAIL] Test failed: {e}")
        sys.exit(1)
