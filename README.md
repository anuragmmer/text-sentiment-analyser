

# Sentiment Analysis and Data Visualization on a Text file

This Python code performs sentiment analysis and data visualization on a text file using several libraries:

- **NLTK**: Natural Language Toolkit, used for text processing tasks such as tokenization and part-of-speech tagging.
- **TextBlob**: Python library built on top of NLTK, used for sentiment analysis and other natural language processing tasks.
- **Tkinter**: Python's standard GUI toolkit, used for creating a file dialog to select the input text file.
- **Pandas**: Data manipulation library, used for creating and manipulating data frames.
- **Plotly**: Data visualization library, used for creating interactive bar charts.

## How to Run the Code

To run this code, you'll need to follow these steps:

1. Install the required libraries by running these commands in your command prompt or terminal:
```
pip install nltk
pip install textblob
pip install pandas
pip install plotly
```

2. Open a new Python file and copy/paste the code or download the file.

3. Run the code in your Python environment such as Anaconda IDLE, Windows command prompt or PowerShell terminal.

When you run the code, a file dialog will open asking you to select a text file. Once you've selected a file, the code will perform sentiment analysis on the file's text and display three bar charts using Plotly. The first bar chart displays the top 10 most frequent adjectives and adverbs, the second bar chart displays the top 10 most frequent noun phrases and lemmatized words, and the third bar chart displays the sentiment polarity and subjectivity of the text.

## How to read the graph

Sentiment polarity and sentiment subjectivity are two key aspects of sentiment analysis that help describe and quantify the emotional content of a piece of text.

1. **Sentiment Polarity:**
   - **Definition:** Sentiment polarity measures the degree of positivity or negativity expressed in a piece of text.
   - **Scale:** It is typically represented on a numerical scale, where values range from -1 to 1.
     - A score of -1 indicates extremely negative sentiment.
     - A score of 0 represents neutral sentiment.
     - A score of 1 signifies extremely positive sentiment.
   - **Example:** In the sentence "I love this product," the sentiment polarity would be close to 1, indicating a highly positive sentiment.

2. **Sentiment Subjectivity:**
   - **Definition:** Sentiment subjectivity measures the degree to which a piece of text is subjective or objective.
   - **Scale:** It is often represented on a numerical scale, typically ranging from 0 to 1.
     - A score of 0 indicates complete objectivity, meaning the text is purely factual and lacks any personal opinion or emotion.
     - A score of 1 suggests high subjectivity, indicating that the text is more opinionated and includes personal feelings or experiences.
   - **Example:** In the sentence "I feel that this movie is amazing," the sentiment subjectivity would be higher than in a more objective statement like "The movie is two hours long."

In the context of TextBlob, the sentiment analysis function provides both sentiment polarity and sentiment subjectivity scores for a given piece of text. These scores can be useful for understanding the overall sentiment conveyed in a document, review, or social media post.
