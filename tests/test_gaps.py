import pytest
from datetime import datetime
from .context import gaps
from .context import InvalidSegmentError

data = [
    ([], []),
    ([[1, 2], [3, 4]], [[2, 3]]),
    ([[3, 4], [1, 2]], [[2, 3]]),
    ([[-1, 0], [-2, 1]], []),
    ([[-1, 0], [-2, 0]], []),
    ([["a", "b"], ["c", "d"]], [["b", "c"]]),
    ([["c", "d"], ["a", "b"]], [["b", "c"]]),
    ([["b", "c"], ["a", "d"]], []),
    ([["b", "c"], ["a", "c"]], []),
    (
        [
            [datetime(2019, 1, 1), datetime(2019, 1, 8)],
            [datetime(2019, 1, 12), datetime(2019, 1, 20)],
        ],
        [[datetime(2019, 1, 8), datetime(2019, 1, 12)]],
    ),
]


@pytest.mark.parametrize("segmentation,expected", data)
def test_gaps(segmentation, expected):
    result = gaps(segmentation)
    assert result == expected


def test_gaps_exception():
    with pytest.raises(InvalidSegmentError):
        assert gaps([[0, 1], [5, 4]])
