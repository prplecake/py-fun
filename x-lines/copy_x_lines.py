# copy_x_lines.py
# 2016-02-15
# https://github.com/mattjorgs/x-lines
#
# Author:	Matthew Jorgensen
# Contact:	mattjorgs@gmail.com
# Version:	1.0
# Latest Revision:	2016-02-19
#
# This script copies x-number of lines from a file and copies them to a new
# file with a timestamp appended. If it's a dotfile, the leading dot is
# stripped.
#
# To do:
# * Better naming with files with extensions (see issue #5)

import os
import argparse
import datetime

# initialize the argument parser
parser = argparse.ArgumentParser()
parser.add_argument("filename", help="the file to be copied from")
parser.add_argument(
    "lines", type=int,
    help="the number of lines to copy from the beginning of the file")
parser.add_argument(
    "-d", "--debug", action="store_true",
    help="enables some (sparse) debugging features")
args = parser.parse_args()

if args.debug:
    debug = True
else:
    debug = False


# remove leading dot from dotfiles:
def RemoveLeadingDot(filename):
    head, tail = os.path.split(filename)
    if tail[:1] == ".":
        return os.path.join(head, tail[1:])
    return filename


if debug is True:
    print("Leading dot test: %s" % RemoveLeadingDot(args.filename))


# append timestamp to filename
def StampTime(filename, fmt='{fname}_%Y-%m-%d-%H-%M-%S{fext}'):
    # disect filename
    head, tail = os.path.split(filename)
    # disect tail ("test.txt" -> "text", ".txt")
    name, extension = os.path.splitext(tail)
    sansExt = os.path.join(head, name)
    return datetime.datetime.now().strftime(fmt).format(
        fname=sansExt, fext=extension)


datedFilename = StampTime(RemoveLeadingDot(args.filename))

if debug is True:
    print("datedFilename: %s" % datedFilename)


def GetNumLines(filename):
    with open(filename) as target:
        num_lines = sum(1 for line in target)
    return num_lines


if debug is True:
    print("Number of lines in file: %d" % GetNumLines(args.filename))


def CheckLines(linesWanted, linesInFile):
    if linesWanted <= linesInFile:
        pass
    elif linesWanted > linesInFile:
        print("You're asking for too many lines.")
        print("The file only has %d lines." % linesInFile)
        exit()


def CopyFile(readFile, writeFile, lines):
    with open(writeFile, "w") as wtarget:
        with open(readFile, "r") as rtarget:
            i = 0
            while i <= lines + 1:
                wtarget.write(rtarget.readline(i))
                i += 1


if __name__ == '__main__':
    if debug is True:
        pass
    else:
        CheckLines(args.lines, GetNumLines(args.filename))
        CopyFile(args.filename, datedFilename, args.lines)
