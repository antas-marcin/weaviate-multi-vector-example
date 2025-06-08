import os
from pdf2image import convert_from_path

# Path to the PDF file
pdf_path = "./NVIDIA-Investor-Presentation-Oct-2024.pdf"

# Convert PDF pages to images
images = convert_from_path(pdf_path)

# Create output folder if it doesn't exist
if not os.path.exists("./pages"):
    os.makedirs("./pages")

# Save or process each page as an image
for i, image in enumerate(images):
    file_path = f"./pages/page_{i+1}.png"
    image.save(file_path, "PNG")
