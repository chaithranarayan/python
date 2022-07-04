'''fileptr=open("D:\python.txt",'r')
fileptr.read()
if fileptr:
    print("its opened")
else:
    print("not opend")
fileptr.close()'''
with open("D:\python.txt")as m:
    m.write("hello")
    m.read()