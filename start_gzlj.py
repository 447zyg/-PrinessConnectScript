import pyautogui
import time


def mana_tan_suo():
    click_img("icon\\icon_maoxian.png", need_click=False)
    click_img("icon\\icon_tansuo.png", need_click=False)
    click_img("icon\\icon_exp.png", need_click=False)

    click_img("icon\\icon_exp_mana_top.png", need_click=False)
    click_img("icon\\icon_exp_mana_saodang.png", need_click=False)
    click_img("icon\\dialog_ok.png", need_click=False)

    click_img("icon\\from_exp_2_mana.png", need_click=False)

    click_img("icon\\icon_exp_mana_top.png", need_click=False)
    click_img("icon\\icon_exp_mana_saodang.png", need_click=False)
    click_img("icon\\dialog_ok.png", need_click=False)

    click_img("icon\\tan_suo_finish.png", need_click=False)


# 获取小屋内部东西
def gonghui_xiaowu():
    click_img("icon\\gong_hui_xiao_wu.png", need_click=False)
    click_img("icon\\xiaowu_get_all.png")
    time.sleep(2)
    click_img("icon\\xiaowu_get_close.png", need_click=False)


# 免费10连
def free_ten_get():
    time.sleep(3)
    click_img("icon\\icon_zhuandan.png",need_click=False)
    click_img("icon\\putong.png",need_click=False, other_icon="icon\\putong_small.png",
              third_icon="icon\\putong_bak_1.png")
    click_img("icon\\icon_mianfeishilian.png",need_click=False, other_icon="icon\\icon_mianfeishilian_bak.png")
    click_img("icon\\free_get_ok.png")
    click_img("icon\\icon_ok_white.png")


# 购买mana和点赞
def bug_mana_and_zan():
    time.sleep(3)
    click_img("icon\\zhuye.png",need_click=False)
    click_img("icon\\shouye_youshangjiao_icon_1.png", False, True, x_move=-820, y_move=25)
    click_img("icon\\buy_mana.png",need_click=False)
    click_img("icon\\buy_mana_ok.png",need_click=False)
    click_img("icon\\icon_cancel.png",need_click=False)
    click_img("icon\\icon_zhandui.png",need_click=False)
    time.sleep(3)
    click_img("icon\\icon_chengyuan.png",need_click=False, sec_icon="icon\\tuandui_dianzan.png")
    click_img("icon\\icon_zan.png")
    click_img("icon\\icon_ok.png",need_click=False)


# 刚启动初始化 废弃
def init_click():
    click_img("icon\\icon.png", need_click=False)
    time.sleep(10)
    click_img("icon\\so_net_logo.png")
    click_img("icon\\icon_close_tips.png")


# 地下城new skip
def di_xia_cheng_new():
    time.sleep(3)
    click_img("icon\\icon_maoxian.png",need_click=False)
    click_img("icon\\dixiacheng.png",need_click=False)
    # click_img("icon\\lvlongdixiaceng.png", need_click=False)
    time.sleep(3)
    click_img("icon\\fuyoudixiacheng.png", need_click=False)
    # click_img("icon\\dixiacheng_ok.png",need_click=False)
    click_img("icon\\dixiacheng_skip_blue.png",need_click=False)
    click_img("icon\\dixiacheng_ok_white.png",need_click=False)

