

# check for given sum in array
def printPairs(a, a_size, n):
    s = set()
    print('I am 1')
    temp, sum = 0, 0
    for i in range(0, a_size):
        temp = sum - a[i]
        print('I am 2')
        if temp in s:
            print('Pair with given sum ' + str(sum) + ' is ' + str(a[i]) + ' , ' + str(temp))
            s.add(a[i])


a = [10, 20, 30, 1, 6]
n = 16
print('I am')
printPairs(a, len(a),  n)
