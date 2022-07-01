from selenium.webdriver.common.by import By
from locator.hahaloloLocator import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def click_halo_btn(self):
        halo_login_btn = WebDriverWait(self.driver, 1800).until(EC.element_to_be_clickable((By.XPATH, get_halo_btn())))
        halo_login_btn.click()

    def enter_acc_id(self, acc_id):
        account_id = WebDriverWait(self.driver, 1800).until(EC.element_to_be_clickable((By.ID, get_acc_id())))
        account_id.send_keys(acc_id)

    def enter_pwd(self, password):
        pwd = WebDriverWait(self.driver, 1800).until(EC.element_to_be_clickable((By.ID, get_pwd_id())))
        pwd.send_keys(password)

    def click_login_btn(self):
        login_btn = WebDriverWait(self.driver, 1800).until(EC.element_to_be_clickable((By.XPATH, get_login_btn())))
        login_btn.click()

    def click_continue_btn(self):
        continue_btn = WebDriverWait(self.driver, 1800).until(EC.element_to_be_clickable((By.XPATH, get_continue_btn())))
        continue_btn.click()

    def enter_pin(self, pin_code):
        pin = WebDriverWait(self.driver, 1800).until(EC.element_to_be_clickable((By.XPATH, get_pin_code())))
        pin.send_keys(pin_code)

    def click_forget_pin(self):
        forget_pin = WebDriverWait(self.driver, 1800).until(EC.element_to_be_clickable((By.XPATH, get_forget_pin())))
        forget_pin.click()

    def click_accpet_btn(self):
        accept_btn = WebDriverWait(self.driver, 1800).until(EC.element_to_be_clickable((By.XPATH, get_accept_btn())))
        accept_btn.click()

    def click_off_notification_btn(self):
        off_notification_btn = WebDriverWait(self.driver, 1800).until(EC.element_to_be_clickable((By.XPATH, get_off_notification())))
        off_notification_btn.click()

    def click_avatar_btn(self):
        avatar_btn = WebDriverWait(self.driver, 1800).until(EC.element_to_be_clickable((By.XPATH, get_avatar_btn())))
        avatar_btn.click()

    def enter_chat(self, chat_user):
        chat = WebDriverWait(self.driver, 1800).until(EC.element_to_be_clickable((By.XPATH, get_chat_user())))
        chat.send_keys(chat_user)

    def click_send_btn(self):
        send_btn = WebDriverWait(self.driver, 1800).until(EC.element_to_be_clickable((By.ID, get_send_chat_btn())))
        send_btn.click()

    def click_icon_btn(self):
        icon_btn = WebDriverWait(self.driver, 1800).until(EC.element_to_be_clickable((By.XPATH, get_icon_group_btn())))
        icon_btn.click()

    def click_group_chat(self):
        group_chat = WebDriverWait(self.driver, 1800).until(EC.element_to_be_clickable((By.XPATH, get_group_chat_btn())))
        group_chat.click()

    def enter_chat_group(self, import_chat_group):
        chat_group = WebDriverWait(self.driver, 1800).until(EC.element_to_be_clickable((By.ID, get_import_chat_group())))
        chat_group.send_keys(import_chat_group)

    def click_send_chat_group(self):
        send_chat_group = WebDriverWait(self.driver, 1800).until(EC.element_to_be_clickable((By.ID, get_send_chat_group())))
        send_chat_group.click()

    def click_avatar(self):
        avatar = WebDriverWait(self.driver, 1800).until(EC.element_to_be_clickable((By.XPATH, get_press_avatar())))
        avatar.click()

    def click_log_out(self):
        log_out = WebDriverWait(self.driver, 1800).until(EC.element_to_be_clickable((By.XPATH, get_press_log_out())))
        log_out.click()

    def click_agree_log_out(self):
        agree_out = WebDriverWait(self.driver, 1800).until(EC.element_to_be_clickable((By.ID, get_agree_log_out())))
        agree_out.click()

    def click_not_you_btn(self):
        not_you_btn = WebDriverWait(self.driver, 1800).until(EC.element_to_be_clickable((By.XPATH, get_not_you_btn())))
        not_you_btn.click()

    # def clear_id(self):
    #     clear_id = self.driver.find_element(By.ID, get_clear_id())
    #     clear_id.clear()
    #
    # def clear_pwd(self):
    #     clear_pwd = self.driver.find_element(By.ID, get_clear_pwd())
    #     clear_pwd.clear()

    def enter_otp_fail(self, otp_fail):
        otp = WebDriverWait(self.driver, 1800).until(EC.element_to_be_clickable((By.ID, get_otp_fail())))
        otp.send_keys(otp_fail)

    def click_otp_fail_btn(self):
        otp_fail_btn = WebDriverWait(self.driver, 1800).until(EC.element_to_be_clickable((By.XPATH, get_otp_fail_btn())))
        otp_fail_btn.click()

    def click_send_otp_btn(self):
        send_otp = WebDriverWait(self.driver, 1800).until(EC.element_to_be_clickable((By.ID, get_send_otp_btn())))
        send_otp.click()

    def enter_otp_ok(self, otp_ok_btn):
        otp_ok = WebDriverWait(self.driver, 1800).until(EC.element_to_be_clickable((By.XPATH, get_otp_ok())))
        otp_ok.send_keys(otp_ok_btn)

    def click_otp_ok_btn(self):
        otp_ok_btn = WebDriverWait(self.driver, 1800).until(EC.element_to_be_clickable((By.XPATH, get_otp_ok_btn())))
        otp_ok_btn.click()

    def enter_otp_new(self, otp_new):
        new = WebDriverWait(self.driver, 1800).until(EC.element_to_be_clickable((By.XPATH, get_otp_new())))
        new.send_keys(otp_new)

    def click_save_otp(self):
        save_otp = WebDriverWait(self.driver, 1800).until(EC.element_to_be_clickable((By.CSS_SELECTOR, get_save_otp())))
        save_otp.click()

    def click_come_back(self):
        come_back = WebDriverWait(self.driver, 1800).until(EC.element_to_be_clickable((By.XPATH, get_come_back())))
        come_back.click()

    def click_cancel_btn(self):
        # cancel_btn = self.driver.find_element(By.XPATH, get_cancel_btn())
        # cancel_btn = WebDriverWait(self.driver, 180).until(EC.presence_of_element_located((By.XPATH, get_cancel_btn())))
        cancel_btn = WebDriverWait(self.driver, 1800).until(EC.element_to_be_clickable((By.XPATH, get_cancel_btn())))
        cancel_btn.click()

    def get_login_err_messager(self):
        err = WebDriverWait(self.driver, 1800).until(EC.presence_of_element_located((By.CSS_SELECTOR, get_login_err())))
        return err.text

    def get_err_pin(self):
        err_pin = WebDriverWait(self.driver, 2000).until(EC.element_to_be_clickable((By.CSS_SELECTOR, get_err_pin())))
        return err_pin.getText()


