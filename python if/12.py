'''
write a python script to accept one complex number from the user and sisplay the greater number between real part and imaginary part
'''

x=complex(input("Enter a co9mplkex number \t"))
if (x.imag>x.real):
    print("imaginary is greater")
else :
    print("Real part is greater")