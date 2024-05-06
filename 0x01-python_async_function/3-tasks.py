#!/usr/bin/env python3
"""this the module that returns a task"""
import asyncio
from typing import Coroutine, Any


wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: float) -> asyncio.Task:
    """This function creates and returns an asyncio.Task object."""
    task: asyncio.Task = asyncio.create_task(wait_random(max_delay))
    return task
