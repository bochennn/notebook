

def save_array_as_f(filename, output):
  with open(filename, 'w') as f:
    [ f.write('%s\n' % item) for item in output ]

def save_as_pkl():
  pass


