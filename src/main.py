import argparse
import extract

parser = argparse.ArgumentParser(description='Extract pdf text from each page.')
parser.add_argument('--pdf', required=True, help="filepath to pdf")
parser.add_argument('--ignore', help="filepath to file containing words to ignore")
args = parser.parse_args()

pages = extract.pages(args.pdf)

for page in pages:
  print('Page# {}:\n{}'.format(page.page_number, page.text))
