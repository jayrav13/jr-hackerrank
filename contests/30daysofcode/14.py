# Add your code here
def __init__(self, a):
	self.a = a
	self.maximumDifference = -1

def computeDifference(self):
	for i in range(0, len(self.a)):
		for j in range(i, len(self.a)):
			if abs(self.a[i] - self.a[j]) > self.maximumDifference:
				self.maximumDifference = abs(self.a[i] - self.a[j])
