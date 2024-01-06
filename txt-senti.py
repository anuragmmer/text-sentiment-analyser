import nltk
from textblob import TextBlob
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import plotly.express as px
import re
from nltk.corpus import stopwords
import pandas as pd

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('brown')
nltk.download('stopwords')

def preprocess_text(text):
    text = re.sub(r'[^\w\s]', '', text)  
    text = text.lower()  
    return text

root = Tk()
root.withdraw()
filename = askopenfilename(title="Select a file", filetypes=[("Text files", "*.txt")])

with open(filename, 'r') as f:
    comments = f.read()
    comments = preprocess_text(comments)
    blob = TextBlob(comments)
stop_words = set(stopwords.words('english'))
adj_list = [w for w, t in blob.tags if t in ['JJ', 'JJR', 'JJS', 'RB', 'RBR', 'RBS'] and w not in stop_words]
adj_freq = nltk.FreqDist(adj_list)
adj_top = adj_freq.most_common(10)
adj_top_df = pd.DataFrame(adj_top, columns=['word', 'frequency'])
np_lem = blob.noun_phrases + [w.lemmatize() for w in blob.words]
np_lem_freq = nltk.FreqDist(np_lem)
np_lem_top = np_lem_freq.most_common(10)
np_lem_top_df = pd.DataFrame(np_lem_top, columns=['word', 'frequency'])

sentiment_polarity, sentiment_subjectivity = blob.sentiment.polarity, blob.sentiment.subjectivity
sentiment_df = pd.DataFrame({'sentiment': ['Sentiment Polarity', 'Sentiment Subjectivity'],
                             'value': [sentiment_polarity, sentiment_subjectivity]})

fig1 = px.bar(data_frame=adj_top_df, x='word', y='frequency', title='Top 10 Adjectives and Adverbs',
              labels={'x': 'Words', 'y': 'Frequency'}, color_discrete_sequence=['#636EFA'], hover_data=['word'],
              text='frequency')

fig2 = px.bar(data_frame=np_lem_top_df, x='word', y='frequency', title='Top 10 Noun Phrases and Lemmatized Words',
              labels={'x': 'Words', 'y': 'Frequency'}, color_discrete_sequence=['#EF553B'], hover_data=['word'],
              text='frequency')

fig3 = px.bar(data_frame=sentiment_df, x='sentiment', y='value', title='Sentiment Analysis',
              labels={'x': 'Sentiment', 'y': 'Value'}, color_discrete_sequence=['#00CC96', '#636EFA'],
              hover_data=['value'])

fig1.show()
fig2.show()
fig3.show()
