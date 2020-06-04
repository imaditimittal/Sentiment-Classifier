f = open('project_twitter_data.csv','r')

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

lin = f.readlines()
file = f.read()

# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())
def get_pos(lin):
    lin  = lin.split()
    count = 0
    for l in lin:
        l = l.lower()
        l = strip_punctuation(l)
        if l in positive_words:
            count += 1
    return count

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
def get_neg(lin):
    lin  = lin.split()
    count2 = 0
    for l in lin:
        l = l.lower()
        l = strip_punctuation(l)
        if l in negative_words:
            count2 += 1
    return count2

def strip_punctuation(file):
    for l in file:
        if l in punctuation_chars:
            file = file.replace(l,'')
    return file


fname = open('resulting_data.csv','w')
fname.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')
fname.write('\n')
m = f.readlines()
headerDontUsed= m.pop(0)
for linesTD in m:
    listTD = linesTD.strip().split(',')
    fname.write("{}, {}, {}, {}, {}".format(listTD[1], listTD[2], get_pos(listTD[0]), get_neg(listTD[0]), (get_pos(listTD[0])-get_neg(listTD[0]))))    
    fname.write("\n")


