# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word
    
    def get_word(self):
        return self._word
    
    def set_word(self, word):
        if isinstance(word, str):
            self._word = word
        else:
            raise TypeError("Word must be a string")
        
    word = property(get_word, set_word)

    def match(self, list_of_words):

        def make_list_of_characters():
            list_of_characters = [sorted(list(word)) for word in list_of_words]
            return list_of_characters

        sorted_list_of_characters = make_list_of_characters()
        sorted_self_word = sorted(self._word)
        list_of_anagrams = []
        
        for i in range(0,len(list_of_words)):
            if sorted_self_word == sorted_list_of_characters[i]:
                list_of_anagrams.append(list_of_words[i])
        
        return list_of_anagrams
    
listen = Anagram("listen")


        
