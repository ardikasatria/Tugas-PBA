from typing import Tuple, Dict

from . import yahoo_answer

def get_label_map(dataset: str) -> Tuple[Dict[str, int], Dict[int, str]]:
    if dataset == 'yahoo_answers':
        classes = yahoo_answer.classes
    else:
        raise Exception("Dataset not supported: ", dataset)

    label_map = {k: v for v, k in enumerate(classes)}
    rev_label_map = {v: k for k, v in label_map.items()}

    return label_map, rev_label_map
