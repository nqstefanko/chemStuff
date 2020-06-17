import periodictable as pt
import os
from decimal import Decimal

water = pt.H.mass * 2 + pt.O.mass
ammonia = pt.N.mass + (4 * pt.H.mass)
co2 = pt.C.mass + (2 * pt.O.mass)
hcl = pt.H.mass + pt.Cl.mass
nacl = pt.Na.mass + pt.Cl.mass
nitrate = pt.N.mass + 3 * pt.O.mass
sulfate = pt.S.mass + 3 * pt.O.mass

ava = 6.022e23
r = .0821 # ideal gas constant
c = 3e8 # m/s Speed of Light
h = 6.62607004e-34 #m2 kg / s planks constant

def sn(num):
	print(f"{Decimal(num):.5E}")

def K(c):
	return c + 273

def atm(t):
	return t / 760

def pvnrt(P, V, n, T):
	x = None
	if(P == None):
		x = (n * r * T) / V 
		print("PRESSURE: " , (n * r * T) / V , "atm")
	elif(V == None):
		x = (n * r * T) / P
		print("VOLUME:", (n * r * T) / P, "L")
	elif(n == None):
		x = (P * V)/(T * r)
		print("MOLES:", (P * V)/(T * r), "mols")
	elif(T == None):
		x = (P * V)/(n * r)
		print("TEMP:", (P * V)/(n * r), "K")
	else:
		print("R (ideal constant):", (P * V)/(n * T))
		x = (P * V)/(n * T)
	return x


def pe(r, t):
	return abs((r-t)/t * 100)

