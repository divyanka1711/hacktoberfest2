def fibo(Number):
	if Number == 0:
		return 0
	elif Number == 1:
		return 1
	else:
		return fibo(Number - 1) + fibo(Number - 2)


n = int(input())
print("Fibonacci series:", end=' ')
for n in range(0, n):
	print(fibo(n), end=' ')
