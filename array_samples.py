

# check for given sum in array
def printPairs(a, sum):
    s = set(a)

    print("Printing pairs of given sum if exists ")
    for i in range(0, len(a)):
        temp = sum - a[i]
        if temp in s:
            print('Pair with given sum ' + str(sum) + ' is (' + str(a[i]) + ' , ' + str(temp) + ' )')
            s.add(a[i])


def printMissingElement(arr, low, high):
    print("Missing Element: ")
    s = set(arr)
    for x in range(low, high+1):
        if x not in s:
            print(x, end=' ')


def printMissingElementBySorting(arr, low, high):
    print("\n Missing Element: ")
    from bisect import bisect_left
    arr_size = len(arr)
    arr.sort()
    ptr = bisect_left(arr,low)
    i = ptr
    x = low
    while i < arr_size and x <= high:
        if arr[i] != x :
            print(arr[i], end= ' ')
        else:
            i = i +1
        x = x+1

    while x <= high:
        print(x, end = ' ')
        x = x + 1


a = [10, 20, 30, 1, 6, 0, 16]
n = 16
printPairs(a, n)
arr = [1, 3, 5, 4]
low, high = 1,10
printMissingElement(arr, low, high)
printMissingElementBySorting(arr,low,high)
