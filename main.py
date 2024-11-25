def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        file_words_length = len(words)
        characters_count = count_character(file_contents)
        
        sorted_characters_count = dict(sorted(characters_count.items(), key=lambda item: item[1], reverse=True))
        report(file_words_length, sorted_characters_count)

def count_character(file_contents):
    alphabet = {
        'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0,
        'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0,
        't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0
    }
    
    for char in file_contents.lower():
        if char in alphabet:
            alphabet[char] += 1;
    
    return alphabet;
    
def report(file_words_length, characters_count):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{file_words_length} words found in the document")
    
    for character in characters_count:
        print(f"The '{character}' was found {characters_count[character]} times")
    
main();
    
