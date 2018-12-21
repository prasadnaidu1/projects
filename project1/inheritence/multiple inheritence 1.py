class K:
    def __init__(self):
        print("K's constuructor")
        super().__init__()
class P(K):
    def __init__(self):
        print("P'constructor")
        super().__init__()
class A:
    def __init__(self):
        print("A'constructor")
        super().__init__()

class B:
    def __init__(self):
        print("B'constructor")
        super().__init__()
class X(A,B):
    def __init__(self):
        print("X'constructor")
        super().__init__()
class M(P,X):
    def __init__(self):
        print("M'constructor")
        super().__init__()

#calling block
mobj=M()
