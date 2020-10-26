if __name__ == "__main__":
    target_words = ("outside", "today", "weather", "raining", "nice", "rain", "snow", "day", "winter", "cold")
    ntarget_words = []
    word = ""
    while word != "exit":
        word = input("Word: ")
        if not word in target_words or word == "exit":
            ntarget_words.append(word)
    print("Words that are not target words:", ", ".join(ntarget_words))
