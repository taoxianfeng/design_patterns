https://zhuanlan.zhihu.com/p/37543017
class Proxy(object):

    def __init__(self, target):
        self.target = target

    def __getattribute__(self, name):
        target = object.__getattribute__(self, "target")
        attr = object.__getattribute__(target, name)

        def newAttr(*args, **kwargs):  # 包装
            print("before print")
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
