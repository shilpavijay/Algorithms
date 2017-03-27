#Problem Description:
#The real and the decimal part of a set of numbers is given in two different arrays as shown in the example below:
# A=[0, 1, 2, 2, 3, 5]
# B=[500000, 500000, 0, 0, 0, 20000]
# The first number can be recovered by:C[0] A[0] + B[0] / 1000000
# Find the number of Multiplicatives in the Array.
# Multiplicative (p,q) is given by: 0<p<q<N; C[p]*C[q] >= C[p] + C[q]

def solution(A, B):
	#compute C:
	C=[]
	for i in range(0,len(A)):
		C.append(A[i] + (B[i] / 1000000))
	print (C)
	count = 0
	for i in range(0,len(C)):
		for j in range(i+1,len(C)):
			mult = C[i]*C[j]
			addn = C[i]+C[j]
			if mult >= addn:
				print(str(i) + "," +str(j))
				count += 1  
	return (count)


A=[0, 1, 2, 2, 3, 5]
B=[500000, 500000, 0, 0, 0, 20000]

print(solution(A,B))