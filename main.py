from stats import *
import sys
def main():
    if(len(sys.argv) != 2 ):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path = sys.argv[1]
    text = get_book_text(path)
    count = word_Count(text)

    print(f" Found {count} total words")
    dictFinal = count_Char(text)
    dictFinal = sorted_by(dictFinal)
    
    for d in dictFinal:
        print(f"{d["char"]}: {d["num"]}") 
main()
    

