months = ('JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT')
print("The contents of object {} are {}".format(id(months), months))

months = months + ('NOV', 'DEC')
print("The contents of object {} are {}".format(id(months), months))

precipitation2018 = [15.5, 12.1, 18.5, 15.6, 10.7, 62.2, 41.4, 58.3, 15.7, 15.3, 24.8]

precipitation2018.insert(6, 67.8)

print("{}mm fell in {} 2018".format(precipitation2018[months.index('APR')], 'APR'))

month = input("Please enter a month: ").strip()
print("{}mm fell in {} 2018.".format(precipitation2018[months.index(month)],month))
