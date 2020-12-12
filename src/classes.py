class Page(object):
  def __init__(self, page_number, text):
    self.page_number = page_number
    self.text = text


class Index(object):
  def __init__(self):
    self.store = {}

  def add(self, term, page_number):
    if term not in self.store:
      self.store[term] = set([page_number])
    else:
      pages = self.store[term]
      pages.add(page_number)
      self.store[term] = pages

  def __iter__(self):
    return iter(self.store.items())



