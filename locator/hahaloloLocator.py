def get_halo_btn():
    return "/html/body/div/div/div[2]/div/div/button[2]/div"

#nhập tài khoản


def get_acc_id():
    return "accountId"

#nhập mật khẩu


def get_pwd_id():
    return "password"


#nút đăng nhập


def get_login_btn():
     return "/html/body/div/div[1]/div/div[1]/div/div[2]/div/div/div/div[2]/button"

#nút tiếp tục


def get_continue_btn():
    return "/html/body/div/div/div[2]/div/div/div[3]/div/button/div"

#nhập mã pin


def get_pin_code():
    return "/html/body/div/div/div[2]/div/div/div[3]/div/div[1]/div[1]/input"

#nút chấp nhận mã pin


def get_accept_btn():
      return "/html/body/div/div/div[2]/div/div/div[3]/div/div[2]/button/div"

      # return "platforms-halo"


#nhấn quên mã pin


def get_forget_pin():
    return "/html/body/div/div/div[2]/div/div/div[3]/div[2]/div[2]/div"

#nút tắt thông báo sau khi đăng nhập thành công


def get_off_notification():
    return "/html/body/div/div/div[3]/div/div/div[2]/button[2]"

#nhấn vào user muốn chat


def get_avatar_btn():
    return "/html/body/div/div/div[2]/div[1]/div[2]/div[2]/div[8]/div/div/a/div[2]/div"

#soạn tin nhắn chat 1-1


def get_chat_user():
    return "/html/body/div/div/div[2]/div[2]/div/div[3]/div/div/div[2]/div[2]/div/div/p"

#nhấn nút gửi tin nhắn


def get_send_chat_btn():
    return "composer-button-send-all"


# nhấn icon chat nhóm
def get_icon_group_btn():
    return "appbar-channels"


#chọn group muốn chat

def get_group_chat_btn():
    return "/html/body/div/div/div[2]/div[1]/div[2]/div[2]/div[1]/div/div/a/div[2]"

#nhấn nút soạn gửi tin nhắn group


def get_import_chat_group():
    return "/html/body/div/div/div[2]/div[2]/div/div[3]/div/div/div[2]/div[2]/div/div/p"

#nhấn nút gửi tin nhắn group


def get_send_chat_group():
    return "composer-button-send-all"

#nhấn vào avatar cá nhân


def get_press_avatar():
    return "/html/body/div/div/div[1]/div/div/img"


#nhấn đăng xuất


def get_press_log_out():
    return "/html/body/div/div/div[2]/div[2]/div/div/div/div[5]/div[6]/div/h3"


#nhấn đồng ý đăng xuất


def get_agree_log_out():
    return "modal-button-ok"

#nhấn vào nút không phải nick của bạn


def get_not_you_btn():
    return "/html/body/div/div/div[2]/div/div/div[3]/div/p[2]"

#xóa tài khoản


def get_clear_id():
    return "accountId"


#xóa mật khẩu


def get_clear_pwd():
    return "password"


#nhập mã xác thực sai


def get_otp_fail():
    return "/html/body/div/div/div[2]/div/div/div[3]/div/div[1]/div[1]/input"

#nhấn btn chấp nhận mã xác thực sai


def get_otp_fail_btn():
    return "/html/body/div/div/div[2]/div/div/div[3]/div/div[2]/button[2]/div"

#nhấn gửi lại mã xác thực


def get_send_otp_btn():
    return "halo-pin-form-otp-button-resend"


#nhập mã xác thực đúng


def get_otp_ok():
    return "/html/body/div/div/div[2]/div/div/div[3]/div/div[1]/div[1]/input"

#nhấn btn chấp nhận mã xác thực đúng


def get_otp_ok_btn():
    return "/html/body/div/div/div[2]/div/div/div[3]/div/div[2]/button[2]/div"

#nhập mã pin mới


def get_otp_new():
    return "/html/body/div/div/div[2]/div/div/div[3]/div[1]/div[1]/div[4]/input"

#btn lưu mã xác thực


def get_save_otp():
     # return "/html/body/div/div/div[2]/div/div/div[3]/div[2]/button/div"
    return "#platforms-halo div"
#btn quay lại


def get_come_back():
    # return "platforms-halo"
    return "/html/body/div/div/div[2]/div/div/div[5]"

#nhấn hủy


def get_cancel_btn():
    return "/html/body/div/div/div[2]/div/div/div[3]/div/div[2]/div"

# câu hiển thị khi nhập sai


def get_login_err():
    return "div.MuiTypography-gutterBottom > span"
    # return "/html/body/div/div[1]/div/div[1]/div/div[2]/div/div/div/div[1]/div[3]/div/div/div/div[2]/div/span"

# câu hiển thị khi nhập pin sai


def get_err_pin():
    return ".bg-red-primary"