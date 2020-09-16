def printList(str) :
    arr = [];
    for x in range(len(str)-1, -1, -1) :
        # print(str[x]);
        codePoint = 65;
        if ord(str[x]) == 90 :
            arr.append(chr(codePoint));
        else :
            arr.append(chr(ord(str[x])+1));
    print(*arr);
    
printList("ABCDEF");