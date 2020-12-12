import argparse
import collections

import extract
from classes import Index
from indexer import clean_text, page_words


def index(args):
  pages = extract.pages(args.pdf)
  index = Index()

  for page in pages:
    words = page_words(page)

    for w in words:
      index.add(w, page.page_number)

  sorted_index = collections.OrderedDict(sorted(index))
  for term, pages in sorted_index.items():
    print('{} - {}'.format(term, ','.join(map(str, pages))))


def uniq_words(args):
  words = set({})
  pages = extract.pages(args.pdf)

  for page in pages:
    clean = clean_text(page.text)

    for c in clean.split(' '):
      if len(c) > 0:
        words.add(c)

  # sort words
  words = sorted([*words, ])
  words = list(filter(lambda w: w.isalpha(), words))

  for w in words:
    print(w)


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
