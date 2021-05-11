import numpy as np
import mayavi.mlab as mlab

def check_numpy_to_torch(x):
  import torch
  if isinstance(x, np.ndarray):
    return torch.from_numpy(x).float(), True
  return x, False

def rotate_points_along_z(points, angle):
  """
  Args:
    points: (B, N, 3 + C)
    angle: (B), angle along z-axis, angle increases x ==> y
  Returns:

  """
  import torch
  points, is_numpy = check_numpy_to_torch(points)
  angle, _ = check_numpy_to_torch(angle)

  cosa = torch.cos(angle)
  sina = torch.sin(angle)
  zeros = angle.new_zeros(points.shape[0])
  ones = angle.new_ones(points.shape[0])
  rot_matrix = torch.stack((
    cosa,  sina, zeros,
    -sina, cosa, zeros,
    zeros, zeros, ones
  ), dim=1).view(-1, 3, 3).float()
  points_rot = torch.matmul(points[:, :, 0:3], rot_matrix)
  points_rot = torch.cat((points_rot, points[:, :, 3:]), dim=-1)
  return points_rot.numpy() if is_numpy else points_rot

def boxes_to_corners_3d(boxes3d):
  """
      7 -------- 4
     /|         /|
    6 -------- 5 .
    | |        | |
    . 3 -------- 0
    |/         |/
    2 -------- 1
  Args:
    boxes3d:  (N, 7) [x, y, z, dx, dy, dz, heading], (x, y, z) is the box center

  Returns:
  """
  boxes3d, is_numpy = check_numpy_to_torch(boxes3d)

  template = boxes3d.new_tensor((
    [1, 1, -1], [1, -1, -1], [-1, -1, -1], [-1, 1, -1],
    [1, 1, 1], [1, -1, 1], [-1, -1, 1], [-1, 1, 1],
  )) / 2

  corners3d = boxes3d[:, None, 3:6].repeat(1, 8, 1) * template[None, :, :]
  corners3d = rotate_points_along_z(corners3d.view(-1, 8, 3), boxes3d[:, 6]).view(-1, 8, 3)
  corners3d += boxes3d[:, None, 0:3]

  return corners3d.numpy() if is_numpy else corners3d

def draw_multi_grid_range(fig, grid_size=10, bv_range=(-60, -60, 60, 60)):
  for x in range(bv_range[0], bv_range[2], grid_size):
    for y in range(bv_range[1], bv_range[3], grid_size):
      fig = draw_grid(x, y, x + grid_size, y + grid_size, fig)
  return fig


def draw_corners3d(corners3d, fig, color=(1, 1, 1), line_width=2, cls=None, tag='', max_num=500, tube_radius=None):
  num = min(max_num, len(corners3d))
  for n in range(num):
    b = corners3d[n]  # (8, 3)

    if cls is not None:
      if isinstance(cls, np.ndarray):
        mlab.text3d(b[6, 0], b[6, 1], b[6, 2], '%.2f' % cls[n], scale=(0.3, 0.3, 0.3), color=color, figure=fig)
      else:
        mlab.text3d(b[6, 0], b[6, 1], b[6, 2], '%s' % cls[n], scale=(0.3, 0.3, 0.3), color=color, figure=fig)

    for k in range(0, 4):
      i, j = k, (k + 1) % 4
      mlab.plot3d([b[i, 0], b[j, 0]], [b[i, 1], b[j, 1]], [b[i, 2], b[j, 2]], 
                  color=color, tube_radius=tube_radius,
                  line_width=line_width, figure=fig)
      i, j = k + 4, (k + 1) % 4 + 4
      mlab.plot3d([b[i, 0], b[j, 0]], [b[i, 1], b[j, 1]], [b[i, 2], b[j, 2]], 
                  color=color, tube_radius=tube_radius,
                  line_width=line_width, figure=fig)
      i, j = k, k + 4
      mlab.plot3d([b[i, 0], b[j, 0]], [b[i, 1], b[j, 1]], [b[i, 2], b[j, 2]], 
                  color=color, tube_radius=tube_radius,
                  line_width=line_width, figure=fig)

    i, j = 0, 5
    mlab.plot3d([b[i, 0], b[j, 0]], [b[i, 1], b[j, 1]], [b[i, 2], b[j, 2]], 
                color=color, tube_radius=tube_radius,
                line_width=line_width, figure=fig)
    i, j = 1, 4
    mlab.plot3d([b[i, 0], b[j, 0]], [b[i, 1], b[j, 1]], [b[i, 2], b[j, 2]], 
                color=color, tube_radius=tube_radius,
                line_width=line_width, figure=fig)
  return fig


