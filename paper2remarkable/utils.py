# -*- coding: utf-8 -*-

"""Utility functions for a2r

Author: G.J.J. van den Burg
License: See LICENSE file
Copyright: 2019, G.J.J. van den Burg

"""


import PyPDF2
import sys

GITHUB_URL = "https://github.com/GjjvdBurg/arxiv2remarkable"


def exception(msg):
    print("ERROR: " + msg, file=sys.stderr)
    print("Error occurred. Exiting.", file=sys.stderr)
    print("", file=sys.stderr)
    print(
        "If you think this might be a bug, please raise an issue on GitHub: %s"
        % GITHUB_URL
    )
    raise SystemExit(1)


def check_file_is_pdf(filename):
    try:
        fp = open(filename, "rb")
        pdf = PyPDF2.PdfFileReader(fp, strict=False)
        fp.close()
        del pdf
        return True
    except PyPDF2.utils.PdfReadError:
        exception("Downloaded file isn't a valid pdf file.")