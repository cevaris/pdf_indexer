import argparse

from pdfreader import SimplePDFViewer, PageDoesNotExist


parser = argparse.ArgumentParser(description='Extract pdf text from each page.')
parser.add_argument('--file_name', required=True)
args = parser.parse_args()

viewer_fd = open(args.file_name, "rb")
viewer = SimplePDFViewer(viewer_fd)

page = 1
while True:
  try:
    viewer.navigate(page)
    viewer.render()

    print(''.join(viewer.canvas.strings))

    page += 1
  except PageDoesNotExist as e:
    print('all done')
    break
