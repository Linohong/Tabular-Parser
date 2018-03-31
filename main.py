import createDict as CD
import TRIEconstruct as TC
import TabularParser as TP

# FUNCTION FOR FINAL RESULT
# All Combinations of every possible cases of result
def MorpCombination(Strings, res) :
    new_String = []
    for case in Strings :
        for cur in res : # res => [[('나', 'VV'), ('는', 'E')], [('나', 'NP'), ('는', 'JX')]]
            adding_morp = ''
            for morp in cur :
                adding_morp += morp[0] + '/' + morp[1] + '+'
            adding_morp = adding_morp.strip('+') # adding_morp => 나/VV+는/E

            new_String.append( (case + ' ' + adding_morp).strip(' ') )

    return new_String



# Making Grammar, Dictionary
LeftToRight, RightToLeft, dictName = CD.createDict('morph_rule.txt') # Grammar Information(LeftToRight, RightToLeft, dictionary)
dict_lines = open(dictName).read().strip().split('\n')
TRIE = TC.Tree() # Create TRIE data structure Dictionary
for morp in dict_lines :
    morp, pos = morp.split('/')[0], morp.split('/')[1]
    TRIE.addNode(morp, pos)




# Tabular Parse !
input_lines = open('input.txt').read().strip().split('\n')
output_file = open('morp_analysis.txt', 'w')

for line in input_lines : # For every lines of input
    words = line.split(' ')
    Strings = ['']
    for word in words : # Tabular parse every word of a sentence input
        tabular = TP.TabularParser(word, TRIE, LeftToRight)[0][len(word)]

        # removing repetition
        res = []
        for entry in tabular :
            if entry not in res :
                res.append(entry)

        # Make Combinations in current input sentence till current word result
        Strings = MorpCombination(Strings, res)

    # when tabular parsing of current sentence is over, write to the file and screen (standard output)
    for string in Strings :
        output_file.write(string + '\n')
        print(string)


