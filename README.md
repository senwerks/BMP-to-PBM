# BMP-to-PBM

Converts a BMP image to a black and white PBM file for use on ePaper displays, such as in my [Bin-Mate project](https://github.com/senwerks/Bin-Mate).

Gets unreliable if the files are over ~512x512. I'll look into that someday. Maybe.

## Requirements

`pip install Pillow numpy`

## Usage

`python bmp-to-pbm.py <input-file.bmp>`

Output will be in same folder with same filename but .pbm extension
