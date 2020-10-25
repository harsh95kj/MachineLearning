import pandas as pd;
import matplotlib.pyplot as plt;
from wordcloud import WordCloud, STOPWORDS;
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def sentiment_scores(sentence):
    sobj = SentimentIntensityAnalyzer()
    sentDict = sobj.polarity_scores(sentence)
    print(sentence)
    print('Positive', sentDict['pos']*100)
    print('Negative', sentDict['neg'] * 100)
    print('Neutral', sentDict['neu']*100)
    if sentDict['compound'] >= 0.05:
        print('Overall Sentence is Positive')
    elif sentDict['compound']<=-0.05:
        print('Overall Sentence is Negative')
    else:
        print('Overall Sentence is Neutral')

def build_wordcloud(df, title):
    wordcloud = WordCloud(
        background_color='white',
        stopwords=set(STOPWORDS),
        max_words=50,
        max_font_size=40,
        random_state=666
    ).generate(str(df))

    fig = plt.figure(1, figsize=(15, 15), facecolor=None)
    plt.axis('off')
    fig.suptitle(title, fontsize=16)
    fig.subplots_adjust(top=1)

    plt.imshow(wordcloud)
    plt.show()


data = pd.read_csv(r'C:\Users\harsh\Downloads\india-news-headlines.csv')
data['publish_date'] = pd.to_datetime(data['publish_date'].astype(str), format='%Y%m%d')
print(data.info())
count = pd.DataFrame()
count['columns'] = data.columns
count['value'] = [data[col].isnull().sum() for col in data.columns]
print(count)
data['category counts'] = data['headline_category'].apply(lambda x: len(x.split('.')))
data.loc[data['headline_category'] == 'unknown', 'category counts'] = 0
data['categCount'] = data['category counts'].astype(str) + ' category'
abc = pd.DataFrame()
abc = data.groupby(['publish_date']).count()
print(abc)
#build_wordcloud(data['headline_text'], 'title')

for i in range(50):
    s=data['headline_text']
    sentiment_scores(s[i])
