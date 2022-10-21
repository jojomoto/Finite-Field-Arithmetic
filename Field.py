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
    def __rmul__(self : object, coefficient : int) -> str:
        x = (self.x * coefficient) % self.p
        return self.__class__(x, self.p)
