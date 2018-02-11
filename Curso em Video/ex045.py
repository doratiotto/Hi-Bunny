# for c in range(n0, n1, d):
# Contar c para [n0,n1) com acréscimos de d
# s = s + n; ou; s += n



n0 = int(input('n0 = '))
n1 = int(input('n1 = '))
a  = int(input('Acréscimo = '))
s = 0

for i in range(n0, n1, a):
	n = int(input("número {} = " .format(i+1)))
	s += n

print (s)