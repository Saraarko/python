#Giraffe Language
#vowels -> guess
----------
#dog->dgg
#cat->cgt
def translate (phrase):
    resulttranslation=""
    vowels="AOIEYUaeiouyu"
    for letter in phrase:
        if letter in vowels:
        resulttranslation=resulttranslation+"g"
        else:
        resulttranslation=resulttranslation+letter

    return resulttranslation
print(resulttranslation(input("enter a phrase")))



