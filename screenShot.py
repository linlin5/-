#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import keyboard # 监控键盘  pip install keyboard
from PIL import Image,ImageGrab  # Pillow
from time import sleep
import sys
from baidu import BaiDuAPI
from getText import GetText

def screenShot():
    '''用于获取剪切板图片信息并保存到本地'''

    #截图开始 Ctrl+Alt+a,开始截图
    if keyboard.wait(hotkey='Ctrl+Alt+a') == None:
        #截图结束的条件，回车结束截图
        if keyboard.wait(hotkey='Enter') == None:
            sleep(0.01)  # 停顿一下，否则粘贴板里面不是最新的图片
            # 复制剪切板里面的图片
            im = ImageGrab.grabclipboard()
           # if isinstance(im, Image.Image):
            im.save('LL.png')

            #else:
            #   print('请重新截图！！')
        else:
            print('请按F1,Ctrl+C实现识别')


if __name__ == '__main__':

    baiduapi=BaiDuAPI('password.ini')

    for _ in range(sys.maxsize):
        screenShot()

        texts = baiduapi.picture2Text('LL.png')
        #print(baiduapi.picture2Text('LL.png'))
        GetText.setText(texts)
        sleep(0.01)
        GetText.getText()