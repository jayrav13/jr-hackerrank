# n - number of items in the array
# m - array of numbers (-, + or 0)
n = int(raw_input())
m = [int(x) for x in raw_input().split(" ")]

solution = [0.0, 0.0, 0.0]

for value in range(0, n): 
        if m[value] < 0:
                solution[1] = solution[1] + 1 
        elif m[value] > 0:
                solution[0] = solution[0] + 1 
        else:
                solution[2] = solution[2] + 1 

solution = [x/n for x in solution]

for x in solution:
        print x
