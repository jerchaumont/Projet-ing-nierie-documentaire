# Documentary engineering project
Our project consists of transforming a play from plain text to html format, by using XML and a XSLT stylesheet. We chose _L'amour et la raison_ by [Pigault-Lebrun](https://fr.wikipedia.org/wiki/Pigault-Lebrun). The plain text of the play can be foud on the [Project Gutenger](https://www.gutenberg.org/ebooks/26810).


## Development Context
This project was developed by [Chloé Luthier](https://github.com/cluthier), [Laure Torello](https://github.com/ltorello) and [Jeremy Chaumont](https://github.com/jerchaumont) as part of the _Ingénierie documentaire_ course, taught by Michael Piotrowski and Moritz Feichtinger (Master in Digital Humanities, University of Lausanne) - Fall 2021.

# Project stages
1. Clean up the text by removing metadata
2. Find regular expressions to select stage names, characters,
stage directions and lines.
3. Create an XML tree structure
4. Create an XSLT stylesheet

## Clean up text by removing metadata
The plain text contained introductory metadata that were not used for our project,
so we removed them manually.

## Regular expressions
- Regex for scenes: `r'(SCENE [A-Z]{2,8}\.)'`
- Regex for characters: `r'([A-Z]{6,8})'`
- Regex for stage directions: `r'([A-Z]{6,8})'`
- Regex for lines: _work in progress_

## Create the XML file
In order to create the XML file with a python script, we use the `inputFile` and the `ElementTree` modules. Here is an snippet from our code which illustrates the methods used:
```python
tree = ET.ElementTree(element = ET.Element('document'))
root = tree.getroot()

play = ET.Element('play')
root.append(play)

for line in fileinput.input(files=inputFile):
        m = re.match(r'(SCENE [A-Z]{2,8}\.)', line)
        if m:
            scene = ET.SubElement(play, 'scene', attrib = {'n': m.group()})
            scene.text = m.group()
```  

## Create the XSLT stylesheet
_Not done yet_

