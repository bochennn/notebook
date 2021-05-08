#!/usr/bin/env python3
import numpy as np
from pathlib import Path


class PointCloudViewer():
  def __init__(self, filename):
    self.filepath_ = Path(filename)
    self.read_pts_ = False
    self.get_data_from_path()

  def get_data_from_path(self):
    if not self.filepath_.is_file():
      print('not a file')
      return False
    
    self.basename_ = self.filepath_.name.split('.')[0]
    file_type = self.filepath_.name.split('.')[-1]

    if file_type == 'ply':
      from load_ply import load_ply
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
  
  def save(self, filepath, filetype='.bin'):
    if not self.read_pts_ or not Path(filepath).is_dir():
      return False
    
    save_path = Path(filepath) / (self.basename_ + filetype)
    if filetype == '.bin':
      with open(save_path, 'w') as f:
        self.data_np_.tofile(f)
    elif filetype == '.npy':
      np.save(save_path, self.data_np_)
    else:
      print('not support filetype')
      return False
    print('saved')
    return True
  
  def show(self):
    if not self.read_pts_:
      return False
    
    from mayavi import mlab
    fig = mlab.figure(bgcolor=(0, 0, 0), size=(640, 500))
    mlab.points3d(self.data_np_[:, 0], self.data_np_[:, 1], 
                  self.data_np_[:, 2], self.data_np_[:, 2], 
                  mode="point", colormap='gnuplot', figure=fig, )

    mlab.points3d(0, 0, 0, color=(1, 1, 1), mode="sphere", scale_factor=0.2)
    axes = np.array(
        [[20.0, 0.0, 0.0, 0.0], [0.0, 20.0, 0.0, 0.0], [0.0, 0.0, 20.0, 0.0]],
        dtype=np.float64,
    )
    mlab.plot3d([0, axes[0, 0]], [0, axes[0, 1]], [0, axes[0, 2]],
                color=(1, 0, 0), tube_radius=None, figure=fig, )
    mlab.plot3d([0, axes[1, 0]], [0, axes[1, 1]], [0, axes[1, 2]],
                color=(0, 1, 0), tube_radius=None, figure=fig, )
    mlab.plot3d([0, axes[2, 0]], [0, axes[2, 1]], [0, axes[2, 2]],
                color=(0, 0, 1), tube_radius=None, figure=fig, )
    mlab.show()




