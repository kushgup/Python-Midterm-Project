def lstSequence(k,lst):
    dictionary = {}

    for line in lst:
        for i in range(len(line)):
            sequence = line[i:i+k]
            if len(sequence) == k:
                dictionary[sequence] = dictionary.get(sequence,0) + 1

    return dictionary

def diffFunc(dictPre, dictPost, word): # Testing Function
    pre = dictPre.get(word,0)
    post = dictPost.get(word,0)

    print("word:{0}".format(word))
    print("Pre_treat {0}: = {1}".format(word,pre))
    print("Post_treat {0}: = {1}".format(word,post))

def differencesDict(dictPre, dictPost):
    differences = {}
    keys = list(dictPre.keys())
    for i in keys:
        diff = (dictPre.get(i,0) - dictPost.get(i,0))
        differences[i] = diff

    return differences

def calcGreatestDiff(dictDiff):
    keys = list(dictDiff.keys())
    
    greatestKey = ""
    greatestValue = 0
    
    for i in keys:
        if dictDiff.get(i,0) > greatestValue:
            greatestKey = i
            greatestValue = dictDiff.get(i,0)

    lstGreatestKeys = [greatestKey]
    for i in keys:
        if dictDiff.get(1,0) == greatestValue:
            lstGreatestKeys.append(i)

    return lstGreatestKeys
    
def main():
    pretreat = open("pre_treat.txt",'r')
    preString = pretreat.read()
    lstPreLines = preString.split('\n')
    print(1)

    posttreat = open("post_treat.txt",'r')
    postString = posttreat.read()
    lstPostLines = postString.split('\n')
    print(2)

    k = int(input("Enter a number k (<10) for protein sequence length: "))
    print(3)

    dictPre = lstSequence(k,lstPreLines) # Dictionary of pre_treat broken up into sequences of len(k)
    dictPost = lstSequence(k,lstPostLines) # Dictionary of post_treat broken up into sequences of len(k)
    print(4)


    dictDiff = differencesDict(dictPre, dictPost) # Dictionary of differences
    lstGreatestKeys = calcGreatestDiff(dictDiff) # Dictionary of sequences with the greatest difference

    print("\nThe sequence of length {0} with greatest variation:".format(k))
    for i in lstGreatestKeys:
        print("{0} diff = {1}; pre_treat = {2}, post_treat = {3}".format(i,dictDiff.get(i,0),dictPre.get(i,0),dictPost.get(i,0)))


''' Testing Code:

    diffFunc(dictPre, dictPost, 'LPVL') # THIS ONLY WORKS IF YOUR BREAK UP THE PROTEINS BY SIZE K = 4
    
'''


main()
