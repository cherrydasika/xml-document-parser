#XML Document Inversion

import xml.etree.cElementTree as ET 
import xml.dom.minidom as minidom
filename = 'C:\\Users\\siva.dasika\\Documents\\Test\\test3.xml'
newfilename = 'C:\\Users\\siva.dasika\\Documents\\Test\\new.xml'
mytree = ET.parse(filename)
myroot = mytree.getroot()

new_node_arr = []

#Get all tags in the xml document
all_tags = [elem.tag for elem in myroot.iter() ]

#Reverse the tags
all_tags.reverse()

#Create a new root element
newroot = ET.Element(all_tags[0])
new_node_arr.append(newroot)

for i in range(len(all_tags)):
    if i!=0:    
        new_node = ET.SubElement(new_node_arr[i-1],all_tags[i]) 
        new_node_arr.append(new_node) 

newtree = ET.ElementTree(newroot)

#Write the modified structure to a new file
newtree.write(newfilename)

#Print the new xml structure
xml = minidom.parse(newfilename)
xml_pretty_str = xml.toprettyxml()
print(xml_pretty_str)



