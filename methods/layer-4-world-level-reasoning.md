# Layer 4: Language-Guided World-Level Reasoning

[Back to methods](README.md) · [Back to home](../README.md)

World-grounded verification. The detector moves beyond within-video agreement and asks whether the implied claims remain consistent with external facts, commonsense, physical rules, and explicit evidence chains.

## Subcategory Guide

- **A. Prompts and adapters for representation calibration**: Language priors and lightweight tuning to bind forgery evidence to semantic hypotheses.
- **B. Tool-augmented agents for evidence gathering**: Observe-tool-integrate pipelines, retrieval, and modular analyzers.
- **C. Post-training, preferences and rewards**: Post-training for explainable reasoning, preference alignment, and reward modeling.

## July 2026 refresh

These methods use language to calibrate forgery representations, explain localized evidence, retrieve external support, or reason over physical and social claims. VLAForge is Layer 4 rather than Layer 3 because text is a representation prior, not an observed stream whose consistency is tested.

| Date | Method | Paper | Decisive mechanism | Output | Venue |
| --- | --- | --- | --- | --- | --- |
| 05/2026 | Artifact-Bench | [Artifact-Bench: Evaluating MLLMs on Detecting and Assessing the Artifacts of AI-Generated Videos](https://arxiv.org/abs/2605.18984)<br>Tang et al. | MLLM classification, comparison, and fine-grained artifact diagnosis | Verdict+exp. | arXiv |
| 04/2026 | DVAR | [DVAR: Adversarial Multi-Agent Debate for Video Authenticity Detection](https://arxiv.org/abs/2604.16987)<br>Qi et al. | Competing natural/generative agents, GenVideoKB, and MDL adjudication | Verdict+exp. | arXiv |
| 07/2026 | Hermes | [Hermes: An Evidence-Driven Agentic Framework for Trustworthy and Explainable AI-Generated Video Detection](https://icml.cc/virtual/2026/poster/61817)<br>Li et al. | Retrieved evidence graphs and deliberation | Verdict+exp. | ICML |
| 07/2026 | SafeGuard | [SafeGuard: A Multi-Agent Perception-Reasoning Framework for Social-Risk AI-Generated Video Detection](https://arxiv.org/abs/2607.03069)<br>Wu et al. | Forensic agents plus physical/social-risk reasoning | Verdict+exp. | arXiv; ECCV author-reported |
| 06/2026 | FLARE | [From Detector Evidence to Language: Explainable Deepfake Video Detection](https://openaccess.thecvf.com/content/CVPR2026W/FoundGen-Bio/html/Panahi_From_Detector_Evidence_to_Language_Explainable_Deepfake_Video_Detection_CVPRW_2026_paper.html)<br>Panahi et al. | Detector evidence maps ground VLM explanations | Verdict+loc.+exp. | CVPRW |
| 06/2026 | VMD-FACT | [VMD-FACT: A New Video Dataset and MLLM-Based Method for Detecting Realistic AI-Generated Video Misinformation](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_VMD-FACT_A_New_Video_Dataset_and_MLLM-based_method_for_Detecting_CVPR_2026_paper.html)<br>Zhang et al. | Multimodal evidence and fact-check graphs | Verdict+exp. | CVPR |
| 06/2026 | MSLoc | [Explainable Forensics of Manipulated Segments in Untrimmed Long Videos](https://arxiv.org/abs/2606.02402)<br>Feng et al. | MLLM proposal refinement and rationales | Verdict+loc.+exp. | ICML |
| 05/2026 | CoCoDetect | [CoCoVideo: The High-Quality Commercial-Model-Based Contrastive Benchmark for AI-Generated Video Detection](https://openaccess.thecvf.com/content/CVPR2026/html/Feng_CoCoVideo_The_High-Quality_Commercial-Model-Based_Contrastive_Benchmark_for_AI-Generated_Video_Detection_CVPR_2026_paper.html)<br>Feng et al. | MLLM reasoning for uncertain temporal cases | Verdict+exp. | CVPR |
| 03/2026 | VLAForge | [Unleashing Vision-Language Semantics for Deepfake Video Detection](https://openaccess.thecvf.com/content/CVPR2026/html/Zhu_Unleashing_Vision-Language_Semantics_for_Deepfake_Video_Detection_CVPR_2026_paper.html)<br>Zhu et al. | Identity-aware language calibration | Score | CVPR |
| 03/2026 | GenVideoLens | [GenVideoLens: Where LVLMs Fall Short in AI-Generated Video Detection?](https://arxiv.org/abs/2603.18625)<br>Zou et al. | Fine-grained perceptual, optical, physical, and temporal diagnosis | Verdict+exp. | arXiv |
| 03/2026 | ForensicZip | [ForensicZip: More Tokens are Better but Not Necessary in Forensic Vision-Language Models](https://arxiv.org/abs/2603.12208)<br>Lai et al. | Temporal-token transport for efficient forensic VLMs | Verdict | arXiv |

## A. Prompts and adapters for representation calibration

Language priors and lightweight tuning to bind forgery evidence to semantic hypotheses.

| Date | Method | Paper | Base model / system | Training | Output | Venue |
| --- | --- | --- | --- | --- | --- | --- |
| 07/2025 | LVLMDFD | [Unlocking the Capabilities of Large Vision-Language Models for Generalizable and Explainable Deepfake Detection](https://proceedings.mlr.press/v267/yu25d.html)<br>Yu et al. | LVLM + LLM | Detector+prompt learner | Verdict+loc.+exp. | ICML |
| 06/2025 | AuthGuard | [AuthGuard: Generalizable Deepfake Detection via Language Guidance](https://arxiv.org/abs/2506.04501)<br>Shen et al. | Vision encoder + LLM | Cls+ITC; uncertainty | Verdict+exp. | arXiv |
| 04/2025 | RepDFD | [Standing on the Shoulders of Giants: Reprogramming Visual-Language Model for General Deepfake Detection](https://ojs.aaai.org/index.php/AAAI/article/view/32559)<br>Lin et al. | Frozen VLM | Prompt tuning | Label | AAAI |
| 01/2025 | DeepFake-Adapter | [DeepFake-Adapter: Dual-Level Adapter for DeepFake Detection](http://dx.doi.org/10.1007/s11263-024-02274-6)<br>Shao et al. | ViT (frozen) | Adapter tuning | Frame label (agg.) | IJCV |
| 11/2024 | CPML | [Prompt-guided Multi-modal contrastive learning for Cross-compression-rate Deepfake Detection](https://papers.bmvc2024.org/0619.pdf)<br>Lai et al.<br><br>[On Using rPPG Signals for DeepFake Detection: A Cautionary Note](https://doi.org/10.1007/978-3-031-43153-1_20)<br>D'Amelio et al. | rPPG+landmark encoder | Prompt-guided | Score | BMVC<br>ICIAP |
| 06/2024 | ChatGPT Detect | [Can ChatGPT Detect DeepFakes? A Study of Using Multimodal Large Language Models for Media Forensics](https://openaccess.thecvf.com/content/CVPR2024W/WMF/papers/Jia_Can_ChatGPT_Detect_DeepFakes_A_Study_of_Using_Multimodal_Large_CVPRW_2024_paper.pdf)<br>Jia et al.<br><br>[How Good is ChatGPT at Audiovisual Deepfake Detection: A Comparative Study of ChatGPT, AI Models and Human Perception](https://www.nowpublishers.com/article/OpenAccessDownload/SIP-20250004)<br>Shahzad et al. | ChatGPT | Prompt | Verdict+exp. | CVPR<br>APSIPA Transactions on Signal and Information Processing |

## B. Tool-augmented agents for evidence gathering

Observe-tool-integrate pipelines, retrieval, and modular analyzers.

| Date | Method | Paper | Base model / system | Training | Output | Venue |
| --- | --- | --- | --- | --- | --- | --- |
| 12/2025 | DeepAgent | [DeepAgent: A Dual Stream Multi Agent Fusion for Robust Multimodal Deepfake Detection](https://arxiv.org/abs/2512.07351)<br>Zaman et al. | Multi-agent pipeline | Not stated | MM verdict | arXiv |
| 08/2025 | FakeHunter | [Memory-Anchored Multimodal Reasoning for Explainable Video Forensics](https://arxiv.org/abs/2508.14581)<br>Chen et al. | Vision+audio encoders + VLM agent | Agent+retrieval | Verdict+evidence | arXiv |
| 06/2025 | DAVID-XR1 | [DAVID-XR1: Detecting AI-Generated Videos with Explainable Reasoning](https://arxiv.org/abs/2506.14827)<br>Gao et al. | Video VLM | SFT | Loc.+defect reasoning | arXiv |
| 02/2025 | LAVID | [LAVID: An Agentic LVLM Framework for Diffusion-Generated Video Detection](https://arxiv.org/abs/2502.14994)<br>Liu et al. | LVLM agent + tools | Tool loop | Verdict+evidence | arXiv |

## C. Post-training, preferences and rewards

Post-training for explainable reasoning, preference alignment, and reward modeling.

| Date | Method | Paper | Base model / system | Training | Output | Venue |
| --- | --- | --- | --- | --- | --- | --- |
| 02/2026 | VideoVeritas | [VideoVeritas: AI-Generated Video Detection via Perception Pretext Reinforcement Learning](https://doi.org/10.48550/ARXIV.2602.08828)<br>Tan et al. | Video MLLM | Pref. align + PPRL | Verdict+reasoning | arXiv |
| 12/2025 | Skyra and Skyra-RL | [Skyra: AI-Generated Video Detection via Grounded Artifact Reasoning](https://arxiv.org/abs/2512.15693)<br>Li et al. | Qwen2.5-VL | SFT -> RL | Verdict+grounded reasoning | arXiv |
| 10/2025 | VidGuard-R1 | [VidGuard-R1: AI-Generated Video Detection and Explanation via Reasoning MLLMs and RL](https://arxiv.org/abs/2510.02282)<br>Park et al. | Qwen2.5-VL | SFT -> DPO -> GRPO | Verdict+exp. | arXiv |
| 10/2025 | EDVD-LLaMA | [EDVD-LLaMA: Explainable Deepfake Video Detection via Multimodal Large Language Model Reasoning](https://arxiv.org/abs/2510.16442)<br>Sun et al. | Qwen2.5-7B + video encoder | SFT | Verdict+exp. | arXiv |
| 09/2025 | DeeptraceReward | [Learning Human-Perceived Fakeness in AI-Generated Videos via Multimodal LLMs](https://arxiv.org/abs/2509.22646)<br>Fu et al. | VideoLLaMA3 and Qwen2.5-VL with reward modeling | Reward-model train | Reward | arXiv |
| 08/2025 | VERITAS | [Veritas: Generalizable Deepfake Detection via Pattern-Aware Reasoning](https://arxiv.org/abs/2508.21048)<br>Tan et al. | InternVL3 and Qwen2.5-VL | SFT -> MiPO -> P-GRPO | Verdict+exp. | arXiv |
| 07/2025 | BusterX++ | [BusterX++: Towards Unified Cross-Modal AI-Generated Content Detection and Explanation with MLLM](https://arxiv.org/abs/2507.14632)<br>Wen et al. | Qwen2.5-VL | RL -> SFT -> RL | Verdict+struct. exp. | arXiv |
| 05/2025 | BusterX | [BusterX: MLLM-Powered AI-Generated Video Forgery Detection and Explanation](https://arxiv.org/abs/2505.12620)<br>Wen et al. | Qwen2.5-VL | SFT -> RL | Verdict+exp. | arXiv |
| 10/2024 | X2-DFD | [X2-DFD: A framework for eXplainable and eXtendable Deepfake Detection](https://arxiv.org/abs/2410.06126)<br>Chen et al. | LLaVA + aux detectors | SFT (explainable data) | Verdict+exp. | arXiv |

<details>
<summary>Additional cited works discussed in this layer</summary>

- [Do generative video models understand physical principles?](https://arxiv.org/abs/2501.09038) (Motamed et al. · arXiv)

</details>
