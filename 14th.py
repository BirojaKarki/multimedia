def compress(data):
# Initialize the dictionary with all single-character strings
  dictionary = {chr(i): i for i in range(256)}
next_code = 256
# Initialize the output and the current string
output = []
current = ''
# Process the input data one character at a time
for char in data:
# If the current string + the next character is in the dictionary, update the current string
 if current + char in dictionary:
  current = current + char
# Otherwise, output the code for the current string and add the current string + the next character to the dictionary
 else:
  output.append(dictionary[current])
  dictionary[current + char] = next_code
next_code += 1
current = char
# Output the code for the final string
output.append(dictionary[current])
return output
def decompress(codes):
# Initialize the dictionary with all single-character strings
dictionary = {i: chr(i) for i in range(256)}
next_code = 256
# Initialize the output and the previous code
output = ''
previous = codes.pop(0)
# Process the codes one at a time
for code in codes:
# If the code is in the dictionary, add it to the output and update the previous code
if code in dictionary:
current = dictionary[code]
output += current

dictionary[next_code] = dictionary[previous] + current[0]
next_code += 1
# Otherwise, the code must be the first character of the previous string plus the first character
of the current string
else:
current = dictionary[previous] + dictionary[previous][0]
output += current
dictionary[next_code] = current
next_code += 1
previous = code
return output