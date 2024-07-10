with open('sample.txt', 'r') as file:
    data = file.read().lower()

words_to_count = ["example", "all", "word", "up", "did", "him"]
word_count = {word: data.count(word) for word in words_to_count}
for word, count in word_count.items():
    print(f'{word}: {count}')
