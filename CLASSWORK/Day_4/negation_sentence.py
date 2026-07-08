'''from negate import Negator     #NLP library for negating sentences

# Initialize the negator
negator = Negator()

sentence_1 = input("Enter a sentence : ")
print(negator.negate_sentence(sentence_1)) 

sentence_2 = input("Enter a sentence : ")
print(negator.negate_sentence(sentence_2)) '''

def negate_sentence_Pos_sentence(sentence):
    words = sentence.split()
    negated_words = []
    corrected_words = []
    for word in words:
        if word.lower() in ["is", "are", "was", "were", "am"]:
            negated_words.append("not")
        negated_words.append(word)
    
    #negated_words.extend(corrected_words)
    return " ".join(negated_words)



sentence_3 = input("Enter a sentence : ")
print(negate_sentence_Pos_sentence(sentence_3))
