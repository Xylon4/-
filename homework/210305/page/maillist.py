from basepage import BasePage
from addmember import AddMember


class MailList(BasePage):
    def goto_addmember(self):
        self.parse_action("D:\PycharmProjects\-\homework/\/210305\page/\/addmember.yaml", "maillist")
        return AddMember(self.driver)
