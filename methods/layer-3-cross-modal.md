# Layer 3: Cross-Modal Consistency

[Back to methods](README.md) · [Back to home](../README.md)

Within-video multimodal verification. The detector asks whether audio, speech, text, and visual evidence all describe the same event, speaker, and semantics.

## Subcategory Guide

- **A. Audio-visual consistency detection**: Synchrony, symbolic lip-sync, and voice-face identity coherence.
- **B. Text-video semantic consistency reasoning**: Caption, transcript, or prompt semantics checked against visual evidence.
- **C. Robust learning and temporal localization**: Localization-oriented multimodal learning under sparse inconsistency.

## A. Audio-visual consistency detection

Synchrony, symbolic lip-sync, and voice-face identity coherence.

| Date | Method | Paper | Cue | Input | Mechanism | Output | Venue |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 03/2026 | X-AVDT | [X-AVDT: Audio-Visual Cross-Attention for Robust Deepfake Detection](https://doi.org/10.48550/ARXIV.2603.08483)<br>Kim et al. | Generator-internal audio-visual correspondence | Speech+Face | DDIM inversion + cross-attention probing | Score | CVPR |
| 01/2026 | ConLLM | [Revealing the Truth with ConLLM for Detecting Multi-Modal Deepfakes](https://doi.org/10.48550/ARXIV.2601.17530)<br>Kashyap et al. | Multimodal semantic inconsistency | Speech+Face | Contrastive alignment + LLM reasoning | Score | arXiv |
| 10/2025 | PIA | [PIA: Deepfake Detection Using Phoneme-Temporal and Identity-Dynamic Analysis](https://arxiv.org/abs/2510.14241)<br>Datta et al. | Phoneme-timing mismatch + ID dynamics | Speech+Lip | Phoneme timing + ID dynamics | Score | arXiv |
| 10/2025 | KLASSify to Verify | [KLASSify to Verify: Audio-Visual Deepfake Detection Using SSL-based Audio and Handcrafted Visual Features](https://arxiv.org/abs/2508.07337)<br>Kukanov et al. | Robust audio-visual cues (unseen attacks) | Speech+Face | Audio SSL + graph attn + handcrafted | Score+loc. | arXiv |
| 05/2025 | CAD | [CAD: A General Multimodal Framework for Video Deepfake Detection via Cross-Modal Alignment and Distillation](https://arxiv.org/abs/2505.15233)<br>Du et al. | Semantic audio-visual misalignment + cues | Speech+Face | Alignment + distillation | Score | arXiv |
| 04/2025 | Multi-task Audio-Visual Prompt Learning | [Multi-modal deepfake detection via multi-task audio-visual prompt learning](https://doi.org/10.1609/aaai.v39i1.32042)<br>Miao et al. | Fine-grained audio-visual consistency | Speech+Face | Prompting + matching loss + fusion | Score | AAAI |
| 06/2024 | Lost in Translation | [Lost in Translation: Lip-Sync Deepfake Detection from Audio-Video Mismatch](https://doi.org/10.1109/cvprw63382.2024.00435)<br>Bohacek et al. | Language-aware audio-visual mismatch | Speech+Lip | Language-conditioned lip-sync | Score | CVPR |
| 06/2024 | AVFF | [AVFF: Audio-Visual Feature Fusion for Video Deepfake Detection](https://arxiv.org/abs/2406.02951)<br>Oorloff et al. | Intrinsic audio-visual correspondences | Speech+Face | Real-only SSL pretrain + classifier | Score | arXiv |
| 06/2024 | Zero-Shot AV Consistency | [Zero-Shot Fake Video Detection by Audio-Visual Consistency](https://arxiv.org/abs/2406.07854)<br>Li et al. | Zero-shot audio-visual mismatch | Speech+Face | Consistency checking without task-specific training | Score | arXiv |
| 11/2023 | Voice-Face Homogeneity | [Voice-Face Homogeneity Tells Deepfake](https://arxiv.org/abs/2203.02195)<br>Cheng et al. | Voice-face identity coherence | Voice+Face-ID | Compare voice and face-ID embeddings | Score | arXiv |
| 10/2023 | Integrated AV Features | [Integrating Audio-Visual Features for Multimodal Deepfake Detection](https://arxiv.org/abs/2310.03827)<br>Muppalla et al. | Joint audio-visual feature alignment | Speech+Face | Integrated multimodal feature fusion | Score | arXiv |
| 11/2022 | Lip Sync Matters | [Lip Sync Matters: A Novel Multimodal Forgery Detector](https://doi.org/10.23919/APSIPAASC55919.2022.9980296)<br>Shahzad et al. | Symbolic lip-sync mismatch | Speech+Lip | Token and phoneme sequence comparison | Score | APSIPA ASC |
| 04/2022 | Person-of-Interest Detection | [Audio-Visual Person-of-Interest DeepFake Detection](https://arxiv.org/abs/2204.03083)<br>Cozzolino et al. | Person-centric audio-visual mismatch | Speech+Face | Person-of-interest multimodal verification | Score | arXiv |
| 03/2022 | Audio-Visual Attention | [An Audio-Visual Attention Based Multimodal Network for Fake Talking Face Videos Detection](https://arxiv.org/abs/2203.05178)<br>Wang et al. | Cross-modal alignment | Speech+Face | Cross-attention fusion | Score | arXiv |
| 10/2021 | Joint Audio-Visual Detection | [Joint Audio-Visual Deepfake Detection](https://doi.org/10.1109/ICCV48922.2021.01453)<br>Zhou et al. | Audio-visual synchrony and semantics | Speech+Face | Joint synchrony+semantic modeling | Score | ICCV |
| 07/2021 | Self-Supervised Decoupling | [DeepFake Videos Detection Using Self-Supervised Decoupling Network](https://doi.org/10.1109/ICME51207.2021.9428368)<br>Zhang et al. | Audio-visual consistency through self-supervision | Speech+Face | Self-supervised decoupling of multimodal cues | Score | ICME |
| 06/2021 | Aural-Oral Dynamics | [Detecting Deep-Fake Videos From Aural and Oral Dynamics](https://doi.org/10.1109/cvprw53098.2021.00109)<br>Agarwal et al. | Aural-oral dynamics coherence | Speech+Lip | Audio+mouth dynamics features | Score | CVPR |
| 12/2020 | Dynamic Lip Movement | [Preventing DeepFake Attacks on Speaker Authentication by Dynamic Lip Movement Analysis](https://api.semanticscholar.org/CorpusID:230998982)<br>Yang et al. | Lip motion vs. speech mismatch | Speech+Lip | Lip-motion dynamics analysis | Score | IEEE TIFS |
| 10/2020 | Not Made for Each Other | [Not made for each other- Audio-Visual Dissonance-based Deepfake Detection and Localization](https://doi.org/10.1145/3394171.3413700)<br>Chugh et al. | Audio-visual dissonance | Speech+Face | Cross-modal mismatch + localization | Score+loc. | ACM MM |

## B. Text-video semantic consistency reasoning

Caption, transcript, or prompt semantics checked against visual evidence.

| Date | Method | Paper | Cue | Input | Mechanism | Output | Venue |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 07/2025 | T^3SVFND | [T^3SVFND: Towards an Evolving Fake News Detector for Emergencies with Test-time Training on Short Video Platforms](https://arxiv.org/abs/2507.20286)<br>Wang et al. | Event-shifted semantics | Video+Text | Test-time MLM reconstruction | Score | arXiv |
| 06/2025 | CSCL | [Unleashing the Potential of Consistency Learning for Detecting and Grounding Multi-Modal Media Manipulation](https://arxiv.org/abs/2506.05890)<br>Liu et al. | Text-image inconsistency grounding | Frame+Text | Cascaded consistency decoders | Score+loc. | arXiv |
| 04/2025 | CA-FVD | [Consistency-aware Fake Videos Detection on Short Video Platforms](https://arxiv.org/abs/2504.21495)<br>Zhang et al. | Video-text semantic mismatch | Video+Text | VLM pseudo-labels + consistency loss | Score | arXiv |

## C. Robust learning and temporal localization

Localization-oriented multimodal learning under sparse inconsistency.

| Date | Method | Paper | Cue | Input | Mechanism | Output | Venue |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 02/2026 | Divide and Conquer | [Divide and Conquer: Multimodal Video Deepfake Detection via Cross-Modal Fusion and Localization](https://doi.org/10.48550/ARXIV.2602.00209)<br>Li et al. | Cross-modal fusion + temporal localization | Speech+Face | Unimodal detectors + score fusion | Score+loc. | arXiv |
| 01/2026 | A-V Shift Prediction | [A-V Representation Learning via Audio Shift Prediction for Multimodal Deepfake Detection and Temporal Localization](https://wacv.thecvf.com/Conferences/2026/AcceptedPapers)<br>Anshul et al. | Temporal audio-visual perturbation cues | Speech+Face | Audio shift prediction + localization | Score+loc. | WACV |
| 10/2025 | HOLA | [HOLA: Enhancing Audio-visual Deepfake Detection via Hierarchical Contextual Aggregations and Efficient Pre-training](https://arxiv.org/abs/2507.22781)<br>Wu et al. | Hierarchical audio-visual aggregation | Speech+Face | SSL pretrain + gated aggregation | Score | arXiv |
| 10/2025 | Weakly-Supervised Temporal Localization | [A Multimodal Deviation Perceiving Framework for Weakly-Supervised Temporal Forgery Localization](http://dx.doi.org/10.1145/3746027.3755534)<br>Xu et al. | Sparse multimodal deviations | Speech+Face | Weak supervision + deviation modeling | Score+loc. | ACM MM |
| 08/2025 | SpeechForensics | [SpeechForensics: Audio-Visual Speech Representation Learning for Face Forgery Detection](https://arxiv.org/abs/2508.09913)<br>Liang et al. | Real-only audio-visual repr. learning | Speech+Lip | SSL pretrain on real + fine-tune | Score | arXiv |
| 08/2025 | WMMT | [Weakly Supervised Multimodal Temporal Forgery Localization via Multitask Learning](https://arxiv.org/abs/2508.02179)<br>Xu et al. | Weakly-sup. temporal loc. | Speech+Face | Multitask + MoE + deviation loss | Score+loc. | arXiv |
| 06/2025 | Circumventing Shortcuts | [Circumventing Shortcuts in Audio-visual Deepfake Detection Datasets with Unsupervised Learning](https://arxiv.org/abs/2412.00175)<br>Smeu et al. | Shortcut-robust audio-visual reps (silence) | Speech+Face | Real-only SSL audio-visual alignment | Score | CVPR |
| 04/2025 | Audio-Visual Local Inconsistencies | [Audio-Visual Deepfake Detection With Local Temporal Inconsistencies](https://arxiv.org/abs/2501.08137)<br>Astrid et al. | Local temporal audio-visual inconsistency | Speech+Face | Local inconsistency + localization | Score+loc. | arXiv |
| 11/2024 | DiMoDif | [DiMoDif: Discourse Modality-information Differentiation for Audio-visual Deepfake Detection and Localization](https://arxiv.org/abs/2411.10193)<br>Koutlis et al. | Modality-specific localization under mismatch | Speech+Face | Modality-information differentiation | Score+loc. | arXiv |
| 04/2024 | Cross- and Within-Modality Regularization | [Cross-Modality and Within-Modality Regularization for Audio-Visual DeepFake Detection](https://arxiv.org/abs/2401.05746)<br>Zou et al. | Modality separation under perturb. | Speech+Face | Audio-visual Transformer + cross and within regs | Score | arXiv |
| 06/2023 | AV Anomaly Detection | [Self-supervised video forensics by audio-visual anomaly detection](https://doi.org/10.1109/cvpr52729.2023.01011)<br>Feng et al. | Self-supervised multimodal anomaly cues | Speech+Face | Audio-visual anomaly detection | Score | CVPR |

<details>
<summary>Additional cited works discussed in this layer</summary>

- [Leveraging Large Multimodal Models for Audio-Video Deepfake Detection: A Pilot Study](https://doi.org/10.48550/ARXIV.2602.23393) (Cao et al. · ICASSP)

</details>
