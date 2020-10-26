if __name__ == "__main__":
    try:
        my_list = [int(i) for i in input("Enter integers (separated by a single splace): ").split()]
        my_list.reverse()
        my_list.append(3)
        del my_list[0]
        my_list.extend([1,2,3])
        my_list.append(my_list[0]+my_list[1])
        my_list.reverse()
        print(my_list)
    except ValueError:
        print("Invalid Input")
