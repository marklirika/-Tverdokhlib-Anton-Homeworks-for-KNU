import re

all_vowels = 'аоуиеієяюї'

# use regex to delete all vowels from word if word has at least one consonant and is longer then 2 symbols
def del_vowels_if(word):
    if re.search('[^%s]' % re.escape(all_vowels), word) and len(word) > 2:
        return del_vowels(word)
    else:
        return word


def del_vowels(word):
    return re.sub('[%s]' % re.escape(all_vowels), '', word)


file_path = 'text.txt'
formatted_file_path = file_path.replace('.txt', '_formatted.txt')

with open(file_path, 'r') as f:
    with open(formatted_file_path, 'w') as f_formatted:
        for line in f:
            f_formatted.write(' '.join([del_vowels_if(word) for word in line.split(' ')]) + '')