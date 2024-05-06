#!/usr/bin/env python3
"""This is the module that waits for some seconds"""
import asyncio
import random
from typing import Union


async def wait_random(max_delay: int = 10) -> Union[int, float]:
    """_summary_

    Args:
        max_delay (int, optional): _description_. Defaults to 10.

    Returns:
        Union[int, float]: _description_
    """
    await asyncio.sleep(max_delay)
    return random.random() * max_delay 
