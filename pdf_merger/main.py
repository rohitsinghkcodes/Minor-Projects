import PyPDF2

pdf_files_list = ["javascript.pdf", "python.pdf"]

merger = PyPDF2.PdfMerger()

for pdf in pdf_files_list:
    file = open(pdf,"rb")
    pdf_reader = PyPDF2.PdfReader(file)
    merger.append(pdf_reader)
    file.close()
merger.write("Merged.pdf")