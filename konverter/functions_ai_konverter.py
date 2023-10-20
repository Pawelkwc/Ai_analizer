#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 11:04:48 2023

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
                    
            if atom == ")" and structure[index+1] != "(":
                break
            
            if atom == "=" and structure[index+1] != "(":
                break
            
            
            

            # if atom == ")" and count == 0:

            #     num_of_branches+=1
            #     count-=1
            #     if index+1 < len(structure) and structure[index+1] in ["="]:
            #         lv_of_branches+=1
            #     if index+1 < len(structure) and structure[index+1] in ["#"]:
            #         lv_of_branches+=2
                
                    
                
                

        return num_of_branches, lv_of_branches
        
def check_parantices_b(structure):
        count = 0
        num_of_branches = 0
        lv_of_branches = 0
        for index, atom in enumerate(structure):
            
            if atom == "(" and count != 0:
                    count -=1
            if atom == ")" and count != 0:
                    count +=1
            if atom == ")" and count == 0:
                num_of_branches+=1
                count+=1

        
                
        
        return num_of_branches, lv_of_branches


def check_atoms_b(index_b, string, items_to_check, atoms_to_check_b, H_atoms, bond_level):
    if index_b >= 0 and string[index_b] in items_to_check:
                  if string[index_b] in atoms_to_check_b:
                    H_atoms-=1
                  if string[index_b] in ["="]:
                    H_atoms-=2
                    bond_level+=1
                  if string[index_b] in ["#"]:
                    H_atoms-=3
                    bond_level+=1

    return H_atoms, bond_level

def check_atoms_f(index_f, string, items_to_check, atoms_to_check_f, H_atoms, bond_level):
    if index_f < len(string) and string[index_f] in items_to_check:
                  if string[index_f] in atoms_to_check_f:
                    H_atoms-=1
                  if string[index_f] in ["="]:
                    H_atoms-=2
                    bond_level+=1
                  if string[index_f] in ["#"]:
                    H_atoms-=3
                    bond_level+=1

    return H_atoms, bond_level