import pyautogui
import time




# click 1中间
def click_img(icon_path, need_click=True, need_sleep=False, x_move=0, y_move=0, sec_icon=None, max_times=-1, other_icon=None):
    result = True
    num = 0
    while result:
        if max_times > 0:
            num = num + 1
            if num > max_times:
                return "fail"
        if need_click:
            pyautogui.click()

        if sec_icon is not None:
            sec_icon_location = pyautogui.locateCenterOnScreen(sec_icon)
            if sec_icon_location is not None:
                pyautogui.moveTo(sec_icon_location)
                pyautogui.click()
        icon_location = pyautogui.locateCenterOnScreen(icon_path)
        if icon_location is None:
            if other_icon is not None:
                icon_location = pyautogui.locateCenterOnScreen(other_icon)

        if icon_location is not None:
            pyautogui.moveTo(x=icon_location.x + x_move, y=icon_location.y + y_move)
            pyautogui.click()
            if need_sleep:
                time.sleep(3)
            result = False
        else:
            print("no get icon location, " + icon_path)
            time.sleep(0.2)


def add_jiban():
    click_img(icon_path="icon\\jiban_icon_can_up.png", need_click=False)
    click_img(icon_path="icon\\jiban_up_btn.png", need_click=False)
    click_img(icon_path="icon\\jiban_max_btn.png", need_click=False)
    click_img(icon_path="icon\\jiben_send_btn.png", need_click=False)
    click_img(icon_path="icon\\jiban_close_1_btn.png", need_click=False, other_icon="icon\\jiban_close_1_btn_bak.png")
    time.sleep(1)
    click_img(icon_path="icon\\jiban_close_2_btn.png", need_click=False, other_icon="icon\\jiban_close_1_btn_bak.png")
    click_img(icon_path="icon\\jiban_icon_can_up.png", need_click=False, x_move=1200, y_move=-100)


for i in range(1,999):
    add_jiban()