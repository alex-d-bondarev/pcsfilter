import pytest  # noqa

from src.sfilter.tools.blue import run_blue
from tests.sfilter.unit.fixtures import create_temp_file  # noqa


@pytest.mark.parametrize(
    "create_temp_file",
    [{"file_name": "temp_test_blue.py", "file_content": "\nimport os"}],
    indirect=True,
)
@pytest.mark.unit
def test_blue(create_temp_file):
    """Test that black is launched"""
    expected = "import os\n"

    run_blue(create_temp_file.name())
    actual = create_temp_file.get_content()

    assert actual == expected
