#!/usr/bin/env python3
#! first one
def return_evens(num_list):
    even_elements = [num for num in num_list if num % 2 ==0]
    return even_elements



input_sequence = [1,2,3,4,5,6,7,8,9]
even_elements = return_evens(input_sequence)


#! second one
def make_exclamation(sentence_list):
    exclamation_sentences = [sentence + "!" for sentence in sentence_list]
    return exclamation_sentences



input = ["finally", "a worthy opponent", "our battle shall be legendary"]
exclamation_sentences = make_exclamation(input)
for sentence in exclamation_sentences:
    print(sentence)