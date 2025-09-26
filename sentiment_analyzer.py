from textblob import TextBlob
import matplotlib.pyplot as plt

# Step 1: Take input text
text = input("Enter your sentence: ")

# Step 2: Create a TextBlob object
blob = TextBlob(text)

# Step 3: Get polarity (-1 = negative, 0 = neutral, +1 = positive)
sentiment_score = blob.sentiment.polarity

# Step 4: Decide sentiment label
if sentiment_score > 0:
    sentiment = "Positive"
elif sentiment_score < 0:
    sentiment = "Negative"
else:
    sentiment = "Neutral"

print(f"Sentiment: {sentiment} (Score: {sentiment_score})")

# Step 5: Visualization
labels = ['Negative', 'Neutral', 'Positive']
scores = [max(0, -sentiment_score), 1 - abs(sentiment_score), max(0, sentiment_score)]

plt.bar(labels, scores, color=['red', 'gray', 'green'])
plt.title("Sentiment Analysis Result")

# ✅ Save images before showing
plt.savefig("graph.png")   # full graph
plt.savefig("banner.png")  # banner (same graph, you can crop later if needed)

plt.show()  # show after saving
