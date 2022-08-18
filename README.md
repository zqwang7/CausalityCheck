# Causality Check in Frame-online Speech Separation

Many recent speech separation challenges require frame-online processing with a strict constraint on algorithmic latency, which equals the allowed amount of future context to be used for separation.

For example, the [Clarity challenge](https://claritychallenge.org/docs/cec2/taking_part/cec2_rules#computational-restrictions) requires that, to obtain the separation result at the current sample, the separation model cannot use information >= 5 ms into the future.

Simiar constraint can be found in the recent [DNS challenges](https://www.microsoft.com/en-us/research/academic-program/deep-noise-suppression-challenge-icassp-2022/).

Such constraints are often unconsciously violated by challenge participants, resulting in unfair rankings and misleading comparison among different submissions.

This code provides one example to verify whether a separation model peeks future context beyond the allowed range.

## Citations

```
@inproceedings{Wang2022,
author = {Wang, Zhong-Qiu and Wichern, Gordon and {Le Roux}, Jonathan and Watanabe, Shinji},
booktitle = {arXiv preprint arXiv:2204.09911},
title = {{STFT-Domain Neural Speech Enhancement with Very Low Algorithmic Latency}},
year = {2022}
url={https://arxiv.org/abs/2204.09911}
}

```
