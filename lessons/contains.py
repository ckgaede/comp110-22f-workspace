"""Example implementing a list utility function."""

# Function name: contains
# We will have two parameters: needle (str), haystack (list[str])
# Return type bool
def contains(needle: str, haystack: list[str]) -> bool:
    i: int = 0
    while i < len(haystack):
        if haystack[i] == needle:
            # We found it! No more work to do!
            return True
        i += 1
    # We tried searching each item and came up short!
    return False