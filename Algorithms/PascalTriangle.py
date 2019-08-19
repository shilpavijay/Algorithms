def PascalTriangle(n):
	for line in range(1,n+1):
		C = 1
		for each in range(1,line+1):
			print(C,end="")
			C = int(C * (line-each)/each)
		print("")

PascalTriangle(10)