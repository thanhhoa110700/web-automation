import time
import unittest
from selenium import webdriver
from page.hahaloloPage import LoginPage
from selenium.common import NoSuchElementException



class LoginTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="D:/PYTHON/test/chromedriver.exe")
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.login_page = LoginPage(self.driver)
        self.driver.get("https://sb.halome.dev/")
        self.url = "https://sb.halome.dev/"
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

    # login successful
    #
    # def test_login(self):
    #     self.login_page.click_halo_btn()
    #     time.sleep(2)
    #     self.login_page.enter_acc_id("halome106@skyoi.tk")
    #     self.login_page.enter_pwd("admin@123")
    #     self.login_page.click_login_btn()
    #     self.login_page.click_continue_btn()
    #     self.login_page.enter_pin("123456")
    #     self.login_page.click_accpet_btn()
    #     self.login_page.click_off_notification_btn()
    #     assert self.driver.current_url == self.url
    #     self.login_page.click_avatar()
    #     self.login_page.click_log_out()
    #     self.login_page.click_agree_log_out()
    #
    # # login fail account
    # def test_login_fail_tk(self):
    #     self.login_page.click_halo_btn()
    #     time.sleep(3)
    #     self.login_page.enter_acc_id("halome106@skyoi.th")
    #     self.login_page.enter_pwd("admin@123")
    #     self.login_page.click_login_btn()
    #     time.sleep(3)
    #     print(self.login_page.get_login_err_messager())
    #     assert self.login_page.get_login_err_messager() == "Tên tài khoản hoặc mật khẩu không chính xác"
    #
    # # login fail password
    # def test_login_fail_pw(self):
    #     self.login_page.click_halo_btn()
    #     time.sleep(3)
    #     self.login_page.enter_acc_id("halome106@skyoi.tk")
    #     self.login_page.enter_pwd("admin123")
    #     self.login_page.click_login_btn()
    #     time.sleep(3)
    #     print(self.login_page.get_login_err_messager())
    #     assert self.login_page.get_login_err_messager() == "Tên tài khoản hoặc mật khẩu không chính xác"
    #
    # # # login fail account, password
    # def test_login_fail_tk_pw(self):
    #     self.login_page.click_halo_btn()
    #     time.sleep(3)
    #     self.login_page.enter_acc_id("halome106skyoi.tk")
    #     self.login_page.enter_pwd("admin123")
    #     self.login_page.click_login_btn()
    #     time.sleep(3)
    #     print(self.login_page.get_login_err_messager())
    #     assert self.login_page.get_login_err_messager() == "Tên tài khoản hoặc mật khẩu không chính xác"
    #
    # # import pin fail
    # def test_login_pin_fail(self):
    #     self.login_page.click_halo_btn()
    #     time.sleep(3)
    #     self.login_page.enter_acc_id("halome106@skyoi.tk")
    #     self.login_page.enter_pwd("admin@123")
    #     self.login_page.click_login_btn()
    #     self.login_page.click_continue_btn()
    #     self.login_page.enter_pin("111111")
    #     self.login_page.click_accpet_btn()
    #     self.login_page.click_come_back()
    #
    # # import pin and otp fail
    # def test_login_pin_fail_otp_much(self):
    #         self.login_page.click_halo_btn()
    #         time.sleep(3)
    #         self.login_page.enter_acc_id("halome106@skyoi.tk")
    #         self.login_page.enter_pwd("admin@123")
    #         self.login_page.click_login_btn()
    #         time.sleep(3)
    #         self.login_page.click_continue_btn()
    #         self.login_page.enter_pin("111111")
    #         self.login_page.click_accpet_btn()
    #         self.login_page.click_forget_pin()
    #         self.login_page.enter_pin("555555")
    #         self.login_page.click_cancel_btn()
    #         self.login_page.click_come_back()
    #
    # # import pin fail, otp true
    # def test_login_pin_fail_otp_t(self):
    #         self.login_page.click_halo_btn()
    #         time.sleep(3)
    #         self.login_page.enter_acc_id("halome106@skyoi.tk")
    #         self.login_page.enter_pwd("admin@123")
    #         self.login_page.click_login_btn()
    #         time.sleep(3)
    #         self.login_page.click_continue_btn()
    #         self.login_page.enter_pin("111111")
    #         self.login_page.click_accpet_btn()
    #         self.login_page.click_forget_pin()
    #         self.login_page.enter_pin("000000")
    #         self.login_page.click_accpet_btn()
    #         self.login_page.enter_pin("123456123456")
    #         self.login_page.click_save_otp()
    #         self.login_page.enter_pin("123456")
    #         self.login_page.click_accpet_btn()
    #         self.login_page.click_off_notification_btn()
    #         self.login_page.click_avatar()
    #         self.login_page.click_log_out()
    #         self.login_page.click_agree_log_out()

    def test_login_no_you(self):
        self.login_page.click_halo_btn()
        time.sleep(3)
        self.login_page.enter_acc_id("halome106@skyoi.tk")
        self.login_page.enter_pwd("admin@123")
        self.login_page.click_login_btn()
        time.sleep(3)
        self.login_page.click_not_you_btn()
        time.sleep(5)
        self.login_page.enter_acc_id("0342929839")
        self.login_page.enter_pwd("admin123")
        self.login_page.click_login_btn()
        time.sleep(3)
        self.login_page.click_continue_btn()
        self.login_page.enter_pin("123456")
        self.login_page.click_accpet_btn()
        self.login_page.click_off_notification_btn()
        assert self.driver.current_url == self.url
        self.login_page.click_avatar()
        self.login_page.click_log_out()
        self.login_page.click_agree_log_out()




if __name__ == '__main__':
    unittest.main()
