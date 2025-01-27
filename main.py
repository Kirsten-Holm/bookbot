def main():
    bookPath = "books/frankenstein.txt"
    bookReport(bookPath)

    



def countWords(bookString):
    bookList = bookString.split()
    return len(bookList)

def getBookText(path):
    with open(path) as f:
        return f.read()
    
def sortOn(dict):
    return dict["count"]

def getListDict(dict):
    charDictList = []
    for char,count in dict.items():
        charDictList.append({"char": char, "count":count})
    return charDictList

def getCharacterCounts(BookString):
    BookString = BookString.lower()
    charDict = {}
    for char in BookString:
        if char not in charDict:
            charDict[char] = 1
        else:
            charDict[char] +=1
    return charDict

def bookReport(pathToBook):
    print(f"--- Begin report of {pathToBook} ---")
    text = getBookText(pathToBook)
    print(f"{countWords(text)} words found in the document\n\n")
    charCount = getCharacterCounts(text)
    charCountList = getListDict(charCount) 
    charCountList.sort(reverse=True,key=sortOn)
    for char in charCountList:
        if char["char"].isalpha():
            print(f"The '{char["char"]}' character was found {char["count"]} times")
        else:
            pass
    print("\n ---End of Report--- ")



main()    
