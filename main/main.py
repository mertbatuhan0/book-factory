import random 
import os 
import sys

class Book:
    def __init__(self,title,author):
        self.title = title;
        self.author = author


def GenerateBooks():
    books = [
        {"title":"The Little Prince", "author": "Antoine de Saint-Exupéry"},
        {"title":"Charlotte's Web","author":" E. B. White"}]
    
    choosen_book = random.choice(books)
    return Book(choosen_book["title"], 
                choosen_book["author"])


b1 = GenerateBooks()
print(f"book: {b1.title}, author: {b1.author}")



        






 