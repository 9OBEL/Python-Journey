def pin_extractor(poems):
    secret_codes = []
    for poem in poems:
        secret_code = ''  # Reset the PIN string for the current poem
        lines = poem.split('\n')  # Split the poem line by line

        for line_index, line in enumerate(lines):
            # This loop keeps track of the line index (0, 1, 2, etc.)
            words = line.split()  # Split the current line into a list of words

            # Check if the line has enough words to match the required line index
            if len(words) > line_index:
                # Extract the word at the current line index,
                # get its length, and add it to the secret code
                secret_code += str(len(words[line_index]))
            else:
                # If there aren't enough words, add '0' instead
                secret_code += '0'

        secret_codes.append(secret_code)  # Store the final PIN for this poem
    return secret_codes


# --- Input Data ---
poem = """Stars and the moon
shine in the sky
white and
until the end of the night"""

poem2 = 'The grass is green\nhere and there\nhoping for rain\nbefore it turns yellow'
poem3 = 'There\nonce\nwas\na\ndragon'

# --- Execution ---
print(pin_extractor([poem, poem2, poem3]))