import PyPDF2

# Otwieranie pliku PDF
with open('ExamplePDF.pdf', 'rb') as pdf_file:
    reader = PyPDF2.PdfReader(pdf_file)
    
    # Odczytywanie liczby stron
    num_pages = len(reader.pages)
    
    # Odczyt wszystkich stron PDF
    for page_num in range(num_pages):
        page = reader.pages[page_num]
        text = page.extract_text()
        print(f"Strona {page_num + 1}:")
        print(text)
