#!/usr/bin/env python3
import functools


class CalculatorBase:
    name: str

    def __init__(self, **kwargs):
        self.name = kwargs.get("name") or "Not defined"


class Calculator:
    def sum(self, a, b):
        return (a or 0) + (b or 0)

    def sum_list(self, values):
        if not values:
            return None
        return functools.reduce(self.sum, values)