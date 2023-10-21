#!/usr/bin/env python3

# Copyright (C) 2023  Realswitzer/Switz

# LZString encoder/decoder

import lzstring
import argparse
import os
import json

LZString = lzstring.LZString()

parser = argparse.ArgumentParser()
modegroup = parser.add_mutually_exclusive_group(required = True)
modegroup.add_argument('-d', '--decode', '--decompress', action='store_true', help='Decode mode (save -> json)')
modegroup.add_argument('-e', '--encode', '--compress', action='store_true', help='Encode mode (json -> save)')
parser.add_argument('input', type=str, help='input file location')
parser.add_argument('output', type=str, help='output file name')
parser.add_argument(
    '-b', '--beautify', action='store_true', help='Decode exclusive: Beautify output'
)
parser.add_argument('-c', '--overwrite', action='store_true', help='Confirm overwrite')
args = parser.parse_args()

if os.path.exists(args.input):
    inputfile = open(args.input)
    inputfile.close()
else:
    print('Nonexistent file, unable to proceed.')
    exit()

if '.' in args.output:  # Check for user provided file extension
    output = args.output
elif args.decode:  # else automatically add appropriate file extension
    output = args.output + '.json'
elif args.encode:
    output = args.output + '.save'

if not args.overwrite:
    if os.path.exists(output):
        if (
            input('Output file already exists. Overwrite? (Yes/No) ').lower() == 'yes'
            or 'y'
        ):
            os.remove(output)
        else:
            print('Exiting.')
            exit()

inputfile = open(args.input)
if args.decode:
    print('Decoding file')
    try:
        data = LZString.decompressFromBase64(inputfile.read())
        if args.beautify:
            data = json.loads(data)
            data = json.dumps(data, indent=2)
    except Exception as fuckywucky:
        print(f'Exception: {fuckywucky}')
        print('Were you trying to decompress a decompressed json file?')
        exit()
elif args.encode:
    print('Encoding file')
    try:
        data = inputfile.read()
        data = json.loads(data)
        data = json.dumps(data, separators=(',', ':'))
        data = LZString.compressToBase64(data)
    except Exception as fuckywucky:
        print(f'Exception: {fuckywucky}')
        print('Were you trying to compress a compressed save file?')
        exit()
else:
    print('you shouldnt see this')
    exit()

inputfile.close()
outputfile = open(output, 'w')
outputfile.write(data)
print('File written')
