def pattern(num) :
    arr = [];
    for i in range(1, num+1) :
        if i%2 == 0 :
            arr = [];
            for j in range(i, 0, -1) :
                arr.append(j);
            print(str(arr)[1:-1]);
        else :
            arr = [];
            for j in range(1, i+1) :
                arr.append(j);
            print(str(arr)[1:-1]);
    for i in range(num-1, 0, -1) :
        if i%2 == 0 :
            arr = [];
            for j in range(i, 0, -1) :
                arr.append(j);
            print(str(arr)[1:-1]);
        else :
            arr = [];
            for j in range(1, i+1) :
                arr.append(j);
            print(str(arr)[1:-1]);
    
pattern(10);