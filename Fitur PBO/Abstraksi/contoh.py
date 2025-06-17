from abc import ABC, abstractmethod
 
# class abstrak
class MyClass(ABC):
    @abstractmethod
    def myMethod1(self):   
        pass
    def myMethod2(self):
        print("Hello World")
 
# subclass dari MyClass
class MySubClass(MyClass):
    # implementasi dari myMethod1()
    def myMethod1(self):
        print("Hello Python")

c = MySubClass()
 
c.myMethod1() # menampilkan "Hello World"
c.myMethod2() # menampilkan "Hello Python"