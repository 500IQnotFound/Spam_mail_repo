
# Spam Mail Classifier

# Importing required libraries

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

#Training Data

texts = [
    "Win money now",
    "Hello friend how are you",
    "Free lottery prize claim",
    "Let’s meet for lunch",
    "Congratulations you won a car",
    "Get a free mobile recharge",
    "Are you joining the class today?",
    "Lowest price guaranteed, click here",
    "Can we play cricket tomorrow?",
    "Exclusive offer just for you",
    "Good morning, have a nice day",
    "Claim your free ticket now",
    "Shall we work on the project?",
    "You are selected for a lucky draw",
    "Don’t forget to submit your homework"
]

labels = [
    "spam", "ham", "spam", "ham", "spam",
    "spam", "ham", "spam", "ham", "spam",
    "ham", "spam", "ham", "spam", "ham"
]

#Convert Text → Numbers

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

#Train Model

model = MultinomialNB()
model.fit(X, labels)

#User Input

print("----- Spam Mail Classifier -----")
user_message = input("Enter a message to check if it's spam or not: ")
X_user = vectorizer.transform([user_message])
user_pred = model.predict(X_user)
print(user_message, "->", user_pred[0])
