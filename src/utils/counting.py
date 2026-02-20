from nexios.utils.concurrency import AsyncLazy


def count_numbers_lazy(start: int, end: int, step: int = 1):
    """Lazy function that counts from start to end using AsyncLazy"""

    async def _count():
        numbers = []
        for i in range(start, end + 1, step):
            # Simulate async work for each number
            import asyncio

            await asyncio.sleep(0.01)  # Small delay to demonstrate async behavior
            numbers.append(i)
        return numbers

    return AsyncLazy(_count).get()
