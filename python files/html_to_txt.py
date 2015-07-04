import glob

htmlFiles = glob.glob("content/posts/*.html")

for i in range(len(htmlFiles)):
    text_file = open("posts.txt", "w")
    text_file.write(htmlFiles[i].split(".html")[0])
    text_file.close()
