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




