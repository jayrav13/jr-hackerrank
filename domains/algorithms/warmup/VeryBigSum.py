# Enter your code here. Read input from STDIN. Print output to STDOUT

def sum(arr):
    sum = 0
    for elem in arr:
        sum = sum + int(elem)
    
    return sum
        
n = int(raw_input())
for elem in range(0, n):
    arr = raw_input().split(" ")
    print sum(arr)
