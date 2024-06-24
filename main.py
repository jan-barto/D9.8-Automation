from pypdf import PdfReader, PdfWriter
import os


# https://pypi.org/project/pypdf/
# https://pypdf.readthedocs.io/en/stable/

def pdf_splitter(file_name):
    reader = PdfReader(file_name)

    for x in range(0, len(reader.pages), 2):
        output = PdfWriter()
        output.add_page(reader.pages[x])
        output.add_page(reader.pages[x + 1])
        with open(f"document_page_{x}-{x + 1}.pdf", "wb") as outputStream:
            output.write(outputStream)


def pdf_merger():
    x = [a for a in os.listdir() if a.endswith(".pdf")]
    merger = PdfWriter()

    for pdf in x:
        merger.append(pdf)

    merger.write("merged-pdf.pdf")
    merger.close()

# pdf_splitter("Proměna - Franz Kafka.pdf")
# pdf_merger()
