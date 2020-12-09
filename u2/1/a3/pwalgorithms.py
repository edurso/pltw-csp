# Module pwalgorithms

# get words from password dictionary file
def get_dictionary():
    words = []
    dictionary_file = open("dictionary.txt")
    for line in dictionary_file:
        # store word, ommitting trailing new-line
        words.append(line[:-1])
    dictionary_file.close()
    return words

# analyze a one-word password
def one_word(password):
    words = get_dictionary()
    guesses = 0
    # get each word from the dictionary file
    for w in words:
        guesses += 1
        if (w == password):
            return True, guesses
    return False, guesses

def two_word(password):
	"""
    Function attempts to guess the given password.

    Parameters
    ----------
    password : str
        The password (2 words separated by a space) that the function will try to guess.

    Returns
    -------
	bool
		True if the function was able to guess the password, false otherwise.
    int
        The number of guesses it took the function until it has found the first word in the passowrd. If it does not find the password, this will be the number of attempts.
	int
        The number of guesses it took the function until it has found the second word in the passowrd after it knows the first word. If it does not find the password, this will be the number of attempts.
    """
	guesses1, guesses2 = 0, 0
	w1_, w2_ = password.split()
	for w1 in get_dictionary():
		guesses1 += 1
		if w1 == w1_:
			for w2 in get_dictionary():
				guesses2 += 1
				if w2 == w2_:
					return True, guesses1, guesses2
	return False, guesses1, guesses2