# 地下城
def di_xia_cheng():
    time.sleep(3)
    click_img("icon\\icon_maoxian.png",need_click=False)
    click_img("icon\\dixiacheng.png",need_click=False)
    click_img("icon\\dixiacheng_bottom_icon.png", need_click=False,y_move=200)
    click_img("icon\\dixiacheng_ok.png",need_click=False)

    click_img("icon\\yi_ceng.png",need_click=False)
    click_img("icon\\dixiacheng_jinxingtiaozhan.png",need_click=False)
    click_img("icon\\wodeduiwu.png",need_click=False)
    click_img("icon\\bianzu3.png",need_click=False)
    time.sleep(1)
    click_img("icon\\hujiao_diyizu.png",need_click=False)
    time.sleep(1)
    click_img("icon\\dixiacheng_zhandoukaishi.png",need_click=False)
    time.sleep(10)
    click_img("icon\\dixiacheng_next.png",need_click=False)
    click_img("icon\\dixiacheng_baoxiang_ok.png",need_click=False)

    click_img("icon\\dixiaceng_2ceng.png",need_click=False)
    click_img("icon\\dixiacheng_jinxingtiaozhan.png",need_click=False)
    click_img("icon\\dixiacheng_zhandoukaishi.png",need_click=False)
    time.sleep(10)
    click_img("icon\\dixiacheng_next.png",need_click=False)
    click_img("icon\\dixiacheng_baoxiang_ok.png",need_click=False)

    click_img("icon\\dixiaceng_sanceng.png",need_click=False, other_icon="icon\\dixiaceng_sanceng_bak.png")
    click_img("icon\\dixiacheng_jinxingtiaozhan.png",need_click=False)
    click_img("icon\\dixiacheng_zhandoukaishi.png",need_click=False)
    time.sleep(10)
    click_img("icon\\dixiacheng_next.png",need_click=False)
    click_img("icon\\dixiacheng_baoxiang_ok.png",need_click=False)

    click_img("icon\\dixiacheng_sicheng.png",need_click=False, other_icon="icon\\dixiacheng_sicheng_bak.png")
    click_img("icon\\dixiacheng_jinxingtiaozhan.png",need_click=False)
    click_img("icon\\dixiacheng_zhandoukaishi.png",need_click=False)
    time.sleep(10)
    click_img("icon\\dixiacheng_next.png",need_click=False)
    click_img("icon\\dixiacheng_baoxiang_ok.png",need_click=False)

    click_img("icon\\dixiacheng_wucheng.png",need_click=False)
    click_img("icon\\dixiacheng_jinxingtiaozhan.png",need_click=False)
    click_img("icon\\dixiacheng_zhandoukaishi.png",need_click=False)
    time.sleep(30)
    click_img("icon\\dixiacheng_boss_fail.png",need_click=False)
    click_img("icon\\dixiacheng_wucheng.png",need_click=False)
    click_img("icon\\dixiacheng_jinxingtiaozhan.png",need_click=False)
    click_img("icon\\wodeduiwu.png",need_click=False)
    click_img("icon\\bianzu3.png",need_click=False)
    time.sleep(1)
    click_img("icon\\hujian_duiwu_3_2.png",need_click=False)
    time.sleep(1)
    click_img("icon\\dixiacheng_zhandoukaishi.png",need_click=False)
    time.sleep(40)
    click_img("icon\\dixiacheng_next.png",need_click=False)
    click_img("icon\\dixiacheng_baoxiang_ok.png",need_click=False)


# 回首页领取东西
def go_home_get():
    time.sleep(3)
    click_img("icon\\zhuye.png",need_click=False)
    click_img("icon\\zhuye_liwu.png")
    click_img("icon\\zhuye_liwu_get_all.png",need_click=False)
    click_img("icon\\zhuye_liwu_ok.png",need_click=False)
    click_img("icon\\zhuye_liwu_second_ok_white.png",need_click=False)
    click_img("icon\\zhuye_liwu_cancel.png",need_click=False)


# 自动打jjc
def play_jjc():
    click_img("icon\\icon_maoxian.png", need_click=False)
    click_img("icon\\jjc.png", need_click=False, other_icon="icon\\jjc_bak.png")
    click_img("icon\\jjc_select.png", need_click=False, x_move=200, y_move=50, sec_icon="icon\\jjc_fangshou_dialog_quxiao.png")
    click_img("icon\\jjc_zhandoukaishi.png", need_click=False)
    time.sleep(20)
    click_img("icon\\jjc_next.png", need_click=False, other_icon="icon\\jjc_next_bak.png")
    time.sleep(3)
    # click_img("icon\\zhuye.png", need_click=False)
    # time.sleep(3)


