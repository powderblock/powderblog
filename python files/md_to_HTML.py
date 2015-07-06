# Used for string.replace()
import string
import sys
import re

def markdown_to_HTML(filename):
    print filename
    # Take input from the user:
    with open(filename, 'r') as content_file:
        md = content_file.read()

    # Have we found bold or italic characters yet?
    bold = False
    italics = False
    # No. That's why these are false.

    #Header code:
    allHeaders = re.findall(r'\#+ .*?\n', md, re.M)
    for i in range(0, len(allHeaders)):
        title = allHeaders[i].replace("# ", "").replace("#", "")
        if "###### " in allHeaders[i]:
            md = md.replace(allHeaders[i],"<H6>" + title + "</H6>")

        elif "##### " in allHeaders[i]:
            md = md.replace(allHeaders[i],"<H5>" + title + "</H5>")

        elif "#### " in allHeaders[i - 1]:
            md = md.replace(allHeaders[i],"<H4>" + title + "</H4>")

        elif "### " in allHeaders[i]:
            md = md.replace(allHeaders[i],"<H3>" + title + "</H3>")

        elif "## " in allHeaders[i]:
            md = md.replace(allHeaders[i],"<H2>" + title + "</H2>")

        elif "# " in allHeaders[i]:
            md = md.replace(allHeaders[i],"<H1>" + title + "</H1>")

    whole = re.findall(r'\[.*?\)', md)
    for i in range(0, len(whole)):
        whole = str(re.findall(r'\[.*?\)', md)[i - 1])

        link = str(re.findall(r'\(.*?\)', whole)[i - 1].replace("(", "").replace(")", ""))

        title = str(re.findall(r'\[.*?\]', whole)[i - 1].replace("[", "").replace("]", ""))

        md = md.replace(whole, "<a href = " + '"' + link + '">' + title + "</a>")

    # Replace some characters so the string is easier to work with:
    md = string.replace(md, "***", "*_")
    md = string.replace(md, "**", "_")
    md = string.replace(md, "__", "_")
    
    # Change the user input into a list:
    html = list(md)
    for letter in  range(len(html)):
        if html[letter] == "\n":
            html[letter] = "\n <br>"
        # Bold code:
        elif html[letter] == "_" and bold == False:
            html[letter] = "<strong>"
            # Awesome! We found a bold character! Switch that baby to true!
            bold = True

        elif html[letter] == "_" and bold == True:
            html[letter] = "</strong>"
            # That's all, folks!
            bold = False

        # Italics code:
        elif html[letter] == "*" and italics == False:
            html[letter] = "<em>"
            # Italic character found, sweet! Make sure our bool knows it.
            italics = True

        elif html[letter] == "*" and italics == True:
            # If the user did ***, switch current order so it ends </strong> </em>
            if html[letter + 1] == "_":
                html[letter] = "</strong>"
                html[letter + 1] = "</em>"
            else:
                html[letter] = "</em>"
            # No more italics for you, that's a shame. (End of it found.)
            italics = False

    # Rejoin the input back into a string from a list:
    html = "".join(html)

    #Save the file to the "html" directory:
    filename = filename.replace("md\\", "html/").replace(".md", "")
    print filename
    text_file = open(filename + ".html", "w+")
    text_file.write(html)
    text_file.close()