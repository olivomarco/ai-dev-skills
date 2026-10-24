def discounted_price(cents: int, percent: int) -> int:
    if cents < 0:
        raise ValueError("Price must be nonnegative")
    if not 0 <= percent <= 100:
        raise ValueError("Discount must be between 0 and 100")
    return cents * (100 - percent) // 100
