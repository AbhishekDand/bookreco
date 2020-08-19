# bookreco
Recommending books to user based on the summary of the book.
db.sqlite3 is the database of 20 books. It has Book title, ISBN, summary, langauge etc details of the book.
We use content based recommendation system where we use the summary and then performing data cleaning and feature extraction of text using Tfid Vectorizer.
We then build a cosine similarity matrix using tfidvectorizer and then we give recommendation based of the cosine similarity score.
I have built a flask web app around this recommendation system.
 ## Running your code
 - If you want to run this program then change the database address in the bookreco.py file.
 - Run train(df2) to train the model
 - Run app.py and go to local host
 - type in book name present in the database
 - on the result page you will get the predictions.
 
