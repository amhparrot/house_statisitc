#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian
# 此代码仅供学习与交流，请勿用于商业用途。
# 二手房信息的数据结构


class ErShou(object):
    def __init__(self, district, area, name, price,unitprice,desc, pic):
    #def __init__(self, district, area, name, price,unitprice):
        self.district = district
        self.area = area
        self.price = price
        self.unitprice = unitprice
        self.name = name
        if desc is None:
            print(name)
        else:
            self.desc = desc
        if pic is None:
            print(pic)
        else:
            self.pic = pic
        #self.pic = pic
        

    def text(self):
        return self.district + "," + \
                self.area + "," + \
                self.name + "," + \
                self.price + "," + \
                self.unitprice + "," + \
                self.desc + "," + \
                self.pic
         
