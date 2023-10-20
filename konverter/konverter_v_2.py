# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 09:29:13 2023

@author: pawel
"""

import functions_ai_konverter as aif



string = "CC(=O)OC(=O)C" 
string = "C1=C2C(=CC(=C1Cl)Cl)OC3=CC(=C(C=C3O2)Cl)Cl"
# string = 'C1=CC=C2C=CC=CC2=C1'
# new_format = [["Atom",["Hyb","Rin","Amound"]]]
new_format = [["Atom",["Hyb","Rin","H:Num"]]]
add_hydrogen = False

items_to_check = ["C","N","O","I","=","#","(",")"]
atoms_to_check_f = [atom for atom in items_to_check if atom not in [")","=","#"]]
atoms_to_check_b = [atom for atom in items_to_check if atom not in ["=","#"]]


for index, atom in enumerate(string):
    parameters = []
    if atom in ["C","N","O","c", "B"]:

          rings = []
          index_f = index+1
          index_b = index-1
          #moves index_forwards if hits rings forwards
          if index_f < len(string) and string[index_f].isnumeric():
              index_f, rings= aif.check_if_ring_f(index_f, string, rings)
          #Moves index_backwards if hits ring backawards
          if index_b >0 and string[index_b].isnumeric():
              index_b = aif.check_if_ring_b(index_b, string)
        

          if atom in ["C"] and (not (index_f < len(string) and string[index_f].islower()) or index_f == len(string)):
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
              
              if index_b >= 0 and string[index_b] in [")"]:
                    num_of_branches, lv_of_branches = aif.check_parantices_b(string[::-1])     
                    H_atoms -= lv_of_branches
                    bond_level += lv_of_branches
                    
              
              #check for bonds in rings for hybridization
              if index_f < len(string) and string[index_f] in ["="]:
                   bond_level+=1
                   if string[index_f+1].isnumeric():
                       i, rings = aif.check_if_ring_f(index_f+1, string, rings)
                    
                 
              H_atoms, bond_level = aif.check_atoms_b(index_b, string, items_to_check, atoms_to_check_b, H_atoms, bond_level)
             
              H_atoms, bond_level = aif.check_atoms_f(index_f, string, items_to_check, atoms_to_check_f, H_atoms, bond_level)
              
              if len(rings) == 0:
                  rings = [0]
                  

              new_format.append([atom,f"H:{H_atoms}", rings])
              
          if atom  in ["O", "S"]:
             
             H_atoms = 2
             bond_level = 0
             H_atoms-=len(rings)

             H_atoms, bond_level = aif.check_atoms_b(index_b, string, items_to_check, atoms_to_check_b, H_atoms, bond_level)
 
             H_atoms, bond_level = aif.check_atoms_f(index_f, string, items_to_check, atoms_to_check_f, H_atoms, bond_level)
             
             if len(rings) == 0:
                  rings = [0]
             new_format.append([atom,f"H:{H_atoms}"])
             
          if atom in ["N","P"]:
             H_atoms = 3
             bond_level = 0
             H_atoms-=len(rings)

             H_atoms, bond_level = aif.check_atoms_b(index_b, string, items_to_check, atoms_to_check_b, H_atoms, bond_level)
 
             H_atoms, bond_level = aif.check_atoms_f(index_f, string, items_to_check, atoms_to_check_f, H_atoms, bond_level)


             if len(rings) == 0:
                  rings = [0]
             new_format.append([atom,f"H:{H_atoms}"])
          if atom in ["I"]:
             H_atoms = 1
             bond_level = 0
             H_atoms-=len(rings)

             H_atoms, bond_level = aif.check_atoms_b(index_b, string, items_to_check, atoms_to_check_b, H_atoms, bond_level)
 
             H_atoms, bond_level = aif.check_atoms_f(index_f, string, items_to_check, atoms_to_check_f, H_atoms, bond_level)


             if len(rings) == 0:
                  rings = [0]
             new_format.append([atom,f"H:{H_atoms}"])            

         

          if atom in ["C"] and ((index_f < len(string) and string[index_f] in ["l"])):
             H_atoms = 1
             bond_level = 0
             H_atoms-=len(rings)

             H_atoms, bond_level = aif.check_atoms_b(index_b, string, items_to_check, atoms_to_check_b, H_atoms, bond_level)
 
             H_atoms, bond_level = aif.check_atoms_f(index_f, string, items_to_check, atoms_to_check_f, H_atoms, bond_level)

             if len(rings) == 0:
                  rings = [0]
             new_format.append([atom + string[index_f],f"H:{H_atoms}"])
             


            
          if atom in ["B"] and ((index_f < len(string) and string[index_f] in ["r"])):
             H_atoms = 1
             bond_level = 0
             H_atoms-=len(rings)

             H_atoms, bond_level = aif.check_atoms_b(index_b, string, items_to_check, atoms_to_check_b, H_atoms, bond_level)
 
             H_atoms, bond_level = aif.check_atoms_f(index_f, string, items_to_check, atoms_to_check_f, H_atoms, bond_level)

             if len(rings) == 0:
                  rings = [0]
             new_format.append([atom + string[index_f],f"H:{H_atoms}"])
            
             
            
           #create array of parameters    
          # parameters.append(bond_level+1)
          # parameters.append(rings)
          # parameters.append(1)
          # parameters.append(f"H:{H_atoms}")
          # new_format.append([atom, parameters])
          if H_atoms != 0 and add_hydrogen == True:   
              new_format.append(["H",[1,[0],H_atoms]])
              
          
            

        
             
             
for data in new_format:
    print(index[data], data)
                 
             