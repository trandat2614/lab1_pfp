
# Viet chuong trinh xac dinh xem to giay có độ dày 0.1mm. Phải gấp đôi bn lần để có độ dày >=1m 
#1m = 1000mm
# Kiem tra do day to giay
dem = 0
do_day = 0.1
while do_day < 1000:
    do_day *= 2
    dem += 1

print(f"Phai gap {dem} lan de co do day >= 1m")