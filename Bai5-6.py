number_1 = int(input("Nhập vào số nguyên thứ nhất: "))
number_2 = int(input("Nhập vào số nguyên thứ hai: "))

ucln = 1
bcnn = 1

for i in range(1, max(number_1, number_2) + 1): #max để chọn range đến số lớn hơn
    if number_1 % i == 0 and number_2 % i == 0:
        ucln = i

bcnn = number_1 * number_2 // ucln

print(f"UCLN của {number_1} và {number_2} là:", ucln)
print(f"BCNN của {number_1} và {number_2} là:", bcnn)