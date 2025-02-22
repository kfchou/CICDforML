"""Tests for the example module."""

from ds_python_template.example_module import add_one


def test_add_one() -> None:
    """Test for add_one."""
    assert add_one(2) == 3
