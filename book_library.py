my_library=[]
first_book=input("enter the name of a book you own ")
second_book=input("enter the nam of another book you own or press enter to skip ")
if second_book:
  my_library.append(first_book)
  my_library.append(second_book)
else:
  first_book.append(first_book)
print("your library are")
print(my_library)
wishlist=[]
wish_book=input("enter the name of book you wish to have in the future")
dream_book=input("enter the name another book you wish to have or press enter to skip")
if deram_book
 wishlist.append(wish_book)
 wishlist.append(dream_book)
else:
 wishlist.append(wish_book)
print("your wish list")
print(wishlist)
acquired_wishbook=input("enter name of a book from your wish list that you have get it or press enter to skip ")
if acquired_wishbook in wishlist
 my_library.append(acquired_wishbook)
 wish_list.remove(acquired_wishbook)
print(f"updet my library{my_library}")
print(f"updet my wish list{wishlist}")
donate_book=input("enter the name of book from your library you wish donat or press enter to skip")
if donate_book in my_library:
  my_library.remove(donate_book)
  print("final library after donation")
  print(my_library)
