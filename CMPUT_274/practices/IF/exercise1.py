if __name__ == "__main__":
    char = input("Enter a character: ").strip()
    vowel = ("a", "e", "i", "o", "u")
    if char in vowel:
        print("A vowel", vowel)
    elif char == "y":
        print("Sometimes a vowel, sometimes a consonant(y)")
    else:
        print("A consonant")
