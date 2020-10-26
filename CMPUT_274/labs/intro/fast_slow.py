if __name__ == "__main__":
    c_1 = float(12)
    c_2 = float(12)
    mp  = float(0)
    while True:
        hrp += 1
        c_1 -= 0.2
        c_2 += 0.2
        if not c_1 // 12 == 0.0:
            c_1 = c_1 % 12 
        if not c_2 // 12 == 0.0:
            c_2 = c_2 % 12
        if c_1 == c_2:
            break
