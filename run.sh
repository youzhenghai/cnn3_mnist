#!/bin/bash

# Setting values of arguments

# Training
gpus=1
batch_size=64
epochs=10
num_workers=4

# Dataset
val_ratio=0.2

# Seed
seeds=(1 10 100 1000 10000)

# Model
model_names=("CNN3BNNPara" "CNN3BNPara" "CNN3GNNPara" "CNN3GNPara" "CNN3INNPara" "CNN3INPara" "CNN3LNNPara" "CNN3LNPara")

# Experiment
for seed in "${seeds[@]}"; do
  for model_name in "${model_names[@]}"; do
    experiment_name="MNIST-Model=${model_name}-Seed=${seed}"
    echo "training ${experiment_name}"
    python train.py --gpus $gpus \
      --val_ratio $val_ratio \
      --batch_size $batch_size \
      --seed $seed \
      --epochs $epochs \
      --num_workers $num_workers \
      --model_name $model_name \
      --experiment_name $experiment_name
  done
done
