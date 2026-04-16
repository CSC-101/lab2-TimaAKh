def smallest(n:float, m:float) -> float:
    if n < m:
        return n             # For which calls below is this statement evaluated? for the call by first
    else:
        return m

first = smallest(3, 2)       # What is the value of first? first = 2
second = smallest(2, 2)      # What is the value of second? Is this a reasonable result? Why or why not?
                                    # it returns 2, but thats not a reasonale result, since theyre equal.
print()