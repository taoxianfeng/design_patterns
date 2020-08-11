#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
module name:force proxy design pattern
module description:
强制代理模式对外暴露的接口仅是真实用户类，由真实用户指定代理用户
Authors: taoxianfeng(taoxianfeng2012@163.com)
Date:    2020/08/09

游戏物理编程模拟场景：
玩家A：name: Tony  passwd:123
玩家B：name: Alice  passwd:456

玩家A指定王家B做代理

"""

from abc import ABC, abstractmethod


class IGamePlayer(ABC):
    @abstractmethod
    def login(self, user: str, passwd: str):
        pass

    @abstractmethod
    def killskill(self):
        pass

    @abstractmethod
    def getproxy(self, gameplayer):
        return gameplayer


class GamePlayer(IGamePlayer):
    def __init__(self, user: str = None, passwd: str = None):
        self._name = user
        self._passwd = passwd
        self._play_mode = True
        self._proxy = None
        self.login(user=user, passwd=passwd)

    @property
    def name(self):
        return self._name

    def login(self, user: str, passwd: str):
        print("user:{} login successful")

    def _proxy_ensure(self, proxy_name):
        print("请玩家{}确认，请输入Y/N".format(proxy_name))
        value = input()
        if value.upper() == 'Y':
            print("玩家{}同意,玩家{}被迫处于观察模式".format(
                proxy_name, self._name))
            # init proxy object

            return True
        elif value.upper() == 'N':
            print("玩家{}拒绝代打请求".format(proxy_name))
            return False
        else:
            print("输入不合法，请重新输入Y/N")
            self._proxy_ensure(proxy_name)

    # def _mode_init(self):
    def getproxy(self, gameplayer: IGamePlayer):
        print("玩家{}进入代打申请流程".format(self.name))
        print("请输入代打玩家ID：")
        self._proxy_user_name = input()
        if self._proxy_ensure(self._proxy_user_name):
            print("玩家{}向玩家{}发起代打申请通过".format(self.name, self._proxy_user_name))
            self._proxy = GameplayerProxy(
                self, proxy_name=self._proxy_user_name)
        else:
            print("玩家{}拒绝，玩家{}发起代打申请失败".format(
                self._proxy_user_name, self.name))

    def killskill(self):
        if not self._proxy:
            print("用玩家{}使用kill技能")
        else:
            self._proxy.killskill()


class GameplayerProxy(IGamePlayer):
    def __init__(self, gameplayer: IGamePlayer, proxy_name: str):
        try:
            self._gameplayer = gameplayer
            self._proxy_name = proxy_name
            print("请玩家{}输入登录密码".format(gameplayer.name))
            passwd = input()
            self.login(user=gameplayer.name, passwd=passwd)
            print("玩家{}处于代打模式；玩家{}处于观察模式".format(
                proxy_name, gameplayer.name))
        except Exception as e:
            print("init {} invalid,exception: {}".format(
                self.__class__.__name__, e))

    def killskill(self):
        self._gameplayer.skill()

    def login(self, user: str, passwd: str):
        self._gameplayer.login(user=user, passwd=passwd)

    def getproxy(self):
        return self


class Client():
    """
    真实角色查找到代理角色
    """
    @staticmethod
    def excute():
        playtony = GamePlayer(user="Tony", passwd="123456")
        playtony.getproxy(playtony)


if __name__ == "__main__":
    Client.excute()
