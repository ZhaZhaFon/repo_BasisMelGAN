# prepare-basismelgan-BZNSYP (repo_convtasnet4vocoder)

prepare-basismelgan:
	python dataset/basismelgan.py --dataset_dir /home/jiangji/basic/dataset-basismelgan/BZNSYP-decoderbasis
	python bin/preprocess.py --data_path ./dataset/basismelgan.txt --save_path /home/jiangji/basic/dataset-basismelgan/BZNSYP-basismelgan/npy --audio_index_path /home/jiangji/basic/dataset-basismelgan/BZNSYP-basismelgan/audio --mel_index_path /home/jiangji/basic/dataset-basismelgan/BZNSYP-basismelgan/mel

train:
	rm -rf /home/jiangji/basic/exp-basismelgan/basismelgan_0420
	CUDA_VISIBLE_DEVICES=2 python bin/train.py --basis_dir /home/jiangji/basic/dataset-basismelgan/BZNSYP-decoderbasis \
										   --audio_index_path /home/jiangji/basic/dataset-basismelgan/BZNSYP-basismelgan/audio/train \
										   --mel_index_path /home/jiangji/basic/dataset-basismelgan/BZNSYP-basismelgan/mel/train \
										   --audio_index_valid_path /home/jiangji/basic/dataset-basismelgan/BZNSYP-basismelgan/audio/valid \
										   --mel_index_valid_path /home/jiangji/basic/dataset-basismelgan/BZNSYP-basismelgan/mel/valid \
										   --model_name basis-melgan \
										   --config /home/jiangji/basic/codebase/repo_BasisMelGAN/conf/basis-melgan/light.yaml \
										    --use_scheduler 0 \
										   --mixprecision 0 \
										   --checkpoint_path "" \
										   --restore_step 0 \
										   --save_dir /home/jiangji/basic/exp-basismelgan/basismelgan_0420