import os

dest = "commonFiles.txt"

def fileSponge( dirs ):
    createCommonDir()
    findCommon(dirs[0], dirs[1])
    extractCommon(dest)
   
def createCommonDir():
    os.system('mkdir common')

def findCommon( dirA, dirB ):
    diff = "diff --brief -Nrs %s %s" % (dirA, dirB)
    grep = "egrep '^Files .+ and .+ are identical$'"
    awk = "awk -F '(Files | and | are identical)' '{print $2}'"
    command = "%s | %s | %s >> %s" % (diff, grep, awk, dest)

    os.system(command)

def extractCommon(commonFileList):
    destPath =  "common"
    exclusions = ".\w"
    os.chdir('..')
    basePath = os.getcwd()
    os.chdir('FileSponge')

    command = "rsync -arv --exclude=%s --files-from=%s %s %s" % (exclusions, commonFileList, basePath, destPath)

    os.system(command)

