try:
    num1, num2=eval(input("enter two numbers seperated by a comma"))
    result=num1/num2
    print("result", result)
except ZeroDivisionError:
    print("dividion by zero is not valid")
except SyntaxError:
    print("missing comma")
except:
    print("wrong answer")
else:
    print("no exception")
finally:
    print("code end")