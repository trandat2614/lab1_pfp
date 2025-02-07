#Vừa gà vừa chó
#Bó lại cho tròn
#Ba mươi sau con
#100 chân chẵn
#Hỏi số gà và số chó

#goi so ga, cho lần lượt là x,y
#ta có hệ phương trình:
# x + y = 36
# 2x + 4y = 100

for x in range(37):
    y = 36 - x
    if 2*x + 4*y == 100:
        print(f"Số gà: {x}, Số chó: {y}")
