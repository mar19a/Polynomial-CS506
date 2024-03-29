class X:
    def __init__(self):
        pass

    def __repr__(self):
        return "X"

    def evaluate(self, value):
        return value

class Int:
    def __init__(self, i):
        self.i = i
    
    def __repr__(self):
        return str(self.i)

    def evaluate(self, value):
        return self.i

class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)

    def evaluate(self, value):
        return self.p1.evaluate(value) + self.p2.evaluate(value)

class Sub:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        if isinstance(self.p2, Add) or isinstance(self.p2, Sub):
            return repr(self.p1) + " - (" + repr(self.p2) + ")"
        return repr(self.p1) + " - " + repr(self.p2)

    def evaluate(self, value):
        return self.p1.evaluate(value) - self.p2.evaluate(value)

class Mul:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        p1_str = "( " + repr(self.p1) + " )" if isinstance(self.p1, Add) or isinstance(self.p1, Sub) else repr(self.p1)
        p2_str = "( " + repr(self.p2) + " )" if isinstance(self.p2, Add) or isinstance(self.p2, Sub) else repr(self.p2)
        return p1_str + " * " + p2_str
    
    def evaluate(self, value):
        return self.p1.evaluate(value) * self.p2.evaluate(value)

class Div:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        p1_str = "( " + repr(self.p1) + " )" if isinstance(self.p1, Add) or isinstance(self.p1, Sub) else repr(self.p1)
        p2_str = "( " + repr(self.p2) + " )" if isinstance(self.p2, Add) or isinstance(self.p2, Sub) else repr(self.p2)
        return p1_str + " / " + p2_str

    def evaluate(self, value):
        return self.p1.evaluate(value) / self.p2.evaluate(value)

# Example usage
poly = Add( Add( Int(4), Int(3)), Add( X(), Mul( Int(1), Add( Mul(X(), X()), Int(1)))))
print(poly.evaluate(-1))


expression = Add(Int(3), Int(4))
result = expression.evaluate(0)  # The value of X is irrelevant here
print("Evaluate Test 1 Result:", result)

expression = Mul(X(), Int(4))
result = expression.evaluate(2)
print("Evaluate Test 2 Result:", result)

expression = Add(Mul(X(), Int(3)), Int(7))
result = expression.evaluate(-1)
print("Evaluate Test 3 Result:", result)

expression = Sub(Int(10), X())
result = expression.evaluate(3)
print("Evaluate Test 4 Result:", result)

expression = Mul(Add(X(), Int(2)), Sub(X(), Int(1)))
result = expression.evaluate(4)
print("Evaluate Test 5 Result:", result)

expression = Div(Mul(X(), Int(5)), Int(2))
result = expression.evaluate(3)
print("Evaluate Test 6 Result:", result)

expression = Add(Mul(X(), Sub(X(), Int(2))), Div(Add(Int(3), X()), X()))
result = expression.evaluate(5)
print("Evaluate Test 7 Result:", result)



#print("Test 1:", Add(Int(3), Int(4)))
#rint("Test 2:", Sub(Int(5), Int(2)))
#print("Test 3:", Add(Sub(Int(4), Int(3)), Int(2)))
#print("Test 4:", Mul(Add(Int(2), X()), Int(3)))
#print("Test 5:", Add(Mul(X(), Sub(Int(5), X())), Div(Add(X(), Int(4)), X())))
#print("Test 6:", Sub(Add(Int(1), Mul(X(), Int(2))), Div(X(), Add(Int(3), X()))))