# 自动打pjjc
def play_pjjc():
    time.sleep(3)
    click_img("icon\\icon_maoxian.png", need_click=False)
    click_img(icon_path="icon\\pjjc.png", need_click=False)
    click_img("icon\\pjjc_top_text.png", need_click=False, x_move=200, y_move=50, sec_icon="icon\\pjjc_fangshou_dialog_quxiao.png")
    click_img("icon\\pjjc_duiwu3.png", need_click=False)
    click_img("icon\\jjc_zhandoukaishi.png", need_click=False)
    click_img("icon\\pjjc_next.png", need_click=False, other_icon="icon\\pjjc_next_small.png")


# 扫荡活动
def sao_dang_huo_dong(huodong_icon="icon\\icon_huodong.png"):
    click_img("icon\\icon_maoxian.png", need_click=False)
    click_img(huodong_icon)
    # click_img("icon\\huodong_close.png", max_times=100)

    click_img("icon\\icon_huodong_maoxian.png", False, True, sec_icon="icon\\huodong_close.png", max_times=20)
    click_img("icon\\huodong_hard.png", y_move=200)
    click_img("icon\\huodong_jinxingtiaozhan.png", need_click=False)
    click_img("icon\\huodong_zhandoukaishi.png", need_click=False)
    time.sleep(20)
    click_img("icon\\huodong_xiayibu.png", need_click=False)
    click_img("icon\\huodong_xiayibu_2.png", need_click=False)
    time.sleep(5)
    # click_img("icon\\renwu_iii.png", y_move=150, need_click=False)
    click_img("icon\\huodong_hard.png", need_click=False,x_move=-240, y_move=150)

    for i in range(1, 6):
        click_img("icon\\juese_saodang_jiahao.png", need_click=False)
        click_img("icon\\juese_saodang_jiahao.png", need_click=False)
        result = click_img("icon\\sanci_sandang.png", need_click=False)
        if result == "fail":
            print("no enough, break")
            break

        click_img("icon\\juese_saodang_ok.png", need_click=False)
        click_img("icon\\juese_saodang_3ci_ok_white.png", need_click=False)

        time.sleep(1)
        click_img("icon\\huodong_jiangli.png", need_click=False, x_move=-85, y_move=-150,
                  sec_icon="icon\\xianshishangdian_cancel.png")
        time.sleep(1)

    click_img("icon\\juese_saodang_quxiao.png", need_click=False)
    click_img("icon\\huodong_renwu.png", need_click=False)
    click_img("icon\\huodongrenwu_get_all.png", need_click=False, other_icon="icon\\huodong_quanbulingqu_bak.png")
    click_img("icon\\huodong_renwu_close.png",need_click=False)
    time.sleep(2)


