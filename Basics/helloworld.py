import random, sys
print('Enter a value less than 50 and positive')
x = int(input())
if x <= 50 and x > 0:
    print('Winner')
else:
    print('loser.')
t = 'Tony'
i = 0
while i < len(t):
    if len(t) < 1:
        break
    print(t[i])
    i = i + 1
for i in range(2,len(t)):
    print(t[i])
for i in range(5):
    print(random.randint(1, 6))
sys.exit()
