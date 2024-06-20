from opration import do_addition, do_subtraction


def main():
    print('welcome to calculator app')
    print("""
          \n select the function from below options
          1. add
          2. subtract
""")
    
    user_input = input("select the function")

    a = int(input('value of a'))
    b = int(input('value of b'))

    if user_input=="1":
        print(do_addition(a,b))
    elif user_input=="2":
        print(do_subtraction(a,b))
    else:
        print("something is wrong") 

if __name__ == "__main__":
    main()   


