class A:
    def info(self):
        print("hello world")


class D:
    def info2(self):
            print("hello ptik")


class B(A):
    pass

class C(B,D):
    pass
    
c = C()
c.info()
c.info2()