import Levenshtein

def compare_strings(str1, str2):
    """
    Compare two strings using the Levenshtein distance algorithm.
    Returns a float between 0 and 1 representing the similarity of the strings.
    """
    distance = Levenshtein.distance(str1.lower(), str2.lower())
    max_length = max(len(str1), len(str2))
    if max_length == 0:
        return 1.0
    else:
        return 1 - (distance / max_length)
