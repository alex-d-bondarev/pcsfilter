import pytest  # noqa

from src.sfilter.tools.flake8 import run_flake8
from src.sfilter.file_helper import FileHelper
from tests.fixtures import create_temp_file  # noqa


@pytest.mark.parametrize("create_temp_file", [{
    "file_name": "temp_test_flake8.py",
    "file_content": "\nimport os"
}], indirect=True)
def test_flake8(create_temp_file):
    """Test that flake8 is launched"""
    error1 = "F401 'os' imported but unused"
    error2 = "W292 no newline at end of file"
    run_flake8(create_temp_file)

    file_util = FileHelper("flake8.log")
    actual_content = file_util.get_file_content()
    file_util.delete_file()

    assert error1 in actual_content
    assert error2 in actual_content
