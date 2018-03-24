def reverse(x):
    t = ""
    for i in range(len(x)-1, -1, -1):
        t = t + x[i]
    return t

def ispalindrome(x):
    t = reverse(x)
    if t == x:
        return True
    else:
        return False


print(ispalindrome(""))
