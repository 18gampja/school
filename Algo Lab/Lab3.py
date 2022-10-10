# Jacob
# CMPSC 413
# Pattern Matching

from typing import List


def naivePat(searchString, pat):

    index = 0
    occurrences = []

    for char in searchString:
 
        count = 0

        if char == pat[0]:

            currentString = searchString[index :]
            pattern = True

            while count < len(pat):

                if count + 1 > len(currentString):

                    pattern = False
                    break

                if pat[count] == currentString[count]:

                    count += 1
                    pass

                else:

                    count += 1
                    pattern = False
                    break
            
            if count == len(pat) and pattern == True:
                occurrences.append(f'Pattern detected at index {index}')
        
        index += 1

    for instance in occurrences:

        print(instance)

# print()
# print('Searching for "CMPSC":')
# naivePat('This is a CMPSC 412 lab course. Students take this course along with CMPSC 462', 'CMPSC')
# print()
# print('Searching for "course": ')
# naivePat('This is a CMPSC 412 lab course. Students take this course along with CMPSC 462', 'course')
# print()
# print('Seraching for "BBBBBA"')
# naivePat('AABAACAADAABAABAABBBBBAAABDCBA', 'BBBBBA')
# print()

def computeLPS(pattern: str) -> List[int]:
    
    # Longest Proper Prefix that is suffix
    lps = [0] * len(pattern)
    top = 0

    for bottom in range(1, len(pattern)):

        # Phase 3: roll the prefix pointer back until match or beginning of pattern is reached
        while top and pattern[bottom] != pattern[top]:
            top = lps[top - 1]

        # Phase 2: if match, record the LSP for the current 'top' and move prefix pointer
        if pattern[top] == pattern[bottom]:
            top += 1
            lps[bottom] = top

    return lps

def kmp(pattern: str, text: str) -> List[int]:

    matchIndices = []
    patternLPS = computeLPS(pattern)

    patterni = 0

    for i, ch in enumerate(text):

        # Phase 3: if a mismatch was found, roll back the pattern index using the information in LPS
        while patterni and pattern[patterni] != ch:
            patterni = patternLPS[patterni - 1]

        # Phase 2: if match
        if pattern[patterni] == ch:

            # If the end of a pattern is reached, record a result and use information in LSP array to shift the index
            if patterni == len(pattern) - 1:

                matchIndices.append(f'Match found at index {i - patterni}')
                patterni = patternLPS[patterni]

            else:

                # Move the pattern index forward
                patterni += 1

    for match in matchIndices:
        print(match)

    return matchIndices

# print()
# print('Searching for "CMPSC" : ')
# kmp('CMPSC', 'This is a CMPSC 412 lab course. Students take this course along with CMPSC 462')
# print()
# print('Searching for "course" : ')
# kmp('course', 'This is a CMPSC 412 lab course. Students take this course along with CMPSC 462')
# print()
# print('Searching for "BBBBBA" :')
# kmp('BBBBBA', 'AABAACAADAABAABAABBBBBAAABDCBA')
# print()