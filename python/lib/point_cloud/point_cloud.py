#!/usr/bin/env python3
from pathlib import Path as pth

from .viewer import *
from ..util import load_ply


class PointCloud():
  def __init__(self, filename):
    self.filepath_ = pth(filename)
    self.read_pts_ = False
    self.get_lidar_from_file()
    gt_boxes = np.array()

  def get_lidar_from_file(self):
    if not self.filepath_.is_file():
      print('not a file')
      return False
    
    #self.basename_ = self.filepath_.stem
    file_type = self.filepath_.name.split('.')[-1]

    if file_type == 'ply':
      self.data_np_ = load_ply(self.filepath_)
    elif file_type == 'npy':
      self.data_np_ = np.load(self.filepath_)
    elif file_type == 'bin':
      self.data_np_ = np.fromfile(self.filepath_, dtype=np.float32).reshape((-1,4))
    else:
      print('not a readable file')
      return False
      
    self.read_pts_ = True
    print('load points:', self.data_np_)
    print('shape:', self.data_np_.shape)
    return True

  def get_boxes_from_file(self, filename):
    # (N, 7) [[cx, cy, cz, dx, dy, dz, heading], ...]
    self.gt_boxes = 
      np.array([[-10.323968207955874, -3.2961178526047914, -1.211074799881243, 
                 4.6, 1.5775530936759088, 1.986088468320048, 0.022485378351759122],
                [-28.339757492665015, -2.857812812511744, -1.3066531733140345, 
                 4.6, 1.455773544797935, 1.7, 0.008343393996970372]])
  
  def save(self, filepath, basename=None, filetype='.bin'):
    if not self.read_pts_ or not pth(filepath).is_dir():
      return False
    
    basename = self.filepath_.stem if basename is None else basename
    save_path = pth(filepath) / (basename + filetype)

    if filetype == '.bin':
      with open(save_path, 'w') as f:
        self.data_np_.tofile(f)
    elif filetype == '.npy':
      np.save(save_path, self.data_np_)
    else:
      print('not support filetype')
      return False
    print('save to file:', save_path)
    return True
  
  def show(self):
    if not self.read_pts_:
      return False
    
    fig = mlab.figure(bgcolor=(0, 0, 0), size=(800, 600))
    mlab.points3d(self.data_np_[:, 0], self.data_np_[:, 1], 
                  self.data_np_[:, 2], self.data_np_[:, 2], 
                  mode="point", colormap='gnuplot', figure=fig)

    if self.gt_boxes.shape[0] > 0:
      corners3d = boxes_to_corners_3d(self.gt_boxes)
      fig = draw_corners3d(corners3d, fig=fig, color=(0, 0, 1), max_num=100)

    mlab.points3d(0, 0, 0, color=(1, 1, 1), mode="sphere", scale_factor=0.2)
    axes = np.array([[5, 0, 0, 0], [0, 5, 0, 0], [0, 0, 5, 0]], dtype=np.float64)
    mlab.plot3d([0, axes[0, 0]], [0, axes[0, 1]], [0, axes[0, 2]],
                color=(1, 0, 0), tube_radius=None, figure=fig)
    mlab.plot3d([0, axes[1, 0]], [0, axes[1, 1]], [0, axes[1, 2]],
                color=(0, 1, 0), tube_radius=None, figure=fig)
    mlab.plot3d([0, axes[2, 0]], [0, axes[2, 1]], [0, axes[2, 2]],
                color=(0, 0, 1), tube_radius=None, figure=fig)
    mlab.show()


