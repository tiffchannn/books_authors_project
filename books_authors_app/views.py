from django.shortcuts import render, redirect, HttpResponse
from .models import Book, Author

# Create your views here.
def index(request):
  context = {
    'all_books': Book.objects.all(),
    'all_authors': Author.objects.all()
  }
  print('*'*70)
  print('This is from index!')
  return render(request, 'index.html', context)

def author(request):
  context = {
    'all_authors': Author.objects.all()
  }
  print('*'*70)
  print('This is from author!')
  return render(request, 'authors.html', context)


def addBook(request):
  if request.method == 'POST':
    form_title = request.POST['title']
    form_desc = request.POST['desc']

    Book.objects.create(title=form_title, desc=form_desc)

  print('*'*70)
  print('New Book Added: ', request.POST)
  return redirect('/')


def addAuthor(request):
  if request.method == 'POST':
    form_firstName = request.POST['first_name']
    form_lastName = request.POST['last_name']
    form_notes = request.POST['notes']

    Author.objects.create(first_name=form_firstName, last_name=form_lastName, notes=form_notes)

  print('*'*70)
  print('New Author Added: ', request.POST)
  return redirect('/')

def addAuthorToBook(request):
  if request.method == 'POST':
    print('*'*70)
    print('POST Request: ', request.POST)
    # print('Author ID from Form ', request.POST['author_id'])

    addedAuthor = request.POST['author_id']
    book_id = request.POST['book_id']
    Book.objects.get(id=book_id).authors.add(addedAuthor)

    # print("This Book's Authors: ". this_book.authors.all())

  return redirect(f"/books/{book_id}")

def addBookToAuthor(request):
  if request.method == 'POST':
    print('*'*70)
    print('POST Method:', request.POST)

    addedBook = request.POST['book_id']
    author_id = request.POST['author_id']
    Author.objects.get(id=author_id).books.add(addedBook)

    # all_authors_books = Author.objects.get(id=author_id).books.all()
    # print("This Book's Authors: ", all_authors_books)

  return redirect(f"/authors/{author_id}")

def displayBook(request, book_id):
  print('in the display author function ------ ')
  print('*'*70)

  context = {
    'this_book': Book.objects.get(id=book_id),
    'all_authors': Author.objects.all(),
    'book_authors': Book.objects.get(id=book_id).authors.all() # will show specific authors
  }
  return render(request, 'showBook.html', context)

def displayAuthor(request, author_id):
  print('in the display author function ------')
  print('*'*70)
  # print("author id:", author_id)

  context = {
    'all_books': Book.objects.all(),
    'this_author': Author.objects.get(id=author_id),
    'all_authors': Author.objects.all(),
    'authors_books': Author.objects.get(id=author_id).books.all() # will show specific books by this author
  }
  # print('this_author', context.this_author)
  return render(request, 'showAuthor.html', context)

