class Number:
	def __init__(self, value):
		self.value = value
	def __iadd__(self, increment):
		return Number(self.value + increment)
n = Number(5)
n += 3
print n.value
