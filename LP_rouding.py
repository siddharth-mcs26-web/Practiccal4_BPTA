from scipy.optimize import linprog
def LP_rounding(edges, n):

  vertex = [0 for i in range(n)]
  c = [1 for i in range(n)]
  A = []
  B = []
  for edge in edges:
    arr = [0 for i in range(n)]
    arr[edge[0]] = -1
    arr[edge[1]] = -1
    A.append(arr)
    B.append(-1)

  bounds = [(0,1) for i in range(n)]
  res = linprog(c, A_ub = A, b_ub = B, bounds = bounds)

  result = res.x
  cover = []
  for i in range(len(result)):
    if result[i] >= 0.5:
        cover.append(i)

  return cover