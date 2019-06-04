# coding:utf8
import time
from appium import webdriver
from PIL import Image
import os

screenshotPath = ".//test.png"
saveImagePath = ".//base.png"

base_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/'


def into_notices_page():
    """
        进入我的页面

    """
    driver.find_element_by_xpath(base_xpath + 'android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.support.v7.widget.LinearLayoutCompat/'
                                 'android.widget.HorizontalScrollView/android.widget.LinearLayout/android.support.v7.app.a.c[5]').click()
    time.sleep(0.5)


def recognition_img_txt(img_name):
    """
    将图片中文件识别出来

    """
    if os.path.isfile(img_name):
        os.system('tesseract {} out -l chi_sim makebox'.format(img_name))
        print("输出坐标文件 out.box")
    else:
        print("{} not found.format(img_name)")


def get_position(word, img_name):
    """
    根据文字获取需要点击坐标
    """
    recognition_img_txt(img_name)
    lists = []
    print()
    if os.path.isfile('out.box'):
        with open('out.box', 'r', encoding='UTF-8') as f:
            for line in f:
                if line.split()[0] in word:
                    lists.append(line.split())
    return lists


def cancel_notices():
    for i in range(100):
        # 进入关注列表
        driver.find_element_by_xpath(base_xpath + 'android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/'
                                     'android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/'
                                     'android.view.ViewGroup[1]/android.widget.TextView[6]').click()
        time.sleep(1)
        # 点击第一个关注的问题
        driver.find_element_by_xpath(base_xpath + 'android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.FrameLayout/'
                                                  'android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.view.ViewGroup/'
                                                  'android.support.v7.widget.RecyclerView/android.support.v7.widget.LinearLayoutCompat[1]').click()
        time.sleep(2)
        driver.save_screenshot(screenshotPath)
        # imglement = driver.find_element_by_id("com.zhihu.android:id/question_header")  # 定位[已关注]按钮
        imglement = driver.find_element_by_id("root")
        location = imglement.location  # 获取元素X,Y的坐标
        print(location)
        size = imglement.size  # 获取元素的长宽
        print(size)
        # 指定位置坐标
        # rangle = (int(int(size['width'])*0.5), int(location['y'] + int(int(size['height'])*0.5)), int(size['width']), int(location['y'] + size['height']))
        rangle = (int(int(size['width'])*0.5), int(location['y']), int(size['width']-10), int(location['y'] + size['height']))
        print(rangle)
        image = Image.open(screenshotPath)  # 打开截图
        frame4 = image.crop(rangle)  # 使用image的crop函数，截取指定区域
        frame4.save(saveImagePath)
        recognition_img_txt(saveImagePath)
        lists = get_position('已关注', saveImagePath)
        print(lists)
        print((int(0.5*size['width']) + int(lists[0][1]), int(location['y'] + size['height']) - int(lists[0][4])))
        print((int(0.5*size['width']) + int(lists[-1][3]), int(location['y'] + size['height']) - int(lists[-1][2])))
        # driver.tap([(int(0.5*size['width']) + int(lists[0][1]), int(location['y'] + size['height']) - int(lists[0][4])),
        #             (int(0.5*size['width']) + int(lists[-1][3]), int(location['y'] + size['height']) - int(lists[-1][2]))], 100)
        driver.tap([(int(0.5*size['width']) + int(lists[0][1]) + 100, int(location['y'] + size['height']) - int(lists[0][4]) + 50)], 100)

        frame4.close()
        image.close()

        time.sleep(2)
        driver.press_keycode(4)
        time.sleep(0.5)
        driver.press_keycode(4)
        time.sleep(2)

    time.sleep(3)


if __name__ == '__main__':
    capabilities = dict()
    capabilities['platformName'] = 'Android'
    capabilities['platformVersion'] = '9.0'
    capabilities['deviceName'] = 'ONEPLUS A5010'
    capabilities['udid'] = '4f37087f'
    capabilities['appPackage'] = 'com.zhihu.android'
    capabilities['appActivity'] = 'com.zhihu.android.app.ui.activity.MainActivity'
    capabilities['unicodeKeyboard'] = 'True'
    capabilities['resetKeyboard'] = 'True'
    capabilities['noReset'] = 'True'
    capabilities['noSign'] = 'True'
    # 连接测试机所在服务器
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', capabilities)
    time.sleep(6)
    into_notices_page()
    cancel_notices()
    driver.quit()
