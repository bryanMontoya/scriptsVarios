def run():
    """my_dict = {}

    for i in range(1, 101):
        my_dict[i] = i**2"""
    
    my_dict = {i: i**2 for i in range(1,101) if i % 3 != 0}    
    #print(my_dict)

    my_dict = {i: i**0.5 for i in range(1, 101)}
    print(my_dict)
    
if __name__ == '__main__':
    run()
