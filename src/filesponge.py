#!/usr/bin/env python
import subprocess, os, sys, argparse

parser = argparse.ArgumentParser()
parser.add_argument("directory", help="First target directory for evaluation")
parser.add_argument("directories", nargs='+', help="All other directories to be evaluated")
parser.add_argument("-o", "--output", help="Output destination. If none specified, defaults to STDOUT")

args = parser.parse_args()

def fileSponge(dirs, outputDir):
    commonList = findIdentical(dirs).rstrip()
    outputCommon(commonList, outputDir)

def findIdentical(dirs):
    prev = None

    for index in dirs:
        if prev is None:
            prev = index
        else:
            diff = "diff --brief -Nrs %s %s" % (prev, index)
            egrepPattern = "^Files .+ and .+ are identical$"
            awkPattern = "(Files | and | are identical)"

            diffProcess = subprocess.Popen(diff.split(), stdout=subprocess.PIPE)
            egrepProcess = subprocess.Popen(["egrep", egrepPattern], stdout=subprocess.PIPE, stdin=diffProcess.stdout)
            awkProcess = subprocess.Popen(["awk", "-F", awkPattern, "{print($2, \"==\", $3)}"], stdout=subprocess.PIPE, stdin=egrepProcess.stdout)
            (out, err) = awkProcess.communicate()

            return out

def outputCommon(commonList, outputDir):
    if outputDir is not None:
        options = "-av"
        exclusions = "--exclude='*'"
        srcPath = "./"
        destPath = "%s/" % (outputDir)
        targetFiles = isolateTargetFiles(commonList)
        inclusions = "--files-from=./commonFiles.txt"#generateRsyncInclusionString(targetFiles)

        writeInclusionListToDisk(targetFiles)

        rsync = "rsync %s %s %s %s" % (options, inclusions, srcPath, destPath)
        print rsync

        rsyncProcess = subprocess.call(rsync.split())
    else:
        print("Identical files:\n%s" % (commonList))

def isolateTargetFiles(commonList):
    targetFiles = []

    for line in commonList.split('\n'):
        targetFiles.append(line.split()[0])

    return targetFiles

def generateRsyncInclusionString(targetFiles):
    inclusions = ''
    for item in targetFiles:
        inclusions += " --include='./%s'" % (item)

    return inclusions

def writeInclusionListToDisk(targetFiles):
    outfile = open('commonFiles.txt', 'w')
    for item in targetFiles:
        outfile.write("%s\n" % item)

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