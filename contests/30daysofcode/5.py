# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(raw_input().strip())

arr = []

for i in range(0, n):
    arr.append(map(int, raw_input().strip().split(' ')))
    
def NthTerm(b, N):
    return sum([(2**x) * b for x in range(0, N)])

for elem in arr:
    for x in range(1, elem[2] + 1):
        print elem[0] + NthTerm(elem[1], x),
    print "\n",
