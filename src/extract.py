import multiprocessing
import sys
from concurrent import futures
from functools import partial

from pdfreader import PageDoesNotExist, SimplePDFViewer

from classes import Page


def pages(filepath):
    # page_count = 10
    page_count = calculate_page_count(filepath)
    print('found {} pages'.format(page_count))

    curr_page = 1
    viewer_render = partial(page_extractor, filepath)
    return list(map(viewer_render, range(1, page_count)))

    # while curr_page < page_count:
    #     viewer_render(curr_page)
    #     curr_page = curr_page + 1

    # thread_count = multiprocessing.cpu_count() - 1
    # tp = futures.ThreadPoolExecutor(max_workers=thread_count)
    # with tp as executor:
    #     viewer_render = partial(page_extractor, filepath)
    #     return list(executor.map(viewer_render, range(1, page_count)))


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

        # content = content[3:]  # remove page number

        text = ''.join(content)
        print('extracted page {}'.format(page_number), file=sys.stderr)
        return Page(page_number, text)
