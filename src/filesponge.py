#!/usr/bin/env python
import subprocess, os, sys, argparse

parser = argparse.ArgumentParser()
parser.add_argument("directory", help="First target directory for evaluation")
parser.add_argument("directories", nargs='+', help="All other directories to be evaluated")
parser.add_argument("-o", "--output", help="Output destination. If none specified, defaults to STDOUT")

args = parser.parse_args()

def fileSponge(dirs, outputDir):
    commonList = findIdentical(dirs).rstrip()
    print "Files with identical contents:\n" + commonList
    outputCommon(commonList, outputDir)

def findIdentical(dirs):
    prev = None

    for index in dirs:
        print ("prev = %s, index = %s" % (prev, index))
        if prev is None:
            prev = index
        else:
            diff = "diff --brief -Nrs %s %s" % (prev, index)
            egrepPattern = "^Files .+ and .+ are identical$"
            awkPattern = "(Files | and | are identical)"

            diffProcess = subprocess.Popen(diff.split(), stdout=subprocess.PIPE)
            egrepProcess = subprocess.Popen(["egrep", egrepPattern], stdout=subprocess.PIPE, stdin=diffProcess.stdout)
            awkProcess = subprocess.Popen(["awk", "-F", awkPattern, "{print $2}"], stdout=subprocess.PIPE, stdin=egrepProcess.stdout)
            (out, err) = awkProcess.communicate()

            return out

def outputCommon(commonList, outputDir):
    if outputDir is not None:
        options = "-arvn"
        exclusions = "*"
        basePath = os.getcwd()

        # TODO: get rsync to copy files from commonList. Currently not getting files
        args = ["rsync", options, "--include", commonList, "--exclude", exclusions, basePath, outputDir]
        print args

        proc = subprocess.Popen(args, stdout=subprocess.PIPE)
        (out, err) = proc.communicate()

        return out
    else:
        print(commonList)

def usage():
    dirList = []
    outputDir = None

    if args.output:
        outputDir = args.output or None

    if args.directory:
        dirList = args.directory.split()
        if args.directories:
            dirList += args.directories
            fileSponge(dirList, outputDir)

usage()