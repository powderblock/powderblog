import glob
import sys
from md_to_HTML import *

# All the markdown files in the directory:
filesInDir = glob.glob("*.md")

# The args given after the file:
fileNameGiven = sys.argv[1]

if fileNameGiven == "-all":
    for i in range(len(fileNameGiven)):
            print fileNameGiven[i]

else:
    # If if the given filename is not found:
    if fileNameGiven not in filesInDir:
        # Show the user an error:
        print("File not found in directory. (Did you name as a .md?)")
    # If the filename is given:
    elif fileNameGiven in filesInDir:
        # Turn it from markdown into HTML using in the md_to_HTML module:
        markdown_to_HTML(fileNameGiven)
        
