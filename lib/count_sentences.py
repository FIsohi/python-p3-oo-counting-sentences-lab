#!/usr/bin/env python3

class MyString:
    def __init__(self, value=''):
        self._value = ''
        self.value = value
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")
    
    def is_sentence(self):
        return self.value.endswith('.')
    
    def is_question(self):
        return self.value.endswith('?')
    
    def is_exclamation(self):
        return self.value.endswith('!')
    
    def count_sentences(self):
        import re
        if not self.value:
            return 0
        # Split by sentence-ending punctuation
        sentences = re.split(r'[.!?]', self.value)
        # Remove empty strings
        sentences = [s for s in sentences if s.strip()]
        return len(sentences)

# Example usage:
string = MyString()
string.value = "This is a string! It has three sentences. Right?"
print(string.is_sentence())      # False
print(string.is_question())      # True
print(string.is_exclamation())   # False
print(string.count_sentences())  # 3
