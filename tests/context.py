import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from segcheck.core import gaps
from segcheck.core import overlaps
from segcheck.core import has_gaps
from segcheck.core import has_overlaps

from segcheck.core import _intersect
from segcheck.core import _pairwise
from segcheck.core import _validate

from segcheck.exceptions import InvalidSegmentError
