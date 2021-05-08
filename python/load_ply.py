#!/usr/bin/env python3
import numpy as np
import pandas as pd
from plyfile import PlyData


def load_ply(filepath):
  data_ply = PlyData.read(filepath)
  data_pd = pd.DataFrame(data_ply.elements[0].data)
  data_np = np.zeros((data_pd.shape[0], 4), dtype=np.float32)
  for i, name in enumerate(data_ply.elements[0].data[0].dtype.names):
    if name is 'x': data_np[:, 0] = data_pd[name]
    if name is 'y': data_np[:, 1] = data_pd[name]
    if name is 'z': data_np[:, 2] = data_pd[name]
    if name is 'intensity': data_np[:, 3] = data_pd[name]
  return data_np

