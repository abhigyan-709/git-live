def word_frequency(f):
    sword= f.lower().split()
    freq = {}
    for word in sword:
        word = word.strip(".,!?()[]{}:;\"'")
        freq[word] = freq.get(word, 0) + 1
    return freq
text = input("Enter a string: ")
freq_dict = word_frequency(text)
for word, count in freq_dict.items():
    print(f"{word}: {count}")
