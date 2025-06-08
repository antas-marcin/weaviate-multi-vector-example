# Weaviate Multi Vector example

🎯 Overview
-----------

This is a simple demo of how one can use Weaviate and ColPali (ColQwen2) models and perform similarity search over PDF files.

📦 Requirements
----------------

1. Docker
2. Python3

💡 Prepare local environment
----------------------------

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

📖 Examples
----------

1. ColQwen2 example: ([colqwen2.ipynb](./colqwen2.ipynb))


🔗 Useful links
----------

- [Weaviate: More efficient multi-vector embeddings with MUVERA](https://weaviate.io/blog/muvera)
- [ColPali: Efficient Document Retrieval with Vision Language Models](https://arxiv.org/abs/2407.01449)
