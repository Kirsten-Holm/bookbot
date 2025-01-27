def main():
    bookPath = "books/frankenstein.txt"
    text = getBookText(bookPath)
    wordCount = countWords(text)
    charCount = getCharacterCounts(text)
    print(charCount)



def countWords(bookString):
    bookList = bookString.split()
    return len(bookList)



def getBookText(path):
    with open(path) as f:
        return f.read()

def getCharacterCounts(BookString):
    BookString = BookString.lower()
    charDict = {}
    for char in BookString:
        if char not in charDict:
            charDict[char] = 1
        else:
            charDict[char] +=1
    return charDict





main()    
