n= int(input("Nhập vào số nguyên: "))

sum = 0
for i in range(1,n+1):
    if i%2==1:
        sum += (i*i)

print(f"Tổng bình phương các số lẻ từ 1 đến {n} là: {sum}")