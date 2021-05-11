import os
os.chdir('/home/ubuntu/Lidar/OpenPCDet/tools')

from pathlib import Path

from pcdet.datasets import build_dataloader
from pcdet.utils import common_utils
from pcdet.config import cfg, cfg_from_yaml_file

#from train import parse_config
from pcdet.datasets.holomatic.holomatic_dataset import create_holo_infos

def parse_config():
  cfg_file = 'cfgs/holo_models/pv_rcnn.yaml'
  cfg_from_yaml_file(cfg_file, cfg)
  cfg.TAG = Path(cfg_file).stem
  cfg.EXP_GROUP_PATH = '/'.join(cfg_file.split('/')[1:-1])  # remove 'cfgs' and 'xxxx.yaml'

  return cfg

def pre_process():
  import yaml
  from pathlib import Path
  from easydict import EasyDict
  
  dataset_cfg = EasyDict(yaml.load(open('cfgs/dataset_configs/holo_dataset.yaml', 'rb'), Loader=yaml.FullLoader))
  ROOT_DIR = Path('/home/ubuntu/Lidar/OpenPCDet')

  create_holo_infos(
      dataset_cfg=dataset_cfg,
      class_names=['car', 'pedestrian', 'biker'],
      data_path=ROOT_DIR / 'data' / 'holomatic',
      save_path=ROOT_DIR / 'data' / 'holomatic'
  )

def run_train():
  cfg = parse_config()

  log_file = '/home/ubuntu/python/out'
  logger = common_utils.create_logger(log_file, rank=0)

  train_set, train_loader, train_sampler = build_dataloader(
    dataset_cfg=cfg.DATA_CONFIG,
    class_names=cfg.CLASS_NAMES,
    batch_size=2,
    dist=False, workers=8,
    logger=logger,
    training=True,
    merge_all_iters_to_one_epoch=False,
    total_epochs=80
  )
  print(train_set[0]['voxels'].shape)
  print(train_set[0]['voxel_coords'].shape)

if __name__ == '__main__':
  #run_train()
  pre_process()

