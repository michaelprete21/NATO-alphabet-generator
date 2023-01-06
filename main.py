import pandas

npa = pandas.read_csv("nato_phonetic_alphabet.csv")

npa_dict = {row.letter:row.code for (index, row) in npa.iterrows()}

word = input("Please type in a word:").upper()
output_lst = []
output_lst = [npa_dict[letter] for letter in word]

print(output_lst)
