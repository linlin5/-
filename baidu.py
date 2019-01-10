#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from aip import AipOcr
import configparser

class BaiDuAPI:
    '''调用百度云的API实现图片文字识别'''

    #初始化 函数
    def __init__(self, filePath):
        target = configparser.ConfigParser()
        target.read(filePath)
        app_id = target.get('工单密码','APP_ID')
        api_key = target.get('工单密码', 'API_KEY')
        secret_key = target.get('工单密码', 'SECRET_KEY')

        '''你的 APPID AK SK'''
        APP_ID = app_id
        API_KEY = api_key
        SECRET_KEY = secret_key

        self.client =AipOcr(APP_ID, API_KEY, SECRET_KEY)

    def picture2Text(self,filePath):
        # 读取图片
        image = self.getPicture(filePath)
        texts = self.client.basicGeneral(image)
        #print(texts)
        allTexts =''
        for words in texts['words_result']:
            allTexts = allTexts + ''.join(words.get('words',''))
        return allTexts

    @staticmethod #装饰器
    def getPicture(filePath):
        with open(filePath,'rb') as fp:
            return fp.read()


if __name__ == '__main__':

    baiduapi=BaiDuAPI('password.ini')
    print(baiduapi.picture2Text('LL.png'))
    #BaiDuAPI.asd(BaiDuAPI())