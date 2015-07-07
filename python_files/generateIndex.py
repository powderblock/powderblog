import glob
import re
import os

htmlFiles = sorted(glob.glob("../content/posts/html/*.html"), key=os.path.getctime)

index = open("../index.html", "w+")

with open("../content/default_content/header.html", 'r') as content_file:
    header = content_file.read()

index.write(header)
index.write("\n")

with open("../content/default_content/footer.html", 'r') as content_file:
    footer = content_file.read()

for i in range(len(htmlFiles)):
    with open(htmlFiles[i], 'r') as content_file:
        pageContents = content_file.read()
    title = re.findall(r'<!-- title: +.*?-->', pageContents)[0].replace("<!-- title:", "").replace("-->", "")
    date = re.findall(r'<!-- date: +.*?-->', pageContents)[0].replace("<!-- date:", "").replace("-->", "")
    author = re.findall(r'<!-- author: +.*?-->', pageContents)[0].replace("<!-- author:", "").replace("-->", "")
    index.write('       <h2><a href ="powderblog/' + htmlFiles[i] + '">' + title + "</a><h2>")
    index.write('\n       <div id = "postInfo">Posted by: ' + author + ' on ' + date + '</div>')
    

index.write("\n")
index.write(footer)
index.close()
