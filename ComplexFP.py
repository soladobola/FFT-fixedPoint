
from FixedPoint import FXfamily, FXnum
from RoundingUtility import *
import numpy as np


class Complex:
    def __init__(self, r, i, fam):
        """ Initialize values """
        self.real = FXnum(r, fam)
        self.imag = FXnum(i, fam)
        self.fam = fam
    
    def __add__(self, other):
        r = self.real + other.real
        i = self.imag + other.imag
        return Complex(r, i, self.fam)
    
    def __sub__(self, other):
        r = self.real - other.real
        i = self.imag - other.imag
        return Complex(r, i, self.fam)
    
    def __mul__(self, other):
        """ Implicit rounding via FixedPoint libary. """
        r = self.real*other.real - self.imag*other.imag
        i = self.imag*other.real + self.real*other.imag
        return Complex(r, i, self.fam)
    
    def kpower(self, k):
        """ Calculate k-th power of complex number """
        realArg = self.real.acos()*k
        imagArg = self.imag.asin()*k
        r = realArg.cos()
        i = imagArg.sin()
        return Complex(r, i, self.fam)
    
    def print(self):
        imagSign = "+";
        if self.imag < 0:
          imagSign = "";
        print(str(self.real) + " " + imagSign + str(self.imag) + "j");
        
        # Needed for numpy array
    def toPythonComplex(self):
        return complex(self.real, self.imag)
        
        
# fft algoritham
# TODO: make another file for fft

def fft(x, fam):
    """ @param x: Array of complex points
        @param fam: family of fixed pont numbers
    """
    N = len(x)
    pi = fam.pi
    #base = exp(-2*pi*j/N)
    real = FXnum(-2*pi/N, fam).cos()
    imag = FXnum(-2*pi/N, fam).sin()
    base = Complex(real, imag, fam)
    
    if N > 1:
        x = fft(x[::2], fam) + fft(x[1::2], fam)
        for k in range((int)(N/2)):
            xk = x[k]
            x[k] = xk + base.kpower(k)*(x[(int)(k + N/2)])
            x[(int)(k+N/2)] = xk - base.kpower(k)*(x[(int)(k+N/2)])
    return x


def fixedfft(fraction_bits, int_bits, arr, round=None):
    fam = None
    if round is not None:
        rounding = Round.trimBinary(round)
        fam = FXfamily(fraction_bits, int_bits, rounding)
    else:
        fam = FXfamily(fraction_bits, int_bits)
    
    return toNumpyArray(fft(realInComplex(arr, fam), fam))
    

def toNumpyArray(x):
    res = []
    for i in x:
        res.append(i.toPythonComplex())
    return np.array(res)


        
def realInComplex(x, fam):
    """ Convert real signal in complex """
    y = []
    for t in x:
        y.append(Complex(t, 0, fam));
    return y

def magnitude(x):
    y = []
    for i in x:
        y.append((((float)(i.real)*(float)(i.real) + (float)(i.imag)*(float)(i.imag)))**0.5)
    return y
