import json
import re
from collections import Counter
from typing import List, Tuple


def q3_time(file_path: str) -> List[Tuple[str, int]]:
    """
    Extracts the top 10 most mentioned usernames from a JSON file of tweets.

    Args:
    file_path (str): Path to the JSON file containing tweets.

    Returns:
    List[Tuple[str, int]]: Top 10 mentioned usernames with their counts.
    """
    username_pattern = re.compile(r'@(\w+)')
    username_counter = Counter()

    with open(file_path, 'r') as file:
        for line in file:
            tweet = json.loads(line)
            if 'content' in tweet:
                username_counter.update(
                    username_pattern.findall(tweet['content']))

    return username_counter.most_common(10)
