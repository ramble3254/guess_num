import random
r = random.randint(1,100)
while True:
	num = int(input('請猜數字: '))
	if num == r:
		print('恭喜!你猜對了')
		break
	elif num > r:
		print('你的數字比答案大')
	elif num < r:
		print('你的數字比答案小')