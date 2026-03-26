# Adjacent Diagnostics

[Back to benchmarks](README.md) · [Back to home](../README.md)

These resources are not only detector leaderboards. They broaden evaluation toward physical-rule testing, world-dynamics probes, and explanation-oriented diagnosis that are increasingly relevant to AIGC-V detection.

## A. Physical Rule Violations

Stress tests for physical commonsense, impossible scenarios, and localized physics failures.

| Date | Resource | Paper | Type | Focus | Venue |
| --- | --- | --- | --- | --- | --- |
| 03/2026 | Physion-Eval | [Physion-Eval: Evaluating Physical Realism in Generated Video via Human Reasoning](https://arxiv.org/abs/2603.19607)<br>Zhang et al. | Eval | Provides expert reasoning traces, localized physical glitches, and explanations for physical-realism failures in generated videos. | arXiv |
| 01/2026 | VideoPhy-2 | [VideoPhy-2: A Challenging Action-Centric Physical Commonsense Evaluation in Video Generation](https://openreview.net/forum?id=P8vQYmq3TB)<br>Bansal et al. | Eval | Extends physical-commonsense evaluation to more challenging action-centric and interaction-heavy generated videos. | ICLR |
| 07/2025 | PhyWorldBench | [PhyWorldBench: A Physical Realism Benchmark for Text-to-Video Generation](https://arxiv.org/abs/2507.13428)<br>Gu et al. | Eval | Evaluates physical realism of text-to-video models with physics-grounded prompts and anti-physics stress cases. | arXiv |
| 05/2025 | T2VPhysBench | [T2VPhysBench: A First-Principles Benchmark for Physical Consistency in Text-to-Video Generation](https://arxiv.org/abs/2505.00337)<br>Guo et al. | Eval | Tests first-principles physical consistency in text-to-video generation, including counterfactual robustness and state-transition fidelity. | arXiv |
| 04/2025 | Morpheus | [Morpheus: Benchmarking Physical Reasoning of Video Generative Models with Real Physical Experiments](https://arxiv.org/abs/2504.02918)<br>Zhang et al. | Eval | Benchmarks physical reasoning of video generative models with real physical experiments and measurable conservation-law violations. | arXiv |
| 03/2025 | IPV-Bench (Impossible Videos) | [Impossible Videos](https://proceedings.mlr.press/v267/bai25a.html)<br>Bai et al. | Eval | Designs impossible scenarios across physical, geographical, biological, and social domains for stress testing generated videos. | ICML |
| 01/2025 | Physics-IQ | [Do generative video models understand physical principles?](https://arxiv.org/abs/2501.09038)<br>Motamed et al. | Eval | Probes whether text-to-video models obey basic physical principles under controlled prompts. | arXiv |
| 06/2024 | VideoPhy | [VideoPhy: Evaluating Physical Commonsense for Video Generation](https://openreview.net/forum?id=5MWhU3t7WR)<br>Bansal et al. | Eval | Benchmarks whether generated videos satisfy physical commonsense about objects, attributes, and interactions. | ICLR |

## B. World Dynamics and Causality

Benchmarks for simulator-like consistency, temporal causality, and hidden world semantics.

| Date | Resource | Paper | Type | Focus | Venue |
| --- | --- | --- | --- | --- | --- |
| 12/2025 | SVBench | [SVBench: Evaluation of Video Generation Models on Social Reasoning](https://arxiv.org/abs/2512.21507)<br>Peng et al. | Eval | Evaluates social reasoning in video generation, including intention, joint attention, norms, and prosocial behavior. | arXiv |
| 10/2025 | VideoVerse | [VideoVerse: How Far is Your T2V Generator from a World Model?](https://arxiv.org/abs/2510.08398)<br>Wang et al. | Eval | World-model-oriented benchmark with hidden semantics, event-level temporal causality, and world-knowledge questions. | arXiv |
| 07/2025 | T2VWorldBench | [T2VWorldBench: A Benchmark for Evaluating World Knowledge in Text-to-Video Generation](https://arxiv.org/abs/2507.18107)<br>Chen et al. | Eval | Evaluates world-knowledge generation across physics, nature, activity, culture, causality, and object domains. | arXiv |
| 12/2024 | StoryEval | [Is Your World Simulator a Good Story Presenter? A Consecutive Events-Based Benchmark for Future Long Video Generation](https://arxiv.org/abs/2412.16211)<br>Wang et al. | Eval | Benchmarks whether T2V models can present short stories composed of consecutive events for future long-video generation. | arXiv |
| 10/2024 | WorldSimBench | [WorldSimBench: Towards Video Generation Models as World Simulators](https://openreview.net/forum?id=4_hExrLJ7j)<br>Qin et al. | Eval | Evaluates whether video generators behave like world simulators by combining perceptual quality and embodied action consistency. | ICML |
| 10/2024 | Towards World Simulator (PhyGenBench) | [Towards World Simulator: Crafting Physical Commonsense-Based Benchmark for Video Generation](https://proceedings.mlr.press/v267/meng25c.html)<br>Meng et al. | Eval | Crafts a physical-commonsense benchmark for video generation with multi-step dynamics and simulator-style diagnostics. | ICML |

## C. Explanation-Oriented Diagnosis

Resources that turn implausibility judgment and explanation into an explicit evaluation target.

| Date | Resource | Paper | Type | Focus | Venue |
| --- | --- | --- | --- | --- | --- |
| 12/2025 | VideoHallu | [VideoHallu: Evaluating and Mitigating Multi-modal Hallucinations on Synthetic Video Understanding](https://openreview.net/forum?id=NoC9HT7Kf7)<br>Li et al. | Eval | Evaluates multimodal hallucination on synthetic videos and studies mitigation via targeted post-training. | NeurIPS |
| 12/2025 | PhyDetEx | [PhyDetEx: A Benchmark Dataset and Method for Detecting and Explaining Physical Plausibility in Text-to-Video Models](https://arxiv.org/abs/2512.01843)<br>Wang et al. | Method | Introduces a benchmark and trains models to detect and explain violated physical rules in text-to-video outputs. | arXiv |
| 11/2025 | SPOTLIGHT | [SPOTLIGHT: Identifying and Localizing Video Generation Errors Using VLMs](https://arxiv.org/abs/2511.18102)<br>Chinchure et al. | Eval | Fine-grained identification and localization of generation errors using VLMs. | arXiv |
| 10/2025 | TRAVL | [TRAVL: A Recipe for Making Video-Language Models Better Judges of Physics Implausibility](https://arxiv.org/abs/2510.07550)<br>Motamed et al. | Method | Adds intra-frame spatial and trajectory-guided temporal attention and fine-tunes on ImplausiBench to improve VLM judgments of physically implausible videos. | arXiv |
