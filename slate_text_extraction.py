import slate


def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'r') as fh:
        document = slate.PDF(fh, password='', just_text=1)

    for page in document:
        print(page)


if __name__ == '__main__':
    extract_text_from_pdf('C:/Dev/DPF_export_XLSX/well_2253.pdf')
