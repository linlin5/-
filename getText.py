#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import win32con
import win32clipboard as w

class GetText:
    '''用于把图像识别的内容返回到剪贴板'''
    @staticmethod
    def getText():
        '''获取剪贴板的内容'''

        w.OpenClipboard()
        d = w.GetClipboardData(win32con.CF_UNICODETEXT)
        w.CloseClipboard()
        return d

    @classmethod
    def setText(sb,aString):
        '''需要传递一个参数用于复制到剪贴板'''

        w.OpenClipboard()
        w.EmptyClipboard()
        w.SetClipboardData(win32con.CF_UNICODETEXT,aString)
        w.CloseClipboard()

if __name__ == '__main__':

    GetText.setText('666777')
    GetText.getText()