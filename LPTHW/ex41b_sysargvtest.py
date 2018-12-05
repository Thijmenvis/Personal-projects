import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
        "make a class named %%% that is-a %%%",
    "class %%%(object):\n\tdef __init__(self, ***)" :
        "class %%% has-a __init__ that takes self and *** parameters.",
    "class %%%(object):\n\tdef ***(self, @@@)":
        "class %%% has-a function named *** that takes self and @@@ parameters.",
    "*** = @@@()":
        "Set *** to an instance of class %%%",
    "***.***(@@@)":
        "From *** get the *** function, and call it with parameters self, @@@",
    "***.*** = '***'":
        "from *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# load up the words from the website
#read the lines on the webpage using readlines()
for word in urlopen(WORD_URL).readlines():
    # append the words to WORDS after stripping each word from word
    # so it takes one word from the end of the list and appends it to WORDS
    WORDS.append(word.strip())

def convert(snippet, phrase):
    # capitalize the samples you take from WORDS
    class_names = [w.capitalize() for w in
                    # count the amount of %%% in snippet and take that
                    # amount of samples from WORDS
                    random.sample(WORDS, snippet.count("%%%"))]

    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    # chooses a random number of parameters to add:
    # count the amount of @@@ in the dictionary and run this piece of code
    # that many times.
    for i in range(0, snippet.count("@@@")):
        #choose a rondom number between 1 and 3
        param_count = random.randint(1,3)
        # take 2 random samples from words and param_count and append it to
        # param_names using ', '.join() to add a comma between the two samples
        param_names.append(', '.join(random.sample(WORDS, param_count)))

    # I have no idea what this does.........
    for sentence in snippet, phrase:
        result = sentence[:]

        # fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)

        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results

# keep going until they hit CTRL-D
try:
    while True:
        # keys() returns a copy of the dictionary's keys
        snippets = PHRASES.keys()
        # random.shuffle(x[,random])
        # shuffle the sequence x in place
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet,phrase)
            if PHRASE_FIRST:
                question, answer = answer, question
        print question

        raw_input("> ")

        print "ANSWER: %s\n\n" % answer
except EOFError:
    print "\nBye"
