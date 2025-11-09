import os
#תרגיל 1
word = input("enter your messgh ")
f = open('secret.txt', 'w').close()
with open('secret.txt', 'a') as f:
    for i in word:
        if ord(i) >= 97 and ord(i) <= 122:
            ch = ord(i) - 97
            new_ch = chr(122-ch)
            f.write(new_ch)
        elif ord(i) >= 65 and ord(i) <= 90:
            ch = ord(i) - 65
            new_ch = chr(90-ch)    
            f.write(new_ch)
        elif i == ".":
            f.write(f"""\n""")
        else:   
            f.write(i)

with open('secret.txt', 'r') as f:
    for i in f:
        print(i.strip())

with open('secret.txt', 'r') as f:
        for line in f:
            for i in line:
                if ord(i) >= 97 and ord(i) <= 122:
                    ch = ord(i) - 97
                    new_ch = chr(122-ch)
                    print(new_ch,end="")
                elif ord(i) >= 65 and ord(i) <= 90:
                    ch = ord(i) - 65
                    new_ch = chr(90-ch)    
                    print(new_ch,end="")
                # elif i == ".":
                #     f.write(f"""\n""")
                else:   
                    print(i,end="")

#תרגיל 2
f = open('story1.txt', 'w').close()
f = open('story2.txt', 'w').close() 
with open('mixd.txt', 'r') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        if i % 2 == 0:
            with open('story1.txt', 'a') as f:
                f.write(lines[i])
        else:
            with open('story2.txt', 'a') as f:
                f.write(lines[i])

f1 = open('story1.txt', 'w')
f2 = open('story2.txt', 'w')
with open('mixd.txt', 'r') as f:
    counter = 0
    for line in f:
        if counter % 2 == 0:
            f1.write(line)
        else:
            f2.write(line)
        counter += 1
f1.close()
f2.close()
    




            



















