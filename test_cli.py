from click.testing import CliRunner
from cli import genfruit


def test_genfruit():
    """Testing cli for click"""


runner = CliRunner()
result = runner.invoke(genfruit, ["--fruit", "pear"])
assert result.exit_code == 0
assert "apple" or "cherry" or "pear" in result.output
