'''---本程序花了四个小时---
---第一次独立的完成一个程序---'''

print('Welcom to 小猿圈 lottery station')

red_balls = []
blue_balls = []

i = 1
while i < 7:
    print('[',i,']',end = '')
    red_ball = int(input('select red ball:'))

    if red_ball not in range(1,33):
        print('only can select in between 1-32')
        i = i
    else:
        if red_ball in red_balls:
            print('number',red_ball,'is already exist in red ball list')
            i = i
        else:
            red_balls.append(red_ball)
            i += 1
j = 1
while j < 3:
    print('[',j,']',end = '')
    blue_ball = int(input('select blue ball:'))

    if blue_ball not in range(1,17):
        print('only can select in between 1-16')
        j = j
    else:
        if blue_ball in blue_balls:
            print('number',blue_ball,'is already exist in red ball list')
            j = j
        else:
            blue_balls.append(blue_ball)
            j += 1

print('red ball:',red_balls,'\nblue ball:',blue_balls,'\nGood Luck')



