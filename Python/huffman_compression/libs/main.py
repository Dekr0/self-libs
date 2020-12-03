#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys
import huffman
import util


def compress(filename):
    print(f"Compressing {filename} to {filename}.huf")
    with open(filename, 'rb') as uncompressed:
        freqs = huffman.make_freq_table(uncompressed)
        tree = huffman.make_tree(freqs)
        uncompressed.seek(0)

        base_name = os.path.basename(filename)
        target_path = get_path(base_name)

        with open(target_path+'.huf', 'wb') as compressed:
                util.compress(tree, uncompressed, compressed)

    input("Finished")


def decompress(filename):
    try:
            print(f"Decompressing {filename} to {filename}.decomp")
            with open(filename, 'rb') as compressed:

                base_name = os.path.basename(filename)
                target_path = get_path(base_name)
                target_name, target_suffix = os.path.splitext(os.path.splitext(target_path)[0])
                target_name += "decompressed"
                target_path = "".join((target_name, target_suffix))

                with open(target_path, 'wb') as uncompressed:
                        util.decompress(compressed, uncompressed)
            input("Finished")
    except Exception as ex:
        print(ex)
        input()


def get_path(basename):
    if hasattr(sys, "frozen"):
        base_dir = sys.executable
        required_path = os.path.abspath(os.path.join(os.path.dirname(base_dir), basename))
        return required_path