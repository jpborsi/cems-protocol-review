import argparse
import os
import sys

import yaml
from pypdf import PdfWriter, PdfReader

from config import Config


def main(input_pdf, config, output_location):
    sys.setrecursionlimit(2000) # pdfs with lots of objects will exceed the default python recursion limit
    for protocol in config.protocols:
        if os.path.exists(f'{output_location}/{config.version}_{protocol.name}.pdf'):
            continue
        output = PdfWriter()
        for page in protocol.pages:
            output.add_page(input_pdf.pages[page])
        with open(f'{output_location}/{config.version}_{protocol.name}.pdf', 'wb') as output_stream:
            output.write(output_stream)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_pdf', type=str)
    parser.add_argument('config', type=str)
    parser.add_argument('output_location', type=str)

    args = parser.parse_args()
    input_pdf = PdfReader(open(args.input_pdf, 'rb'))
    config_raw = yaml.load(open(args.config, 'r'), Loader=yaml.FullLoader)
    print(config_raw)
    config = Config(config_raw)
    main(input_pdf, config, args.output_location)