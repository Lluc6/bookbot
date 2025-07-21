import string
import sys

#Declare empy dict. to start
charano = {}

#Finds the resource book, pushes the contents into variable f, reads f into a string, splits the string
# into a list (words) and prints them to the console.

def wordcount():
    file_path = sys.argv[1]
    with open(file_path, encoding="utf-8") as f:
        text = f.read()
        words = text.split()
        print (f"Found {(len(words))} total words")
        
#Turns the list of words into a string with no spaces (e.g. fgreagfvavfesavrsargb) and converts all
# to lowercase
#Establishes 

def num_chara():
    #file_path = "books/frankenstein.txt"
    file_path = sys.argv[1]
    with open(file_path, encoding="utf-8") as f:
        text = f.read()
        words = text.split()
        wordstring = "".join(words)
        lowerstring = wordstring.lower()
    
#Counts the number of times a letter (x) appears in the string, then adds the letter to the dictionary IF 
#it matches a letter in the alphabet and only THEN if it actually occurs in the string - adding a count to that key
# each time

    valid_letters = string.ascii_lowercase
    for x in lowerstring:
        if x in valid_letters:
            if x in charano:
                charano[x] += 1
            else:
                charano[x] = 1

#Break dictionary into list of dictionaries:

def sorted_dict():

    def sort_on(list):
            return (list["number"])
     
    letter_num = []
    for c in charano:
        letter_num.append({"chara":f"{c}:", "number": charano[c]})
       
        
# sort dictionaries by number - descending.
    letter_num.sort(reverse=True, key=sort_on)
    for i in range (len(letter_num)): 
        print (letter_num[i]["chara"],letter_num[i]["number"])



    


    


