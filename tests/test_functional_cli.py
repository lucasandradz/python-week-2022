from beerlog.cli import main
from typer.testing import CliRunner

runner = CliRunner()


def test_add_beer():
    name = "Beer"
    result = runner.invoke(
        main, ["add", name, "Style", "--flavor=1", "--image=1", "--cost=1"]
    )
    assert result.exit_code == 0
    assert f"🍺 Beer {name} added successfully." in result.stdout
