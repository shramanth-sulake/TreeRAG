# 🧠 TreeRAG: Document Navigator and Answer Generator
TreeRAG is a cutting-edge document navigator and answer generator that utilizes a tree-like structure to represent documents and provide answers to user-inputted questions. The system is designed to navigate the tree structure to find relevant information and generate answers based on the content of the document. With its advanced features and user-friendly interface, TreeRAG is an ideal solution for anyone looking to efficiently navigate and understand complex documents.

## 🚀 Features
- **Document Navigation**: TreeRAG allows users to navigate documents in a tree-like structure, making it easy to find relevant information.
- **Answer Generation**: The system generates answers to user-inputted questions based on the content of the document.
- **Confidence Scoring**: TreeRAG evaluates the confidence of the generated answers based on their relevance to the question.
- **Large Language Model Integration**: The system uses a Large Language Model (LLM) to generate answers, providing more accurate and informative responses.
- **Fallback Summarization**: If the LLM is not available, TreeRAG uses a simple summarization method to generate answers.

## 🛠️ Tech Stack
- **Frontend**: Streamlit
- **Backend**: Python
- **Database**: None
- **AI Tools**: OpenAI API
- **Build Tools**: None
- **Libraries**: PyMuPDF, `re`, `dotenv`, `openai`

## 📦 Installation
To install TreeRAG, follow these steps:
1. Clone the repository using `git clone`.
2. Install the required libraries using `pip install -r requirements.txt`.
3. Set up your environment variables using a `.env` file.

## 💻 Usage
To use TreeRAG, follow these steps:
1. Run the application using `streamlit run app.py`.
2. Load a document using the file uploader.
3. Input a question in the question box.
4. View the generated answer, reasoning paths, and confidence level.

## 📂 Project Structure
```markdown
.
├── app.py
├── main.py
├── treerag
│   ├── __init__.py
│   ├── answerer.py
│   ├── models.py
│   ├── navigator.py
│   ├── parser.py
│   ├── scorer.py
│   └── tree_builder.py
├── requirements.txt
└── README.md
```


## 🤝 Contributing
To contribute to TreeRAG, please submit a pull request with your changes. Make sure to follow the standard professional guidelines for commit messages and code formatting.
