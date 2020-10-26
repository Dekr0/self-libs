if __name__ == "__main__":
    height = float(input("What is the starting height in meters?: ").strip())
    print("Starting height: {:.1f} m".format(height))
    count = 1
    digit = 2
    while height > 0.001:
       height /= 2
       print("Rebound #{}:  {} m".format(count, round(height, digit)))
       if height <= 2:
           digit += 1
       count += 1
