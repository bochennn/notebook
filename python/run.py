#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#rootpath = '/home/bochen'
filepath = '/home/bochen/data/Holomatic/seq4/compensated_ply/00007641.ply'

def view_point_cloud(filepath):
  from pointcloud_viewer import PointCloudViewer
  viewer = PointCloudViewer(filepath)
  viewer.show()

def save_point_cloud(filepath, savepath):
  from pointcloud_viewer import PointCloudViewer
  viewer = PointCloudViewer(filepath)
  viewer.save(savepath, '.bin')

def view_glog():
  from glog_viewer import GlogViewer
  viewer = GlogViewer()
  viewer.cat_lane_boundary()
  viewer.cat_trajectory()
  viewer.plot_lane()

#view_point_cloud('/home/bochen/00007641.bin')
#save_point_cloud(filepath, '/home/bochen')


