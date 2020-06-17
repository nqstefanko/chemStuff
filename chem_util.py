import periodictable as pt
import os

water = pt.H.mass * 2 + pt.O.mass
co2 = pt.C.mass + (2 * pt.O.mass)
hcl = pt.H.mass + pt.Cl.mass
nacl = pt.Na.mass + pt.Cl.mass
nitrate = pt.N.mass + 3 * pt.O.mass
sulfate = pt.S.mass + 3 * pt.O.mass

r = .08206

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