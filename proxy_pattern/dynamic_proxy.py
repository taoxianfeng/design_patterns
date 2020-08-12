#
"""
code from  https://zhuanlan.zhihu.com/p/37543017
description:
我们使用了神奇的__getattribute__方法。在Python里面类的属性(方法)都是一个对象，
我们先拿到这个类方法对象attr，然后对这个类方法对象进行包装，再返回包装后的新方法对象newAttr。
注意在获取target对象时，不能直接使用self.target，因为self.target会再次调用__getattribute__方法，
这样就会导致死循环致堆栈过深曝出异常。取而代之应该使用object.__getattribute__方法来获取对象的属性值。
"""
class Proxy(object):

    def __init__(self, target):
        # 将target 作为Proxy的属性，可以通过基类object调用 
        self.target = target
        pass

    def __getattribute__(self, name):
        # 调用self.target or object.target 给临时变量target
        target = object.__getattribute__(self, "target")
        # 调用self.target.name给临时变量attr or object.target.name
        attr = object.__getattribute__(target, name)

        def newAttr(*args, **kwargs):  # 包装
            print("before print")
            # attr 替代 self.target.name(*args, **kwargs) or object.target.name(*args, **kwargs)
            res = attr(*args, **kwargs)
            print("before print")
            return res
        
        return newAttr


class RealHello(object):

    def prints(self, s: str):
        print(s)


if __name__ == '__main__':
    t = RealHello()
    p = Proxy(t)
    import pdb
    pdb.set_trace()
    p.prints("world")
