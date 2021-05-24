print('Pick two files to exchange text.')
print(' ')

file1=input('First file :- ')
file2=input('Second file :- ')

f1=open(file1,'r')
text1=f1.read()
f2=open(file2,'r')
text2=f2.read()

f1=open(file1,'w')
t1=f1.write(text2)
f2=open(file2,'w')
t2=f2.write(text1)