def locatecards(query, cards):
  """
  This function finds the index of a specific element in a list.

  Args:
      query: The element to search for.
      cards: The list to search in.

  Returns:
      The index of the element if found, -1 otherwise.
  """
  position = 0
  while True:
    if cards[position] == query:
      return position
    position += 1
    if position == len(cards):
      return -1

# Test case
test = {
  'input': {
    'cards': [13, 11, 10, 7, 4, 3, 1, 0],
    'query': 7
  },
  'output': 3
}

result = locatecards(test['input']['cards'], test['input']['query'])

# Print the result
print(f"Expected output: {test['output']}")
print(f"Actual result: {result}")

if result == test['output']:
  print("Test passed!")
else:
  print("Test failed!")
