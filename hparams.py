import os

# Mel
num_mels = 80
num_freq = 1025
frame_length_ms = 50
frame_shift_ms = 10
fmin = 40
hop_size = 240
sample_rate = 24000
min_level_db = -100
ref_level_db = 20
preemphasize = True
preemphasis = 0.97
rescale_out = 0.4
signal_normalization = True
griffin_lim_iters = 60
power = 1.5


# Train
test_size = 0  # for testing training process
train_size = 9000
valid_size = 500
eval_size = 100

epochs = 100 # 100000  # need stop by your hands
batch_size = 16
batch_expand_size = 8
discriminator_train_start_steps = 100000
n_warm_up_step = 0

use_feature_map_loss = True

learning_rate = 1e-4
learning_rate_discriminator = 5e-5
grad_clip_thresh = 1.0

log_step = 5
clear_time = 20

save_step = 5000
valid_step = 500
valid_num = 100

checkpoint_path = os.path.join("checkpoint")
logger_path = os.path.join("logger")
tensorboard_path = os.path.join("tensorboard")

fixed_length = 140  # biaobei

lambda_adv = 1.0
lambda_fm = 1.0
lambda_stft = 5.0
