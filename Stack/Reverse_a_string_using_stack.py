def reverse(word):
    s1 = []
    s2 = []
    print(len(word))
    for i in word:
        s1.append(i)
    print(s1)

    for i in range(len(s1)):
        q = s1.pop()
        s2.append(q)

    print(s2)


word = 'geeks'
s = reverse(word)


#Alternate
#reverse a string by indexing method
# def reverse(word):
#     result = word[::-1]
#     return result

# s = 'geeks'
# print(reverse(s))
