def convert_numbers():
    """
    This function reads numbers in words from 'input.txt',
    converts them to English numbers, and writes them to 'output.txt'.

    return: None
    """
    numbers = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
        'ten': '10',
        'eleven': '11',
        'twelve': '12',
        'thirteen': '13',
        'fourteen': '14',
        'fifteen': '15',
        'sixteen': '16',
        'seventeen': '17',
        'eighteen': '18',
        'nineteen': '19',
        'twenty': '20'
    }
    with open('input.txt', 'r', encoding="utf-8") as input_file, \
    open('output.txt', 'w', encoding="utf-8") as output_file:
        
        for line in input_file:
            words = line.split()
            # Loop to convert word to number
            for i in range(len(words)):
                if words[i] in numbers:
                    words[i] = numbers[words[i]]
            output_file.write(' '.join(words) + '\n')

convert_numbers()
