# Image Overlay Tool

The Image Overlay Tool is a utility that overlays an image over a video. It allows you to select a video file and an image file, specify the coordinates where the image should be placed on the video, and then overlay the image on every frame of the video. The final output video with the overlaid image will be saved in the `out` folder.

## Requirements

Before using the Image Overlay Tool, make sure you have the following dependencies installed:

- Python (version 3.6 or higher)
- OpenCV (`opencv-python`)
- NumPy (`numpy`)
- Pillow (`pillow`)
- FFmpeg (a multimedia framework for handling video and audio)

You can install the Python dependencies using the following commands:

```
pip install opencv-python
pip install numpy
pip install pillow
```

To install FFmpeg, you can visit the [official FFmpeg website](https://www.ffmpeg.org/download.html) and follow the installation instructions for your operating system.

## Usage

1. Place your video file in the `inp` folder of the tool.
2. Put the image you want to overlay in the `img` folder.

To use the Image Overlay Tool, simply run `main.py` in your terminal or command prompt:

```
python main.py
```

The tool will guide you through the process of overlaying the image on the video.

## Notes

- Make sure the image and video have compatible dimensions to ensure proper overlay.
- The tool supports common video formats like MP4, AVI, MKV, etc., and image formats like JPEG and PNG.
- Deleting temporary files (`frame` folder and `op.avi`) after execution is recommended to avoid errors in future processes.

## Acknowledgments

This tool utilizes the following libraries:

- OpenCV: https://opencv.org/
- NumPy: https://numpy.org/
- Pillow: https://python-pillow.org/

