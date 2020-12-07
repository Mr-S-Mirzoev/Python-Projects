import numpy as np
import re, scipy.spatial

def tokenise(line: str) -> list:
    lst = re.split('[^a-z]', line)
    lst = list(filter(lambda x: x != "", lst))
    return lst

def vector_of_occurancies(words: list, line: list) -> np.array:
    vector = np.zeros(len(words))

    for index, word in enumerate(words):
        vector[index] = line.count(word)

    return vector


with open("sentences.txt", "r") as f:
    lines = f.readlines()
    lines = [line.lower().strip() for line in lines]

    tokenised_lines = [tokenise(line) for line in lines]
    
    set_of_words = set([item for line in tokenised_lines for item in line])
    words_enumerated = list(set_of_words)

    matrix_by_word = np.array([vector_of_occurancies(words_enumerated, line) for line in tokenised_lines])
    
    cosine_min = scipy.spatial.distance.cosine(matrix_by_word[0], matrix_by_word[1])
    cosine_2_min = scipy.spatial.distance.cosine(matrix_by_word[0], matrix_by_word[2])
    idx_min = 1
    idx_2_min = 2

    if cosine_2_min < cosine_min:
        swap_val, swap_idx = cosine_min, idx_min
        cosine_min, idx_min = cosine_2_min, idx_2_min
        cosine_2_min, idx_2_min = swap_val, swap_idx

    for index in range(3, matrix_by_word.shape[0]):
        cur_cosine = scipy.spatial.distance.cosine(matrix_by_word[0], matrix_by_word[index])

        if cur_cosine < cosine_2_min:
            if cur_cosine < cosine_min:
                cosine_2_min, idx_2_min = cosine_min, idx_min
                cosine_min, idx_min = cur_cosine, index
            else:
                cosine_2_min, idx_2_min = cur_cosine, index

    print(idx_min, idx_2_min)