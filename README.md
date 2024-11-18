#Image Conversion Script
This is a small Python script that helps you convert images to the WebP format and optionally resize them.

This is a small script that helps you to convert your images into a specific format.

For Linux users
```bash
. .venv/bin/activate
```
```bash
pip install pipenv
```

```bash
pipenv install
```
```bash

python main.py
```
## Usage
Specify the Image Directory
When prompted, enter the path to the directory containing your image files as a string, e.g.:
```shell
Eingabe: /home/user/Bilder
```
###Resize Option
If you want to resize the images to a specific size, enter "J" when prompted. 
You will then be asked to enter the dimensions in pixels in the format (width, height), e.g., (800, 600).

###Conversion Process
The script will convert images with .jpg, .jpeg, and .png extensions to WebP format and save them in the same directory. 
The original file extension is replaced with .webp, so image.jpg becomes image.webp.

Now the script provides easier input handling and error-checking, ensuring the specified directory exists and handling 
image resizing and conversion efficiently.