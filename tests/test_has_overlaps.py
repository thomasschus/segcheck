import pytest
from .context import has_overlaps
from .context import InvalidSegmentError

testdata = [
    ([], False),
    ([[1, 2], [3, 4]], False),
    ([[3, 4], [1, 2]], False),
    ([[-1, 0], [-2, 1]], True),
    ([[-1, 0], [-2, 0]], True),
]


@pytest.mark.parametrize("segmentation,expected", testdata)
def test_has_overlaps(segmentation, expected):
    result = has_overlaps(segmentation)
    assert result == expected


def test_has_overlaps_exception():
    with pytest.raises(InvalidSegmentError):
        assert has_overlaps([[0, 1], [5, 4]])
