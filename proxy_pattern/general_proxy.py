#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
module name: proxy proto design pattern
module description: 
普通代理模式对外暴露的接口仅是代理类
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
    def killskill(self):
        pass


class GamePlayer(IGamePlayer):
    def __init__(self, name: str, passwd: str):
        self._name = name
        self._passwd = passwd
        self._play_mode = True
        self._proxy = None
        self.login(name=name, passwd=passwd)
        # print(" class name : {}".format(self.__class__.__name__))

    def login(self, name: str, passwd: str):
        print("user: {}  log in successful".format(name))

    def killskill(self):
        print("使用{}".format(
            sys._getframe().f_code.co_name))


class GameplayerProxy(IGamePlayer):
    def __init__(self, name: str, passwd: str, realname: str):
        try:
            #  将self para  init class GamePlayer
            self._name = name
            print("请输入realusers输入登录密码")
            realuserpasswd = input()
            self._gameplayer = GamePlayer(realname, realuserpasswd)

        except Exception as e:
            print("init {} invalid,exception: {}".format(
                self.__class__.__name__, e))

    def killskill(self):
        self._gameplayer.killskill()

    def proxylogin(self, name: str, passwd: str):
        print("{} successful".format(
            sys._getframe().f_code.co_name))

    def login(self, name: str, passwd: str):
        self._gameplayer.login(name=name, passwd=passwd)


class Client():
    """
    代理角色找到真实的角色
    """
    @staticmethod
    def excute():
        proxy = GameplayerProxy(name="Alice", passwd="123456", realname="tony")
        proxy.killskill()


if __name__ == "__main__":
    Client.excute()
