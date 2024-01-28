class X:
    def __init__(self):
        pass

    def __repr__(self):
        return "X"

class Int:
    def __init__(self, i):
        self.i = i
    
    def __repr__(self):
        return str(self.i)

class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)
class Sub:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        if isinstance(self.p2, Add) or isinstance(self.p2, Sub):
            return repr(self.p1) + " - (" + repr(self.p2) + ")"
        return repr(self.p1) + " - " + repr(self.p2)
    
class Mul:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        p1_str = "( " + repr(self.p1) + " )" if isinstance(self.p1, Add) or isinstance(self.p1, Sub) else repr(self.p1)
        p2_str = "( " + repr(self.p2) + " )" if isinstance(self.p2, Add) or isinstance(self.p2, Sub) else repr(self.p2)
        return p1_str + " * " + p2_str


class Div:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        p1_str = "( " + repr(self.p1) + " )" if isinstance(self.p1, Add) or isinstance(self.p1, Sub) else repr(self.p1)
        p2_str = "( " + repr(self.p2) + " )" if isinstance(self.p2, Add) or isinstance(self.p2, Sub) else repr(self.p2)
        return p1_str + " / " + p2_str

# Example usage
poly = Add( Sub( Int(4), Int(3)), Div( X(), Mul( Int(1), Add( Mul(X(), X()), Int(1)))))
print(poly)


#print("Test 1:", Add(Int(3), Int(4)))
#print("Test 2:", Sub(Int(5), Int(2)))
#print("Test 3:", Add(Sub(Int(4), Int(3)), Int(2)))
#print("Test 4:", Mul(Add(Int(2), X()), Int(3)))
#print("Test 5:", Add(Mul(X(), Sub(Int(5), X())), Div(Add(X(), Int(4)), X())))
#print("Test 6:", Sub(Add(Int(1), Mul(X(), Int(2))), Div(X(), Add(Int(3), X()))))
