class A:
    def __init__(self):
        print("A's constructor")
        super().__init__()
class B:
    def __init__(self):
        print("B's constructor")
class C(A,B):
    def __init__(self):
        print("C'sconstructor")
        super().__init__()
#calling  block
cobj=C()
print(C.mro())

