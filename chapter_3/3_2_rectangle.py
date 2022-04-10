rect1_a = int(input("first rectangle side a: "))
rect1_b = int(input("first rectangle side b: "))
rect2_a = int(input("second rectangle side a: "))
rect2_b = int(input("second rectangle side b: "))

rect1 = rect1_a * rect1_b
rect2 = rect2_a * rect2_b

if rect1 > rect2:
    print ('rectangle 1 > than rectangle 2') 
else: 
    print ('rectangle 1 < than rectangle 2')
    