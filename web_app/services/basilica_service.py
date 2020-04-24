import basilica
import os
from dotenv import load_dotenv

load_dotenv()

BASILICA_API_KEY = os.getenv("BASILICA_API_KEY")

connection = basilica.Connection(BASILICA_API_KEY)
print(type(connection))

embedding = connection.embed_sentence('hey this is a cool tweet', model='twitter')
print(embedding)

tweets = ["hello world", "artificail intelligence", "anther tweet here #cool"]
embeddings = connection.embed_sentences(tweets, model="twitter")
for embed in embeddings:
    print("----")
    print(len(embed))