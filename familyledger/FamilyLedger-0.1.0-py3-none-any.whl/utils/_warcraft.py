"""
A module for handling information peculiar to World of Warcraft.

Copyright (C) 2020, fondlez "Anuber"-Kronos, fondlez at protonmail.com
"""


def format_gold(copper_value, format=None, disable=False):
    """Converts the copper value of WoW currency to its denominations.
    
    Args:
        copper_value (str): copper value of WoW currency.
        format (str): Python format() string with value replacements of 
            ``{gold}``, ``{silver}`` and ``{copper}`` available.
        disable (bool): flag to disable function and pass through the value.
        
    Returns:
        str: formatted gold string.
    """
    if disable:
        return copper_value
    silver_part, copper = divmod(int(copper_value), 100)
    gold, silver = divmod(silver_part, 100)
    format = format or '{gold}g {silver:02d}s {copper:02d}c'
    return format.format(gold=gold, silver=silver, copper=copper)


def decimal_gold(copper_value, disable=False):
    """Converts the copper value of WoW currency to decimal gold.
    
    Args:
        copper_value (str): copper value of WoW currency.
        disable (bool): flag to disable function and pass through the value.
        
    Returns:
        float: decimal gold value.
    """
    if disable:
        return copper_value
    return int(copper_value)/10000
