# """

# One approach to analysing some encrypted data where a substitution is suspected is frequency analysis. A count of the different symbols in the message can be used to identify the language used, and sometimes some of the letters. In English, the most common letter is "e", and so the symbol representing "e" should appear most in the encrypted text.
# Write a program that processes a string representing a message and reports the six most common letters, along with the number of times they appear. Case should not matter, so "E" and "e" are considered the same.
# """

def frequency_analyzer(string):
   letter_dict = {}
   count_letters = []

   count = 1
   for i in string:
      
      if i in letter_dict:
         count += 1
      else:
         letter_dict[i] = count

   for k, v in letter_dict.items():
        count_letters.append(v)

   sorted_letters= sorted(letter_dict.items(), key=lambda x : x[1], reverse=True)
   print(sorted_letters)

   most_common = sorted_letters[:6]
   print("Most common letters emerging")
   for i in most_common:
      print(f"{i[0]}: {i[1]}")
 

#    return letter_dict
   

frequency_analyzer("This is saksham")


