# -*- coding:utf-8 -*-
import uiautomator2 as u2

# d = u2.connect_usb('D5F7N18519004450')
# # d = u2.connect('10.110.8.188:7912')
# print(d.info)

d = u2.connect('http://0.0.0.0:7912')


def main():
    jd_sign()
    jd_jr_sign()


def jd_sign():
    d.app_start("com.jingdong.app.mall")
    d(resourceId="com.jingdong.app.mall:id/gf", text=u"领京豆").click()
    # d(resourceId="com.jingdong.app.mall:id/g1", className="android.widget.ImageView", instance=6).click()
    d(text=u"签到领京豆").click()
    d(className="android.widget.ImageView", instance=5).click()
    d(text=u"收入囊中").click()
    d.press("back")
    d(resourceId="com.jd.lib.enjoybuy:id/drag_view").click()


def jd_jr_sign():
    d.app_start("com.jd.jrapp")
    # d(resourceId="com.jd.jrapp:id/btn_jump").click()

    close_btn = d(resourceId="com.jd.jrapp:id/ibtn_zc_product_notice_board_close")
    if close_btn:
        close_btn.click()

    d(resourceId="com.jd.jrapp:id/iv_fourth_icon").click()
    d(resourceId="com.jd.jrapp:id/tv_item_label").click()
    d(description=u"签到领钢镚").click()
    # d.app_stop("com.jd.jrapp")


if __name__ == '__main__':
    main()
