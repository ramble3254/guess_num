import random
r = random.randint(1,100)
count = 0
while True:
	count += 1 # count = count + 1 
	num = int(input('請猜數字: '))
	print('這是你猜的', count, '次')
	if num == r:
		print('恭喜!你猜對了')
		break
	elif num > r:
		print('你的數字比答案大')
	elif num < r:
		print('你的數字比答案小')