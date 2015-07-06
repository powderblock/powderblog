import glob

htmlFiles = glob.glob("../content/posts/html/*.html")

print htmlFiles[0]

index = open("../index.html", "w")

with open("../content/default_content/header.html", 'r') as content_file:
    header = content_file.read()

index.write(header)
index.write("\n")

with open("../content/default_content/footer.html", 'r') as content_file:
    footer = content_file.read()

index.write('<div id = "links">')
for i in range(len(htmlFiles)):
    title = htmlFiles[i].replace("../content/posts/html\\", "").replace(".html", "")
    index.write('<a href ="powderblog/' + htmlFiles[i] + '">' + title + "</a>")
index.write("</div>")

index.write(footer)
index.close()
