#TODO 1. Create a dictionary in this format:
import pandas

nato = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in nato.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter a word: ")
code_word = [nato_dict[letter] for letter in word.upper()]
# for letter in word.upper():
#     code_word.append(nato_dict[letter])
print(code_word)
