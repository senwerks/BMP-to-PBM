import sys

def invert_pbm_p4(input_path, output_path):
    with open(input_path, 'rb') as file:
        # Read the entire file, header + data
        content = file.read()

    # Find the end of the header (first whitespace after the magic number)
    # The header is ASCII, so it's safe to decode just the first part to find it
    end_of_header = content.find(b'\x0A', 3)  # Search for newline after 'P4'

    if end_of_header == -1:
        raise ValueError("Could not find the end of the header in the PBM file")

    header = content[:end_of_header + 1]
    image_data = content[end_of_header + 1:]

    # Invert the image data by flipping all bits
    inverted_data = bytearray(b ^ 0xFF for b in image_data)

    # Save the inverted image
    with open(output_path, 'wb') as file:
        file.write(header + inverted_data)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_path.pbm> <output_path.pbm>")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]
    invert_pbm_p4(input_path, output_path)
    print(f"Inverted P4 PBM saved to {output_path}")
