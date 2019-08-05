def count_number(number):
    result = 0
    s = []
    for i in range(1,10):
        #s.append(i)
        if (i <= n):
            s.append(i)
            result +=1
    print(s)
    print(result)


    # while len(s) != 0:
    #     tp = s[-1]
    #     s.pop()
    #     print('Value of s is: %s ' %tp)

    #     for i in range(tp%10 , 10):
    #         x = tp * 10 + i
    #         print(x)
    #         if (x <= n):
    #             s.append(x)
    #         print(s)

    while len(s) != 0: 
        tp = s[-1]  
        a = s.pop() 
        print('value of tp is: %s' %tp )
        print('value of a is: %s' %a )

        for j in range(tp % 10, 10): 
            x = tp * 10 + j 
            print(x) 
            if (x <= n):
                print(s) 
                s.append(x) 
                print(s)
                result += 1
            else:
                print('greater than n')
    print(s)
    print(result)


if __name__ == "__main__":
    n = 20
    count_number(n)
