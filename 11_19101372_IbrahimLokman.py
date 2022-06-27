#Ibrahim_Lokman
#ID: 19101372
#SEC 11
import random
inputfileAssignment2 = open("assignment2input1.txt", "r")

graph = []
for l in inputfileAssignment2:
  st=l.strip()
  array_list=st.split()
  if(array_list[0] == 'l'):
    graph.append(-int(array_list[1]))
  elif (array_list[0] == 'd'):
    graph.append(int(array_list[1]))
  else:
    array_size = int(array_list[0])

p_S = len(graph)
itter_num = 1000

def fitenesstest(nG,graph):
  sum = 0
  for j in range(len(nG)):
    if (nG[j] == 1):
      sum = sum + graph[j]
  return sum

def bSort(array_list):
  s = True
  while s:
    s = False
    for i in range(len(array_list)-1):
      if abs(array_list[i])>abs(array_list[i+1]):
        array_list[i],array_list[i+1]=array_list[i+1],array_list[i]
        newGen[i], newGen[i+1] = newGen[i+1], newGen[i]
        s = True

def crossover(a, b):
    k = p_S-3
    for i in range(k, len(r)):
      a[i], b[i] = b[i], a[i]
    return a

def mutate(elem):
    a = random.randint(0, p_S-1)
    if elem[a] == 1:
      elem[a] = 0
    else:
      elem[a] = 1
    return elem


inputfileAssignment2.close()

bestCombo = []
bestfitenessScore = 9999
for _ in range(itter_num):
  print(_)
  newGen = []
  for _ in range(p_S):
    members = []
    for _ in range(len(graph)):
      members.append(random.choice([0,1]))
    newGen.append(members)

  fitness = []
  for i in range(p_S):
      fitnessMarks = fitenesstest(newGen[i],graph)
      fitness.append(fitnessMarks)
  bSort(fitness)


  r = newGen[0]
  s = newGen[1]

  newChild = crossover(r,s)
  mutatedChild = mutate(newChild)
  fitnessM = fitenesstest(mutatedChild,graph)

  sum_check = sum(mutatedChild)
  if fitnessM == 0 and sum_check !=0:
    bestfitenessScore = fitnessM
    bestCombo = mutatedChild
    break

if bestfitenessScore == 0:
  print(bestCombo)
else:
  print(-1)