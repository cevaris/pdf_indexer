import argparse

import extract


def index(args):
  pages = extract.pages(args.pdf)
  for page in pages:
    print('Page# {}:\n{}'.format(page.page_number, page.text))


def uniq_words(args):
  pages = extract.pages(args.pdf)
  print('got here', len(pages))


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

index_parser = subparsers.add_parser('index', description='Create pdf index.')
index_parser.add_argument('--pdf', required=True, help="filepath to pdf")
index_parser.add_argument('--ignore', help="filepath to file containing words to ignore")
index_parser.set_defaults(func=index)

uniq_words_parser = subparsers.add_parser('uniq_words', description='Extract all unique words.')
uniq_words_parser.add_argument('--pdf', required=True, help="filepath to pdf")
uniq_words_parser.set_defaults(func=uniq_words)

args = parser.parse_args()
args.func(args)
