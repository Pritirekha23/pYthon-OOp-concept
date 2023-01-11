# dt-09/01/2023 (10.57)
# Add and display BOOK using OOP

class Books:
    def __init__(self):
        self.name=''
        self.author=''
        self.price=0.0
        self.isbn=''

    def inputBOOKdetails(self):
        self.name=input('Enter Book name::')
        self.author=input('Enter author name::')
        self.price=float(input('Enter Book price::'))
        self.isbn=input('Enter Book isbn number::') 
        print(f'{self.name} Book added successfully')
        print('-'*30)

    def Bookdisplay(self):
        print('----printbookdetails-----')
        print(f'Book name : {self.name}')
        print(f'Author name : {self.author}')
        print(f'Book Price : {self.price}')
        print(f'Book ISBN : {self.isbn}')
        print('-'*30)


Book_list = []

while True:
    choice = int(input('Enter your choice\n 1.Add Book\n 2.Display Book\n 3.stop\n'))

    if choice == 1:
        b = Books()
        b.inputBOOKdetails()
        Book_list.append(b)

    elif choice == 2:
        if len(Book_list)==0:
            print('Book is not available')
        else:
          for i in Book_list:
             i.Bookdisplay()

    elif choice == 3:
        print("Thanks for using this application")
        break

    else:
        print('Invalid choice')


print(Book_list)

