#!/usr/bin/env python

import sys, re
from argparse import ArgumentParser

parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
# Add arguments to the parser
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")
parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif")

# If no arguments are provided, print help and exit
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()

# Convert sequence to uppercase
args.seq = args.seq.upper()                 # Note we just added this line

# Check if the sequence contains only valid DNA or RNA characters
if re.search('^[ACGTU]+$', args.seq):
    if re.search('T', args.seq):
        print ('The sequence is DNA')
    elif re.search('U', args.seq):
        print ('The sequence is RNA')
    else:
        print ('The sequence can be DNA or RNA')
else:
    print ('The given sequence is not DNA nor RNA')

# If motif argument is provided, perform motif search
if args.motif:
    args.motif = args.motif.upper()
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end = '')
    if re.search(args.motif, args.seq):
        print("Motif found!")
    else:
	print("NOT FOUND")
