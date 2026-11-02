from click.testing import CliRunner
from gcli.cli import cli
from gcli import __version__


def test_version():
    """checks that the CLI returns the correct version"""
    runner = CliRunner()
    result = runner.invoke(cli, ["config", "version"])

    assert result.exit_code == 0
    assert result.output.startswith(__version__)


if __name__ == "__main__":
    test_version()
