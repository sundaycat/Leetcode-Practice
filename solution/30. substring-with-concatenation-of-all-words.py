def find_word_concatenation(str, words):

    if len(words) == 0 or len(words[0]) == 0:
        return []

    rs, word_freq = [], {}
    for word in words:
        if word not in word_freq:
            word_freq[word] = 0
        word_freq[word] += 1
    
    num_of_words, word_len = len(words), len(words[0])
    for i in range(len(str) - word_len * num_of_words + 1):

        word_seen, j = {}, 0
        while j < num_of_words:

            start, end = i + j * word_len, i + (j + 1) * word_len
            word = str[start : end]

            # break if we dont need this word
            if word not in word_freq:
                break
            
            if word not in word_seen:
                word_seen[word] = 0
            word_seen[word] += 1

            # no need to proceed further if the word has higher frequency than required
            if word_seen[word] > word_freq[word]:
                break

            if j == num_of_words - 1:
                rs.append(i)

            j +=1

    return rs        