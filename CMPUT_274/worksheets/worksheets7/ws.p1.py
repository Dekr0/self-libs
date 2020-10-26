while True:
    try:
        float_list = list(map(float, input().split()))
        print(*float_list, end='')
        print("---> max", max(float_list))
    except EOFError:
        break
