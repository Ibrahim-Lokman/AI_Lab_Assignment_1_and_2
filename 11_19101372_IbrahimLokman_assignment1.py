"""


TASK 01


"""
print("TASK 01 Output:")
inputfile = open("assignment1input1.txt", "r")

class Assignment1Task1:
	def __init__(self, row, col, list_2D):
		self.R = row
		self.C = col
		self.list_2D = list_2D
	def DFSB(self, a, b, value):
		if a < 0 or a >= len(self.list_2D) or \
				b < 0 or b >= len(self.list_2D[0]) or \
				self.list_2D[a][b] != 'Y':
			return
		strvalue = str(value)
		self.list_2D[a][b] = strvalue
		self.DFSB(a,b-1, value); self.DFSB(a,b+1,value);
		self.DFSB(a+1,b-1,value); self.DFSB(a+1,b,value); self.DFSB(a+1,b+1,value);
		self.DFSB(a-1,b-1,value); self.DFSB(a-1,b,value); self.DFSB(a-1,b+1,value);
	def findConnection(self):
		value = 0
		for i in range(self.R):
			for j in range(self.C):
				if self.list_2D[i][j] == 'Y':
					value = value - 1
					self.DFSB(i, j, value)
graph = []
for l in inputfile:
  st=l.strip()
  list=st.split()
  graph.append(list)
inputfile.close()

row2 = len(graph)
col2 = len(graph)
g2 = Assignment1Task1(row2, col2, graph)
g2.findConnection()


oneDlist= [item for sub in graph for item in sub]
Y = [value_saved for value_saved in oneDlist if value_saved != 'N']
frequentValues = max(Y, key=Y.count)

maxcount = 0;
for a in Y:
	if a == frequentValues:
		maxcount = maxcount+1
print(maxcount)

"""


TASK 02


"""

print()
print()
print("TASK 02 Output: ")

inputfile = open("assignment1input2.txt", "r")

graph = []
count = 0
for l in inputfile:
  strip=l.strip()
  list=strip.split()
  if count == 0:
      row = int(list[0])
      count = count + 1
  elif count == 1:
      col = int(list[0])
      count = count + 1
  else:
    graph.append(list)
inputfile.close()

queue = []
for i in range(row):
			for j in range(col):
				if graph[i][j] == 'A':
					queue.append([i,j,0])

def isValid(r,c):
    if (r < 0 or c < 0 or r >= row or c >= col or graph[r][c] == "A" or graph[r][c] == "T"):
        return False
    return True

def BFS(a, b, list,t):
    if (isValid(a,b+1)):
        list[a][b+1] = "A"
        queue.append([a,b+1,t+1])
    if (isValid(a+1,b)):
        list[a+1][b] = "A"
        queue.append([a + 1, b,t+1])
    if (isValid(a-1 , b)):
        print(True,a-1,b,t+1)
        queue.append([a - 1, b, t+1])
    if (isValid(a , b-1)):
        list[a][b -1] = "A"
        queue.append([a, b-1,t+1])
time = 0
while len(queue) != 0:
    list = queue.pop(0)
    i = list[0]
    j = list[1]
    time = list[2]
    BFS(i,j,graph,time)
print("Time:", time,"minutes")

count = 0
for i in range(row):
			for j in range(col):
				if graph[i][j] == 'H':
					count = count+1

if count == 0:
    print("No One Survived")
else:
    print(count, "Survived")