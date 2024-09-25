# Lepton App

## Environment
Lepton Purethermal-3-FS1  
Windows 11  
Python 3.11.9  


## Setup
```
pip install flirpy
```


## To make heat trace MNIST dataset
1. get_raw_img.py  
This program captures raw images.  
In test mode, no images are collected. In capture mode, collected images are stored in output_path.  
Press esc key to exit.

```
python3 .\get_raw_img.py --mode (test/capture) --number [0-9]
```

2. dat2img.py  
```
python3 .\dat2img.py --path YOUR_DATFILE_PATH
```

3. mnist_crop.py  
Crop images to mnist input image size.  
```
python3 .\mnist_crop.py
```

4. centralize.py  
This program centers the numbers and enlarges them if they are small.
```
python3 .\centralize.py
```
