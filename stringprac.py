# msg = "Welcome to learn"
# #0123435..
# print(msg + " " + msg)
# print (msg * 2)
# print(msg.upper())
# print(msg.lower())
# print(msg.capitalize())
# print(msg.title())
# print(len(msg))
# print(msg.count('a')) #case sensitive method
# print(msg[:7])
# #slicing the strings
# print(msg[7])
# print(msg[-1]) #give the last number
# test_msg = "Welcome to Python 101: Strings"
# result = (test_msg[18] +" " +test_msg[0:7] +" " +test_msg[25:29] +" " + test_msg[8:11] + test_msg[8] + test_msg[12] + test_msg[2] + test_msg[6]+ test_msg[25])
# print(result.title())
# print(result[::-1])
# # another_msg = """Dear Terry,,
# # You must cut down the mightiest 
# # tree in the forest with…
# # a herring"""
# # print(another_msg)
# print(msg.replace('W', 'MIO'))
# print(msg)
# #strings are immutable
# #memebership
# print('welcome' in msg) #case sensitive
# print('Failure'not  in msg)
# name = "TERRY"
# color = "RED"
# msg1 = f'{name.capitalize()} loves the color {color.lower()}'
# print(msg1)
# def is_palindrome(input_string):
#     input_string = input_string.replace(" ", "")
    
#     new_string = ""
#     reverse_string = ""

#     for letter in input_string:
#         new_string = new_string + letter
#         reverse_string = letter + reverse_string

#     if reverse_string == new_string:
#         return True
#     return False


# # Test cases
# print(is_palindrome("Never Odd or Even"))  # True
# print(is_palindrome("abc"))                # False
# print(is_palindrome("kayak"))  
# Weather = "Rainfall"
# print(Weather[:4])
def replace_ending(sentence, old, new):
    # Check if the old substring is at the end of the sentence 
    if sentence.endswith(old):
        # Using i as the slicing index, combine the part
        # of the sentence up to the matched string at the 
        # end with the new string
        i = len(sentence) -len(old)
        new_sentence = sentence[:i] + new
        return new_sentence


    # Return the original sentence if there is no match 
    return sentence
    
print(replace_ending("It's raining cats and cats", "cats", "dogs")) 
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts")) 
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april")) 
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April")) 
# Should display "The weather is nice in April"
