# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 09:29:13 2023

@author: pawel
"""

def check_if_ring_b(index, structure):
    if structure[index].isnumeric() and index >0:
        index -=1
        check_if_ring_b(index, structure)
        
    return index
    
def check_if_ring_f(index, structure, rings):
    if structure[index].isnumeric() and index < len(string)-1 :
        
        rings.append(int(structure[index]))
        index +=1
        index, rings = check_if_ring_f(index, structure, rings)

    return index, rings
        
        
        




string = "C1CCCCC1"
new_format = [["Atom",["Hyb","Rin","Hyd"]]]

for index, atom in enumerate(string):
    parameters = []
    if atom in ["C","N","O","c"]:
         rings = []
         index_f = index+1
         index_b = index-1
         print(rings)
         if index_f < len(string) and string[index_f].isnumeric():
             index_f, rings= check_if_ring_f(index_f, string, rings)
         print(rings)   
         if index_b >0 and string[index_b].isnumeric():
             index_b = check_if_ring_b(index_b, string)
        
         if len(rings) == 0:
            rings = [0,0,0,0]
         if atom == "C":
             bond_level = 0
             if index_f < len(string) and string[index_f]=="=":
                 bond_level+=1
                 
             if index_b > 0 and string[index_b]=="=":
                 bond_level+=1
                 
             if index_f < len(string) and string[index_f]=="#":
                 bond_level+=2
                 
             if index_b > 0 and string[index_b]=="#":
                 bond_level+=2
                 
             H_atoms = 4
             
             if index_f < len(string) and string[index_f] in ["C","N","O","=","#"]:
                 if string[index_f].isnumeric():
                     index+=1
                     
                 if string[index_f] in ["C","N","O"]:
                    H_atoms-=1
                 if string[index_f] in ["="]:
                    H_atoms-=2
                 if string[index_f] in ["#"]:
                    H_atoms-=3
                 
             if index_b >= 0 and string[index_b] in ["C","N","O","=","#"]:
                 if string[index_b] in ["C","N","O"]:
                    H_atoms-=1
                 if string[index_b] in ["="]:
                    H_atoms-=2
                 if string[index_b] in ["#"]:
                    H_atoms-=3
                 
            
             
            
             
                 
             parameters.append(bond_level+1)
             parameters.append(rings)
             parameters.append(1)
             new_format.append([atom, parameters])
             if H_atoms != 0:   
                 new_format.append(["H",[1,[0,0,0,0],H_atoms]]) 

for data in new_format:
    print(data)
                 
             