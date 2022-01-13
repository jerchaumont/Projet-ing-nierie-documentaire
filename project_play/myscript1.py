#-----------------------------------------------
#IMPORT MODULES 
#-----------------------------------------------
import os
#import module for regex
import re
#import module for XML
import xml.etree.ElementTree as ET
#import XMLpython 
import fileinput

text = open('piece.txt', 'r')
text = text.read()
text_sans_retour = text.replace('\n', " ")
text_sans_retour2 = text_sans_retour.replace('   ','\n')
text_sans_retour3 = text_sans_retour2.replace('  ','\n')
a = open('new_file.txt', 'w')
a.write(text_sans_retour3)
a.close()
#print(text_sans_retour2[:20])

inputFile = 'new_file.txt'



#-----------------------------------------------
#CLEAN THE TEXT
#-----------------------------------------------

""""
regex to use :
transcript = re.sub(r'(SCENE [A-Z]{2,8}\.)', r'<scene>\1</scene>', transcript)
transcript = re.sub (r'([A-Z]{6,8})', r'<personnage>\1</personnage>', transcript)
transcript = re.sub (r'</personnage>,(.+)\.', r'</personnage><didascalie>\1</didascalie>', transcript)
transcript = re.sub (r'(\((.+)\))', r'<didascalie>\1</didascalie>', transcript)
transcript = re.sub (r'_', '', transcript)
transcript = re.sub (r'_\.', '', transcript)
transcript = re.sub (r'>\.', '', transcript)
transcript = re.sub (r'\n', '', transcript)
transcript = re.sub (r'</personnage>', r'<replique></personnage>', transcript)
transcript = re.sub (r'<personnage>', r'</replique><personnage>', transcript)
"""




#-----------------------------------------------
#XML FILE
#-----------------------------------------------
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

        #personnage match
        b = re.match(r'([A-Z]{6,8})', line)
        if b:
            personnage = ET.SubElement(scene, 'personnage')
            personnage.text = b.group()
            #countPersonnage+=1
        c = re.match(r'(AUGUSTE)', line)
        if c:
            personnage = ET.SubElement(scene, 'personnage')
            personnage.text = c.group()
            # countPersonnage+=1
        

        #didascalie match
        d1 = re.match(r'(\((.+)\))', line)
        d2 = re.match(r'[A-Z]+,(.+)', line)
        #d1 = re.match(r'(((A-Z)\,)/)(.+)\.)', line)
        if d1:
            d = re.sub(r'\((.+)\)', r'\1', line)
            didascalie = ET.SubElement(scene, 'didascalie')
            didascalie.text = d
            #countDidascalie+=1
        elif d2:
            d = re.sub(r'[A-Z]+, (.+)', r'\1', line)
            didascalie = ET.SubElement(scene, 'didascalie')
            didascalie.text = d
            
        #text
        e = re.match(r'(.+)', line)
        if e and not a and not b and not c and not d1 and not d2:
            replique = ET.SubElement(scene, 'replique')
            replique.text = e.group()


with open ('xmlfile2.xml', 'wb') as myxml:
    tree.write(myxml, encoding='utf-8', xml_declaration=True)
