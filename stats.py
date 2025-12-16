
def get_book_text(path):
    text = ""
    with open(path, "r", encoding="utf8") as f:
        text = f.read()
    
    return text   
      
def word_Count(text):
    words = text.split()
    return len(words)

def sort_on(d):
    return d["num"]

def sorted_by(dictionary):
    final_dict = []
    for k,value in dictionary.items():
        if k.isalpha():
            tmp = {"char":k,"num":value}
            final_dict.append(tmp)
    final_dict.sort(reverse=True, key=sort_on)
    return final_dict


def count_Char(string):
    
    dictFinal = {}
    
    for char in string:
        char = char.lower()
        if char in dictFinal:
            dictFinal[char] += 1
        else:
            dictFinal[char] = 1
    return dictFinal
