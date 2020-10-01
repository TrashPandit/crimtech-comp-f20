import random

def random_ints():
    # Your code here!
    num1 = int(input("What is the first num you want to start at: "))
    num2 = int(input("What is the last nun you want to end at: "))
    print(random.randint(num1,num2))

#def test():
#    N = 10000
#    for i in range(N):
#        l = random_ints()
#        assert not 0 in l
#        assert not 11 in l
#        assert l[-1] == 6
#        total_length += len(l)
#    assert abs(total_length / N - 10) < 1 # checks that the length of the random strings are reasonable.
#    print("Success!")

#if __name__ == "__main__":
#    test()

random_ints()
