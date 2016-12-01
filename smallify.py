# smallify

import os, shutil

# for (dirname, subdirs, files) in os.walk('../madrid_files/small2'):
#   files = [file for file in files if file.endswith('.m4a') or file.endswith('.mp3')]
#   for file in files:
#     absfile = os.path.abspath(os.path.join(dirname, file))
#     newfile = os.path.abspath(os.path.join(dirname, '_'+ file))
#     # print absfile, newfile
#     cmd = '/usr/bin/afconvert -f m4af -d aac -b 32000 "%s" "%s"' % (absfile, newfile)
#     print "Compressing... ", file
#     os.system(cmd)

for (dirname, subdirs, files) in os.walk('../madrid_files/small2'):
  # print dirname
  files = [file for file in files if dirname.endswith('PAN PHOTOS') and file.endswith('.jpg')]
  for file in files:
    absfile = os.path.abspath(os.path.join(dirname, file))
    newfile = os.path.abspath(os.path.join(dirname, '_'+ file))
    print absfile, os.path.getsize(absfile)
    # print absfile, newfile
    if (os.path.getsize(absfile) > 1000000):
      cmd = '/usr/local/bin/convert "%s" -resize 10 "%s"' % (absfile, newfile)
      print "Compressing... ", file
      os.system(cmd)
