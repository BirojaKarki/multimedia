def run_length_encoding(input_string):
  """Run-length encoding implementation that takes an input string and returns its RLE
  representation"""
   # Initialize variables
  count = 1
  prev_char =input_string[0]
  output = ""
  # Iterate through the input string, starting from the second character
  for char in input_string[1:]:
# If the current character is the same as the previous one, increment the count
   if char == prev_char:
    count += 1
# If the current character is different from the previous one, add the previous character andcount  to the output
  else:
    output += str(count) + prev_char
    count = 1
    prev_char = char
# Add the last character and count to the output
    output += str(count) + prev_char

  return output

input_string = "aaabbbcccaaa"
encoded_string = run_length_encoding(input_string)
print(encoded_string)
