"""Command line interface for data preprocessing operations."""

import ast

import click

from src import preprocessing


@click.group()
def cli():
    """Main command line interface."""


@cli.group()
def clean():
    """Commands for data cleaning."""


@clean.command()
@click.argument("values")
def remove_missing_values(values):
    """
    Remove missing values from a list.

    Example: clean remove-missing-values "[1, 2, None, 4]"
    """
    values = ast.literal_eval(values)
    result = preprocessing.remove_missing_values(values)
    click.echo(result)


@clean.command()
@click.argument("values")
@click.option(
    "--fill-value",
    default=0,
    type=int,
    help="Value used to replace missing values (default: 0).",
)
def fill_missing_values(values, fill_value):
    """
    Fill missing values in a list.

    Example: clean fill-missing-values "[1, None, 3]" --fill-value 99
    """
    values = ast.literal_eval(values)
    result = preprocessing.fill_missing_values(values, fill_value)
    click.echo(result)


@cli.group()
def numeric():
    """Commands for numerical data processing."""


@numeric.command()
@click.argument("values")
@click.option(
    "--new-min", default=0.0, type=float, help="Minimum value of the new range."
)
@click.option(
    "--new-max", default=1.0, type=float, help="Maximum value of the new range."
)
def normalize(values, new_min, new_max):
    """
    Normalize numerical values using Min-Max scaling.

    Example: numeric normalize "[10, 20, 30]" --new-min 1 --new-max 10
    """
    values = ast.literal_eval(values)
    result = preprocessing.normalize(values, new_min, new_max)
    click.echo(result)


@numeric.command()
@click.argument("values")
def standardize(values):
    """
    Standardize numerical values using Z-score.

    Example: numeric standardize "[1, 2, 3]"
    """
    values = ast.literal_eval(values)
    result = preprocessing.standardize(values)
    click.echo(result)


@numeric.command()
@click.argument("values")
@click.option("--min-value", default=0.0, type=float, help="Minimum value allowed.")
@click.option("--max-value", default=1.0, type=float, help="Maximum value allowed.")
def clip(values, min_value, max_value):
    """
    Clip numerical values to a specified range.

    Example: numeric clip "[-5, 2, 5, 10, 15]" --min-value 0 --max-value 10
    """
    values = ast.literal_eval(values)
    result = preprocessing.clip(values, min_value, max_value)
    click.echo(result)


@numeric.command()
@click.argument("values")
def convert_to_integers(values):
    """
    Convert numerical strings to integers.

    Example: numeric convert-to-integers "['10', 'hello', '25']"
    """
    values = ast.literal_eval(values)
    result = preprocessing.convert_to_integers(values)
    click.echo(result)


@numeric.command()
@click.argument("values")
def log_transform(values):
    """
    Apply logarithmic transformation to positive values.

    Example: numeric log-transform "[1, 2, 0, -3, 10]"
    """
    values = ast.literal_eval(values)
    result = preprocessing.log_transform(values)
    click.echo(result)


@cli.group()
def text():
    """Commands for text processing."""


@text.command()
@click.argument("input_text")
def tokenize(input_text):
    """
    Tokenize text into lowercase alphanumeric words.

    Example: text tokenize "Hello World! This is MLOps."
    """
    result = preprocessing.tokenize(input_text)
    click.echo(result)


@text.command()
@click.argument("input_text")
def remove_punctuation(input_text):
    """
    Remove punctuation from text.

    Example: text remove-punctuation "Hello, World! 123."
    """
    result = preprocessing.keep_alphanumeric(input_text)
    click.echo(result)


@text.command()
@click.argument("input_text")
@click.option(
    "--stop-words", default="", help="Space-separated list of stop words to remove."
)
def remove_stop_words(input_text, stop_words):
    """
    Remove stop words from text.

    Example: text remove-stop-words "This is a project" --stop-words "is a"
    """
    stop_words = stop_words.split()
    result = preprocessing.remove_stop_words(input_text, stop_words)
    click.echo(result)


@cli.group()
def struct():
    """Commands for data structures."""


@struct.command()
@click.argument("values")
@click.option(
    "--seed", default=None, type=int, help="Random seed to ensure reproducibility."
)
def shuffle(values, seed):
    """
    Randomly shuffle a list of values.

    Example: struct shuffle "[1, 2, 3, 4, 5]" --seed 42
    """
    values = ast.literal_eval(values)
    result = preprocessing.shuffle(values, seed)
    click.echo(result)


@struct.command()
@click.argument("values")
def flatten(values):
    """
    Flatten a list of lists.

    Example: struct flatten "[[1, 2], [3, 4], [5, 6]]"
    """
    values = ast.literal_eval(values)
    result = preprocessing.flatten(values)
    click.echo(result)


@struct.command()
@click.argument("values")
def unique_values(values):
    """
    Remove duplicated values from a list.

    Example: struct unique-values "[1, 2, 2, 3, 1, 4]"
    """
    values = ast.literal_eval(values)
    result = preprocessing.remove_duplicates(values)
    click.echo(result)


if __name__ == "__main__":
    cli()
