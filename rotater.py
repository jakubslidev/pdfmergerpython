import PyPDF2

# Open the PDF file in read-binary mode
pdf = open('pdfik.pdf', 'rb')

# Create a PDF reader object
reader = PyPDF2.PdfReader(pdf)

# Create a PDF writer object
writer = PyPDF2.PdfWriter()

# Loop through each page in the PDF file
for page in range(len(reader.pages)):
    # Rotate the page by 90 degrees clockwise
    rotated_page = reader.pages[page].rotate(90)
    # Add the rotated page to the PDF writer
    writer.add_page(rotated_page)

# Create a new PDF file in write-binary mode
output = open('rotated.pdf', 'wb')

# Write the rotated PDF to the output file
writer.write(output)

# Close the input and output files
pdf.close()
output.close()