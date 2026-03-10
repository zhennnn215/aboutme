def square(y):
	print(f"{y}的平方是{y**2}")

def sum_to_n(n):
	total = 0
	for i in range(1, n+1):
		total += i
	return total


x = int(input("請輸入一個整數:"))
#x += 10

if (x<=0):
	print(f"您輸入的值是{x},小於等於0")
else:
	print(f"您輸入的值是{x},大於0")
	for i in range(1,x+1):
		#print(i, end=";")
		square(i)

	s = sum_to_n(x)
	print("1+2+3+...+{}的總和是{}".format(x, s))