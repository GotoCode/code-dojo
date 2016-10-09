'''
    problem statement
    
    Given a string, reverse each word in the string
    (words are separated by one or more spaces)
    
    LESSON OF THE DAY
    
      ~ there is no 'str.reverse()'
'''


def findFirstSpace(s, start):

    if s == None or start < 0:
        return -1
    
    for i in xrange(start, len(s)):
        
        if s[i].isspace():
            return i
        
    return len(s)


def reverseWords(s):
    
    if s == None:
        return None
    
    newStr  = ''
    revDict = {}
    
    
    # build up dictionary of reversed words
    i = 0
    
    while i < len(s):
    
        if s[i].isspace():
        
            newStr += ' '
            i += 1
        
        else:
        
            word = s[i : findFirstSpace(s, i)]
            
            # reverse the extracted word
            revWord = [ch for ch in word]
            revWord.reverse()
            revWord = ''.join(revWord)
            
            newStr += revWord
            
            i = findFirstSpace(s, i)
    
    return newStr



# 'hello  world and  goodbye'
#                           ^

# 'olleh  dlrow dna  eybdoog'


