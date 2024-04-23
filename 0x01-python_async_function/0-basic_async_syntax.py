#!/usr/bin/env python3
'''task for using random and asyncio modules'''


import asyncio
import random


async def wait_random(max_delay: int = 10)-> float:
  """asynchronous coroutine"""
  delay = random.uniform(0, max_delay)
  await asyncio.sleep(delay)
  return delay