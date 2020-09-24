import math

def square_root():
    number = int(input("Enter A number: "))
    print(number)
    placehold = number             
    number = number ** 0.5
    print('The square root of %0.3f is %0.3f'%(placehold ,number))             
    return 0

#def test():
#   assert square_root(4) == 2
#    assert square_root(0) == 0
#    assert square_root("hello") == -1
#    assert square_root(-10) == -1
#    print("Success!")

#if __name__ == "__main__":
#    test()

square_root()
