def even(number):
    s = [0, 2, 4, 6, 8]
    number = str(number)
    l = int(number[len(number)-1])
    if l in s:
        return True
    else:
        return False

    
def sort(array):
    f = array[0]

    if isinstance(f, int) or isinstance(f, float):
        for i in range (0, len(array)):
            num = i
            while num != 0:
                if array[num] > array[num-1]:
                    break
                else:
                    n1 = array[num]
                    n2 = array[num-1]
                    array[num] = n2
                    array[num-1] = n1
                    num -= 1

    elif isinstance(f, str):
        for i in range (0, len(array)):
            num = i
            while num != 0:
                if last_word(array[num-1], array[num]) == array[num]:
                    break
                else:
                    w1 = array[num]
                    w2 = array[num-1]
                    array[num] = w2
                    array[num-1] = w1
                    num -= 1
    return array


def sort_by_length(array):
    for i in range (0, len(array)):
        num = i
        while num != 0:
            if last_word(array[num-1], array[num]) == array[num]:
                break
            else:
                w1 = array[num]
                w2 = array[num-1]
                array[num] = w2
                array[num-1] = w1
                num -= 1
                
    for i in range (0, len(array)):
        num = i
        while num != 0:
            if len(array[num]) >= len(array[num-1]):
                break
            else:
                v1 = array[num]
                v2 = array[num-1]
                array[num] = v2
                array[num-1] = v1
                num -= 1
    return array


def last_word(word1, word2):
    if word1 == word2:
        return word1
    
    lexicon = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    words = [word1, word2]

    for i in range (0, 2):
        word = words[i]
        numbers = []
        for letter in word:
            for j in range (0, len(lexicon)):
                if letter == lexicon[j]:
                    numbers.append(j+1)
                    break
        words[i] = numbers
    num = 0
    l1 = len(word1)
    l2 = len(word2)
    while True:
        if words[1][num] > words[0][num]:
            return word2
        elif words[0][num] > words[1][num]:
            return word1
        else:
            if num == l1-1:
                return word2
            if num == l2-1:
                return word1
            num += 1


def minimum(array):
    smallest_value = array[0]

    for value in array:
        if value < smallest_value:
            smallest_value = value
    return smallest_value


def maximum(array):
    biggest_value = array[0]

    for value in array:
        if value > biggest_value:
            biggest_value = value
    return biggest_value
