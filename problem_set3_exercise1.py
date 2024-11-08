!pip install nltk

import nltk
# download punkt required for word_tokenize
nltk.download('punkt')

from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

# create a variable text
text = "The art of storytelling has been a vital part of human culture for centuries. It allows people to share knowledge, preserve history, and build connections with others. Through stories, we can explore different perspectives, understand complex emotions, and experience lives beyond our own. Whether through books, films, or oral traditions, storytelling continues to evolve and captivate audiences around the world."

# tokenize the text into words
tokens = word_tokenize(text)

# print the list of tokens
print(tokens)

# count the number of tokens
num_tokens = len(tokens)

# print the number of tokens
print("Number of tokens:", num_tokens)

# create a frequency distribution of the tokens
freq_dist = FreqDist(tokens)
print(freq_dist)

# print the frequency of each token
for token, frequency in freq_dist.items():
    print(f"{token}: {frequency}")
