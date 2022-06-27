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