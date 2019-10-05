import pytest
from .context import _validate
from .context import InvalidSegmentError


def test_validate_begin_greater_than_end():
    """InvalidSegmentError should be thrown when the segment begin is greater than the segment end."""
    with pytest.raises(InvalidSegmentError):
        _validate([[1, 2], [5, 3]])


def test_validate_begin_equals_end():
    """InvalidSegmentError should be thrown when the segment begin equals teh segment end."""
    with pytest.raises(InvalidSegmentError):
        _validate([[1, 2], [5, 5]])
