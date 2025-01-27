def main():
    bookPath = "books/frankenstein.txt"
    text = getBookText(bookPath)
    print(countWords(text))



def countWords(bookString):
    bookList = bookString.split()
    return len(bookList)



def getBookText(path):
    with open(path) as f:
        return f.read()







main()    
