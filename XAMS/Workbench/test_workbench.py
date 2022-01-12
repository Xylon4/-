import pytest

from XAMS.Report.conftest import sheet41
from XAMS.Tool.test_excel import TestExcel
from XAMS.Workbench.todo_tasks import TodoTasks


class TestWorkbench:
    # 万能导入用例
    def test_universal(self, stagemark, menu, value, test_goal, step):
        self.list = TestExcel()
        if test_goal == '模拟操作':
            second_menu = f'{menu[1]}-{menu[2]}'
            address = value[0]
            if second_menu == '我的工作台-待审批任务':
                self.test_todo_tasks_excel(stagemark, menu, value, address, step)
            else:
                print("模拟操作案例：该任务暂不支持，请修改用例")
        elif test_goal == '升级对比':
            second_menu = f'{menu[2]}-{menu[3]}'
            address = value[0]
        else:
            print("该测试目的暂不支持，请修改用例")
            return False

    @pytest.mark.skip
    def test_todo_tasks_excel(self, stagemark, menu, value, address, step):
        self.todo_tasks = TodoTasks(address)
        assert self.todo_tasks.todo_tasks_excel(menu, value)
        if step is not None:
            self.todo_tasks.end()
        print(f"{sheet41}模拟操作执行完毕")
        print('-----------------------这是案例分割线-----------------------')
