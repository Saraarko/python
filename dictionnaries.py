monthConversion={
    "jan" : "january",
    "feb" : "february",
    "mar" : "march",
    "apr" : "april",
    "may" : "may",
    "jun" : "june",
    "jul" : "july",
    "aug" : "august",
    "sep" : "september",
}

print(monthConversion["sep"])
print(monthConversion.get("jul"))
print(monthConversion.get("luv","not a valid key"))