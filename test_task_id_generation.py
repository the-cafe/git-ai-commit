"""
测试临时任务号生成功能
Task 3: 验证 ConfigService 临时任务号生成方法
"""
import sys
import os

# 添加项目路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_first_task_id():
    """Test 1: 首次调用 get_next_temp_task_id() 返回 "TEMP-001" """
    from ai_commit_msg.services.config_service import ConfigService

    cs = ConfigService()
    cs.reset_temp_task_counter()
    task_id = cs.get_next_temp_task_id()
    assert task_id == "TEMP-001", f"首次调用应返回 TEMP-001，实际: {task_id}"
    print("[PASS] Test 1: 首次调用返回 TEMP-001")

def test_sequential_task_ids():
    """Test 2: 第二次调用返回 "TEMP-002" """
    from ai_commit_msg.services.config_service import ConfigService

    cs = ConfigService()
    cs.reset_temp_task_counter()
    id1 = cs.get_next_temp_task_id()
    id2 = cs.get_next_temp_task_id()
    assert id1 == "TEMP-001", f"第一次应返回 TEMP-001，实际: {id1}"
    assert id2 == "TEMP-002", f"第二次应返回 TEMP-002，实际: {id2}"
    print("[PASS] Test 2: 连续调用返回递增的任务号")

def test_counter_loop():
    """Test 3: 计数器达到 999 后循环到 1"""
    from ai_commit_msg.services.config_service import ConfigService
    from ai_commit_msg.services.local_db_service import ConfigKeysEnum, LocalDbService, CONFIG_COLLECTION_KEY

    cs = ConfigService()
    # 手动设置计数器为 999
    config = ConfigService.get_config()
    config[ConfigKeysEnum.TEMP_TASK_COUNTER.value] = 999
    LocalDbService().set_db({CONFIG_COLLECTION_KEY: config})

    id1 = cs.get_next_temp_task_id()
    id2 = cs.get_next_temp_task_id()
    assert id1 == "TEMP-999", f"应返回 TEMP-999，实际: {id1}"
    assert id2 == "TEMP-001", f"循环后应返回 TEMP-001，实际: {id2}"
    print("[PASS] Test 3: 计数器达到 999 后循环到 1")

def test_reset_counter():
    """Test 4: reset_temp_task_counter() 重置计数器到 1"""
    from ai_commit_msg.services.config_service import ConfigService

    cs = ConfigService()
    # 生成几个任务号
    cs.get_next_temp_task_id()
    cs.get_next_temp_task_id()
    cs.get_next_temp_task_id()

    # 重置
    cs.reset_temp_task_counter()
    task_id = cs.get_next_temp_task_id()
    assert task_id == "TEMP-001", f"重置后应返回 TEMP-001，实际: {task_id}"
    print("[PASS] Test 4: reset_temp_task_counter 重置计数器")

if __name__ == "__main__":
    print("Running Task 3 tests...\n")
    try:
        test_first_task_id()
        test_sequential_task_ids()
        test_counter_loop()
        test_reset_counter()
        print("\n[SUCCESS] All tests passed!")
        sys.exit(0)
    except (AssertionError, AttributeError) as e:
        print(f"\n[FAIL] Test failed: {e}")
        sys.exit(1)
