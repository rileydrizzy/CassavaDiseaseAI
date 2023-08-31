"""doc
"""
import hydra
import opendatasets as od
from omegaconf import DictConfig
from utils.logger import logger

def download_data(data_url, data_dir):
    """
    DOC
    """
    try:
        od.download(dataset_id_or_url= data_url, data_dir= data_dir)
        return True
    except Exception:
        return False






@hydra.main(config_path='dataset_config', config_name='config', version_base='1.2')
def main(cfg: DictConfig):
    """_summary_

    Parameters
    ----------
    cfg : DictConfig
        _description_
    """
    download_data(data_url= cfg.path.data_url, data_dir= cfg.path.data_dir)


if __name__ == '__main__':
    main()
