# 输出100次5
time = 0
while time < 100:
    print("5")
    time += 1
# 1加到100的和
num = 0
last_num = 0
while num < 100:  # num从0到99循环了100次，
    num += 1
    last_num += num
print(last_num)

num = 1
last_num = 0
while num <= 100:  # num从1到100循环了100次，这个好一点，第一次+1第一百次+100
    last_num += num
    num += 1
print(last_num)
