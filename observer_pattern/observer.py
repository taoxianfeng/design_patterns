'''
Description: 
场景：用户订阅主题
1. user1 user2 订阅 topic1 topic2
2. topic1/2 状态变更时，主动通知user1 user2

用户订阅主题机制；
主题信息更新时，通知用户机制；
用户更新订阅信息机制；

主题属性分析：
1. 每个主题都是全局唯一，所有用户共用主题
2. 主题需要维护订阅的所有的用户
3. 主题的的状态更新时，实时主动通知用户机制

普通用户属性分析：
1. 用户可订阅主题
2. 用户维护所有订阅的主题

管理者用户属性分析（未实现）：
1. 可更新主题状态
2. 设置管理用户的权限


Version: 1.0
Autor: 木瓜
Date: 2020-08-13 23:44:53
'''

from abc import ABC, abstractmethod, abstractstaticmethod

import threading


# class Singleton(object):
#     '''
#     单例模式
#     '''
#     _instance_lock = threading.Lock()

#     # def __init__(self,*args, **kwargs):
#     #     pass

#     def __new__(cls, *args, **kwargs):
#         if not hasattr(Singleton, "_instance"):
#             with Singleton._instance_lock:
#                 if not hasattr(Singleton, "_instance"):
#                     Singleton._instance = object.__new__(cls)
#         return Singleton._instance

def Singleton(cls):
    _instance = {}

    def _singleton(*args, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kargs)
        return _instance[cls]

    return _singleton

class AbstractSubject(ABC):
    '''
    description:
    抽象主题类
    '''
    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass


@Singleton
class Subject(AbstractSubject):
    '''
    description:
    单例主题类
    '''

    def __init__(self, topic: str):
        # self._observers = []
        self._subjectstate = None
        self.topic = topic
        self.observers = []

    @property
    def subjectstate(self):
        return self._subjectstate

    @subjectstate.setter
    def subjectstate(self, state):
        self._subjectstate = state

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self,info):
        for obj in self.observers:
            obj.update(self,info)


class Observer(ABC):
    def __init__(self, name: str):
        self._subjects = []
        self._name = name

    def attach(self, subject: Subject):
        if subject not in self._subjects:
            self._subjects.append(subject)
            subject.attach(observer=self)

    def detach(self, subject: Subject):
        if subject not in self._subjects:
            self._subjects.remove(subject)
            subject.detach(observer=self)

    # @abstractmethod
    def getsubject(self, subject):
        '''
        @description: 获取指定已订阅主题中的当前的状态
        @param: {}
        @return: {}
        @author: 木瓜
        '''
        if subject in self._subjects:
            return subject
        else:
            print('用户{} 未注册主题{}'.format(self._name, subject))
            return

    # @abstractmethod
    def update(self, subject,info):
        '''
        @description: 更新指定已订阅主题的信息
        @param: {}
        @return: {}
        @author: 木瓜
        '''
        if subject in self._subjects:
            print('通知用户{} 主题object:{} 主题信息：{} 通知信息：{} '.format(
                self._name, subject, subject.topic,info))


if __name__ == "__main__":
    # init subject
    sub1 = Subject('吾要成长')
    sub2 = Subject('吾要成长')
    if sub1 is sub2 :
        print('Sbuject is singleon')
    # init user
    alice = Observer('alice')
    tony = Observer('tony')
    #  user 订阅 sub1
    alice.attach(sub1)
    tony.attach(sub1)
    # 主题通知 user
    sub1.notify(info = '午饭时间：14:00')
