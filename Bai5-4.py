n = int(input("Nhập vào số nguyên: "))

#tính tổng nghich đảo của N số nguyên đầu tiên
sum = 0

for i in range(1, n+1):
    sum += 1/i

print(f"Tổng nghịch đảo của {n} số đầu tiên là: {round(sum,3)}")