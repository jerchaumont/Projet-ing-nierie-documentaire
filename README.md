# Documentary engineering project
Our project consists of transforming a play from plain text to html format by using XML and a XSLT stylesheet, with the help of a python script. We chose the play _L'amour et la raison_ by [Pigault-Lebrun](https://fr.wikipedia.org/wiki/Pigault-Lebrun). The plain text of the play can be found on the [Project Gutenberg](https://www.gutenberg.org/ebooks/26810).


## Development Context
This project was developed by [Chloé Luthier](https://github.com/cluthier), [Laure Torello](https://github.com/ltorello) and [Jeremy Chaumont](https://github.com/jerchaumont) as part of the _Ingénierie documentaire_ course, taught by Michael Piotrowski and Moritz Feichtinger (Master in Digital Humanities, University of Lausanne) - Fall 2021.

---

# Project stages
1. Clean up the text by removing metadata
2. Find regular expressions to select stage names, characters,
stage directions and lines.
3. Create an XML tree structure
4. Create an XSL stylesheet

## Clean up text by removing metadata
The plain text contained introductory metadata that were not used for our project,
so we removed them manually.

## Regular expressions
- Regex for scenes: `r'(SCENE [A-Z]{2,8}\.)'`
- Regex for characters: `r'([A-Z]{6,8})'`
- Regex for stage directions: `r'(\((.+)\))|(\,(.+))'`
- Regex for lines: `r'(.+)'`

## Automate work with the python script
Firstly we generate a new text file without line breaks, which will subsequently facilitate our markup of the text in the XML file.
### Create the XML file
In order to create the XML file with a python script, we use the `inputFile` and the `ElementTree` modules. Here is an snippet from our code which illustrates the methods used:
```python
tree = ET.ElementTree(element = ET.Element('document'))
root = tree.getroot()

play = ET.Element('play')
root.append(play)

#for line in fileinput.input(files=inputFile): ######pour mac
with open (inputFile, 'r', encoding="utf-8") as xml_file: ######pour windows
    for line in xml_file:
        #scene match
        a = re.match(r'(SCENE [A-Z]{2,8}\.)', line)
        if a:
            scene = ET.SubElement(play, 'scene', attrib = {'n': a.group()})
            scene.text = a.group()
            #countScene+=1
```  
Then, the rest of the code follows the same logic. It generates a XML file, to which we just have to add a XSL stylesheet.  

### Create the XSL stylesheet
In our XSL stylesheet, we use the current stylesheet `<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">`. Then we have to associate the different elements with our XML tree. 

Finally, the expected result can be displayed with the html file.

