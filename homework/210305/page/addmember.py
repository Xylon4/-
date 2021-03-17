from basepage import BasePage


class AddMember(BasePage):
    def addmember(self):
        # 显式等待元素页面与“手动输入添加”页面不同，单个操作独立实现
        self.find_click("//*[@text='手动输入添加']")
        self.parse_action("D:\PycharmProjects\-\homework/\/210305\page/\/addmember.yaml", "addmember")
