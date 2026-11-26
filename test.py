# ------ Variablen -------------------------------------------------
in_word = "affen,, und\ ufos..."
search_words = []
search_words_clean = []
spezial_chars = '\.,-"\'!?'

# word input & processing
search_words = in_word.split()
for word in search_words:
    search_words_clean.append(word.strip(spezial_chars))

print(search_words_clean)