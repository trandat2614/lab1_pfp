#Trăm trâu, trăm cỏ
#Trâu đứng ăn năm
#Trâu nằm ăn ba
#Ba trâu già ăn một
#hỏi mỗi loại trâu có mấy con

#goi so trau đứng, nằm, già lần lượt là x,y,z
#ta có hệ phương trình:
# x + y + z = 100
# 5x + 3y + 1/3z = 100

# Giới hạn để tìm nghiệm nguyên dương
for x in range(21):
    for y in range(33):
        z = 100 - x - y
        if z >= 0 and 5*x + 3*y + z/3 == 100:
            print(f"Số trâu đứng: {x}, Số trâu nằm: {y}, Số trâu già: {z}")
