#!/usr/bin/python3
# -*- coding: utf-8 -*-

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
    

if __name__ == "__main__":
    subject = RealSubject(topic = "init proxy topic")
    proxy  = Proxy(subject= subject)
    proxy.request()