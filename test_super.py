class A:
    def __init__(self):
        self.n = 2

    def add(self, m):
        print('self is {0} @A.add'.format(self))
        self.n += m

class E:
    def __init__(self):
        self.n = 7

    def add(self, m):
        print('self is {0} @E.add'.format(self))
        self.n += 8

class B(A):
    def __init__(self):
        self.n = 3

    def add(self, m):
        print('self is {} @B.add'.format(self))
        super().add(m)
        self.n += 3


class C(E):
    def __init__(self):
        self.n = 4

    def add(self, m):
        print('self is {0} @C.add'.format(self))
        super().add(m)
        self.n += 4


class D(B, C):
    def __init__(self):
        self.n = 5

    def add(self, m):
        print('self is {0} @D.add'.format(self))
        super().add(m)
        self.n += 5
d = D()
d.add(2)
print(d.n)

# d.n=5+3+4+2+5=19
# self is <__main__.D object at 0x10d99e4e0> @D.add
# self is <__main__.D object at 0x10d99e4e0> @B.add
# self is <__main__.D object at 0x10d99e4e0> @C.add
# self is <__main__.D object at 0x10d99e4e0> @A.add