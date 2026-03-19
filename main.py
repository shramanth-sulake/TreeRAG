from treerag.parser import extract_text_from_pdf
from treerag.tree_builder import build_tree
from treerag.navigator import navigate_tree
from treerag.answerer import generate_answer
from treerag.scorer import compute_confidence


def main():
    pdf_path = "data/sample.pdf"

    pages = extract_text_from_pdf(pdf_path)
    root = build_tree(pages)

    question = "What are the risks?"

    final_nodes, paths = navigate_tree(question, root)

    # 🧠 Generate final answer
    answer = generate_answer(question, final_nodes)

    print("\nQuestion:\n", question)

    print("\nReasoning Paths:\n")
    for path in paths:
        print(" → ".join(path))

    print("\nFinal Answer:\n")
    print(answer)

    confidence = compute_confidence(question, final_nodes, paths)
    print("\nConfidence:", confidence, "%")


if __name__ == "__main__":
    main()