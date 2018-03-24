import sys, random, copy
def div(num, den):
    try:
        return float(num/den)
    except ZeroDivisionError:
        print('Invalid argument boi.')


array = ['elephant', 'crow', 'rhino']


def ReverseArray(arr):
    i = 0
    temparr = []
    for i in range(0, len(arr)):
        temparr.insert(0, arr[i])
    return temparr


print('Original: ' + str(array))
print('Reversed: ' + str(ReverseArray(array)))
newArray = copy.copy(array)
newArray[0] = 'new'
print('New array is: ' + str(newArray))



