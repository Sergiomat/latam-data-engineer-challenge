import json
from collections import Counter
from typing import List, Tuple
import re

def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    mention_pattern = re.compile(r'@\w+')
    mention_counts = Counter()

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            tweet = json.loads(line)
            content = tweet.get('content', '')
            mentions = mention_pattern.findall(content)
            mention_counts.update(mentions)
    
    top_mentions = mention_counts.most_common(10)
    return [(mention[1:], count) for mention, count in top_mentions]  # Remove '@' from username