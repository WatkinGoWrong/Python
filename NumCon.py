#!/user/bin/python
import math

x = 10
y = 25
z = 100
f = 12.453456432
def cmp(a ,b):
	return (a>b)-(a<b)

print("Absolute of x :",abs(x))
print("Ceiling of x :",math.ceil(x))
print("Comparing of x & y :",cmp(x, y))
print("Exponential of x :",math.exp(x))
print("Absolute of x :",math.fabs(x))
print("Floor of x :",math.floor(x))
print("Natural logarithm of x :",math.log(x))
print("Base-10 logarithm of x :",math.log10(x))
print("Max of x,y,z :",max(x,y,z))
print("Min of x,y,z :",min(x,y,z))
print("The fractional and integer parts of x in a two-item tuple :",math.modf(x))
print("The value of x**y :",math.pow(f,y))
print("x rounded to n digits from the decimal point :",round(f, 2))
print("The square root of x for x > 0 :",math.sqrt(x))