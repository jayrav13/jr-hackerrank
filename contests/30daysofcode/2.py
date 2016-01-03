arr = []

arr.append(float(raw_input().strip()))
arr.append(int(raw_input().strip()))
arr.append(int(raw_input().strip()))

print "The final price of the meal is $" + str(int(round(arr[0] + arr[0]*(float(arr[1])/100) + arr[0]*(float(arr[2])/100), 0))) + "."
