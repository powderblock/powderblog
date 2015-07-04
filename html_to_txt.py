import glob

htmlFiles = glob.glob("content/posts/*.html")

for i in range(len(htmlFiles)):
    print htmlFiles[i].split(".html")[0]
