def search4vowels(word:str) -> set:
    vowels = set('aeiou')
    return vowels.intersection(set(word))
def search4letters(word:str, letters:str='aeiou') -> set:
    return set(letters).intersection(set(word))