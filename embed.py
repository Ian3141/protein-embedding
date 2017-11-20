import numpy as np
import tensorflow as tf
import collections
import random


vocab_size = 5
vocab = ['a', 'b', 'c', 'd', 'e', 'a', 'b', 'a']


def create_dataset(vocab, vocab_size):
    frequencies = list()
    frequencies.extend(collections.Counter(vocab).most_common(vocab_size))
    codes = dict()
    letters = dict()
    for letter, _ in frequencies:
        codes[letter] = len(codes)
        letters[len(codes)-1] = letter
    return frequencies, codes, letters


frequencies, codes, letters = create_dataset(vocab, vocab_size)
del vocab
print(frequencies)
print(codes)
print(letters)


index = 0


def create_batch(size, view_size, recycle_data):
    global index
    batch = np.ndarray(size)
    labels = np.ndarray(size, 1)
    context = [l for l in range(view_size * 2 + 1) if l != view_size]
    for i in range (size // recycle_data):
        sample = random.sample(len(context, len(context)))
        for j, word in enumerate(context):
#            batch[i * recycle_data + j] =
#            labels[i* recycle_data + j] =

