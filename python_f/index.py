# 1.  3 input daxil edin və daxil edilən ədələrin fərqini tapın
# 4.  inputdan 3 ədəd götürün və o ədələrin kvadratını bir listə əlavə edin
import math
a=float(input('num1: '))

b=float(input('num2: '))

ferq=a-b

print('ferq: ',(ferq))
pov_a=math.pow(a,2)
pov_b=math.pow(b,2)
pov_ferq=math.pow(ferq,2)

inlist=[pov_a,pov_b,pov_ferq]
print('cixilan,cixan,ferq kvadratlari; ',inlist)


# iki tapsirigi birlesdirdim

