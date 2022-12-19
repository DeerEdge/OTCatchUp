import json

"""
NOTE: Discrepancy between the output of these two test cases (4 & 5). Input is the same but output returns extra characters "can". JSON input for case 5 does not include an "insert" operation that adds "can". Erroneous input or missed handling? Please let me know if the code does not account for some attribute of the JSON input

Case 4:
isValid(
  'Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.',
  'We use operational transformations to keep everyone in a multiplayer repl in sync.',
  '[{"op": "delete", "count": 7}, {"op": "insert", "chars": "We"}, {"op": "skip", "count": 4}, {"op": "delete", "count": 1}]'
); // true

Case 5: 
isValid(
  'Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.',
  'We can use operational transformations to keep everyone in a multiplayer repl in sync.',
  '[{"op": "delete", "count": 7}, {"op": "insert", "chars": "We"}, {"op": "skip", "count": 4}, {"op": "delete", "count": 1}]'
); // false


Case 4 Input => [{"op": "delete", "count": 7}, {"op": "insert", "chars": "We"}, {"op": "skip", "count": 4}, {"op": "delete", "count": 1}]
Case 5 Input => [{"op": "delete", "count": 7}, {"op": "insert", "chars": "We"}, {"op": "skip", "count": 4}, {"op": "delete", "count": 1}]
Case 4 Output => 'We use operational transformations to keep everyone in a multiplayer repl in sync.'
Case 5 Output => 'We can use operational transformations to keep everyone in a multiplayer repl in sync.'

@Author Dheeraj Vislawath
"""


def isValid(stale, latest, otjson):
    string = stale
    stale_length = len(stale)
    position = latest
    for i in range(len(otjson)):
        current_operation = otjson[i]

        if current_operation['op'] == 'insert':
            index_change = len(current_operation['chars'])
            string = string[0:position] + current_operation['chars'] + string[position:stale_length]
            position += index_change

        if current_operation['op'] == 'skip':
            if position + current_operation['count'] <= stale_length:
                position += current_operation['count']
            else:
                return False

        if current_operation['op'] == 'delete':
            if current_operation['count'] <= (stale_length - position):
                string = string.replace((string[position:(position + current_operation['count'])]), '')
                stale_length = len(string)
            else:
                return False
    return True
