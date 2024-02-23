import PyPDF2
import re
from datetime import datetime


def extract_information(pdf_path):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)

        transaction_data = []

        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()

            # Process text line by line
            lines = text.split('\n')

            # Define pattern for extracting relevant information
            record_pattern = r'(\d{2}/\d{2}/\d{4})\s+(.*?)\s+(.*?)\s*(-?[\d,]+(?:\.\d{2})?)?\s*(-?[\d,]+(?:\.\d{2})?|0)\s*(-?[\d,]+(?:\.\d{2})?)'

            for line_num, line in enumerate(lines, start=1):
                # Skip the header line
                if line_num == 14:
                    continue

                # Extract information using regular expressions
                records = re.findall(record_pattern, line)

                if (len(records)>=1):
                    print(records[-1])

                for date, payment_type, detail, credit, debit, balance in records:
                    date_object = datetime.strptime(date, '%d/%m/%Y')

                    # Convert comma-separated numbers to float
                    credit_amount = float(credit.replace(',', '')) if credit else None
                    debit_amount = float(debit.replace(',', '')) if debit else None
                    balance_amount = float(balance.replace(',', ''))

                    transaction_data.append({
                        'date': date_object.strftime('%d/%m/%Y'),  # Format back to '01/01/2024'
                        'payment_type': payment_type.strip(),
                        'detail': detail.strip(),
                        'credit': credit_amount if credit_amount is not None else None,
                        'debit': debit_amount if credit_amount is None else None,  # Use debit when credit is None
                        'balance': balance_amount,
                    })

    return transaction_data

# Replace 'your_pdf_file.pdf' with the actual path to your PDF file
pdf_path = 'statement.pdf'
result = extract_information(pdf_path)
print(type(result))

# Print the extracted information
for transaction in result:
    print(type(transaction))
    print(transaction)
