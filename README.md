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
One of the first things you need to do is download JetPack. 
The Get Started With Jetson Orin Nano Devkit link will tell you to download Jetpack version 6.0 or greater.
The guide was based off of Jetpack 
[5.1.2](https://developer.nvidia.com/embedded/jetpack-sdk-512). 
If you are following this guide I would recommend you use 
[5.1.2](https://developer.nvidia.com/embedded/jetpack-sdk-512).
Whatever you choose, here is the 
[Jetpack Archive](https://developer.nvidia.com/embedded/jetpack-archive) 
where are the Jetpack SDK versions are stored. 

#### 2 Write the Jetpack Image to Your Micro SD Card
The instructions at [Getting Started With Jetson Orin Nano Devkit](https://developer.nvidia.com/embedded/learn/get-started-jetson-orin-nano-devkit)
are sufficient and verbose. Follow the steps there to finish this step 2. 

#### 3 Setup and First Boot
Again, the instructions at [Getting Started With Jetson Orin Nano Devkit](https://developer.nvidia.com/embedded/learn/get-started-jetson-orin-nano-devkit)
are sufficient. Go there. 

#### Helpful commands
- `sudo apt-cache show nvidia-jetpack`: This will show you your jetpack version. 


## Setting Up Your Environment. 
#### Creating a virtual environment
> Use whichever environment manager you like, miniconda or whatever. Here are the insctructinos for using virtualenv.
 In your home directory
 ```bash
 mkdir <your_env_name_here>
 python3 -m venv <your_env_name_here>
 ```
 Activate your environment:
 ```bash
 source <your_env_name_here>/bin/activate
 ```

### Installing packages. 
#### Installing Torch
DO NOT INSTALL TORCH FROM PYTORCH WEBSITE, YOU MUST GET YOUR TORCH FROM NVIDIA.

Here Is what worked for us. 
```bash
 sudo apt install libopenblas-dev
 export TORCH_INSTALL=https://developer.download.nvidia.com/compute/redist/jp/v51/pytorch/torch-1.14.0a0+44dac51c.nv23.01-cp38-cp38-linux_aarch64.whl
 python3 -m pip install --no-cache $TORCH_INSTALL
 ```
#### Installing JetCam 
Go where you want jetcam, home directory is fine. 
 
(with your virtual environment activated)
 ```bash
 git clone git@github.com:NVIDIA-AI-IOT/jetcam.git
 cd jetcam
 pip install -e
 ```
#### Installing Jet Racer
Go where you want jetracer, home directory is fine. 
 
(with your virtual environment activated)
 ```bash
 git clone git@github.com:NVIDIA-AI-IOT/jetracer.git
 cd jetracer
 pip install -e
 ```
#### Installing Jupyter, numpy, opencv-python
 ```bash
 pip install jupyter
 pip install numpy
 pip install torchvision==0.15
 pip install opencv-python
 ```

# Running
## Training
### Collecting Training Data
To get training data, we recorded a video on the car while someone drove it around our track. From other sources, it seemed like 10 minutes or more of video is a good start.

We ssh'ed into the car and rand this command to capture a video:
```bash
ffmpeg -f v4l2 -framerate 60 -video_size 1920x1080 -input_format mjpeg -i /dev/video0 -c copy mjpeg.mkv
```

*Note*: Feel free to modify the command arguments for different resolutions or codecs. We found mjpeg encoding to be fine for our purposes. Consider using a [different codec](https://stackoverflow.com/questions/21216650/ffmpeg-how-to-save-input-camera-stream-into-the-file-with-the-same-codec-format) if the transcoding is reducing performance.

### Labelling the Data
We experienced problems getting the jupyter widgets from the jetracer notebook to work. We decided to write our own script `label_data.py`
```bash
label_data.py video=<input_video> out_file=<where_you_want_it_to_go>.txt --frame_delay=.01666 # .01666 is the default value and is not required. 
```
to run through the video, track the x position of the mouse, and save the labels to a file. After pointing where you want the car to go in the video. Run the `export_frames.py` script to save the frames as individual, labeled images.
```bash
export_frames.py video=<input_video> labels=<output_file_from_label_data.py> save_path=<where_to_save>
```
*Note*:
- Modify the `export_frames.py` `save_path` command line variable to change where the images are saved. Make sure it matches what is expected by the `XYDataset` (i.e. `save_path` matches the arguments to `XYDataset`: path+category).

### Using the Data
Assuming your video frames have been labeled and exported to the proper directory, you can start running the `interactive_regression` notebook. It will walk you through connecting the camera, loading (and augmenting) the data, and training the model.

## Optimizing
After training and exporting your model as a `pth` file, run the `optimize_model` notebook to optimize the model for the hardware.

## Testing
At this point, you have trained and optimized your model. Now you can see what it learned! Follow the `road_following` notebook to run the model on the car.

# TODO
- Modify jetcam instructions or incorporate modified version into code
- Finish reformatting/cleaning jupyter notebooks
- Troubleshooting section, specifically having a rogue kernel binding the camera.
