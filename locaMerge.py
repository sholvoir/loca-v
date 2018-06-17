#!/usr/bin/env python
import re

if __name__ == '__main__':
    chromesome_numbers = []
    for chr_num in range(1,23):
        chromesome_numbers.append(str(chr_num))
    chromesome_numbers.extend("XY")
    for chr_num in chromesome_numbers:
        chr_name = "chr" + chr_num
        with open(chr_name + "_aswphased") as loca_in_file, open(chr_name + ".csv") as loca_out_file, open (chr_name + ".loca", "w") as merge_file:
            column_names = loca_in_file.readline().strip().split()
            column_names.insert(2, 'chromosome')
            print(column_names, sep='\t', file=merge_file)
            for (line_in, line_out) in zip(loca_in_file, loca_out_file):
                row_in = line_in.strip().split()
                row_out = line_out.strip().split(',')
                print(row_in[0], row_in[1], chr_name, '\t'.join(row_out), sep='\t', file=merge_file)