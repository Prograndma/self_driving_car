# Self Driving Car
A repo more interested in helping you build your own self-driving car (with Jetson Orin Nano)

## Required Materials
- A Car  
   - Jetson Orin Nano module with microSD card slot
   - Reference carrier board

 - 19V power supply 
 - microSD card (64GB UHS-1 or bigger recommended)
 - USB keyboard and mouse
 - Computer display
 - USB cable

## Installing Jetpack
[Getting Started With Jetson Orin Nano Devkit](https://developer.nvidia.com/embedded/learn/get-started-jetson-orin-nano-devkit)

Here Is where you will want to go for the instructions to install jetpack straight from Nvidia.
#### 1 Downloading Jetpack
>One of the first things you need to do is download JetPack. 
The Get Started With Jetson Orin Nano Devkit link will tell you to download Jetpack version 6.0 or greater.
The guide was based off of Jetpack 
[5.1.2](https://developer.nvidia.com/embedded/jetpack-sdk-512). 
If you are following this guide I would recommend you use 
[5.1.2](https://developer.nvidia.com/embedded/jetpack-sdk-512).
Whatever you choose, here is the 
[Jetpack Archive](https://developer.nvidia.com/embedded/jetpack-archive) 
where are the Jetpack SDK versions are stored. 

#### 2 Write the Jetpack Image to Your Micro SD Card
> The instructions at [Getting Started With Jetson Orin Nano Devkit](https://developer.nvidia.com/embedded/learn/get-started-jetson-orin-nano-devkit)
are sufficient and verbose. Follow the steps there to finish this step 2. 

#### 3 Setup and First Boot
>Again, the instructions at [Getting Started With Jetson Orin Nano Devkit](https://developer.nvidia.com/embedded/learn/get-started-jetson-orin-nano-devkit)
are sufficient. Go there. 

#### Helpful commands
> `sudo apt-cache show nvidia-jetpack` This will show you your jetpack version. 


## Setting Up Your Environment. 
#### Creating a virtual environment
> Use whichever environment manager you like, miniconda or whatever. Here are the insctructinos for using virtualenv.
> In your home directory
> ```bash
> mdir <your_env_name_here>
> python3 -m venv <your_env_name_here>
> ```
> Activate your environment:
> ```bash
> source <your_env_name_here>/bin/activate
> ```

### Installing packages. 
#### Installing Torch
> DO NOT INSTALL TORCH FROM PYTORCH WEBSITE, YOU MUST GET YOUR TORCH FROM NVIDIA.
> 
> Here Is what worked for us. 
>```bash
> sudo apt install libopenblas-dev
> export TORCH_INSTALL=https://developer.download.nvidia.com/compute/redist/jp/v51/pytorch/torch-1.14.0a0+44dac51c.nv23.01-cp38-cp38-linux_aarch64.whl
> python3 -m pip install --no-cache $TORCH_INSTALL
> ```
#### Installing JetCam 
> Go where you want jetcam, home directory is fine. 
> 
> (with your virtual environment activated)
> ```bash
> git clone git@github.com:NVIDIA-AI-IOT/jetcam.git
> cd jetcam
> pip install -e
> ```
#### Installing Jet Racer
> Go where you want jetracer, home directory is fine. 
> 
> (with your virtual environment activated)
> ```bash
> git clone git@github.com:NVIDIA-AI-IOT/jetracer.git
> cd jetracer
> pip install -e
> ```
#### Installing Jupyter, numpy, opencv-python
> ```bash
> pip install jupyter
> pip install numpy
> pip install torchvision==0.15
> pip install opencv-python
> ```
> 
