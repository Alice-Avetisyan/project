books = {'Harry Potter', 'I, Robot', '451 Fahrenheit'}
print("Enter a number of books you would like to input: ")
num = int(input())
print("Please, enter the name of the book: ")
for book in range(num):
    book_in = input()
    books.add(book_in)
print(books)
