#!/usr/bin/env python3
import time
import pwalgorithms as pwa

password = input("Enter password:")

one_word = False
two_word = True

if one_word:
	print("Analyzing a one-word password ...")
	time_start = time.time()
	found, num_guesses = pwa.one_word(password)
	time_end = time.time()
	if (found):
	    print(password, "found in one-word list in ", num_guesses, "guesses")
	else:
	    print(password, "NOT found in one-word list in", num_guesses, "guesses!")
	print("Time:", format((time_end-time_start), ".8f"))

if two_word:
	print("Analyzing a two-word password ...")
	time_start = time.time()
	found, num_guesses = pwa.two_word(password)
	time_end = time.time()
	if (found):
	    print(password, "found in two-word list in ", num_guesses, "guesses")
	else:
	    print(password, "NOT found in two-word list in", num_guesses, "guesses!")
	print("Time:", format((time_end-time_start), ".8f"))
