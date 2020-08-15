'''
Description: 
Version: 1.0
Autor: 木瓜
Date: 2020-08-13 22:57:06
'''
from abc import ABC,abstractmethod

class Component(ABC):
    @abstractmethod
    def dosomething(self):
        pass

# class Composite(Component):
class Composite:
    def __init__(self):
        self._componentlist = []

    def add(self,component:Component):
        self._componentlist.append(component)

    def remove(self,component:Component):
        self._componentlist.remove(component)

    def getall(self):
        return self._componentlist

class Leaf(Component):
    def dosomething(self):
        print("do something by leaf")


 class Client:
     @staticmethod
     def excute(*argc,**argv):
         pass

