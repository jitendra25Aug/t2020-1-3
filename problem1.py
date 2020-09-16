def printList(arg) :
    if arg > 0 :
        for x in range(1, arg+1) :
           if x%2 == 0 :
               arr = [];
               for y in range(x,0,-1) :
                    arr.append(y);
                    if y > 1 :
                        arr.append('*');
               print("\r");
               print(*arr);
           else :
            #   print(x);
               arr = [];
               for y in range(1,x+1) :
                    arr.append(y);
                    if y < x :
                        arr.append('*');
               print(" ");
               print(*arr);
    else :
        print("Enter valid number");
printList(0);