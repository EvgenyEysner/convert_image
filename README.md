# Image Format Converter

A simple command-line tool to convert and resize images between different formats (WebP, JPG, PNG, GIF).

## Features

- Convert images between multiple formats (WebP, JPG, PNG, GIF)
- Optional image resizing while maintaining aspect ratio
- Batch processing of multiple images in a directory
- Option to delete original files after conversion
- Preserves image quality with optimized settings
- Handles transparency conversion for JPEG format

## Requirements

- Python 3.10
- Pillow (PIL) library

## Installation

1. Clone this repository or download the source code
2. Create a virtual environment:
```bash
python3 -m venv .venv
```
3. Install the required dependency:
```bash
pip install pipenv
pipenv install
```
## Usage
Run the script using Python:
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