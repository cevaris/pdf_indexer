import threading
from concurrent import futures
from functools import partial

from pdfreader import PageDoesNotExist, SimplePDFViewer


viewer_lock = threading.Lock()


class Page(object):
  def __init__(self, page_number, text):
    self.page_number = page_number
    self.text = text


def pages(filepath):
  page_count = 10 # calculate_page_count(filepath)
  print('found {} pages'.format(page_count))

  tp = futures.ThreadPoolExecutor(max_workers=10)
  with tp as executor:
    viewer_render = partial(page_extractor, filepath)
    return executor.map(viewer_render, range(1, page_count + 1))


def calculate_page_count(filepath):
  with open(filepath, "rb") as fd:
    viewer = SimplePDFViewer(fd)
    page = 0
    while True:
      try:
        page += 1
        viewer.navigate(page)
      except PageDoesNotExist:
        break
    return page


def page_extractor(filepath, page_number):
  with open(filepath, "rb") as fd:
    viewer = SimplePDFViewer(fd)
    viewer.navigate(page_number)
    viewer.render()
    content = viewer.canvas.strings

    content = content[3:] # remove page number

    text = ''.join(content)
    return Page(page_number, text)
