import numpy as np
import wordfreq
import random
import math

# Load a list of five-letter words
def load_words():
    """Load a list of five-letter words using wordfreq."""
    words = wordfreq.get_frequency_dict('en', wordlist='best')
    five_letter_words = [word for word in words.keys() if len(word) == 5]
    random.shuffle(five_letter_words)  # Shuffle the words to randomize the starting point
    return five_letter_words

# Filter the word list based on the feedback for a given guess
def filter_words(word_list, guess, feedback):
    """Filter the word list based on the feedback for a given guess."""
    new_list = []
    for word in word_list:
        if (feedback == 'green' and word[-1] == guess[-1]) or \
           (feedback == 'grey' and word[-1] != guess[-1]):
            new_list.append(word)
    return new_list

# Calculate the entropy of a guess based on possible feedback patterns
def calculate_entropy(last_letter, remaining_words, known_part):
    feedback_patterns = {}
    for word in remaining_words:
        feedback = simulate_feedback(known_part + last_letter, word)
        pattern = tuple(feedback)
        feedback_patterns.setdefault(pattern, []).append(word)

    entropy = 0
    total_words = len(remaining_words)
    for words in feedback_patterns.values():
        probability = len(words) / total_words
        entropy -= probability * math.log2(probability)
    return entropy

# Simulate feedback for the guess compared to the actual word
def simulate_feedback(guess, actual_word):
    feedback = 'grey'  # Assume the last letter is incorrect
    if guess[-1] == actual_word[-1]:
        feedback = 'green'  # Last letter is correct
    return feedback

# Select the best last letter guess based on entropy
def best_entropy_guess(remaining_words, known_part):
    max_entropy = -1
    best_guess = None
    last_letters = set(word[-1] for word in remaining_words)  # Get all possible last letters
    for last_letter in last_letters:
        entropy = calculate_entropy(last_letter, remaining_words, known_part)
        if entropy > max_entropy:
            max_entropy = entropy
            best_guess = known_part + last_letter
    return best_guess

# Main Loop
def main():
    words = load_words()
    current_words = words.copy()  # Make a copy of the word list for filtering
    actual_word = random.choice(words)  # Randomly pick an actual word
    known_part = actual_word[:-1]  # Known part is the first four letters

    print("Known part of the word:", known_part)

    for attempt in range(5):  # Allow up to 5 attempts to guess the last letter
        if not current_words:
            print("No more words to guess.")
            break
        guess = best_entropy_guess(current_words, known_part)
        print("Guess:", guess)
        feedback = simulate_feedback(guess, actual_word)
        print("Feedback:", feedback)
        if feedback == 'green':
            print("Congratulations! Puzzle solved.")
            return
        current_words = filter_words(current_words, guess, feedback)

    print("Failed to solve the puzzle.")

if __name__ == "__main__":
    main()
