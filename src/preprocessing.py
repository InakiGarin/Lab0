"""Module containing data preprocessing functions."""

import math
import statistics
import re
import random


def _is_missing(value):
    """Check whether a value is missing."""
    if value is None:
        return True

    if isinstance(value, str) and value.strip() == "":
        return True

    if isinstance(value, float) and math.isnan(value):
        return True

    return False


def remove_missing_values(values):
    """Remove missing values from a list."""
    return [value for value in values if not _is_missing(value)]


def fill_missing_values(values, fill_value=0):
    """Replace missing values with a given value."""
    return [fill_value if _is_missing(value) else value for value in values]


def remove_duplicates(values):
    """Remove duplicated values while preserving order."""
    unique_values = []

    for value in values:
        if value not in unique_values:
            unique_values.append(value)

    return unique_values


def normalize(values, new_min=0.0, new_max=1.0):
    """Normalize numerical values using Min-Max scaling."""
    min_value = min(values)
    max_value = max(values)

    if min_value == max_value:
        return [new_min for _ in values]

    return [
        ((value - min_value) / (max_value - min_value)) * (new_max - new_min) + new_min
        for value in values
    ]


def standardize(values):
    """Standardize numerical values using Z-score."""
    mean = statistics.mean(values)
    std = statistics.pstdev(values)

    if std == 0:
        return [0.0 for _ in values]

    return [(value - mean) / std for value in values]


def clip(values, min_value, max_value):
    """Clip numerical values to a specified range."""
    if min_value > max_value:
        raise ValueError("min_value cannot be greater than max_value")

    return [max(min_value, min(value, max_value)) for value in values]


def convert_to_integers(values):
    """Convert numerical strings to integers."""
    result = []

    for value in values:
        try:
            result.append(int(value))
        except (ValueError, TypeError):
            continue

    return result


def log_transform(values):
    """Apply logarithmic transformation to positive values."""
    return [math.log(value) for value in values if value > 0]


def tokenize(text):
    """Tokenize text into lowercase alphanumeric words."""
    return re.findall(r"[^\W_]+", text.lower())


def keep_alphanumeric(text):
    """Keep only alphanumeric characters and spaces."""
    return "".join(char for char in text if char.isalnum() or char.isspace())


def remove_stop_words(text, stop_words):
    """Remove stop words from lowercase text."""
    words = text.lower().split()
    stop_words = {word.lower() for word in stop_words}

    return " ".join(word for word in words if word not in stop_words)


def flatten(values):
    """Flatten a list of lists."""
    return [item for sublist in values for item in sublist]


def shuffle(values, seed=None):
    """Shuffle a list using an optional random seed."""
    shuffled_values = values.copy()
    random.Random(seed).shuffle(shuffled_values)

    return shuffled_values
