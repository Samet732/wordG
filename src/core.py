import numpy as np

def readFile(path):
    file = open(path, 'r')
    lines = np.array(file.readlines())
    file.close()

    return lines

def readWords(path):
    if not path: raise Exception("Input path mustn't be empty.")
    words = readFile(path)
    if np.size(words) < 2: raise Exception("Number of words mustn't be smaller than 2.")

    return words

def writeWordlist(path, wordlist):
    if not path: raise Exception("Output path mustn't be empty.")
    file = open(path, 'w')

    for i in range(np.size(wordlist)):
        file.write(str(wordlist[i]) + '\n')
    file.close()

def readWordlistForExtending(path):
    if not path: return np.array([], dtype=str)
    else:
        wordlist = readFile(path)
        if not np.size(wordlist): raise Exception("Number of words must be more than 0 (external wordlist).")
        return wordlist

def elementary_generator(words, func):
    arr = np.array([], dtype=str)
    for i in range(np.size(words)):
        arr = np.append(arr, func(words[i]))
    
    return arr

def basic_generator(words):
    arr = np.array([""])
    for i in range(np.size(words)):
        temp = words[i]
        temp_arr = np.delete(words, i)

        for j in range(np.size(temp_arr)):
            # if new generated value not in arr, returns new arr. Else returns arr.
            get_val = lambda a : np.append(arr, a) if not max(np.isin(arr, a)) else arr

            arr = get_val(temp + temp_arr[j])
            arr = get_val(temp_arr[j] + temp)
            arr = get_val(temp + temp_arr[j] + temp)
            arr = get_val(temp_arr[j] + temp + temp_arr[j])
    
    return np.delete(arr, 0)