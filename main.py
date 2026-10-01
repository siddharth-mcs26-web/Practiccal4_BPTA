import time
import pandas as pd
from generate_graph import generate_graph
from LP_optimal import LP_optimal
from LP_rouding import LP_rounding
from read_file import read_file
from draw_graph import draw_graph
n = 20
data_greedy_vc = []
data_LP_rounding = []
for m in range(20, 191, 20):
  edges = read_file(f"graph{m}_{n}.txt")
  start_time = time.perf_counter()
  cover_optimal = LP_optimal(edges, n)
  end_time = time.perf_counter()
  data_greedy_vc.append({
        "n" : n,
        "m" : m,
        "size_of_vc_optimal" : len(cover_optimal),
        "running_LP_optimal" : round(end_time - start_time, 10)
    })
  start_time = time.perf_counter()
  cover_LP_rounding = LP_rounding(edges, n)
  end_time = time.perf_counter()

  data_LP_rounding.append({
        "size_of_vc_LP_rouding" : len(cover_LP_rounding),
        "running_time_LP_rouding" : round(end_time - start_time, 10),
        "approximation_factor" : 2
    })
  draw_graph(edges, cover_LP_rounding, cover_optimal, n )
n = 10
for m in range(10, 46, 5):
  edges = read_file(f"graph{m}.txt")
  start_time = time.perf_counter()
  cover = LP_optimal(edges, n)
  end_time = time.perf_counter()
  data_greedy_vc.append({
        "n" : n,
        "m" : m,
        "size_of_vc_optimal" : len(cover),
        "running_LP_optimal" : round(end_time - start_time, 10)
    })
  #draw_matching(edges, matching, cover)
  start_time = time.perf_counter()
  cover_LP_rounding = LP_rounding(edges, n)
  end_time = time.perf_counter()

  data_LP_rounding.append({
        "size_of_vc_LP_rouding" : len(cover_LP_rounding),
        "running_time_LP_rouding" : round(end_time - start_time, 10),
        "approximation_factor" : 2
    })
  draw_graph(edges, cover_LP=cover_LP_rounding, cover_optimal=cover, n=n)



data = [{**d1, **d2} for d1, d2 in zip(data_greedy_vc, data_LP_rounding)]
for d in data:
    d["approximation_factor"] = round(d["size_of_vc_LP_rouding"] / d["size_of_vc_optimal"], 2)
df = pd.DataFrame(data)
csv_filename = "LP_rouding_approximation.csv"
df.to_csv(csv_filename, index=False)