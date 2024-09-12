import requests

URL_API = "http://127.0.0.1:8000/api/"

def get_books(url: str = URL_API):
    response = requests.get(url+'books')
    print(response.json())

def get_book(id: int):
    response = requests.get(URL_API+'books/'+str(id))
    print(response.json())

if __name__ == "__main__":
    get_books()
    get_book(1)