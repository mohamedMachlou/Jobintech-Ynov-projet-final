def find(lst, condition, default=None):
    """
    Find the first object in a list that satisfies a condition.
    
    Args:
        lst (list): List of objects.
        condition (callable): Function that returns True for the desired object.
        default: Value to return if not found (default: None).
    
    Returns:
        The first matching object, or `default` if not found.
    """
    return next((obj for obj in lst if condition(obj)), default)

