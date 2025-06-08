# Weaviate Multi Vector exmaple

🎯 Overview
-----------

This is a simple demo of how one can run Weaviate and ColPali (ColQwen2) model and perform similarity search over PDF files.

📦 Requirements
----------------

In order to be able to create Weaviate one needs at least:

1. Docker
2. Python3

💡 Running
----------

In order to prepare your environment, issue:

```sh
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

or using uv:

```sh
uv venv --python 3.13
source .venv/bin/activate
uv pip install -r requirements.txt
```

📖 How to use notebooks
----------

Examples:

1. ColQwen2 example: ([colqwen2.ipynb](./colqwen2.ipynb))


🔗 Useful links
----------

- [Weaviate: More efficient multi-vector embeddings with MUVERA](https://weaviate.io/blog/muvera)
- [ColPali: Efficient Document Retrieval with Vision Language Models](https://arxiv.org/abs/2407.01449)
