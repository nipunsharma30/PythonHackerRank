if __name__ == '__main__':
    n = int(input())

a = []
for i in range(n):
    #print(i)
    a.append(i+1)
print(''.join(str(e) for e in a))
