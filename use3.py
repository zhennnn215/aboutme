from mis import mis2a,mis2b

from mis import sum_to_n

x = int(input("請輸入一個整數:"))

if x <= 0:
    print(f"您輸入的值是{x},小於等於0")
else:
    s = sum_to_n(x)
    print(f"1+2+3+...+{x}的總和是{s}")


mis2a()
mis2b()
