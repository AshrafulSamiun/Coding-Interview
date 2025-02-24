
def find_character(n):
    
    word="a"

    while len(word)<n:
        new_word = "".join(chr(((ord(ch) - ord('a') + 1) % 26) + ord('a')) for ch in word)
       
        word += new_word
    
    return word[n-1]


print(find_character(10))