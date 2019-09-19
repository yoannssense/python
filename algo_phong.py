from array import *

# Phong sorting
#
#
# Examples:
# bike -> ebik
# airport   -> apirot
# where > eherw


def phongSort(str):
    vowels, consonents = get_sorted_vowels_consonents(str)
    result = get_alternated_vowels_consonents(str, vowels, consonents)
    return ''.join(result)


def get_alternated_vowels_consonents(str, vowels, consonents):
    result = array('c', [])
    i = 0
    while (len(result) < len(str)):
        try:
            result.append(vowels[i])
        except Exception:
            print('No vowel anymore')

        try:
            result.append(consonents[i])
        except Exception:
            print('No consonent anymore')
        i = i + 1

    return result


def get_sorted_vowels_consonents(str):
    vowels = array('c', [])
    consonents = array('c', [])
    for letter in str:
        if is_vowel(letter):
            vowels.append(letter)
        else:
            consonents.append(letter)

    vowels = sort_alphanumerically(vowels)
    consonents = sort_alphanumerically(consonents)

    return vowels, consonents


def is_vowel(letter):
    vowel = ['a', 'e', 'i', 'o', 'u']
    if letter in vowel:
        return True
    return False


def sort_alphanumerically(str):
    return sorted(str)
    # result = array('c', [])
    # result.fromstring(str)
    # i = 0
    # while (i < len(result)-1):
    #     if (result[i] > result[i+1]):
    #         tmp = result[i]
    #         result[i] = result[i+1]
    #         result[i+1] = tmp
    #     i = i + 1

    # return result


print(phongSort('bike'))
print(phongSort('airport'))
print(phongSort('where'))
