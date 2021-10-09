def countWordsFromFile():
    filename = input("Enter the file name: ")
    f = open(filename, "r")
    numberOfWords=0
    for line in f:
        words = line.split()
        numberOfWords=numberOfWords+len(words)
    print(numberOfWords)


countWordsFromFile()
