#Word Frequency Counter (Dictionaries and Loops)

def word_frequency_counter(text):
    text = text.lower()
    words = text.split()
    frequency = {}
    for word in words:
        word = word.strip('.,!?;"\'()[]{}')
        if word:
            if word in frequency:
                frequency[word] += 1
            else:
                frequency[word] = 1
    return frequency

sample_text = "Hello, world! Hello everyone. Welcome to the world of Python programming. Python is great, and the world loves Python."
word_freq = word_frequency_counter(sample_text)
for word, count in word_freq.items():
    print(f"{word}: {count}")