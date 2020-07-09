def is_digit(values = []):
	if (type(values) is list):
		for i in values:
			try:
				float(i)
			except ValueError:
				print("Bad list element type")
				exit()
	elif (type(values) is int):
		pass
	elif (type(values) is tuple):
		if len(values) != 2:
			print("Tuple needs to have 2 elements")
			exit()
		for i in values:
			try:
				float(i)
			except ValueError:
				print("Bad tuple element type")
				exit()
			else:
				if (type(float(i)) != type(0.0)):
					print("Bad tuple element type")
					exit()
	elif (type(values) is Vector):
		pass
	else:
		print("Bad vector type")
		exit()

class Vector:
	def __init__(self, values = []):
		is_digit(values)
		self.values = []
		if (type(values) is list):
			for i in values:
				self.values.append(float(i))
		elif (type(values) is int):
			self.values = []
			for i in range(0, values):
				self.values.append(float(i))
		elif (type(values) is tuple):
			self.values = []
			for i in range(values[0], values[1]):
				self.values.append(float(i))
		elif (type(values) is Vector):
			self.values = values.values
			self.length = values.length
		else:
			print("Bad vector type")
			exit()
		self.length = len(self.values)


	def __add__(self, other):
		values = []
		if (type(other) == int or type(other) == float):
			for i in range(self.length):
				values.append(self.values[i] + other)
			return Vector(values)
		else:
			if (self.length == other.length):
				for i in range(self.length):
					a = self.values[i]
					b = other.values[i]
					values.append(a + b)
				return Vector(values)
			else:
				print("Element must have same size to be added")


	def __radd__(self, other):
		values = []
		if (type(other) == int or type(other) == float):
			for i in range(self.length):
				values.append(self.values[i] + other)
			return Vector(values)
		else:
			if (self.length == other.length):
				for i in range(self.length):
					a = self.values[i]
					b = other.values[i]
					values.append(a + b)
				return Vector(values)
			else:
				print("Element must have same size to be radded")
	# add : scalars and vectors, can have errors with vectors.


	def __sub__(self, other):
		values = []
		if (type(other) == int or type(other) == float):
			for i in range(self.length):
				values.append(self.values[i] + other)
			return Vector(values)
		else:
			if (self.length == other.length):
				for i in range(self.length):
					a = self.values[i]
					b = other.values[i]
					values.append(a + b)
				return Vector(values)
			else:
				print("Element must have same size to be subbed")


	def __rsub__(self, other):
		values = []
		if (type(other) == int or type(other) == float):
			for i in range(self.length):
				values.append(self.values[i] + other)
			return Vector(values)
		else:
			if (self.length == other.length):
				for i in range(self.length):
					a = self.values[i]
					b = other.values[i]
					values.append(a + b)
				return Vector(values)
			else:
				print("Element must have same size to be rsubbed")
	# sub : scalars and vectors, can have errors with vectors.


	def __truediv__(self, other):
		values = []
		if (type(other) == int or type(other) == float):
			for i in range(self.length):
				if other == 0:
					print("Error: cant div by 0")
					return None
				else:
					values.append(self.values[i] / other)
			return Vector(values)
		else:
				print("rtruediv needs to have a scalar")


	def __rtruediv__(self, other):
		values = []
		if (type(other) == int or type(other) == float):
			for i in range(self.length):
				if self.values[i] == 0:
					print("Error: cant div by 0")
					return None
					# exit()
				else:
					values.append(other / self.values[i])
			return Vector(values)
		else:
				print("rtruediv needs to have a scalar")
	# div : only scalars.


	def __mul__(self, other):
		values = []
		if (type(other) == int or type(other) == float):
			for i in range(self.length):
				values.append(self.values[i] * other)
			return Vector(values)
		else:
			if (self.length == other.length):
				for i in range(self.length):
					a = self.values[i]
					b = other.values[i]
					values.append(a * b)
				return Vector(values)
			else:
				print("Element must have same size to be mul")


	def __rmul__(self, other):
		values = []
		if (type(other) == int or type(other) == float):
			for i in range(self.length):
				values.append(self.values[i] * other)
			return Vector(values)
		else:
			if (self.length == other.length):
				for i in range(self.length):
					values.append(self.values[i] * other.values[i])
				return Vector(values)
			else:
				print("Element must have same size to be mul")
	# mul : scalars and vectors, can have errors with vectors,
	# return a scalar is we perform Vector * Vector (dot product)


	def __str__(self):
		return str(self.values)


	def __repr__(self, other):
		pass
