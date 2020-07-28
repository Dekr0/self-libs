#!/usr/bin/env python
# -*- coding:utf-8 -*-

from tqdm import tqdm

class ModifiedTqdm(tqdm):

    unit = ['byte', 'kB', 'MB', 'GB']
    @staticmethod
    def size_convert(file_size_byte, index=0):
        if file_size_byte < 1024 or index == 3:
            size_unit = "{} {}".format(str(file_size_byte)[0:4], ModifiedTqdm.unit[index])
            return size_unit
        else:
            file_size_byte = float(file_size_byte / 1024)
            index += 1
            return ModifiedTqdm.size_convert(file_size_byte, index)

    @property
    def format_dict(self):
        d = super(ModifiedTqdm, self).format_dict
        total_time = d["elapsed"] * (d["total"] or 0) / max(d["n"], 1)
        d.update(total_time=self.format_interval(total_time) + " in total")
        return d
