import pandas

npa = pandas.read_csv("nato_phonetic_alphabet.csv")

npa_dict = {row.letter:row.code for (index, row) in npa.iterrows()}


def generate_phonetic():
    word = input("Please type in a word:").upper()
    output_lst = []
    try:
        output_lst = [npa_dict[letter] for letter in word]
    except KeyError:
        print("Please type in a word without any numbers or special characters. ")
        generate_phonetic()
    else:
        print(output_lst)


generate_phonetic()


