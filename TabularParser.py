# Parsing each word
def TabularParser(word, TRIE, LeftToRight) :
    wordSize = len(word)
    result = []

    # create a empty matrix called result
    for i in range(wordSize+1) :
        result.append([])
        for j in range(wordSize+1) :
            result[i].append([])

    # Tabular Algorithm iteration
    for e in range(1,wordSize+1) : # end point
        for s in range(e-1, -1, -1) : # starting point
            # s ~ e  = s~e + s~k + k~e
            # When the starting point and the end point are given, parse those interval.
            # result will change inside the ParseInside function.
            ParseInside(word, result, e, s, wordSize, TRIE, LeftToRight)

    return result



def ParseInside(word, result, e, s, wordSize, TRIE, LeftToRight) :
    # k between 's to e'
    for k in range(s+1, e+1) :
        # characters from s ~ e
        if ( k == e ) :
            stoeMorp = word[s:k]
            POS = TRIE.searchMorp(stoeMorp)
            if ( POS == False ) :
                continue
            else :
                for pos in POS :
                    result[s][e].append([(stoeMorp, pos)])

        else :
            # Matrix entry of [s][k], [k][e]
            # leftTabular is an already-made morps cases that will be attached at the left side of the result.
            # RightTabular is an already-made morps cases taht will be attached at the right side of the result.
            leftTabular = result[s][k]
            rightTabular = result[k][e]
            if ( rightTabular == None or leftTabular == None ) :
                continue

            for lcandidate in leftTabular :
                for rcandidate in rightTabular :
                    # GrammarCheck
                    if GrammarCheck(lcandidate, rcandidate, LeftToRight) :
                        new = lcandidate + rcandidate
                        result[s][e].append(new)



def GrammarCheck(left, right, LeftToRight) :
    # if attaching characters are exactly the same (= same character, same POS which means that it came from itself)
    if (left[-1] == right[0] ) :
        return True

    if (left[-1][1] in LeftToRight) :
        if (right[0][1] in LeftToRight[left[-1][1]]) :
            return True

    return False




