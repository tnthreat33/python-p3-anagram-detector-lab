# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word
    def match(self,w_list):
        anagrams = []

        for w in w_list:
            if sorted(w.lower()) == sorted(self.word):
                anagrams.append(w)
        return anagrams
        