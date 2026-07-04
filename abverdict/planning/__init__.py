"""
Test Planning Module.

Tools to help plan A/B tests before you run them:
- Minimum Detectable Effect (MDE) calculator
- Test duration recommendations
- Traffic allocation optimization
"""

from abverdict.planning.mde import (
    minimum_detectable_effect,
    MDEResult,
)
from abverdict.planning.duration import (
    recommend_duration,
    DurationRecommendation,
)

__all__ = [
    "minimum_detectable_effect",
    "MDEResult",
    "recommend_duration",
    "DurationRecommendation",
]
