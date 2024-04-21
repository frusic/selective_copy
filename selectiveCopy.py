from os import listdir, stat, remove
from os.path import join, isfile
from shutil import copy2, copytree, rmtree
import sys

def recursiveCopy(inputOrigPath, inputDestPath):
    originFolder = listdir(inputOrigPath)
    destinationFolder = listdir(inputDestPath)
    for origFile in originFolder:
        if origFile not in destinationFolder:
            origPath = join(inputOrigPath, origFile)
            destPath = join(inputDestPath)
            if isfile(origPath):
                # print('copying file', origPath, destPath)
                copy2(origPath, destPath)
            else:
                destPathFolder = origPath.split('/')
                destPathFolder[0] = destPath
                destPathFolder = '/'.join(destPathFolder)
                # print('copying full folder', origPath, destPathFolder)
                copytree(origPath, destPathFolder, dirs_exist_ok=True)
        else:
            origPath = join(inputOrigPath, origFile)
            destPath = join(inputDestPath, origFile)
            if isfile(origPath):
                # compare metadata
                origModified = stat(origPath).st_mtime
                destModified = stat(destPath).st_mtime
                if (origModified != destModified):
                    # print('copying file, replace', origPath, destPath)
                    copy2(origPath, destPath)
                else:
                    # print('equal modified, skip')
                    pass
            else:
                # print('not a file, recursive copy', origPath, destPath)
                recursiveCopy(origPath, destPath)

def recursiveDelete(inputOrigPath, inputDestPath):
    originFolder = listdir(inputOrigPath)
    destinationFolder = listdir(inputDestPath)
    for destPath in destinationFolder:
        if destPath not in originFolder:
            destPath = join(inputDestPath, destPath)
            if isfile(destPath):
                # print('deleting path', destPath)
                remove(destPath)
            else:
                # print('deleting full folder', destPath)
                rmtree(destPath)
        else:
            origPath = join(inputOrigPath, destPath)
            destPath = join(inputDestPath, destPath)
            if isfile(origPath):
                # print('files exist in both, skip', inputOrigPath, destPath)
                pass
            else:
                # print('not a file, recursive delete', origPath, destPath)
                recursiveDelete(origPath, destPath)



if __name__ == "__main__":
    originPath = sys.argv[1]
    destinationPath = sys.argv[2]
    print('--- Starting with args:', originPath, destinationPath, '---')
    # look through all files in the original folder not in the destination
    # print('Performing recusive copy')
    recursiveCopy(originPath, destinationPath)
    # look through all files in destination not in original
    # print('Performing recursive delete')
    recursiveDelete(originPath, destinationPath)
    print('--- Complete ---')
