import re


strip_chars_regex = re.compile('[\[\](){}<>:.,“"…]')


def clean_text(raw_text):
  return strip_chars_regex.sub('', raw_text)


def page_words(page):
  words = set()
  clean = clean_text(page.text)

  for c in clean.split(' '):
    if len(c) > 0 and c.isalpha():
      words.add(c)
  return words