# 角色 刷前x个喜欢的角色碎片
def juese_qianghua(num):
    time.sleep(3)
    click_img("icon\\jiaose.png", need_click=False)
    click_img("icon\\juese_shaixuan.png", need_click=False)
    click_img("icon\\juese_my_love.png", need_click=False)
    click_img("icon\\juese_ok.png", need_click=False)

    click_img("icon\\juese_top_left.png", need_click=False, y_move=150)
    click_img("icon\\juese_jinengqianghua.png", need_click=False)
    click_img("icon\\juese_jinengqianghua_qianghua.png", need_click=False)

    click_img("icon\\juese_cainengkaihua.png", need_click=False)

    # 这里修改几个扫荡几个角色的碎片 1-11 就是10个。以此类推
    for i in range(1, num):
        # is_six_star
        a = find_img("icon\\is_six_star.png", "icon\\qudefangfa_grap.png", "icon\\juese_qudefangfa.png")
        if a == 2:
            continue
        if a == 1:
            click_img("icon\\is_six_star.png", need_click=False, x_move=-300,y_move=-280)
            b = find_img("icon\\qudefangfa_grap.png", "icon\\juese_qudefangfa.png")
            if b == 0:
                continue

        click_img("icon\\juese_qudefangfa.png", need_click=False)
        click_img("icon\\juese_guanbi.png", need_click=False, y_move=-100)
        click_img("icon\\juese_saodang_jiahao.png", need_click=False)
        click_img("icon\\juese_saodang_jiahao.png", need_click=False)

        result = click_img("icon\\sanci_sandang.png", need_click=False, max_times=10)
        if result == "fail":
            print("no enough, break")
            click_img("icon\\juese_saodang_quxiao.png", need_click=False)
            click_img("icon\\juese_guanbi.png")
            break
        click_img("icon\\juese_saodang_ok.png", need_click=False)
        click_img("icon\\juese_saodang_3ci_ok_white.png", need_click=False)
        click_img("icon\\juese_saodang_quxiao.png", need_click=False,
                  sec_icon="icon\\xianshi_shangdian_quxiao.png", sec_icon_1="icon\\gonghuizhantanchuangquxiao.png")
        click_img("icon\\juese_guanbi.png")
        click_img("icon\\juese_qudefangfa.png", need_click=False, x_move=450, y_move=-225, other_icon="icon\\qudefangfa_grap.png")
        time.sleep(1)


# 领取每日任务奖励
def lingqu_meirirenwu_jiangli(no_in_home = True):
    time.sleep(3)
    if no_in_home:
        click_img("icon\\zhuye.png",need_click=False)
    time.sleep(3)
    click_img("icon\\zhuye_liwu_bak_3.png", need_click=False, other_icon="icon\\zhuye_renwu_bak.png", third_icon="icon\\zhuye_renwu_bak_11.png")
    click_img("icon\\zhuye_renwu_quanbulingqu.png", need_click=False)
    click_img("icon\\zhuye_renwu_lingquguanbi.png", need_click=False)


# 露娜塔
def luna_ta():
    click_img("icon\\icon_maoxian.png", need_click=False)
    click_img("icon\\lunazhita.png")
    for i in range(1, 5):
        click_img("icon\\lunata_saodang.png", need_click=False)
    click_img("icon\\lunata_wuzhang_saodang.png", need_click=False)
    click_img("icon\\juese_saodang_ok.png", need_click=False)
    click_img("icon\\juese_saodang_3ci_ok_white.png", need_click=False,
              sec_icon="icon\\xianshishangdian_cancel.png")


def open_mu_mu():
    pyautogui.press('winleft')
    pyautogui.typewrite('MuMu')
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(10)
    click_img(icon_path="icon\\mumu_launch_icon.png")


# click 1中间
def click_img(icon_path, need_click=True, need_sleep=False, x_move=0, y_move=0, sec_icon=None, max_times=-1,
              other_icon=None, third_icon=None, sec_icon_1=None):
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
            sec_icon_location = look_for_img(sec_icon)
            if sec_icon_location is not None:
                pyautogui.moveTo(sec_icon_location)
                pyautogui.click()

        if sec_icon_1 is not None:
            sec_icon_location = look_for_img(sec_icon_1)
            if sec_icon_location is not None:
                pyautogui.moveTo(sec_icon_location)
                pyautogui.click()

        icon_location = look_for_img(icon_path)
        if icon_location is None:
            if other_icon is not None:
                icon_location = look_for_img(other_icon)
                if icon_location is None:
                    if third_icon is not None:
                        icon_location = look_for_img(third_icon)

        if icon_location is not None:
            pyautogui.moveTo(x=icon_location.x + x_move, y=icon_location.y + y_move)
            pyautogui.click()
            if need_sleep:
                time.sleep(3)
            result = False
        else:
            print("no get icon location, " + icon_path)
            time.sleep(0.2)


# 回到主页
def go_home():
    time.sleep(3)
    click_img("icon\\zhuye.png", need_click=False)
    # click_img("icon\\zhuye_zhujiaodengji.png")


