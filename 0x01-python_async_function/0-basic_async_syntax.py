#!/usr/bin/env python3
"""This is the module that waits for some seconds"""
import asyncio
import random
from typing import Union


async def wait_random(max_delay: int = 10) -> Union[int, float]:
    
    
    await asyncio.sleep(max_delay)
    return random.random() * max_delay 
