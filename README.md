# repo_BasisMelGAN

[原始仓库链接](https://github.com/xcmyz/FastVocoder), 做了一些修改方便使用

### 文件组织
```
    bin/
        preprocess.py 处理Conv-TasNet生成的basis数据用于训练集
        train.py 训练循环
    data/
        audio.py 音频处理实现
        dataset.py 数据集处理实现
    dataset/
        basismelgan.py 处理Conv-TasNet生成的basis数据用于训练集
    Makefile HOW-TO use
```

---
---

# Fast (GAN Based Neural) Vocoder

## Todo

- [x] Support Basis-MelGAN
- [x] Add more demo
- [x] Add pretrained model
- [ ] Support NHV

## Discription

Include Basis-MelGAN (paper link: https://arxiv.org/pdf/2106.13419.pdf), MelGAN, HifiGAN and Multiband-HifiGAN, maybe include Neural Homomorphic Vocoder in the future. Developed on [BiaoBei dataset](https://www.data-baker.com/#/data/index/source), you can modify `conf` and `hparams.py` to fit your own dataset and model.

## Demo

- [Demo README](/resource/demo/README.md)
- [Basis-MelGAN demo page](https://blog.xcmyz.xyz/demo/)
- [Basis-MelGAN pretrained Model](https://github.com/xcmyz/FastVocoder/releases/download/v1.0/basis.melgan.pt)

## RTF

- Platform: MacBook Pro M1
- HiFiGAN (large): NaN
- HiFiGAN (light, baseline): 0.2424
- MultiBand-HiFiGAN (large): 0.4956
- MultiBand-HiFiGAN (light): 0.1591
- Basis-MelGAN: 0.0498
- HiFiGAN (light) : MultiBand-HiFiGAN (large) : MultiBand-HiFiGAN (light) : Basis-MelGAN = 50 : 102 : 33 : 10

## Usage (of Basis-MelGAN)

### 1. abstract

Recent studies have shown that neural vocoders based on generative adversarial network (GAN) can generate audios with high quality. While GAN based neural vocoders have shown to be computationally much more efficient than those based on autoregressive predictions, the real-time generation of the highest quality audio on CPU is still a very challenging task. One major computation of all GAN-based neural vocoders comes from the stacked upsampling layers, which were designed to match the length of the waveform's length of output and temporal resolution. Meanwhile, the computational complexity of upsampling networks is closely correlated with the numbers of samples generated for each window. To reduce the computation of upsampling layers, we propose a new GAN based neural vocoder called Basis-MelGAN where the raw audio samples are decomposed with a learned basis and their associated weights. As the prediction targets of Basis-MelGAN are the weight values associated with each learned basis instead of the raw audio samples, the upsampling layers in Basis-MelGAN can be designed with much simpler networks. Compared with other GAN based neural vocoders, the proposed Basis-MelGAN could produce comparable high-quality audio but significantly reduced computational complexity from HiFi-GAN V1's 17.74 GFLOPs to 7.95 GFLOPs.

### 2. Prepare data

- Refer to [xcmyz: ConvTasNet4BasisMelGAN](https://github.com/xcmyz/ConvTasNet4BasisMelGAN) to get dataset for Basis-MelGAN
- Move `ConvTasNet4BasisMelGAN/Basis-MelGAN-dataset` to `FastVocoder`
- Write path of wav data in a file, for example: ``` cd dataset && python3 basismelgan.py ```
- Run ``` bash preprocess.sh dataset/basismelgan.txt Basis-MelGAN-dataset/processed dataset/audio dataset/mel ```

### 3. Train

- command:
```
bash train.sh \
    <GPU ids> \
    /path/to/audio/train \
    /path/to/audio/valid \
    /path/to/mel/train \
    /path/to/mel/valid \
    <model name> \
    /path/to/configuration/file \
    <if use scheduler> \
    <if mix precision training>
```

- for example:
```
bash train.sh \
    0 \
    dataset/audio/train \
    dataset/audio/valid \
    dataset/mel/train \
    dataset/mel/valid \
    basis-melgan \
    conf/basis-melgan/light.yaml \
    0 0
```

### 4. Train from checkpoint
- command:
```
bash train.sh \
    <GPU ids> \
    /path/to/audio/train \
    /path/to/audio/valid \
    /path/to/mel/train \
    /path/to/mel/valid \
    <model name> \
    /path/to/configuration/file \
    <if use scheduler> \
    <if mix precision training> \
    /path/to/checkpoint \
    <step of checkpoint>
```

### 5. Synthesize
- command:
```
bash synthesize.sh \
    /path/to/checkpoint \
    /path/to/mel \
    /path/for/saving/wav \
    <model name> \
    /path/to/configuration/file
```

## Usage (of MelGAN, HifiGAN and Multiband-HifiGAN)

### 1. Prepare data

- write path of wav data in a file, for example: ``` cd dataset && python3 biaobei.py ```
- ``` bash preprocess.sh <wav path file> <path to save processed data> dataset/audio dataset/mel ```
- for example: ``` bash preprocess.sh dataset/BZNSYP.txt processed dataset/audio dataset/mel ```

### 2. Train
- command:
```
bash train.sh \
    <GPU ids> \
    /path/to/audio/train \
    /path/to/audio/valid \
    /path/to/mel/train \
    /path/to/mel/valid \
    <model name> \
    /path/to/configuration/file \
    <if use scheduler> \
    <if mix precision training>
```
- for example:
```
bash train.sh \
    0 \
    dataset/audio/train \
    dataset/audio/valid \
    dataset/mel/train \
    dataset/mel/valid \
    hifigan \
    conf/hifigan/light.yaml \
    0 0
```

### 3. Train from checkpoint
- command:
```
bash train.sh \
    <GPU ids> \
    /path/to/audio/train \
    /path/to/audio/valid \
    /path/to/mel/train \
    /path/to/mel/valid \
    <model name> \
    /path/to/configuration/file \
    <if use scheduler> \
    <if mix precision training> \
    /path/to/checkpoint \
    <step of checkpoint>
```

### 4. Synthesize
- command:
```
bash synthesize.sh \
    /path/to/checkpoint \
    /path/to/mel \
    /path/for/saving/wav \
    <model name> \
    /path/to/configuration/file
```
