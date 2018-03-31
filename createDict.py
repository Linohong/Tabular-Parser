def createDict(filename) :
    LeftToRight = {}
    RightToLeft = {}
    morps = []
    lines = open(filename).read().strip().split('\n')

    # parse every
    for line in lines :
        words = line.split(' ')
        line_morps = [word.split('+') for word in words]

        for morps_in_word in line_morps :
            createGrammar(morps_in_word, LeftToRight, RightToLeft)
            for morp in morps_in_word :
                morps.append(morp)

    dict = open('morp_dict.txt', 'w')
    for morp in morps :
        dict.write(morp + '\n')

    # return the Grammar results and the file name of the dictionary
    return LeftToRight, RightToLeft, 'morp_dict.txt'



def createGrammar(morps_in_word, LeftToRight, RightToLeft) :
    for i in range(len(morps_in_word)-1) :
        first_POS = morps_in_word[i].split('/')[1]
        scnd_POS = morps_in_word[i+1].split('/')[1]

        # in a word, there could be several morps and their corresponding POSs.
        # add those information into these grammar information variable (LeftToRight, RightToLeft)
        if first_POS not in LeftToRight :
            LeftToRight[first_POS] = [scnd_POS]
        else :
            if (scnd_POS not in LeftToRight[first_POS]) :
                LeftToRight[first_POS].append(scnd_POS)

        if scnd_POS not in RightToLeft :
            RightToLeft[scnd_POS] = [first_POS]
        else :
            if (first_POS not in RightToLeft[scnd_POS]) :
                RightToLeft[scnd_POS].append(first_POS)



