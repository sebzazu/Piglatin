
import os

while True:
    vowels = ['a', 'e', 'i', 'o', 'u']

    words_to_translate = input('What Would You Like To Translate? ').lower()

    word_list = words_to_translate.split(' ')
    for word in word_list:

        if word[0] in vowels:
            vstart_translated_word = ''.join(word) + 'yay'
            print(vstart_translated_word)
        if word[0] not in vowels:
            indexa = word.find('a')
            indexe = word.find('e')
            indexi = word.find('i')
            indexo = word.find('o')
            indexu = word.find('u')

            vowel_index_list = [indexe, indexo, indexi, indexu, indexa]
            for vowel_index in vowel_index_list:
                if vowel_index < 0:
                    vowel_index_list.remove(vowel_index)

            first_vowel_index = min(vowel_index_list)

            letter_list = [*word]

            word_start = letter_list[first_vowel_index:len(letter_list) + 1]
            word_end = letter_list[0:first_vowel_index]


            cstart_translated_list = word_start + word_end
            cstart_translated_word = ''.join(cstart_translated_list) + 'ay'

            print(cstart_translated_word)

            os.system('say ' + cstart_translated_word)