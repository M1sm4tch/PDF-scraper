import PyPDF2

def read_pdf_line_by_line(pdf_path):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)

        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()

            print("===== Text Extracted from Page {} =====".format(page_num + 1))

            # Process text line by line
            lines = text.split('\n')

            for line_num, line in enumerate(lines, start=1):
                print("Line {}: {}".format(line_num, line))

            print("===== End of Text for Page {} =====".format(page_num + 1))

# Replace 'your_pdf_file.pdf' with the actual path to your PDF file
pdf_path = 'statement.pdf'
read_pdf_line_by_line(pdf_path)
