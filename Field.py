# -*- coding: utf-8 -*-
"""
This class defines finite fields (Particularly Galois Fields (prime fields)).
Some operations may not be accurate if 'p' is not prime.
"""

class Field:
    #initializing finite field element
    def __init__(self : object, x : int, p : int):
        if x >= p:
            x %= p
        self.x = x
        self.p = p
        
    def __repr__(self : object) -> str:
        return "FieldElement_{}({})".format(self.p ,self.x)
    
    #overwriting "==" since objects are stored in seperate memory
    #    locations, regardless of values
    def __eq__(self : object, other : object) -> bool:
        if other is None:
            return False
        if (self.x == other.x) and (self.p == other.p):
            return True
        return False
    
    #inverse of "=="
    def __ne__(self : object, other : object) -> bool:
        return not (self == other)

    #addition on finite field elements
    def __add__(self : object, other : object) -> str:
        if self.p != other.p:
            raise ValueError("These elements belong to different fields")
        return self.__class__((self.x + other.x) % self.p, self.p)
    
    #subtraction on finite field elements
    def __sub__(self : object, other : object) -> str:
        if self.p != other.p:
            raise ValueError("These elements belong to different fields")
        return self.__class__((self.x - other.x) % self.p, self.p)
    
    #multiplication on finite field elements
    def __mul__(self : object, other : object) -> str:
        if self.p != other.p:
            raise ValueError("These elements belong to different fields")
        return self.__class__((self.x * other.x) % self.p, self.p)
    
    #powers of finite field elements
    def __pow__(self : object, exponent : int) -> str:
        n = exponent % (self.p - 1)
        x = pow(self.x, n, self.p)
        return self.__class__(x, self.p)
    
    
    #division on finite field elements
    #Fermats Little Theorem for other.x inverse(This is only reliable when p is prime)   
    def __truediv__(self : object, other : object) -> str:
        if self.p != other.p:
            raise ValueError("These elements belong to different fields")
        x = (self.x * pow(other.x, self.p - 2, self.p)) % self.p
        return self.__class__(x, self.p)
        
    #multiplication of integer and fields element  
    def __rmul__(self, coefficient):
        x = (self.x * coefficient) % self.p
        return self.__class__(x, self.p)

#a = Field(2,7)
#b = Field(3,7)
#print( a + b)

##################TESTING####################
def Testing():
    #TEST 1
    a1, b1, c1 = Field(2,7), Field(3,7), Field(5,7)
    #TEST 2
    a2, b2, c2 = Field(-2,7), Field(3,7), Field(1,7)
    #TEST 3
    a3, b3, c3 = Field(2,7), Field(-3,7), Field(6,7)
    #TESTc4
    a4, b4, c4 = Field(-2,7), Field(-3,7), Field(2,7)
    print("Testing addition.")
    print("\t{}:\n\t\t {} + {} \n\t\t\t\t== {}".format("Passed" if (a1 +b1 == c1) else "Failed", a1, b1, a1 + b1))        
    print("\t{}:\n\t\t {} + {} \n\t\t\t\t== {}".format("Passed" if (a2 +b2 == c2) else "Failed", a2, b2, a2 + b2))        
    print("\t{}:\n\t\t {} + {} \n\t\t\t\t== {}".format("Passed" if (a3 +b3 == c3) else "Failed", a3, b3, a3 + b3))        
    print("\t{}:\n\t\t {} + {} \n\t\t\t\t== {}".format("Passed" if (a4 +b4 == c4) else "Failed", a4, b4, a4 + b4))        
 
if __name__ == "__main__":
    
    Testing()
   