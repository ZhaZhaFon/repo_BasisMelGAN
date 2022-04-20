# reference
# GitHub@xcmyz: https://github.com/xcmyz/FastVocoder/dataset/basismelgan.py

# modified and re-distributed by Zifeng Zhao @ Peking University

import os

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--dataset_dir', required=True, type=str, help='path to the generated basis (of Conv-TasNet decoder)')
args = parser.parse_args()

#data_path = os.path.join(args.dataset_dir, "Basis-MelGAN-dataset", "generated")
data_path = os.path.join(args.dataset_dir, "generated")
with open("basismelgan.txt", "w", encoding="utf-8") as f:
    for filename in os.listdir(data_path):
        f.write(os.path.abspath(os.path.join(data_path, filename))+"\n")
