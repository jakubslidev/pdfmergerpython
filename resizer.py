import PyPDF2

# Open the first PDF file in read-binary mode
pdf1 = open('pdf.pdf', 'rb')

# Open the second PDF file in read-binary mode
pdf2 = open('2.pdf', 'rb')

# Create a PDF merger object
merger = PyPDF2.PdfMerger()

# Add the first PDF file to the merger
merger.append(pdf1)

# Add the second PDF file to the merger
merger.append(pdf2)

# Create a new PDF file in write-binary mode
output = open('merged.pdf', 'wb')

# Write the merged PDF to the output file
merger.write(output)

# Close the input and output files
pdf1.close()
pdf2.close()
output.close()