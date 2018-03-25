import random
random.seed()

class family():
	boys = 0
	girls = 0

	def haveChildren(self):
		while not self.boys:
			if random.randint(0, 1):
				self.boys += 1
			else:
				self.girls += 1

country = [family() for fam in range(1000000)]

boyCnt = 0
girlCnt = 0
for family in country:
	family.haveChildren()
	boyCnt += family.boys
	girlCnt += family.girls

print("Number of boys: " + str(boyCnt))
print("Number of girls: " + str(girlCnt))
print("Ratio of boys to girls: " + str( boyCnt/girlCnt ))