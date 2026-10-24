def is_overdue(days_past_due: int) -> bool:
    """Return True only after the due date; zero means due today."""
    return days_past_due >= 0
