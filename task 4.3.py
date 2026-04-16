def surprising(L:list[str], other:str) -> list[str]:
    L.append(other.upper())
    return L


words = ["this", "is", "confusing", "code."]
first = surprising(words, "Avoid")
second = surprising(words, "such.")
         # What is the value of words at this point?
         # What are the values of first and second at this point? all 3, words, first, and second, are all the same values with the same list.
         # What happened? The function added words AVOID and SUCh to the end of the list and made first & second direct calsl to the same list
print()