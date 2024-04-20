# Word Guessing Game AI

## Overview

This Python script is designed to play a word-guessing game, similar to popular games like Wordle. The AI attempts to guess the last letter of a five-letter word, given the first four letters. The script utilizes concepts from information theory, specifically entropy, to make the most informed guesses based on feedback received after each guess.

## Features

- **Dynamic Word Loading**: Loads a list of five-letter words using the `wordfreq` library to ensure a diverse playing field.
- **Feedback-Based Filtering**: Filters possible words based on feedback ('green' for correct and 'grey' for incorrect guesses).
- **Entropy Calculation**: Calculates the entropy for each possible guess to determine which has the highest potential to be correct, aiding the AI in making smarter decisions.
- **Simulation of Feedback**: Generates simulated feedback for AI guesses compared to the actual word, facilitating the AI's learning process.

## Requirements

- Python 3.x
- NumPy
- wordfreq

Ensure you have Python installed on your machine. You can download Python [here](https://www.python.org/downloads/).

## Installation

To run this script, you will need to install the required Python libraries. You can install these using pip:

```bash
pip install numpy
pip install wordfreq
