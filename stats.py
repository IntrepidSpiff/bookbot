def get_word_count(booktext):
    wordcount=len(booktext.split())
    return wordcount
    
def get_character_count(characters):
    character_dictionary={}
    lowercase = characters.lower()
    for i in lowercase:
        if i not in character_dictionary:
            character_dictionary[i]=1
        else:
#            count = character_dictionary[i]
            character_dictionary[i]+=1
    return character_dictionary

def sort_on(items):
    return items["num"]

def sort_character_count(character_count):
    sorted_characters = []
    character_dict={}
#    char_dict={}
    for i in character_count:
        character_dict={"char":i, "num":character_count[i]}
        sorted_characters.append(character_dict)
    sorted_characters.sort(reverse=True, key=sort_on)
    return sorted_characters
