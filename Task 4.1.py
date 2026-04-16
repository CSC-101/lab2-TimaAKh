from typing import Optional             # gain access to the Optional[X] type hint


def checked_access(L:list[int], idx:int) -> Optional[int]:
    test = idx >= 0 and idx < len(L)    # What is the value of test on each call? first call test is F, second T
    if test:                            # What is this check preventing? to not run into an error if the index is longer than the length of the list
        return L[idx]
    else:
        return None


first = checked_access([1, 0, 1], 9)     # What is the value of first? frist = none
second = checked_access([1, 0, 1], 2)    # What is the value of second? second = 1
print()