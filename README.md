# Lepton App
Programs to process images captured by Lepton into MNIST data.

## Environment
Lepton Purethermal-3-FS1  
Windows 11  
Python 3.11.9  


## Setup
```
pip install flirpy
```

## About Lepton
Lepton captures a 16-bit (raw) image.  
The value of DAT file is divided by 100 and subtracted by 273.15 to obtain the Celsius temperature.  
```value / 100.0 - 273.15```


## To make heat trace MNIST dataset
1. get_raw_img.py  
This program captures raw images.  
In test mode, no images are collected. In capture mode, collected images are stored in output_path.  
Press esc key to exit.
```
python3 .\get_raw_img.py --mode (test/capture) --output_path YOUR_OUTPUT_PATH
```

2. dat2img.py  
Converts *.dat to *.jpg  
```
python3 .\dat2img.py --path YOUR_DATFILE_PATH
```

3. mnist_crop.py  
Crop images to mnist input image size (28×28).  
The original image contains a lot of noise, so this code performs noise filtering and masking.
```
python3 .\mnist_crop.py
```

4. centralize.py  
This program centers the numbers and enlarges them if they are small.
```
python3 .\centralize.py
```


## References
[Lepton Integration with Windows](https://www.flir.in/developer/lepton-integration/lepton-integration-windows/)  
[FLIRPY](https://github.com/LJMUAstroecology/flirpy)

