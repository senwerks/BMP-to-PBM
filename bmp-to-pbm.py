#   .-------------.---------------------------------------------.
#   | Project     |   bmp-to-pbm.py                             |
#   | Author      |   SenWerks - senwerks.com                   |
#   | Description |   Convert a BMP image to PBM for ePaper     |
#   | Source      |   https://github.com/senwerks/bmp-to-pbm    |
#   |-------------|---------------------------------------------|
#   | Version     |   V0.1                                      |
#   | Release     |   2024-04-02                                |
#   '-------------'---------------------------------------------'

import sys
from PIL import Image
import numpy as np


def save_pbm(binary_values, width, height, filename):
    if len(binary_values) != width * height:
        raise ValueError("The number of binary values must match width*height")

    header = f"P4\n{width} {height}\n"
    # Group the binary values by 8 to form bytes
    bytes_list = []

    for i in range(0, len(binary_values), 8):
        byte = binary_values[i : i + 8]
        byte_value = sum(bit << (7 - j) for j, bit in enumerate(byte))
        bytes_list.append(byte_value)

    with open(filename, "wb") as f:
        f.write(header.encode())  # Header must be written as ASCII
        f.write(bytearray(bytes_list))  # Image data as bytes


def bmp_to_binary_array(bmp_path):
    # Load the image
    with Image.open(bmp_path) as img:
        # Convert the image to grayscale
        gray_img = img.convert("L")

        # Convert the grayscale image to a numpy array
        img_array = np.array(gray_img)

        # Determine the threshold (128 out of 255, because 50% darkness)
        threshold = 200

        # Convert the array to a binary array based on the threshold
        # Pixels with values < threshold are set to 0, otherwise 1
        binary_array = (img_array >= threshold).astype(int)

        # Output the size
        output_size = list(binary_array.shape)
        print(f"output_size = {output_size}")

        # Print the binary array in the specified format
        print("output_binary = [")
        for row in binary_array:
            print(", ".join(str(val) for val in row))
        print("]")

        bmp_width = output_size[1]
        bmp_height = output_size[0]

        # Flatten the binary array to a 1D list
        binary_values_flat = binary_array.ravel().tolist()

        # Save the flattened binary array to a PBM file
        pbm_filename = f"{bmp_path.rsplit('.', 1)[0]}.pbm"
        save_pbm(binary_values_flat, bmp_width, bmp_height, pbm_filename)
        print(f"Saved PBM file to {pbm_filename}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_bmp_file>")
        sys.exit(1)

    bmp_path = sys.argv[1]
    bmp_to_binary_array(bmp_path)