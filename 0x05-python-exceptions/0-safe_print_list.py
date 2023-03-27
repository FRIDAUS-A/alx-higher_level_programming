def safe_print_list(my_list=[], x=0):
    count = 0
    for ele in my_list:
        try:
            if (count < x):
                print(ele, end="")
                count += 1
        except:
            pass
    print()
    return (count)
