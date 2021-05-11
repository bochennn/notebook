#!/usr/bin/env python3
from pathlib import Path as pth

homepath = pth().home()

def view_point_cloud(filepath):
  from lib.point_cloud import PointCloudViewer
  viewer = PointCloudViewer(filepath)
  viewer.show()

def save_point_cloud(filepath, savepath):
  from lib.point_cloud import PointCloudViewer
  viewer = PointCloudViewer(filepath)
  viewer.save(savepath, filetype='.bin')

def save_recursively():
  from lib.point_cloud import PointCloudViewer
  from lib.util import load_file
  files = load_file('training.txt')
  root_path = pth().home() / 'Data/Holomatic/data/seq2/compensated_ply'
  save_path = pth().home() / 'Lidar/OpenPCDet/data/holomatic/training/pc'
  for filename in files:
    read_filepath = root_path / ('%s.ply' % filename)
    save_point_cloud(read_filepath, save_path)

def generate_random_sample():
  import numpy as np
  from lib.file import load_file_as_array, save_array_as_f
  from lib.data import random_sample
  sample_list = load_file_as_array(
    '/home/ubuntu/Lidar/OpenPCDet/data/holomatic/ImageSets/sample_list.txt')
  sample_a, sample_b = random_sample(sample_list, 4800)

  save_array_as_f('train.txt', sample_a)
  save_array_as_f('test.txt', sample_a)
  #[ print(n) for n in sample_list[sample_idx] ]

def view_glog():
  from glog_viewer import GlogViewer
  viewer = GlogViewer()
  viewer.cat_lane_boundary()
  viewer.cat_trajectory()
  viewer.plot_lane()

#view_point_cloud('/home/ubuntu/Lidar/OpenPCDet/data/holomatic/gt_database/00002450_car_0.bin')
#view_point_cloud('/home/ubuntu/Lidar/OpenPCDet/data/holomatic/training/pc/00002450.bin')
#view_point_cloud('/home/ubuntu/Lidar/OpenPCDet/data/kitti/gt_database/000253_Car_0.bin')
#save_point_cloud(filepath, '/home/bochen')
#save_recursively()

generate_random_sample()

