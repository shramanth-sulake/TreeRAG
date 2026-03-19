import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # loads .env

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

import re

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)  # remove punctuation
    return text

def choose_sections(question, nodes):
    stopwords = {"what", "are", "the", "is", "in", "of", "and", "to"}

    question_words = [
        clean_text(word)
        for word in question.split()
        if word.lower() not in stopwords
    ]

    scored = []

    for node in nodes:
        title_clean = clean_text(node.title)

        score = 0

        for word in question_words:
            if word and word in title_clean:
                score += 2

        scored.append((score, node))

    # sort by score
    scored.sort(reverse=True, key=lambda x: x[0])

    # strong match
    if scored and scored[0][0] > 0:
        max_score = scored[0][0]
        return [node for score, node in scored if score == max_score]

    # fallback → best guess
    return [scored[0][1]]

def should_stop(node, question):
    """
    Decide whether current node is sufficient to answer the question
    """

    # clean text
    question_words = question.lower().split()
    title = node.title.lower()

    # ✅ if node title directly matches question intent → stop
    if any(word in title for word in question_words):
        return True

    # ✅ if no children → must stop
    if not node.children:
        return True

    # ❌ otherwise continue exploring
    return False

def navigate_tree(question, node, path=None):
    if path is None:
        path = []

    path.append(node.title)

    # 🧠 NEW: smarter stopping
    if should_stop(node, question):
        return [node], [path]

    selected_nodes = choose_sections(question, node.children)

    if not selected_nodes:
        return [node], [path]

    results = []
    paths = []

    for selected in selected_nodes:
        child_nodes, child_paths = navigate_tree(
            question,
            selected,
            path.copy()
        )

        results.extend(child_nodes)
        paths.extend(child_paths)

    return results, paths