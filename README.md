# zero-to-hero-ai

Working through Andrej Karpathy's [Neural Networks: Zero to Hero](https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ) lecture series. Started January 2026 as the foundation phase of a transition from backend systems engineering toward ML systems infrastructure.

The work here is hands-on reimplementation: I followed each lecture by typing out the code, running it, breaking it, and going down side-rabbit-holes (KV caching, FlashAttention, PagedAttention) when something piqued my interest. The goal was understanding the substrate of modern transformer training and inference at the level of "I can rebuild this from scratch," not at the level of "I can call a library."

## Contents

- `01_micrograd/` — scalar autograd engine following lecture 1
- `02_makemore/` — bigram and statistical character-level models
- `03_makemore_mlp/` — MLP-based character model (lectures 3-5)
- `04_batchnorm/` — diving into batch normalization internals
- `07_gpt/` — toy GPT trained on Tiny Shakespeare. `bigram.py` is the starting point; `v2.py` adds multi-head self-attention, residual connections, layer norm, and a generation loop.
- `labs/` — adjacent experiments (Docker learning)

## Status

Complete. Foundational learning phase (Jan-Feb 2026). See [cuda-kernels](https://github.com/jonathangao91/cuda-kernels) for current work.

Companion blog: jonathangao.bearblog.dev