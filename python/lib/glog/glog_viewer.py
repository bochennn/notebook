from pylab import *

class GlogViewer():
  def __init__(self, filepath='/home/bochen/cat_log'):
    self.left_lane_boundary = []
    self.right_lane_boundary = []
    self.center_line = []
    
    self.obs_flu = []
    
    self.log = self.get_log_content(filepath)
    self.log.reverse() # func pop() only remove last element
    
  def get_log_content(self, logpath):
    logfile = open(logpath)
    content = []
    try:
      for line in logfile:
        content.append(line.strip())
    finally:
      logfile.close()
    return content
  
  def log_empty(self):
    return len(self.log) is 0

  def plot_lane(self):
    plot(self.left_lane_boundary[0], self.left_lane_boundary[1], 'bo-')
    plot(self.right_lane_boundary[0], self.right_lane_boundary[1], 'bo-')
    plot(self.center_line[0], self.center_line[1], 'go-')
    plot(self.obs_flu[0], self.obs_flu[1], 'ro-')
    show()

  def trim_glog_prefix(self, prefix):
    pass
    
  def cat_point(self, line):
    point_start = 'point2: ('
    pt1_indx = line.index(point_start) + len(point_start)
    pt1 = float(line[pt1_indx : line.index(', ', pt1_indx)])
    pt2_indx = line.index(', ', pt1_indx) + len(', ')
    pt2 = float(line[pt2_indx : -1])
    return [pt1, pt2]

  def cat_lane_boundary(self):
    if self.log_empty(): return False
    
    if 'sampling left lane boundary' in self.log[-1]:
      self.log.pop()
      while not self.log_empty() and '->' not in self.log[-1]:
        self.left_lane_boundary.append(self.cat_point(self.log.pop()))
      self.left_lane_boundary = np.array(self.left_lane_boundary).transpose()
    
    if 'sampling right lane boundary' in self.log[-1]:
      self.log.pop()
      while not self.log_empty() and '->' not in self.log[-1]:
        self.right_lane_boundary.append(self.cat_point(self.log.pop()))
      self.right_lane_boundary = np.array(self.right_lane_boundary).transpose()
      
    if 'get center line' in self.log[-1]:
      self.log.pop()
      while not self.log_empty() and '->' not in self.log[-1]:
        self.center_line.append(self.cat_point(self.log.pop()))
      self.center_line = np.array(self.center_line).transpose()
    return True
    
  def cat_trajectory(self):
    if self.log_empty(): return False
    
    if 'convert agents in frenet' in self.log[-1]:
      self.log.pop()
      while not self.log_empty() and '->' not in self.log[-1]:
        line = self.log.pop()
        try:
          pt1_indx = line.index('flu, x, ') + len('flu, x, ')
          pt1 = float(line[pt1_indx : line.index(', ', pt1_indx)])
          pt2_indx = line.index(', y, ', pt1_indx) + len(', y, ')
          pt2 = float(line[pt2_indx : line.index(', ', pt2_indx)])
          self.obs_flu.append([pt1, pt2])
        except:
          pass
      self.obs_flu = np.array(self.obs_flu).transpose()
      print(self.obs_flu)


