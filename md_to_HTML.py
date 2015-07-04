# Used for string.replace()
import string
import sys
import re

def markdown_to_HTML(filename):
    # Take input from the user:
    with open(filename, 'r') as content_file:
        md = content_file.read()

    # Have we found bold or italic characters yet?
    bold = False
    italics = False
    # No. That's why these are false.

    whole = re.findall(r'\[.*?\)', md)
    for i in range(-1, len(whole) - 1):
        print i
        whole = str(re.findall(r'\[.*?\)', md)[i])
        print whole

        link = str(re.findall(r'\(.*?\)', whole)[i].replace("(", "").replace(")", ""))

        title = str(re.findall(r'\[.*?\]', whole)[i].replace("[", "").replace("]", ""))

        txt = ""
        md = md.replace(whole, "<a href = " + '"' + link + '">' + title + "</a>")
        print md

    # Replace some characters so the string is easier to work with:
    md = string.replace(md, "***", "*_")
    md = string.replace(md, "**", "_")
    md = string.replace(md, "__", "_")
    
    # Change the user input into a list:
    html = list(md)
    print html
    for letter in  range(len(html)):
    # Bold code:
            if html[letter] == "_" and bold == False:
                html[letter] = "<strong>"
                # Awesome! We found a bold character! Switch that baby to true!
                bold = True

            if html[letter] == "_" and bold == True:
                html[letter] = "</strong>"
                # That's all, folks!
                bold = False

    # Italics code:
            if html[letter] == "*" and italics == False:
                html[letter] = "<em>"
                # Italic character found, sweet! Make sure our bool knows it.
                italics = True

            if html[letter] == "*" and italics == True:
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

    text_file = open(filename.split(".")[0]+".html", "w")
    text_file.write(html)
    text_file.close()
