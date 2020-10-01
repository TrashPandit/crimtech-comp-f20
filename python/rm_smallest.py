def rm_smallest(num1, num2):
    if(num1 < num2):
        print(str(num1) + " is smaller than the second number")
    else:
        print(str(num2) + " is smaller than the first number")

#def test():
#    assert 'a' in rm_smallest({'a':1,'b':-10}).keys()
#    assert not 'b' in rm_smallest({'a':1,'b':-10}).keys()
#    assert not 'a' in rm_smallest({'a':1,'b':5,'c':3}).keys()
#    rm_smallest({})
#    print("Success!")

#if __name__ == "__main__":
#    test()

rm_smallest(5,8)
