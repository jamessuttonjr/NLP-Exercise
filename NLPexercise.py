from pathlib import Path
import pandas as pd
import imageio
from wordcloud import WordCloud
from operator import itemgetter
from textblob import TextBlob
import nltk
from nltk.corpus import stopwords
import matplotlib.pyplot as plt

nltk.download("stopwords")
stops = stopwords.words("english")
#print(stops)

more_stops = ["thy", "ye", "verily", "thee", "hath", "say", "thou", "art", "shall", "saith unto", "thou hast"]

stops += more_stops

#print(stops)

blob = TextBlob(Path("book of John text.txt").read_text())

words = blob.np_counts.items()

clean_words = [i for i in words if i[0] not in stops]

sorted_words = sorted(clean_words, key=itemgetter(1), reverse=True)

top15 = sorted_words[:15]
print(top15)

top15 = dict(top15)


wordcloud = WordCloud(colormap='Blues',background_color='Grey')

wordcloud = wordcloud.generate_from_frequencies(top15)

wordcloud = wordcloud.to_file("BookofJohn.png")

