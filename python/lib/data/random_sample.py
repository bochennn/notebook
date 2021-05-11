import random

def random_sample(data, n_sample):
  n_items = len(data)
  sample_indx = random.sample(range(n_items), n_sample)
  
  selected, remains = [], []
  for idx in range(n_items):
    selected.append(data[idx]) if idx in sample_indx else remains.append(data[idx])

  return selected, remains
