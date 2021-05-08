import os
os.chdir('/home/ubuntu/Lidar/OpenPCDet/tools')

from pathlib import Path

from pcdet.datasets import build_dataloader
#from pcdet.utils import common_utils
#from pcdet.config import cfg, cfg_from_yaml_file

#from train import parse_config
from pcdet.datasets.holomatic.holomatic_dataset import create_holo_infos

def run():
  import yaml
  from pathlib import Path
  from easydict import EasyDict

  #output_dir = '/home/ubuntu/python'
  holo_configs = 'cfgs/holo_models/pv_rcnn.yaml'
  dataset_configs = 'cfgs/dataset_configs/holo_dataset.yaml'

  dataset_cfg = EasyDict(yaml.load(open(dataset_configs, 'rb'), Loader=yaml.FullLoader))
  ROOT_DIR = Path('/home/ubuntu/Lidar/OpenPCDet')

  #log_file = output_dir + '/out'
  #logger = common_utils.create_logger(log_file, rank=0)

  #cfg_from_yaml_file(cfg_file, cfg)
  #cfg.TAG = Path(cfg_file).stem
  #cfg.EXP_GROUP_PATH = '/'.join(cfg_file.split('/')[1:-1])  # remove 'cfgs' and 'xxxx.yaml'

  '''train_set, train_loader, train_sampler = build_dataloader(
    dataset_cfg=cfg.DATA_CONFIG,
    class_names=cfg.CLASS_NAMES,
    batch_size=2,
    dist=False, workers=8,
    logger=logger,
    training=True,
    merge_all_iters_to_one_epoch=False,
    total_epochs=80
  )'''
  create_holo_infos(
      dataset_cfg=dataset_cfg,
      class_names=['Car', 'Pedestrian', 'Cyclist'],
      data_path=ROOT_DIR / 'data' / 'holomatic',
      save_path=ROOT_DIR / 'data' / 'holomatic'
  )

if __name__ == '__main__':
  run()

