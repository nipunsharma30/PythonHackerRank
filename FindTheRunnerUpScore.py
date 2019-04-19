
def input_raw():
    n = int(input())
    arr = list(map(int, input().split()))
    if validation(n,arr) != True:
        #print('Values out of range')
        input_raw()
    else:
        return n, arr

def validation(n, arr):
    if (n >= 2) & (n <= 10):
        if (max(arr) <= 100) & (min(arr) >= -100):
            return True
        #else:
            #print('Values out of range')
    #else:
        #print('Values out of range')



if __name__ == '__main__':
    n, arr = input_raw()
    z = max(arr)
    while max(arr) == z:
        arr.remove(max(arr))
    print(max(arr))