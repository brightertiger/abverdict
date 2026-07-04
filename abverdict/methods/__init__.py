"""
Statistical methods for A/B testing.

This module provides different statistical approaches:
- sequential: Sequential testing with early stopping
- bayesian: Bayesian A/B testing
"""

from abverdict.methods import sequential
from abverdict.methods import bayesian

__all__ = ["sequential", "bayesian"]
