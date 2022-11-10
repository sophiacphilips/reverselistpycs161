#Author: Sophia Philips
#GitHub Username: sophiacphilips
#Date: 11/09/22
#This program is designed to take a list of numbers and mutate them into the reverse order without slicing.

def reverse_list(vals):
    """this function will reverse the order of the given list by working from each half of the length of the list and swapping each number"""
    size_of_list=len(vals) #determines how many elements are in the list
    half_of_list=int(size_of_list/2) #halves the amount of elements
    for i in range(int(half_of_list)): #iteration of half of the list
        first_half=vals[i]
        vals[i]=vals[size_of_list-i-1]
        vals[size_of_list-i-1]=first_half
#testing
#vals= [7, -3, 12, 9]
#reverse_list(vals)
#print(vals)
