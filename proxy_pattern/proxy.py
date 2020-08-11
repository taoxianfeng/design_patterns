#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
module name: proxy proto design pattern
module description: 
Authors: taoxianfeng(taoxianfeng2012@163.com)
Date:    2020/08/09

20200811
add abstract class iproxy include count function 
"""

from abc import ABC, abstractmethod


class Iproxy(ABC):
    @abstractmethod
    def count(self):
        """
        计费
        """
        return


class Subject(ABC):
    @abstractmethod
    def request(self):
        pass


class RealSubject(Subject):
    def __init__(self, topic: str):
        # super.__init__()
        self._topic = topic
        pass

    def request(self):
        print("excute {} request method".format(RealSubject.__name__))
        print("subject topic : {}".format(self._topic))


class Proxy(Subject, Iproxy):
    def __init__(self, subject: Subject):
        self._suject = subject

    def _before(self):
        pass

    def _after(self):
        pass

    def request(self):
        self._before()
        self._suject.request()
        self._after()

    def count(self):
        print("代理费用为：50元")


class Client():
    def __init__(self):
        pass

    def excute(self):
        subject = RealSubject(topic="init proxy topic")
        proxy = Proxy(subject=subject)
        proxy.request()
        proxy.count()


if __name__ == "__main__":
    client = Client()
    client.excute()
