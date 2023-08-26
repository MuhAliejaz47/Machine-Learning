from textblob import TextBlob

with open('positive_text.txt', 'r') as f:
    text = f.read()
blob = TextBlob(text)
sentiment = blob.sentiment.polarity # -1 to 1
print(f'The score of the positive text is: {sentiment}')


with open('negative_text.txt', 'r') as f:
    text = f.read()
blob2 = TextBlob(text)
sentiment2 = blob2.sentiment.polarity # -1 to 1
print(f'The score of the negative text is: {sentiment2}')



with open('neutral_text.txt', 'r') as f:
    text = f.read()
blob3 = TextBlob(text)
sentiment3 = blob3.sentiment.polarity # -1 to 1
print(f'The score of the neutral text is: {sentiment3}')
