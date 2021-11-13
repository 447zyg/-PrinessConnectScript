import pyautogui
import time
import start_gzlj as sg


def jue_se_ju_qing():
    result = find_img("icon\\jiban_icon_can_up.png", "icon\\jiban_icon_normal.png")
    print("find result = ")
    print(result)
    if result == 1:
        click_img("icon\\jiban_icon_can_up.png", need_click=False)
        click_img(icon_path="icon\\jiban_up_btn.png", need_click=False, y_move=-240)
        for i in range(1, 100):
            a = ju_qing_zidong()
            if a:
                break

    click_img(icon_path="icon\\jiban_juqing_icon_over.png", need_click=False, x_move=1200, y_move=-100)


def find_img(icon_1, icon_2, icon_3=None, icon_4=None):
    while True:
        i1 = sg.look_for_img(icon_1)
        if i1:
            return 1
        i2 = sg.look_for_img(icon_2)
        if i2:
            return 2
        if icon_3 is not None:
            i3 = sg.look_for_img(icon_3)
            if i3:
                return 3
        if icon_4 is not None:
            i4 = sg.look_for_img(icon_4)
            if i4:
                return 4


def ju_qing_zidong():
    return click_img(icon_path="icon\\juqing_close.png", icon_sec_path="icon\\juqing_close_bak.png", need_click=False,
              other_icon="icon\\juqing_menu.png", other_icon_1="icon\\juqing_skip.png",
              other_icon_2="icon\\juqing_skip_confirm_btn.png",
              other_icon_4="icon\\juqing_ok.png",
              other_icon_3="icon\\juqing_skip_bak.png", need_break=False,
                     break_icon="icon\\break_icon_return.png")


def check_icon(icon):
    if icon is not None:
        icon_location = sg.look_for_img(icon)
        if icon_location is not None:
            pyautogui.moveTo(icon_location)
            pyautogui.click()
            return True
    return False


def click_img(icon_path, icon_sec_path=None,need_click=True, need_sleep=False, x_move=0, y_move=0, max_times=-1, click_one_return=False,
              other_icon=None, other_icon_1=None, other_icon_2=None, other_icon_3=None, end_times=-1, other_icon_4=None,
              need_break=True, break_icon=None):
    result = True
    num = 0
    times = 0
    while result:
        if max_times > 0:
            num = num + 1
            if num > max_times:
                return "fail"
        if need_click:
            pyautogui.click()

        r1 = check_icon(other_icon)
        r2 = check_icon(other_icon_1)
        r3 = check_icon(other_icon_2)
        if r3:
            for i in range(1, 4):
                print("pause ")
                print(i)
                time.sleep(1)
                pyautogui.click()
        r4 = check_icon(other_icon_3)
        r5 = check_icon(other_icon_4)
        if click_one_return & (r1 | r2 | r3 | r4):
            return
        if r1 | r2 | r3 | r4:
            print("click one")
        else:
            times = times + 1
            if times > 40:
                for i in range(1, 4):
                    print("pause ")
                    print(i)
                    time.sleep(0.2)
                    pyautogui.click()
        icon_location = sg.look_for_img(icon_path)

        if icon_location is not None:
            pyautogui.moveTo(x=icon_location.x + x_move, y=icon_location.y + y_move)
            pyautogui.click()
            if need_sleep:
                time.sleep(0.5)
            if need_break:
                result = False
        else:
            if icon_sec_path is not None:
                icon_location = sg.look_for_img(icon_sec_path)
                if icon_location is not None:
                    pyautogui.moveTo(x=icon_location.x + x_move, y=icon_location.y + y_move)
                    pyautogui.click()
                    if need_sleep:
                        time.sleep(0.5)
                    if need_break:
                        result = False
            else:
                print("no get icon location, " + icon_path)
                time.sleep(0.2)
        if break_icon is not None:
            break_icon_location = sg.look_for_img(break_icon)
            if break_icon_location is not None:
                print("break icon find , break")
                pyautogui.moveTo(x=break_icon_location.x, y=break_icon_location.y)
                pyautogui.click()
                return True
    return False


# click 1中间
def click_img_2_choose_one(icon_path, need_click=True, need_sleep=False, x_move=0, y_move=0, sec_icon=None, max_times=-1, other_icon=None):
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
            sec_icon_location = sg.look_for_img(sec_icon)
            if sec_icon_location is not None:
                pyautogui.moveTo(sec_icon_location)
                pyautogui.click()
        icon_location = sg.look_for_img(icon_path)
        if icon_location is None:
            if other_icon is not None:
                icon_location = sg.look_for_img(other_icon)

        if icon_location is not None:
            pyautogui.moveTo(x=icon_location.x + x_move, y=icon_location.y + y_move)
            pyautogui.click()
            if need_sleep:
                time.sleep(3)
            result = False
        else:
            print("no get icon location, " + icon_path)
            time.sleep(0.2)


import start_gzlj as gj


def xin_lai_du():
    while True:
        gj.click_img("icon\\zhuye.png", y_move=-600)
        gj.click_img("icon\\xinlaidu_select_blue.png", other_icon="icon\\xinlaidu_select_yellow.png")


def duihuan_zidong():
    click_img(icon_path="icon\\switch_again.png", icon_sec_path="icon\\qudeyu_yilan.png", need_click=False,
              other_icon="icon\\switch_again_again.png", other_icon_1="icon\\switch_ok.png",
              other_icon_2="icon\\switch_reset.png",
              other_icon_4="icon\\switch_100.png",
              other_icon_3="icon\\switch_100.png", need_break=False,
              break_icon="icon\\switch_100.png")


xin_lai_du()
# while True:
    # jue_se_ju_qing()
    # ju_qing_zidong()
    # duihuan_zidong()
