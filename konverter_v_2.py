# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 09:29:13 2023

@author: pawel
"""

import functions_ai_konverter as aif



string = "CC(=O)C" 
new_format = [["Atom",["Hyb","Rin","Amound"]]]
add_hydrogen = True
for index, atom in enumerate(string):
    parameters = []
    if atom in ["C","N","O","c"]:
          rings = []
          index_f = index+1
          index_b = index-1
          #moves index_forwards if hits rings forwards
          if index_f < len(string) and string[index_f].isnumeric():
              index_f, rings= aif.check_if_ring_f(index_f, string, rings)
          #Moves index_backwards if hits ring backawards
          if index_b >0 and string[index_b].isnumeric():
              index_b = aif.check_if_ring_b(index_b, string)
        

          if atom in ["C"]:
              #assumes 4 hydrogens
              H_atoms = 4
              #assumes sp3 hybridization
              bond_level = 0
              #removes hydrogen due to rings
              H_atoms-=len(rings)
              #check for branches in order to calculate carbons and hybridization
              if index_f < len(string) and string[index_f] in ["(", "="]:
                  num_of_branches, lv_of_branches = aif.check_parantices_f(string[index_f::])     
                  bond_level += lv_of_branches
                  H_atoms -= (lv_of_branches+num_of_branches)
              
              if index_b > 0 and string[index_b] in [")"]:
                    num_of_branches, lv_of_branches = aif.check_parantices_b(string[::-1])     
                    H_atoms -= lv_of_branches
                    bond_level += lv_of_branches
                    
              
              #check for bonds in rings for hybridization
              if index_f < len(string) and string[index_f] in ["="]:
                  bond_level+=1
                  if string[index_f+1].isnumeric():
                      i, rings = aif.check_if_ring_f(index_f+1, string, rings)
                    
                 
              if index_b > 0 and string[index_b]=="=":
                  bond_level+=1
                 
              # check for bonds for hybridization
              if index_f < len(string) and string[index_f]=="#":
                  bond_level+=2
                 
              if index_b > 0 and string[index_b]=="#":
                  bond_level+=2
                  
                  
              # if index_f < len(string) and string[index_f]=="(":
              #     if index_f+1 < len(string) and string[index_f+1]=="=":
              #         bond_level+=1
              #     if index_f+1 < len(string) and string[index_f+1]=="#":
              #         bond_level+=2
                 
              
             #check for atoms and bonds after atoms in order to calculate hydrogens
              if index_f < len(string) and string[index_f] in ["C","N","O","=","#","(",")"]:
                  
                  if string[index_f] in ["C","N","O","("]:
                    H_atoms-=1
                  if string[index_f] in ["="]:
                    H_atoms-=2
                  if string[index_f] in ["#"]:
                    H_atoms-=3
                  
                    
                    
              # check for atoms befere atom in order to calculate hydrogens
              if index_b >= 0 and string[index_b] in ["C","N","O","=","#","(",")"]:
                  if string[index_b] in ["C","N","O","(",")"]:
                    H_atoms-=1
                  if string[index_b] in ["="]:
                    H_atoms-=2
                  if string[index_b] in ["#"]:
                    H_atoms-=3

          if atom  in ["O", "S"]:
             
             H_atoms = 2
             bond_level = 0
             H_atoms-=len(rings)
             
             
             if index_b > 0 and string[index_b] in ["C","N","O", "(","="]:
                 if string[index_b] in ["H","C","N","O"]:
                     H_atoms-=1

                 
                 if string[index_b] in ["="]:
                     H_atoms-=2
                     bond_level+=1
                     
                     
             if index_f < len(string) and string[index_f] in ["H","C","N","O"]:

                 H_atoms-=1
             
        

          #add 0 if no rings for consistancy
          if len(rings) == 0:
             rings = [0]
        
             
           #create array of parameters    
          parameters.append(bond_level+1)
          parameters.append(rings)
          parameters.append(1)
          new_format.append([atom, parameters])
          if H_atoms != 0 and add_hydrogen == True:   
              new_format.append(["H",[1,[0],H_atoms]]) 
               
          

             
 
             
         
            
          if atom in ["N","P"]:
             pass
         
            
        
             
             
for data in new_format:
    print(data)
                 
             