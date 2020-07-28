#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
from tqdm import tqdm
from tqdm.utils import CallbackIOWrapper

file_size = os.stat("F:/file.7z").st_size
with tqdm(total=file_size, unit='B', unit_scale=True, unit_divisor=1024, dynamic_ncols=True) as t:
    file = CallbackIOWrapper(t.update, open("F:/file.7z", "rb"), "read")
    while True:
        chunk = file.read(1024)
        if not chunk:
            break