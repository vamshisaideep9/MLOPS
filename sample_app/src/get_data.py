## Read params
## Process
## return dataframe

import os
import yaml
import pandas as pd
import argparse


def read_params(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

def get_data(config_path):
    config = read_params(config_path)
    data_path = config["data_source"]["s3_source"]
    df = pd.read_csv(data_path, sep=",", encoding="utf-8")
    return df


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="c:/Users/vamsh/OneDrive/Desktop/mlops/MLOPS/sample_app/params.yaml")
    parsed_args = args.parse_args()
    get_data(config_path=parsed_args.config)

