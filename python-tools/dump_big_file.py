#!/usr/bin/env python
#
#  This is an example of how to use the autogenerated Python module
# to parse CTR's BIGFILE.BIG
#
# Example usage:
#  * install kaitai-struct (http://kaitai.io/#download)
#
#  * compile the `.ksy` into a python module (this generates `ctr_big.py`)
#     ksc --target python --outdir . bigfile.ksy
#
#  * install kaitai-struct for python
#     pip install kaitaistruct
#
#  * you can now run this script to parse you BIGFILE.BIG
#    ./parse_bigfile_example.py /path/to/BIGFILE.BIG
#
#  * sample output:
#    BIGFILE contains 608 entries
#    000: offset=6144, size=458808
#    001: offset=466944, size=551532
#    002: offset=1019904, size=458808
#    003: offset=1480704, size=517820
#    004: offset=1998848, size=458808
#    ...
#


import sys
import os

from ctr.ctr_big import CtrBig


if len(sys.argv) != 3:
    print('Usage: ' + sys.argv[0] + ' </path/to/BIGFILE.BIG> <dump path>')
    sys.exit(1)

bigfile = sys.argv[1]
dump_path = sys.argv[2]

# parse the file
# we can also use `from_bytes` to parse from in-memory files
ctr = CtrBig.from_file(bigfile)


print('BIGFILE contains {} entries'.format(ctr.total_files))


# actual dump
for idx, entry in enumerate(ctr.index):
    print(idx)

    content = entry.file_content

    output_filename = dump_path + os.path.sep + '{:03d}'.format(idx)
    destination = open(output_filename, 'wb')
    destination.write(content)

