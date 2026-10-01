from scipy.optimize import milp
from scipy.optimize import LinearConstraint, Bounds

def LP_optimal(edges, n):

  c = [1 for i in range(n)]
  # 1 <= Ax <= 2
  A = []
  for edge in edges:
    arr = [0 for i in range(n)]
    arr[edge[0]] = 1
    arr[edge[1]] = 1
    A.append(arr)

  bounds = Bounds(0,1)
  const = LinearConstraint(A, lb=[1]*len(A), ub=[2]*len(A))
  res = milp(c=c, integrality=1,bounds=bounds,constraints=const)

  result = res.x
  cover = []
  for i in range(len(result)):
      if result[i] != 0:
        cover.append(i)

  return cover