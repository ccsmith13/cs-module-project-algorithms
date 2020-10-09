'''
Input: an integer
Returns: an integer

if n = 1:
    return 1 

elif n = 2: 
    return 2

else n >= 3: 

    example:    50 =>  f(49) f(48) + f(47)...
'''
def eating_cookies(n):
    # Your code here
    counter = 0
    if n is None: 
        return 
    elif n == 0: 
        return 1
    elif n == 1: 
        return 1
    elif n == 2: 
        return 2
    elif n == 3: 
        return 4
    else:
        counter += 1
        return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")
