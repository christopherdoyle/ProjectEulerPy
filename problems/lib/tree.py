from __future__ import annotations

import logging
from typing import Generic, TypeVar

logger = logging.getLogger(__name__)


T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, value: T, left: Node[T] = None, right: Node[T] = None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"Node({self.value})"


def _max_path_sum(node, result):
    if node is None:
        return 0
    left = max(0, _max_path_sum(node.left, result))
    right = max(0, _max_path_sum(node.right, result))
    return node.value + max(left, right)


def max_path_sum(node: Node[T]) -> T:
    """Finds the maximum sum of a path down the entire tree."""
    logger.info("Finding maximum path in tree")
    return _max_path_sum(node, 0)
