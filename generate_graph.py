import random
def generate_graph(n,m):
  all_edges = []
  for i in range(n):
    for j in range(n):
      if i != j :
        all_edges.append((i,j))
  random.shuffle(all_edges)
  edges = all_edges[:m]
  f = open(f"graph{m}_{n}.txt", 'w')
  for i in edges:
      s = str(i) + '\n'
      f.write(s)
  f.close()
