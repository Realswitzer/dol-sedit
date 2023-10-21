#!python3
# have to use messy shebang to bypass python on my arch system being super fucked.
import argparse
import os

import lzstring

class Generic:
    Confirmation: list[str] = ['y', 'yes', 'ys', 'yeah', 'yep', 'yea']


class Config:
    temp_file: str = './temp.tmp' # May change to /tmp/ though unable to test if that'll shit itself on Windows.


parser = argparse.ArgumentParser()
parser.add_argument("file", type=str, help="Input file")
parser.add_argument("-o", "--output", type=str, help="Output file")
parser.add_argument("-c", "--overwrite", action="store_true", help="Confirm overwrite")
parser.add_argument("--no_temp", action="store_true",
                    help="Do not store temp save")
args = parser.parse_args()

if os.path.exists(Config.temp_file):
    if input(f"Temp save ({Config.temp_file}) found. Would you like to load this instead? ").lower() in Generic.Confirmation:
        inputfile = Config.temp_file
    else:
        inputfile = args.file
else:
    inputfile = args.file

print(inputfile)
