if __name__ == "__main__":
    date = input("Enter a date (format: year month day): ").split()
    date.reverse()
    date[0], date[1] = date[1], date[0]
    print("The new date format is %s." % ".".join(date))
