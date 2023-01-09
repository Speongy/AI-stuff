input = input("Enter words or sentence: ")
vowels = {'a', 'e', 'i', 'o', 'u'}

def pigLatin (input):
    words = input.strip().split(' ') #removes spaces at the beginning and end of user input
    pl = []

    for x in words:
        if x[0] in vowels: # if x at index 0 is a vowel, just slap ay at the end of it
            pl.append(x + 'ay')
        else: # else if x is a consonant, add the first letter to 'ay' and then slice off character before index 1 
            pl.append(x[1:] + x[0] + 'ay')
    return ' '.join(pl)
print(pigLatin(input))

