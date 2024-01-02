M = {1,3,5,7}
k = 8

RESULTS = set[frozenset]

def subset_sum_aux(M: set, k: int, s: set, results: RESULTS):
        if k == 0:
              results.add(frozenset(s))
        elif k < 0 or len(M) == 0:
              return None
        for num in M:
            result = subset_sum_aux(M - {num}, k - num, s | {num}, results)
            if result is not None:
                  return result
        return None


def subset_sum(M: set, k: int):
      res: RESULTS = set()
      subset_sum_aux(M, k, set(), res)
      return res
            
print(subset_sum(M, k))