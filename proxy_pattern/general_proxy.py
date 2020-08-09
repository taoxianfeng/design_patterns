#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
module name: proxy proto design pattern
module description: 
普通代理模式对外暴露的接口仅是代理类
用户层仅需要初始化代理后，调用代理类的方法可执行对应执行步骤
此处相当于代理类重新封装了业务类，通过代理类初始化业务类，执行业务类的业务，整体的输入与输出未改变
Authors: taoxianfeng(taoxianfeng2012@163.com)
Date:    2020/08/09
"""
from abc import ABC, abstractmethod, abstractstaticmethod
import sys


class IGamePlayer(ABC):
    @abstractmethod
    def login(self, name: str, password: str):
        pass

    @abstractmethod
    def killboss(self):
        pass

    @abstractmethod
    def update(self):
        pass


class GamePlayer(IGamePlayer):
    def __init__(self, gameplayer: IGamePlayer, name: str):
        self._name = name
        if gameplayer:
            self._gameplayer = gameplayer
        else:
            raise Exception("Do not creat real user")
        print(" class name : {}".format(self.__class__.__name__))

    def login(self, name: str, passwd: str):
        print("user: {}  log in successful".format(name))
    

    def killboss(self):
        print("user: {} is killing boss ".format(
            sys._getframe().f_code.co_name))

    def update(self):
        print("user: {} is updating".format(sys._getframe().f_code.co_name))


class GameplayerProxy(IGamePlayer):
    def __init__(self, name: str):
        try:
            #  将self para  init class GamePlayer
            self._name = name
            self._gameplayer = GamePlayer(self, name)

        except Exception as e:
            print("init {} invalid,exception: {}".format(
                self.__class__.__name__, e))

    def killboss(self):
        self._gameplayer.killboss()

    def login(self, name: str, passwd: str):
        self._gameplayer.login(name=name, passwd=passwd)

    def update(self):
        self._gameplayer.update()


class Client():
    @staticmethod
    def excute(name: str):
        proxy = GameplayerProxy(name=name)
        from datetime import datetime
        print("begin time : {}".format(datetime.now()))
        proxy.login(name=name, passwd='123456')
        proxy.killboss()
        proxy.update()


if __name__ == "__main__":
    Client.excute(name="taoxianfeng")
