import sys
from PIL import Image
from pdf2image import convert_from_path, convert_from_bytes
import pytesseract
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("invalid arguments provided")
        exit()
    file_path = sys.argv[1]
    print(file_path)
    images = convert_from_path(file_path)
    print(images)
    text = ""
    for image in images:
        text += pytesseract.image_to_string(image)

    with open("output.txt", "w") as file:
        file.write(text)
        