n = int(raw_input().strip())

st = []
arr = []

for i in range(0, n):
	st.append(raw_input().strip().split(' '))
	arr.append(raw_input().strip().split(' '))

	filt = [x for x in arr[i] if int(x) <= 0]

	if len(filt) >= int(st[i][1]):
		print "NO"
	else:
		print "YES"

