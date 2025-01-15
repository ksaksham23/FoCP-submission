"""
Write and test three functions that each take two words (strings) as parameters and
return sorted lists (as defined above) representing respectively:
Letters that appear in at least one of the two words.
Letters that appear in both words.
Letters that appear in either word, but not in both.
"""

def combine_words(word1, word2):
    letters1 = [x for x in word1]
    letters2 = [y for y in word2]

    comb = letters1 + letters2

    return letters1, letters2, comb

def atleast_one(word1, word2):
    letters1, letters2, comb = combine_words(word1, word2)

    for let in comb:
        if let in letters1 or let in letters2:
            print(let)

def appear_both(word1, word2):
    letters1, letters2, comb = combine_words(word1, word2)

    for let in comb:
        if let in letters1 and let in letters2:
            print(let)

def either_word(word1, word2):  
    letters1, letters2, comb = combine_words(word1, word2)

    for let in comb:
        if not let in letters1 and let in letters2:
            print(let)

appear_both('sakama', 'kshao')