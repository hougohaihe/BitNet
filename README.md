# bitnet.cpp
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
![version](https://img.shields.io/badge/version-1.0-blue)

[<img src="./assets/header_model_release.png" alt="BitNet Model on Hugging Face" width="800"/>](https://huggingface.co/microsoft/BitNet-b1.58-2B-4T)

Try it out via this [demo](https://demo-bitnet-h0h8hcfqeqhrf5gf.canadacentral-01.azurewebsites.net/), or build and run it on your own [CPU](https://github.com/microsoft/BitNet?tab=readme-ov-file#build-from-source) or [GPU](https://github.com/microsoft/BitNet/blob/main/gpu/README.md).

bitnet.cpp is the official inference framework for 1-bit LLMs (e.g., BitNet b1.58). It offers a suite of optimized kernels, that support **fast** and **lossless** inference of 1.58-bit models on CPU and GPU (NPU support will coming next).

The first release of bitnet.cpp is to support inference on CPUs. bitnet.cpp achieves speedups of **1.37x** to **5.07x** on ARM CPUs, with larger models experiencing greater performance gains. Additionally, it reduces energy consumption by **55.4%** to **70.0%**, further boosting overall efficiency. On x86 CPUs, speedups range from **2.37x** to **6.17x** with energy reductions between **71.9%** to **82.2%**. Furthermore, bitnet.cpp can run a 100B BitNet b1.58 model on a single CPU, achieving speeds comparable to human reading (5-7 tokens per second), significantly enhancing the potential for running LLMs on local devices. Please refer to the [technical report](https://arxiv.org/abs/2410.16144) for more details.

**Latest optimization** introduces parallel kernel implementations with configurable tiling and embedding quantization support, achieving **1.15x to 2.1x** additional speedup over the original implementation across different hardware platforms and workloads. For detailed technical information, see the [optimization guide](src/README.md).

<img src="./assets/performance.png" alt="performance_comparison" width="800"/>


## Demo

A demo of bitnet.cpp running a BitNet b1.58 3B model on Apple M2:

https://github.com/user-attachments/assets/7f46b736-edec-4828-b809-4be780a3e5b1

## Personal Notes

> **Fork notes (for my own reference):** I'm using this primarily to experiment with the 2B model locally on my x86 Linux machine. The `src/README.md` optimization guide is especially useful — I saw ~1.8x speedup with tiling enabled on my Ryzen 7. Next I want to try the GPU kernel on my RTX 3070.
>
> **RTX 3070 GPU results (updated):** Got the GPU kernel working. Using `--n-gpu-layers 32` gave me roughly 28 tok/s on the 2B model — noticeably faster than CPU-only. Had to build with `-DGGML_CUDA=ON` and make sure CUDA 12.x was on PATH. Worth it.
>
> **Context length experiment:** Tried bumping `--ctx-size` from the default 2048 up to 4096 on the 2B model. Still fits in VRAM on the 3070 (8GB) with a bit of headroom. Response quality on longer prompts noticeably improved. Keeping 4096 as my personal default going forward.
>
> **Batch size tuning:** Experimented with `--batch-size` (prompt eval batch size). Default is 512; bumping to 1024 shaved a second or two off prompt processing on longer inputs with no stability issues. Will keep 1024 as my default for interactive use.
