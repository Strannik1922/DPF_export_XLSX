import json
import os

from main import extract_text_by_page


def export_as_json(pdf_path, json_path):
    filename = os.path.splitext(os.path.basename(pdf_path))[0]
    data = {'Filename': filename}
    data['Pages'] = []

    counter = 1
    for page in extract_text_by_page(pdf_path):
        text = page[0:100]
        page = {'Page_{}'.format(counter): text}
        data['Pages'].append(page)
        counter += 1

    with open(json_path, 'w') as fh:
        json.dump(data, fh)


if __name__ == '__main__':
    pdf_path = 'C:/Dev/DPF_export_XLSX/well_2253.pdf'
    json_path = 'C:/Dev/DPF_export_XLSX/well_2253.json'
    export_as_json(pdf_path, json_path)
