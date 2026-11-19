"""Unit tests for the preprocessing module."""

import math

import pytest

from src import preprocessing


@pytest.fixture
def sample_numbers():
    """Return a sample list of numerical values."""
    return [1, 2, 3, 4, 5]


@pytest.fixture
def sample_missing_values():
    """Return a list containing different missing values."""
    return [1, None, "", float("nan"), 2]


@pytest.mark.parametrize(
    "values, expected",
    [
        ([1, None, 2], [1, 2]),
        (["hello", "", "world"], ["hello", "world"]),
        ([1, float("nan"), 3], [1, 3]),
        ([], []),
    ],
)
def test_remove_missing_values(values, expected):
    assert preprocessing.remove_missing_values(values) == expected


def test_remove_missing_values_fixture(sample_missing_values):
    result = preprocessing.remove_missing_values(sample_missing_values)
    assert result == [1, 2]


def test_fill_missing_values():
    result = preprocessing.fill_missing_values([1, None, "", 2])
    assert result == [1, 0, 0, 2]


def test_fill_missing_values_custom_value():
    result = preprocessing.fill_missing_values([1, None, 2], fill_value=-1)
    assert result == [1, -1, 2]


def test_remove_duplicates():
    result = preprocessing.remove_duplicates([1, 2, 2, 3, 1])
    assert result == [1, 2, 3]


def test_normalize(sample_numbers):
    result = preprocessing.normalize(sample_numbers)
    assert result == [0.0, 0.25, 0.5, 0.75, 1.0]


def test_normalize_custom_range():
    result = preprocessing.normalize([1, 2, 3], new_min=-1, new_max=1)
    assert result == [-1.0, 0.0, 1.0]


def test_normalize_constant_values():
    result = preprocessing.normalize([5, 5, 5])
    assert result == [0.0, 0.0, 0.0]


@pytest.mark.parametrize(
    "values, min_value, max_value, expected",
    [
        ([1, 2, 3], 0, 2, [1, 2, 2]),
        ([-5, 0, 5], -2, 2, [-2, 0, 2]),
        ([1, 2, 3], 1, 3, [1, 2, 3]),
        ([10, 20, 30], 0, 100, [10, 20, 30]),
    ],
)
def test_clip(values, min_value, max_value, expected):
    assert preprocessing.clip(values, min_value, max_value) == expected


def test_clip_invalid_range():
    with pytest.raises(ValueError):
        preprocessing.clip([1, 2, 3], 5, 1)


def test_standardize():
    result = preprocessing.standardize([1, 2, 3])
    assert result == pytest.approx([-1.2247, 0.0, 1.2247], abs=0.001)


def test_standardize_constant_values():
    result = preprocessing.standardize([5, 5, 5])
    assert result == [0.0, 0.0, 0.0]


def test_convert_to_integers():
    result = preprocessing.convert_to_integers(["1", "2", "hello", "3"])
    assert result == [1, 2, 3]


def test_log_transform():
    result = preprocessing.log_transform([1, math.e, 0, -1])
    assert result == pytest.approx([0.0, 1.0])


def test_tokenize():
    result = preprocessing.tokenize("Hello, WORLD! This is a test.")
    assert result == ["hello", "world", "this", "is", "a", "test"]


def test_keep_alphanumeric():
    result = preprocessing.keep_alphanumeric("Hello, world! 123.")
    assert result == "Hello world 123"


def test_remove_stop_words():
    result = preprocessing.remove_stop_words(
        "This is a simple test",
        ["is", "a"],
    )
    assert result == "this simple test"


def test_flatten():
    result = preprocessing.flatten([[1, 2], [3, 4], [5]])
    assert result == [1, 2, 3, 4, 5]


def test_shuffle():
    values = [1, 2, 3, 4, 5]

    result1 = preprocessing.shuffle(values, seed=42)
    result2 = preprocessing.shuffle(values, seed=42)

    assert result1 == result2
    assert sorted(result1) == sorted(values)
    assert values == [1, 2, 3, 4, 5]
