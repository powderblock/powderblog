import glob
import sys
# Local module:
from md_to_HTML import *
import os

# All the markdown files in the directory:
filesInDir = sorted(glob.glob("../content/posts/md/*.md"), key=os.path.getctime)

# The args given after the file:
fileNameGiven = sys.argv[1]

if fileNameGiven == "-all":
    for i in range(len(filesInDir)):
            markdown_to_HTML(filesInDir[i])

else:
    # Turn it from markdown into HTML using in the md_to_HTML module:
    markdown_to_HTML("../content/posts/md/" + fileNameGiven)
        
