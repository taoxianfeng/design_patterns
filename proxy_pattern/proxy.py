#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
module name: proxy proto design pattern
module description: 
Authors: taoxianfeng(taoxianfeng2012@163.com)
Date:    2020/08/09
"""

from abc import ABC, abstractmethod


class Subject(ABC):
    @abstractmethod
    def request(self):
        pass


class RealSubject(Subject):
    def __init__(self,topic:str):
    # super.__init__()
        self._topic =  topic
        pass

    def request(self):
        print("excute {} request method".format(RealSubject.__name__))
        print("subject topic : {}".format(self._topic))


class Proxy(Subject):
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
    
class Client():
    def __init__(self):
        pass

    def excute(self):
        subject = RealSubject(topic = "init proxy topic")
        proxy  = Proxy(subject= subject)
        proxy.request()


if __name__ == "__main__":
    client = Client()
    client.excute()
 