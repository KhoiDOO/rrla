# rrla
RRLA - Robotic Reinforcement Learning Archive

# Setup
## Pre Installation
```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python3.x-dev # 3.x is the verion of your Python
sudo apt-get install build-essential
sudo apt-get install libpq-dev python-dev libxml2-dev libxslt1-dev libldap2-dev libsasl2-dev libffi-dev libjpeg-dev zlib1g-dev libosmesa6-dev patchelf
```

## Mujoco Setup
```
pip install mujoco
```
## Mujoco Extra Setup
1. Download the MuJoCo version 2.1 binaries for
   [Linux](https://mujoco.org/download/mujoco210-linux-x86_64.tar.gz) or
   [OSX](https://mujoco.org/download/mujoco210-macos-x86_64.tar.gz).
2. Extract the downloaded `mujoco210` directory into `~/.mujoco/mujoco210`.
3. export path to ```~/.bashrc```
```
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/kohido/.mujoco/mujoco210/bin
source ~/.bashrc # Reset the .bashrc file
echo $LD_LIBRARY_PATH # Verify path exporting
```

## Setup Gymnasium Robotics
```
pip install gymnasium-robotics[mujoco-py]
```

## Logging Setup

### 1. Install Tensorboard
```
pip install tensorboard
```
### 2. Install WandB
```
pip install wandb
```

## Setup Torch
```
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```
