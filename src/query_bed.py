"""Tool for cleaning up a BED file."""

import argparse  # we use this module for option parsing. See main for details.

import sys
from bed import (
    parse_line, print_line
)
from query import Table


def main() -> None:
    """Run the program."""
    # Setting up the option parsing using the argparse module
    argparser = argparse.ArgumentParser(
        description="Extract regions from a BED file")
    argparser.add_argument('bed', type=argparse.FileType('r'))
    argparser.add_argument('query', type=argparse.FileType('r'))

    # 'outfile' is either provided as a file name or we use stdout
    argparser.add_argument('-o', '--outfile',  # use an option to specify this
                           metavar='output',  # name used in help text
                           type=argparse.FileType('w'),  # file for writing
                           default=sys.stdout)

    # Parse options and put them in the table args
    args = argparser.parse_args()

    # With all the options handled, we just need to do the real work
    # FIXME: put your code here


    bed_table = Table() ## process bed file (input)
    for line in args.bed:
        bed_table.add_line(parse_line(line))

    for line in args.query:
        value_query = line.split()
        new_table = bed_table.get_chrom("chr" + value_query[0][-1])
        new_table
        if len(new_table) > 0:
            for x_bed in new_table:
                if x_bed[1] >= int(value_query[1]) and x_bed[1] > int(value_query[2]):
                    print_line(x_bed, args.outfile)
                
        


if __name__ == '__main__':
    main()
