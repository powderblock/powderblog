import glob

htmlFiles = glob.glob("../content/posts/html/*.html")

print htmlFiles[0]

index = open("../index.html", "w+")

with open("../content/default_content/header.html", 'r') as content_file:
    header = content_file.read()

index.write(header)
index.write("\n")

with open("../content/default_content/footer.html", 'r') as content_file:
    footer = content_file.read()

for i in range(len(htmlFiles)):
    postTitle = htmlFiles[i].replace("../content/posts/html\\", "").replace(".html", "")
    index.write('       <h3><a href ="powderblog/' + htmlFiles[i] + '">' + postTitle + "</a><h3>")

index.write("\n")
index.write(footer)
index.close()
