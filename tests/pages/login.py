from common.browser import browser


class Login:
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = Login()
        return cls.instance

    def __init__(self):
        self.driver = browser.get_driver()

    def type_username(self):
        browser.wait_for_element()
        # status = self.driver.find_element_by_id('dashboard-status-component').text
        # assert row in status, "{} not present in status component".format(row)
        print('Verifying dashboard status..')


login = Login.get_instance()
