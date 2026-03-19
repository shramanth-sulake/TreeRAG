import re


def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    return text


def compute_confidence(question, nodes, paths):
    question_words = clean_text(question).split()

    total_score = 0

    for node in nodes:
        title = clean_text(node.title)

        match_score = sum(1 for word in question_words if word in title)

        total_score += match_score

    # average match
    avg_match = total_score / max(len(nodes), 1)

    # depth score (longer path = deeper)
    avg_depth = sum(len(p) for p in paths) / max(len(paths), 1)

    # normalize (simple heuristic)
    confidence = (avg_match * 0.6) + (avg_depth * 0.4)

    # scale to percentage
    confidence = min(confidence / 5, 1.0)  # normalize

    return round(confidence * 100, 2)