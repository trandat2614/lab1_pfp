#viet chuogn trinh tinh tong bac 3 cua N so nguyen dau tien
N = int(input("Nhập vào số N: "))

sum = 0
for i in range(1, N + 1):
    sum += i**3

print(f"Tổng bậc 3 của {N} số đầu tiên là: {sum}")
