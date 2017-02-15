#!/usr/bin/python3
"""
From list in local text file download images, and save on local drive.
"""

import argparse
import os
import sys
from urllib.request import urlopen


def input_parser():
    """parse argument and and return input file"""
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', dest='input_file', required=True,
                        help='input file with list')
    parser.add_argument('-o', dest='dst_dir', required=True,
                        help='destination path')

    return parser.parse_args()


def folder_creator(dst_dir):
    """Create of output directory if not exists
    """
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
        print('Destination folder not exists and will be created')


def download_image(url, dst_dir):
    reply = urlopen(url)
    file_name = url_converter(url)
    src_file = os.path.join(dst_dir, file_name)
    print("Downloading file from {} ...".format(url))
    print("Writing file to local path {}".format(src_file))
    with open(src_file, 'wb+') as f:
        f.write(reply.read())



def url_converter(url):
    """url returns resource name"""
    return url.split('/')[-1]


def image_downloader(input_file, dst_dir):
    """
    Reader for the source file list with writer for selected out put folder.
    """
    try:
        with open(input_file) as f:
            [download_image(url.strip(), dst_dir) for url in f]
    except IOError:
        print("Invalid input file name : {}".format(input_file))
        sys.exit(2)
    except ValueError:
        print("Done, end of source list file  : {}".format(input_file))
        sys.exit(2)


if __name__ == "__main__":
    args = input_parser()
    input_file = args.input_file
    dst_dir = args.dst_dir

    if not input_file:
        sys.exit(2)

    folder_creator(dst_dir)

    image_downloader(input_file, dst_dir)
