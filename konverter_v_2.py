# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 09:29:13 2023

@author: pawel
"""

def check_if_ring_b(index, structure):
    if index >0 and structure[index].isnumeric():
        index -=1
        check_if_ring_b(index, structure)
        
    return index
    
def check_if_ring_f(index, structure, rings):
    if index < len(structure) and structure[index].isnumeric():
        
        rings.append(int(structure[index]))
        index +=1
        index, rings = check_if_ring_f(index, structure, rings)

    return index, rings
        
def check_parantices_f(structure):
        count = 0
        num_of_branches = 0
        lv_of_branches = 0
        for index, atom in enumerate(structure):
            
            if atom == "(" and count != 0:
                    count +=1
            if atom == ")" and count != 0:
                    count -=1
            if atom == "(" and count == 0:
                num_of_branches+=1
                count+=1
                if index+1 < len(structure) and structure[index+1] in ["="]:
                    lv_of_branches+=1
                if index+1 < len(structure) and structure[index+1] in ["#"]:
                    lv_of_branches+=2
                
                    
                
                

        return num_of_branches, lv_of_branches
  

        
# def check_parantices_b(structure):
#         count = 0
#         num_of_branches = 0
#         for atom in structure[::-1]:
            
#             if atom == "(" and count != 0:
#                     count -=1
#             if atom == ")" and count != 0:
#                     count +=1
#             if atom == ")" and count == 0:
#                 num_of_branches+=1
#                 count+=1
#         return num_of_branches       





string = "C1CCCCC1" 
new_format = [["Atom",["Hyb","Rin","Amound"]]]

for index, atom in enumerate(string):
    parameters = []
    if atom in ["C","N","O","c"]:
          rings = []
          index_f = index+1
          index_b = index-1
          
          if index_f < len(string) and string[index_f].isnumeric():
              index_f, rings= check_if_ring_f(index_f, string, rings)

          if index_b >0 and string[index_b].isnumeric():
              index_b = check_if_ring_b(index_b, string)
        

          if atom == "C":
              H_atoms = 4
              bond_level = 0
              H_atoms-=len(rings)
              
              if index_f < len(string) and string[index_f] in ["("]:
                  num_of_branches, lv_of_branches = check_parantices_f(string[index_f::])     
                  bond_level += lv_of_branches
                  H_atoms -= (lv_of_branches+num_of_branches)
              
              
              
              if index_f < len(string) and string[index_f] in ["="]:
                  bond_level+=1
                  if string[index_f+1].isnumeric():
                      i, rings = check_if_ring_f(index_f+1, string, rings)
                    
                 
              if index_b > 0 and string[index_b]=="=":
                  bond_level+=1
                 
                 
              if index_f < len(string) and string[index_f]=="#":
                  bond_level+=2
                 
              if index_b > 0 and string[index_b]=="#":
                  bond_level+=2
                  
                  
              # if index_f < len(string) and string[index_f]=="(":
              #     if index_f+1 < len(string) and string[index_f+1]=="=":
              #         bond_level+=1
              #     if index_f+1 < len(string) and string[index_f+1]=="#":
              #         bond_level+=2
                 
              
             
              if index_f < len(string) and string[index_f] in ["C","N","O","=","#","(",")"]:
                  if string[index_f].isnumeric():
                      index_f+=1
                     
                  if string[index_f] in ["C","N","O","("]:
                    H_atoms-=1
                  if string[index_f] in ["="]:
                    H_atoms-=2
                  if string[index_f] in ["#"]:
                    H_atoms-=3
                  
                    
                    
                 
              if index_b >= 0 and string[index_b] in ["C","N","O","=","#","(",")"]:
                  if string[index_b] in ["C","N","O","(",")"]:
                    H_atoms-=1
                  if string[index_b] in ["="]:
                    H_atoms-=2
                  if string[index_b] in ["#"]:
                    H_atoms-=3

                 
                
              if len(rings) == 0:
                  rings = [0]
            
             
                 
              parameters.append(bond_level+1)
              parameters.append(rings)
              parameters.append(1)
              new_format.append([atom, parameters])
              if H_atoms != 0:   
                  new_format.append(["H",[1,[0],H_atoms]]) 

for data in new_format:
    print(data)
                 
             