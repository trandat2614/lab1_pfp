n = int(input("Nhập vào số nguyên: "))

#kiem tra tat ca cac uoc
uoc = []

for i in range(1, n + 1):
    if n % i == 0:
        uoc.append(i)

print(f"Tất cả các ước của {n} là: {uoc}")