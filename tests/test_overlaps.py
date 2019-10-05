import pytest
from datetime import datetime
from .context import overlaps
from .context import InvalidSegmentError

data = [
    ([], []),
    ([[1, 2], [3, 4]], []),
    ([[3, 4], [1, 2]], []),
    ([[-1, 0], [-2, 1]], [[-1, 0]]),
    ([[-1, 0], [-2, 0]], [[-1, 0]]),
    ([["a", "b"], ["c", "d"]], []),
    ([["c", "d"], ["a", "b"]], []),
    ([["b", "c"], ["a", "d"]], [["b", "c"]]),
    ([["b", "c"], ["a", "c"]], [["b", "c"]]),
    (
        [
            [datetime(2019, 1, 1), datetime(2019, 1, 12)],
            [datetime(2019, 1, 8), datetime(2019, 1, 20)],
        ],
        [[datetime(2019, 1, 8), datetime(2019, 1, 12)]],
    ),
]


@pytest.mark.parametrize("segmentation,expected", data)
def test_overlaps(segmentation, expected):
    result = overlaps(segmentation)
    assert result == expected


def test_overlaps_exception():
    with pytest.raises(InvalidSegmentError):
        assert overlaps([[0, 1], [5, 4]])
