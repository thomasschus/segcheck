import pytest
from .context import has_gaps
from .context import InvalidSegmentError

testdata = [
    ([], False),
    ([[1, 2], [3, 4]], True),
    ([[3, 4], [1, 2]], True),
    ([[-1, 0], [-2, 1]], False),
    ([[-1, 0], [-2, 0]], False),
]


@pytest.mark.parametrize("segmentation,expected", testdata)
def test_has_gaps(segmentation, expected):
    result = has_gaps(segmentation)
    assert result == expected


def test_has_gaps_exception():
    with pytest.raises(InvalidSegmentError):
        assert has_gaps([[0, 1], [5, 4]])
