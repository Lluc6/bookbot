import sys
if (len(sys.argv)) < 2:
    print ("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
    

def main():
    from stats import wordcount
    from stats import num_chara
    from stats import sorted_dict
    wordcount()
    num_chara()
    sorted_dict()

main ()



