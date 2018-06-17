#!/usr/bin/env python

if __name__ == '__main__':
    filename = []
    for x in range(1,23):
        filename.append(str(x))
    filename.extend("XY")
    for x in filename:
        with open("data/chr" + x + "_aswphased") as loca_in_file, open("data/chr" + x + ".csv") as loca_out_file, open ("data/chr" + x + ".loca", "w") as merge_file:
            print(loca_in_file.readline(), file=merge_file, end='')
            for (line_in, line_out) in zip(loca_in_file, loca_out_file):
                row_in = line_in.strip().split()
                row_out = line_out.strip().split(',')
                print(row_in[0], row_in[1], '\t'.join(row_out), sep='\t', file=merge_file)


if '__main__' == __name__:
    chromesome_numbers = []
    for chr_num in range(1, 23):
        chromesome_numbers.append(str(chr_num))
    chromesome_numbers.extend('XY')
    with open("merged.loca", "w") as merge_file:
        sample_ids = {}
        for chr_num in chromesome_numbers:
            with open("chr" + x + "_aswphased") as loca_in_file:
                loca_in_file.readline().split(',')
