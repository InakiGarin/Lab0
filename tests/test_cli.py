import ast
import pytest

from click.testing import CliRunner
from src.cli import cli


@pytest.fixture
def runner():
    """Create a CLI runner to invoke commands."""
    return CliRunner()


def test_remove_missing_values_cli(runner):
    """Test the remove-missing-values CLI command."""
    result = runner.invoke(cli, ["clean", "remove-missing-values", "[1, 2, None, 4]"])

    assert result.exit_code == 0
    assert ast.literal_eval(result.output) == [1, 2, 4]


def test_fill_missing_values_cli(runner):
    """Test the fill-missing-values CLI command."""
    result = runner.invoke(cli, ["clean", "fill-missing-values", "[1, None, 3]"])

    assert result.exit_code == 0
    assert ast.literal_eval(result.output) == [1, 0, 3]


def test_fill_missing_values_custom_cli(runner):
    """Test filling missing values with a custom value through CLI."""
    result = runner.invoke(
        cli,
        [
            "clean",
            "fill-missing-values",
            "[1, None, 3]",
            "--fill-value",
            "99",
        ],
    )

    assert result.exit_code == 0
    assert ast.literal_eval(result.output) == [1, 99, 3]


def test_normalize_cli(runner):
    """Test the normalize CLI command."""
    result = runner.invoke(cli, ["numeric", "normalize", "[10, 20, 30]"])

    assert result.exit_code == 0
    assert ast.literal_eval(result.output) == [0.0, 0.5, 1.0]


def test_normalize_custom_range_cli(runner):
    """Test normalization with a custom range through CLI."""
    result = runner.invoke(
        cli,
        [
            "numeric",
            "normalize",
            "[10, 20, 30]",
            "--new-min",
            "1",
            "--new-max",
            "10",
        ],
    )

    assert result.exit_code == 0
    assert ast.literal_eval(result.output) == [1.0, 5.5, 10.0]


def test_standardize_cli(runner):
    """Test the standardize CLI command."""
    result = runner.invoke(cli, ["numeric", "standardize", "[1, 2, 3]"])

    assert result.exit_code == 0

    assert ast.literal_eval(result.output) == pytest.approx(
        [-1.224744871, 0.0, 1.224744871]
    )


def test_clip_cli(runner):
    """Test the clip CLI command."""
    result = runner.invoke(
        cli,
        [
            "numeric",
            "clip",
            "[-5, 2, 5, 10, 15]",
            "--min-value",
            "0",
            "--max-value",
            "10",
        ],
    )

    assert result.exit_code == 0
    assert ast.literal_eval(result.output) == [0.0, 2, 5, 10, 10]


def test_convert_to_integers_cli(runner):
    """Test the convert-to-integers CLI command."""
    result = runner.invoke(
        cli,
        [
            "numeric",
            "convert-to-integers",
            "['10', 'hello', '25', '30']",
        ],
    )

    assert result.exit_code == 0
    assert ast.literal_eval(result.output) == [10, 25, 30]


def test_log_transform_cli(runner):
    """Test the log-transform CLI command."""
    result = runner.invoke(cli, ["numeric", "log-transform", "[1, 2, 0, -3, 10]"])

    assert result.exit_code == 0

    assert ast.literal_eval(result.output) == pytest.approx(
        [0.0, 0.693147181, 2.302585093]
    )


def test_tokenize_cli(runner):
    """Test the tokenize CLI command."""
    result = runner.invoke(cli, ["text", "tokenize", "Hello World! This is MLOps."])

    assert result.exit_code == 0
    assert ast.literal_eval(result.output) == ["hello", "world", "this", "is", "mlops"]


def test_remove_punctuation_cli(runner):
    """Test the remove-punctuation CLI command."""
    result = runner.invoke(cli, ["text", "remove-punctuation", "Hello, World! 123."])

    assert result.exit_code == 0
    assert result.output.strip() == "Hello World 123"


def test_remove_stop_words_cli(runner):
    """Test the remove-stop-words CLI command."""
    result = runner.invoke(
        cli,
        [
            "text",
            "remove-stop-words",
            "This is a machine learning project",
            "--stop-words",
            "is a",
        ],
    )

    assert result.exit_code == 0
    assert result.output.strip() == "this machine learning project"


def test_shuffle_cli(runner):
    """Test the shuffle CLI command with a fixed seed."""
    result1 = runner.invoke(
        cli, ["struct", "shuffle", "[1, 2, 3, 4, 5]", "--seed", "42"]
    )

    result2 = runner.invoke(
        cli, ["struct", "shuffle", "[1, 2, 3, 4, 5]", "--seed", "42"]
    )

    assert result1.exit_code == 0
    assert result2.exit_code == 0

    shuffled1 = ast.literal_eval(result1.output)
    shuffled2 = ast.literal_eval(result2.output)

    assert shuffled1 == shuffled2
    assert sorted(shuffled1) == [1, 2, 3, 4, 5]


def test_flatten_cli(runner):
    """Test the flatten CLI command."""
    result = runner.invoke(cli, ["struct", "flatten", "[[1, 2], [3, 4], [5, 6]]"])

    assert result.exit_code == 0
    assert ast.literal_eval(result.output) == [1, 2, 3, 4, 5, 6]


def test_unique_values_cli(runner):
    """Test the unique-values CLI command."""
    result = runner.invoke(cli, ["struct", "unique-values", "[1, 2, 2, 3, 1, 4]"])

    assert result.exit_code == 0
    assert ast.literal_eval(result.output) == [1, 2, 3, 4]