def xinsui_saodang():
    go_home()
    time.sleep(3)
    click_img("icon\\icon_maoxian.png", need_click=False)
    click_img("icon\\xinsui.png", need_click=False)
    click_img("icon\\xinsui_baozhu.png", need_click=False)

    click_img("icon\\shendiao_lv2.png", need_click=False)
    for i in range(1, 3):
        xinsui_xiangqing()

    click_img("icon\\shendiao_quxiao.png", need_click=False)
    click_img("icon\\shendian_back.png", need_click=False)
    click_img("icon\\shendian_xinsui.png", need_click=False)
    click_img("icon\\shendian_xinsui3.png", need_click=False)
    for i in range(1, 4):
        xinsui_xiangqing()
    click_img("icon\\shendiao_quxiao.png", need_click=False)


def xinsui_xiangqing():
    for i in range(1, 5):
        click_img("icon\\shendiao_saodang_jiahao.png", need_click=False)
    click_img("icon\\shendiao_saodang_5ci.png", need_click=False)
    click_img("icon\\dialog_ok.png", need_click=False)
    click_img("icon\\shendiao_dialog_white_ok.png", need_click=False)
    click_img("icon\\huodong_jiangli.png", need_click=False, x_move=-85, y_move=-150,
              sec_icon="icon\\xianshishangdian_cancel.png")
    time.sleep(1)


def buy_ti_li(num):
    click_img("icon\\icon_maoxian.png", need_click=False)
    time.sleep(2)
    click_img("icon\\zhuye.png", need_click=False)
    time.sleep(2)
    for i in range(1, num):
        time.sleep(3)
        click_img("icon\\zhuye_zhujiaodengji.png", False, True, x_move=355, y_move=65)
        # click_img("icon\\buy_tili_icon.png", need_click=False)
        click_img("icon\\dialog_ok.png", need_click=False)
        click_img("icon\\icon_buy_tili_white_ok.png", need_click=False)


def buy_ti_li1(num):
    for i in range(1, num):
        click_img("icon\\goumaitili.png", False, True)
        click_img("icon\\dialog_ok.png", need_click=False)
        click_img("icon\\icon_buy_tili_white_ok.png", need_click=False)
        time.sleep(2)


# 新增 模糊度
def look_for_img(path):
    return pyautogui.locateCenterOnScreen(path)


def find_img(icon_1, icon_2, icon_3=None, icon_4=None):
    while True:
        i1 = look_for_img(icon_1)
        if i1:
            return 1
        i2 = look_for_img(icon_2)
        if i2:
            return 2
        if icon_3 is not None:
            i3 = look_for_img(icon_3)
            if i3:
                return 3
        if icon_4 is not None:
            i4 = look_for_img(icon_4)
            if i4:
                return 4


def huodong():
    while True:
        click_img("icon\\renwu_iii.png", y_move=150, need_click=False, sec_icon="icon\\huodong_guanbi_saodadng.png",
                  sec_icon_1="icon\\huodong_quxiao_saodadng.png")
        click_img("icon\\jinxingtiaozhao_huodong_new.png")
        click_img("icon\\huodong_new_zhandoukaishi.png", need_click=False)
        for i in range (1,3):
            click_img("icon\\huodong_new_next.png", need_click=False,
                  sec_icon="icon\\xianshi_shangdian_quxiao.png")
            time.sleep(1)


def xianshishanggdian():
    click_img("icon\\zhuye.png", need_click=False)
    click_img("icon\\shangdian_icon.png", need_click=False)
    click_img("icon\\xianshishangddian_all.png", need_click=False)
    click_img("icon\\xianshishangddian_select_all.png", need_click=False)
    click_img("icon\\xianshishangddian_buy.png", need_click=False)
    click_img("icon\\xianshishangdian_ok.png", need_click=False)
    click_img("icon\\xianshishangdian_ok_2.png", need_click=False)
    return None