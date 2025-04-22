# Image Converter Tool 🔄🖼️

[![Python Version](https://img.shields.io/badge/Python-3.10-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

A user-friendly GUI tool for converting and compressing images between common formats (JPG, PNG, BMP). Built with Python.

## Features ✨

✅ **Format Conversion**  
Convert images between:
- PNG ↔ JPG
- BMP ↔ JPG
- PNG ↔ BMP

✅ **Compression Control**  
Adjust JPG compression quality (1-100) to balance quality and file size

✅ **Simple Interface**  
Intuitive 3-step workflow:
1. Select input image
2. Choose output format
3. Set compression (for JPG)

✅ **Automatic Output Management**  
- Creates output directory if missing
- Preserves original filename with new extension

## Installation 🛠️

1. Clone the repository:
```bash
git clone https://github.com/EvgenyEysner/convert_image.git
cd convert_image
```
2. Set up virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# OR
venv\Scripts\activate  # Windows
```
3. Install dependencies:
```bash
pip install pipenv
pipenv install
```
## Usage 🚀
### Run the script using python:
```bash

python main.py
```
### Follow the interactive prompts:

- Enter the directory path containing your images
- Choose whether to resize images (Y/N)
- Specify target format (webp/jpg/png/gif)
- Choose whether to delete original files (Y/N)
- If resizing, enter dimensions in format: width,height

### Supported Formats
- Input: JPG, JPEG, PNG, GIF
- Output: WebP, JPG, PNG, GIF

### Error Handling
- Validates input directory existence
- Checks for supported file formats
- Provides error messages for failed conversions
- Validates resize dimensions input