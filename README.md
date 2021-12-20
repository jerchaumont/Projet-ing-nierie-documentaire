# Projet ingénierie documentaire
Our project consists of transforming a play from plain text to html format, by using XML and a XSLT stylesheet. 

## Development Context
This project was developed by Chloé Luthier, Laure Torello and Jeremy Chaumont as part of the _Ingénierie documentaire_ course, taught by Michael Piotrowski and Moritz Feichtinger (Master in Digital Humanities, University of Lausanne) - Fall 2021.

# Project stages
1. Clean up text by removing metadata
2. Find regular expressions to select stage names, characters,
stage directions and lines.
3. Create an XML tree structure
4. Create an XSLT stylesheet

# Clean up text by removing metadata
The plain text contained introductory metadata that were not used for our project,
so we removed them manually.

# Regular expressions :
- Regex for scenes : `r'(SCENE [A-Z]{2,8}\.)'`
- Regex for characters : `r'([A-Z]{6,8})'`
- Regex for stage directions : `r'([A-Z]{6,8})'`
- Regex for lines : _work in progress_

