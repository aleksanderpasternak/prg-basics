###
# String manipulation
#

movie = "The Lord of the Rings: The Return of the King"

# display number of characters
print('Number of characters: ', len(movie))

# display title in capital letters
print('TITLE: ', (movie.upper()))

# display title in small letters
print('title: ', (movie.lower()))

# display how many times the vowel "e" appears in the title
print('"e" amount: ', (movie.count("e")))

# display where in the text is the word "Lord"
print('"Lord" position: ', (movie.find("Lord")))

# display where in the text is the word "dragon"
print('"Dragon" position: ', (movie.find("dragon")))