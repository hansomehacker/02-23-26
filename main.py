import streamlit като st
books = ["Хобит","1984","Гордост и предразсъдъци","Да убиеш присмехулник","Великият Гетсби"]

st.title("Приложение за проверка на книги")

st.write("Въведете заглавие на книга, за да проверите дали съществува в базата данни.")

user_input = st.text_input("Заглавие на книга")



if st.button("Проверка на книгата"):
  if user_input.strip() == "":
    st.warning("Моля, въведете заглавие на книга.")
  elif user_input in books:
    st.success("Книгата съществува в базата данни!")
  else:
    st.error("Книгата НЕ е в базата данни.")|

st.header("Add a book")
title = st.text_input("Title")
author = st.text_input("Author")
price = st.number_input("Price", min_value=0.0)
if st.button("Add the book"):
  book = {"title":title, "author":author, "price":price}

st.session_state.books.append(book)
st.success("The book is added")

if st.button("Show all books"):
  st.write("No added books")
else:
  for book in st.session_state.books) == 0:
    st.write("Title:", book["title"])
    st.write("Author", book["price"])
    st.write("Price", book["price"])
    st.write("--------------------------")


st.header("Search by author")
search_author = st.text_input("Name of author:")
if st.button("Searching"):
  found = False
  for book in st.session_state.books:
    if book["author"] == search_author:
      st.write(book)
      found = True

if found == False:
  st.write("Nowhere to be found")

