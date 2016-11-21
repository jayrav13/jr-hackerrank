n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))

total = 0

for i in range(0, n):
    swaps = 0
    
    for j in range(0, n - 1):
        if a[j] > a[j + 1]:
            temp = a[j]
            a[j] = a[j + 1]
            a[j + 1] = temp
            swaps += 1
            total += 1
        
    if swaps == 0:
        break

print "Array is sorted in %d swaps." % total
print "First Element: %d" % a[0]
print "Last Element: %d" % a[-1]
