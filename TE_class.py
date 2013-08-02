import numpy as np
from scipy.special import jn, jvp, jn_zeros
from scipy.integrate import quad
import matlibplot.pyplot as plt

class TE(object):
    def __init__(self,l,m,n,R,L):
        self.l = l
        self.m = m
        self.n = n
    
    k1 = jn_zeros(m,l)/R
    k3 = n*np.pi/L
    
    
    def E_r(self, r, theta, z):
        return -self.l * jn(l,k1*r)/(k1*r) * np.sin(self.l * theta) * np.sin( k3 * z)
        
    def E_theta(self, r, theta, z):
        return -(jvp(self.l,k1*r,1])/k1) * np.cos(self.l* theta)*np.sin(k3*z)
    
    def E_z(self):
        return 0
        
    def H_r(self, r, theta, z):
        return k3
        
    def H_th(self):
        return asdf
        
    def H_z(self):
        return asdf
        
    def Norm(self, V):
        from scipy.integrate import quad
        func = something
        return quad(func,0,V)
    
class TE_Geometry_Factor(TE):
    def __init__(self, radialoffset, lengthoffset):
        self.r_off = radialoffset
        self.z_off = lengthoffset

    def Geom_Factor(self, k):
        from scipy.integrate import quad
        return quad(np.exp(I*x)/(np.abs(x-                y)*E_z(x)*E_z(y), 0, V)
        
    def Plot(self)
        
    
        