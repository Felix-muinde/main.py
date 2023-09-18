import string

def word_frequency(sentence):
    words = sentence.split()
    word_count = {}

    for word in words:
        # Remove punctuation and convert to lowercase
        cleaned_word = word.strip(string.punctuation).lower()
        
        if cleaned_word:
            if cleaned_word in word_count:
                word_count[cleaned_word] += 1
            else:
                word_count[cleaned_word] = 1

    return word_count

sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)
