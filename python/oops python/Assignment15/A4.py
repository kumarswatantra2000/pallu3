# Decorator
def modifind_result(pass_result):
    def pallu(marks):
        for y in marks:
            if y>=70:
                print("Amazing")
            else:
                return pass_result(marks)
        return pallu
    
'''
def pallu(marks):
    for y in marks:
        if y<=70:
            pass
        else:
            print("You are first division")
            break
    else:
        print("you are second division")
pallu({70,34,90,89,78,90})


def pallu(marks):
    for x in marks:
        if x>=40:
            pass
        else:
            print("you are faile")
            break
    else:
        print("you are pass")
pallu({34,67,89,56,32,98})
'''