inputfile = open("assignment1input1.txt", "r")

class Assignment1Task1:
	def __init__(self, row, col, list_of_lists):
		self.R = row
		self.C = col
		self.list_of_lists = list_of_lists

	def DFSB(self, a, b, value):
		if a < 0 or a >= len(self.list_of_lists) or \
				b < 0 or b >= len(self.list_of_lists[0]) or \
				self.list_of_lists[a][b] != 'Y':
			return
		strvalue = str(value)
		self.list_of_lists[a][b] = strvalue
		self.DFSB(a,b-1, value)
		self.DFSB(a,b+1,value)
		self.DFSB(a+1,b-1,value)
		self.DFSB(a+1,b,value)
		self.DFSB(a+1,b+1,value)
		self.DFSB(a-1,b-1,value)
		self.DFSB(a-1,b,value)
		self.DFSB(a-1,b+1,value)
	def findConnection(self):
		value = 0
		for i in range(self.R):
			for j in range(self.C):
				if self.list_of_lists[i][j] == 'Y':
					value = value - 1
					self.DFSB(i, j, value)

#inputfile = open("assignment1input1.txt", "r")
graph = []
for l in inputfile:
  strip=l.strip()
  list=strip.split()
  graph.append(list)
inputfile.close()

row2 = len(graph)
col2 = len(graph)
g2 = Assignment1Task1(row2, col2, graph)
g2.findConnection()


oneDlist= [item for sub in graph for item in sub]
Y = [value_save for value_save in oneDlist if value_save != 'N']
frequentValues = max(Y, key = Y.count)

maxcount = 0;
for a in Y:
	if a == frequentValues:
		maxcount = maxcount+1
print(maxcount)
