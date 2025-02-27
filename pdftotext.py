import sys
from PIL import Image
from pdf2image import convert_from_path, convert_from_bytes
import pytesseract
from fpdf import FPDF
import os
import openai
from openai import OpenAI
from dotenv import load_dotenv

from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)


def img_to_txt(image):
    return pytesseract.image_to_string(image)

def add_page_to_pdf(text, output_file):
    pdf = FPDF()
    text2 = text.encode('latin-1', 'replace').decode('latin-1')
    pdf.add_page()
    pdf.multi_cell(0, 10, txt=text2)


def pdf_to_txt(file_path, output_file):
    images = convert_from_path(file_path)
    text = ""
    for pagenum in range(len(images)):
        text += img_to_txt(images[pagenum])
        
        print(f"page {pagenum + 1}/{len(images)} done!")
    
    with open(output_file, 'w') as text_file:
        text_file.write(text)
    
    return text

def get_chatgpt_response(prompt):
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return completion.choices[0].message.content


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("invalid arguments provided")
        exit()
    

    file_path = sys.argv[1]

    pdf_to_txt(file_path, sys.argv[2])
    

    

        