# Spam Mail Classifier

This is a simple Python project that checks if a message is **spam** or **not spam (ham)**.  
It uses `scikit-learn` with Naive Bayes for classification.

---

## How it works
1. Some sample messages are used for training.  
2. The text is converted into numbers using **CountVectorizer**.  
3. A **Naive Bayes model** is trained.  
4. You can enter your own message, and the program will tell if it’s spam or not.  

---

## Requirements
- Python 3  
- scikit-learn  

Install scikit-learn with:
```bash
pip install scikit-learn
