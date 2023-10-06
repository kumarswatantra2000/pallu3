class student():
    x=34
    y=23
    def f1():
        s3=66
        print(s3)
    def _init_(self,x):
        self.x=x
s1=student(4)
s2=student(8)

'''
!.Local Variable==s3,self,x
ii.Global Variable==s1,s2,student
iii.Function object Variable==F1,__init__
iv.Class object Variable==z,x
v.Instance Object Variable==s1,x,s2,x
'''