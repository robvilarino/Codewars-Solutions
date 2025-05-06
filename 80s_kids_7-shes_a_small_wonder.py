'''
Kata URL: https://www.codewars.com/kata/56743fd3a12043ffbb000049
'''
class Robot:
    def __init__(self):
        self.vocab = []
        
        # Vicky would not be able to respond if she didnt know these words already
        default_words =  "thank you for teaching me " 
        default_words += "i already know the word " 
        default_words += "do not understand input"
        
        for default_word in default_words.split(" "):
            self.vocab.append(default_word)
    
    def learn_word(self, word):
        if word.isalpha():
            if word.lower() not in self.vocab:
                self.vocab.append(word.lower())
                return f"Thank you for teaching me {word}"
            else:
                return f'I already know the word {word}'
        else:
            return "I do not understand the input"