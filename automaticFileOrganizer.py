# os -> used for interacting with operating system 
# shutil -> used for high level file operations
import shutil, os

# absolute path 
path = r"paste-your-'absolute-path'-here"

# list of all items in given directory
fileNames = os.listdir(path)

# iterating to only perform the operation on files and not directories 
for file in fileNames:
    if os.path.isdir(os.path.join(path, file)):
        continue # will skip the iteration if it's a directory

    # fetching file extensions (excluding '.') to give name to folder
    fileExtension = file.split('.')[-1]
    folderName = f"{fileExtension} files"
    folderPath = os.path.join(path, folderName)

    # folder will be created if it doesn't already exist
    if not os.path.exists(folderPath):
        os.makedirs(folderPath)
    sourceFile = os.path.join(path, file) # actual path
    destinationFile = os.path.join(folderPath, file) # path to where file needs to be moves

    # checking whether file already exists in destination folder or not 
    if not os.path.exists(destinationFile):
        shutil.move(sourceFile, destinationFile)
    else:
        print(f"File {file} was not moved because it already exists in destination folder")

print(f"Operation completed successfully")



