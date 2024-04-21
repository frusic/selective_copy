# Intention
Copying the current state of a folder into to a separate location with an old version of the folder can be easily performed by first deleting the destination folder and performing a clean copy.

This unnecessarily increases the time to copy if only several files have changed in a large folder. Manually copying and deleting files to match the current state of the folder is tedious, hence this code that recursively compares the origin and destination folders, copying new files and folders, replacing existing files if the metadata has changed, and deleting files that no longer exist in the origin.

Technically having change management such as git also solves this, however people wouldn't want to set up new repositories just to copy some music files to a mobile device.