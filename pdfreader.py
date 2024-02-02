import PyPDF2
def extract_text_from_pdf(Path):

    # Open the PDF file in binary Format
    with open(Path, 'rb') as file:

        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(file)

        # Get the total number of pages in the PDF
        total_pages = len(pdf_reader.pages)
        print(f"Total number of pages: {total_pages}\n")

        # Extract and display the text content from each page
        for page_number in range(total_pages):
            # Get the specific page
            page = pdf_reader.pages[page_number]

            # Extract text from the page
            text = page.extract_text()

            # Display the text content of each page
            print(f"Page {page_number + 1}:{text}\n")

if __name__ == "__main__":
    # Specify the path to your sample PDF file
    Path = "python.pdf"

    # Call the function to extract text from the PDF
    extract_text_from_pdf(Path)
