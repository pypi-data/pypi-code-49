"""Synchronous polling-based communication protocol stack support."""

# Builtins

import time

# Packages

from phylline.pipelines import PipelineBottomCoupler


class PollingPipelineBottomCoupler(PipelineBottomCoupler):
    """A real-time stack-to-stack coupler."""

    # Override StackCoupler
    def update_clock(self):
        """Override StackCoupler.update_clock."""
        super().update_clock(time.time())
