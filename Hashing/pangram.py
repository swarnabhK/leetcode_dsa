def checkIfPangram(sentence):
    s = set()
    for c in sentence:
        s.add(c)
    return len(s)==26
        

print(checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))