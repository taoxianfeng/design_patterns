# https://blog.csdn.net/water_likud/article/details/80566177
from types import MethodType

class HandlerException(Exception):
    def __init__(self, cls):
        super(HandlerException, self).__init__(cls, 'is not a hanlder class')


class ProxyFactory:
    def __init__(self, hcls):
        if issubclass(hcls, InvocationHandler) or hcls is InvocationHandler:
            self.hcls = hcls
        else:
            raise HandlerException(hcls)

    def __call__(self, cls):

        return Proxy(cls, self.hcls)


class Proxy:
    def __init__(self, cls, hcls):
        self.cls = cls
        self.hcls = hcls
        self.handlers = dict()

    def __call__(self, *args, **kwargs):
        self.obj = self.cls(*args, **kwargs)
        return self

    def __getattr__(self, attr):
        print('get attr', attr)
        isExist = hasattr(self.obj, attr)
        res = None
        if isExist:
            res = getattr(self.obj, attr)
            if isinstance(res, MethodType):
                if self.handlers.get(res) is None:
                    self.handlers[res] = self.hcls(self.obj, res)
                return self.handlers[res]
            else:
                return res
        return res


class InvocationHandler:
    def __init__(self, obj, func):
        self.obj = obj
        self.func = func

    def __call__(self, *args, **kwargs):
        print('handler:', self.func, args, kwargs)
        return self.func(*args, **kwargs)


@ProxyFactory(InvocationHandler)
class Sample:
    def __init__(self, age):
        self.age = age

    def foo(self):
        print('hello', self.age)

    def add(self, x, y):
        return x + y

if __name__ == "__main__":
    # import pdb 
    # pdb.set_trace()
    s = Sample(12)
    print(type(s))
    s.foo()
    s.add(1, 2)
    s.add(2, 4)
    print(s.age)
