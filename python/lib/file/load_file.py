#!/usr/bin/env python3

def load_pkl(filename):
  import pickle
  with open(filename, 'rb') as f:
    return pickle.load(f)

def load_json(filename):
  import json
  with open(filename, 'r', encoding='utf-8') as f:
    return json.load(f)

def load_file(filename):
  with open(filename, 'r', encoding='utf-8') as f:
    content = []
    try:
      for line in f:
        content.append(line.strip())
    finally:
      f.close()
    return content

def load_file_as_array(filename):
  import numpy as np
  return np.array(load_file(filename))

