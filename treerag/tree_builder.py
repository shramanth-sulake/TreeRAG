import re
from treerag.models import Node


def is_heading(line):
    """
    Detect headings like:
    1 Introduction
    1.1 Revenue
    2.3.4 Details
    """
    return bool(re.match(r'^(\d+(\.\d+)*)\s+.+', line))


def get_level(line):
    """
    Heading level based on number of dots
    """
    return line.split()[0].count('.') + 1


def build_tree(pages):
    root = Node("ROOT", level=0, page_number=0)
    stack = [root]

    for page in pages:
        lines = page["text"].split("\n")

        for line in lines:
            line = line.strip()

            if not line:
                continue

            if is_heading(line):
                level = get_level(line)
                node = Node(line, level, page["page_number"])

                # Find correct parent
                while stack and stack[-1].level >= level:
                    stack.pop()

                stack[-1].add_child(node)
                stack.append(node)

            else:
                # Add content to current node
                if stack:
                    stack[-1].content += line + " "

    return root