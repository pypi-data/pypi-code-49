"""
A set of Transforms meant for financial analysis to be used with the datacode package
"""
import datacode as dc

from transforms_fin.portfolio import portfolio_transform

ALL_TRANSFORMS = [
    portfolio_transform,
]

dc.register_transforms(ALL_TRANSFORMS)
