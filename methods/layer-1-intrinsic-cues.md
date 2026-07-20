# Layer 1: Intrinsic Cues Analysis

[Back to methods](README.md) · [Back to home](../README.md)

Frame-level forensic evidence. The detector tests whether low-level visual signals still look like real captured video, including frequency fingerprints, local geometry, physiological traces, and cross-generator distribution gaps.

## Subcategory Guide

- **A. Pixel and geometric artifacts**: Frequency, texture, localization, and geometric plausibility cues.
- **B. Physiological features**: Blink, rPPG, heart-rate, and biological rhythm inconsistencies.
- **C. Distribution discrepancy and robustness**: Transfer-oriented modeling, adaptation, and robustness under shift.

## April--July 2026 additions

The eleven additions below entered after the March snapshot. They are assigned to Layer 1 because their decisive signal is frame-intrinsic, reference-based, or distributional; none requires temporal or cross-modal evidence at inference. Together with DFA (03/2026) in the canonical table below, they bring the 2026 Layer 1 snapshot to twelve representative methods.

| Date | Method | Paper | Decisive cue | Output | Venue |
| --- | --- | --- | --- | --- | --- |
| 05/2026 | SpecSem-Net | [SpecSem-Net: Integrating Spectral and Semantic Features for Robust AI-Generated Video Detection](https://arxiv.org/abs/2605.17311)<br>Wei et al. | Spectral denoising plus frame semantics | Score | arXiv |
| 05/2026 | VINA | [Video as Natural Augmentation: Towards Unified AI-Generated Image and Video Detection](https://arxiv.org/abs/2605.21977)<br>Li et al. | Causally regularized image--video distribution alignment | Score | arXiv |
| 05/2026 | Real Data Lies | [Real Data Lies: Unveiling and Closing the Quality Shortcut in Generalizable AI-Generated Video Detection](https://icml.cc/virtual/2026/poster/61218)<br>Fang et al. | Quality-matched real/fake distributions | Score | ICML |
| 05/2026 | Lightweight Cue Fusion | [Lightweight Complementary-Cue Fusion for Robust Video Face Forgery Detection](https://arxiv.org/abs/2605.29092)<br>Baek et al. | Wavelet-denoised, phase-spectrum, and LBP frame cues | Score | arXiv |
| 06/2026 | DFD-HR | [DFD-HR: Generalizable Deepfake Detection via Hierarchical Routing Learning](https://openaccess.thecvf.com/content/CVPR2026/html/Sun_DFD-HR_Generalizable_Deepfake_Detection_via_Hierarchical_Routing_Learning_CVPR_2026_paper.html)<br>Sun et al. | Adaptive depth pruning, token selection, and MoE routing | Score | CVPR |
| 06/2026 | QTFP | [Beyond &#91;CLS&#93; Token: Query-Driven Token-Level Forgery Purification for Generalizable Deepfake Detection](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_Beyond_CLS_Token_Query-Driven_Token-Level_Forgery_Purification_for_Generalizable_Deepfake_Detection_CVPR_2026_paper.html)<br>Wang et al. | Query-driven purification of local forgery tokens with video-level evaluation | Score | CVPR |
| 06/2026 | TSRL | [Tutor-Student Reinforcement Learning: A Dynamic Curriculum for Robust Deepfake Detection](https://openaccess.thecvf.com/content/CVPR2026/html/Lei_Tutor-Student_Reinforcement_Learning_A_Dynamic_Curriculum_for_Robust_Deepfake_Detection_CVPR_2026_paper.html)<br>Lei et al. | PPO tutor reweights hard-but-learnable video samples | Score | CVPR |
| 06/2026 | Forensic Rewiring | [Forensic Rewiring: Circuit-Level Shortcut Suppression for Generalizable Deepfake Detection](https://openaccess.thecvf.com/content/CVPR2026W/AIMS/html/A_Forensic_Rewiring_Circuit-Level_Shortcut_Suppression_for_Generalizable_Deepfake_Detection_CVPRW_2026_paper.html)<br>Nishitha A et al. | Shortcut-head attribution and selective gradient masking | Score | CVPRW |
| 06/2026 | Seeing the Unseen | [Seeing the Unseen: Enhancing Synthetic Video Detector Transferability to New AI Video Generation Models via Virtual Generators](https://doi.org/10.1145/3785353.3815083)<br>Vahdati et al. | Transferable synthetic-video forensic microstructures learned with virtual generators | Score | ACM IH&MMSec |
| 06/2026 | CUPID | [CUPID: Reconstructing UV Texture Maps for Interpretable Person-of-Interest Deepfake Detection](https://arxiv.org/abs/2606.20302)<br>Affatato et al. | Query-video UV textures matched to pristine POI references | Score+loc. | arXiv |
| 07/2026 | G2VD | [G2VD: Generalizable AI-Generated Video Detection via Counterfactual Intervention and Causal Disentanglement](https://arxiv.org/abs/2607.04607)<br>Du et al. | Counterfactual pixel/frequency disentanglement | Score | arXiv |
## A. Pixel and geometric artifacts

Frequency, texture, localization, and geometric plausibility cues.

| Date | Method | Paper | Cue | Input | Mechanism | Output | Venue |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 12/2024 | FreqBlender | [Freqblender: Enhancing deepfake detection by blending frequency knowledge](https://arxiv.org/abs/2404.13872)<br>Zhou et al. | Frequency-domain fingerprints | F | Spectral blending augmentation for frequency cues | Score | NeurIPS |
| 10/2024 | Real Appearance Modeling | [Real appearance modeling for more general deepfake detection](https://doi.org/10.1007/978-3-031-72943-0_23)<br>Tian et al. | Realness priors under generator shift | V | Appearance modeling of authentic facial structure | Score | ECCV |
| 06/2024 | Beyond Deepfake Images | [Beyond deepfake images: Detecting ai-generated videos](https://doi.org/10.1109/cvprw63382.2024.00443)<br>Vahdati et al. | Intrinsic synthesis cues beyond still-image artifacts | V | Video-level extension of intrinsic forensic features | Score | CVPR |
| 06/2023 | NoiseDF | [Noise based deepfake detection via multi-head relative-interaction](https://doi.org/10.1609/aaai.v37i12.26701)<br>Wang et al. | Forensic noise traces (face vs. bg) | F | Denoiser-based noise extraction + fusion | Score | AAAI |
| 10/2022 | HCIL | [Hierarchical contrastive inconsistency learning for deepfake video detection](https://doi.org/10.1007/978-3-031-19775-8_35)<br>Gu et al. | Region-level inconsistency | V | Hierarchical contrastive learning | Score | ECCV |
| 06/2021 | MagDR | [MagDR: Mask-Guided Detection and Reconstruction for Defending Deepfakes](https://openaccess.thecvf.com/content/CVPR2021/html/Chen_MagDR_Mask-Guided_Detection_and_Reconstruction_for_Defending_Deepfakes_CVPR_2021_paper.html)<br>Chen et al. | Localized artifacts around manipulated regions | F+V | Mask-guided localization + reconstruction loss | Score+loc. | CVPR |
| 06/2021 | Precise Geometric Features | [Improving the efficiency and robustness of deepfakes detection through precise geometric features](https://doi.org/10.1109/cvpr46437.2021.00361)<br>Sun et al. | Landmark geometry and precise structural cues | V | Geometry-aware facial feature modeling | Score | CVPR |
| 05/2019 | Inconsistent Head Poses | [Exposing deep fakes using inconsistent head poses](https://doi.org/10.1109/icassp.2019.8683164)<br>Yang et al. | 3D head-pose inconsistency | V | Head-pose estimation + geometry checks | Score | ICASSP |

## B. Physiological features

Blink, rPPG, heart-rate, and biological rhythm inconsistencies.

| Date | Method | Paper | Cue | Input | Mechanism | Output | Venue |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 02/2024 | Local rPPG Interaction | [Local attention and long-distance interaction of rPPG for deepfake detection](https://doi.org/10.1007/s00371-023-02833-x)<br>Wu et al. | Cross-region rPPG coupling | V | Local attention + long-range rPPG interaction | Score | The Visual Computer |
| 07/2022 | Visual Physiological Representations | [Visual Representations of Physiological Signals for Fake Video Detection](https://arxiv.org/abs/2207.08380)<br>Stefanov et al. | Physiological signal visualization | V | Visual encoding of rPPG-like dynamics | Score | arXiv |
| 10/2021 | Faint-Signal AR-PPG Correlation | [Exposing deepfake with pixel-wise ar and ppg correlation from faint signals](https://arxiv.org/abs/2110.15561)<br>Mao et al. | Pixel-wise physiological correlation from faint signals | V | AR-PPG correlation analysis | Score | arXiv |
| 10/2021 | BPM Information Study | [A study on effective use of bpm information in deepfake detection](https://doi.org/10.1109/ictc52510.2021.9621186)<br>Lee et al. | BPM-based physiological regularity | V | BPM feature analysis for forgery cues | Score | ICTC |
| 10/2020 | DeepRhythm | [Deeprhythm: Exposing deepfakes with attentional visual heartbeat rhythms](https://arxiv.org/abs/2006.07634)<br>Qi et al. | Visual heartbeat rhythms (rPPG) | V | Spatiotemporal attention over rPPG patterns | Score | ACM MM |
| 10/2020 | DeepFakesON-Phys | [Deepfakeson-phys: Deepfakes detection based on heart rate estimation](https://arxiv.org/abs/2010.00400)<br>Hernandez-Ortega et al. | Heart-rate estimation inconsistency | V | rPPG heart-rate estimation + anomaly cues | Score | arXiv |
| 09/2020 | Hearts | [How do the hearts of deep fakes beat? Deep fake source detection via interpreting residuals with biological signals](https://doi.org/10.1109/ijcb48548.2020.9304909)<br>Ciftci et al. | Heart-related signals in residuals | V | Residual maps -> rPPG features | Score | IJCB |
| 07/2020 | FakeCatcher | [Fakecatcher: Detection of synthetic portrait videos using biological signals](https://doi.org/10.1109/tpami.2020.3009287)<br>Ciftci et al. | PPG-like biological signal maps | V | Biological signal maps + detector | Score | IEEE TPAMI |
| 10/2019 | Neural ODE Heart Rate | [Predicting Heart Rate Variations of Deepfake Videos using Neural ODE](https://doi.org/10.1109/ICCVW.2019.00213)<br>Fernandes et al. | Heart-rate variation inconsistency | V | Neural ODE modeling of physiological rhythms | Score | ICCVW |
| 12/2018 | In Ictu Oculi | [In ictu oculi: Exposing ai created fake videos by detecting eye blinking](https://doi.org/10.1109/wifs.2018.8630787)<br>Li et al. | Eye-blink irregularities | V | Blink detection + temporal pattern modeling | Score | WIFS |

## C. Distribution discrepancy and robustness

Transfer-oriented modeling, adaptation, and robustness under shift.

| Date | Method | Paper | Cue | Input | Mechanism | Output | Venue |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 06/2026 | DFD-HR | [DFD-HR: Generalizable Deepfake Detection via Hierarchical Routing Learning](https://openaccess.thecvf.com/content/CVPR2026/html/Sun_DFD-HR_Generalizable_Deepfake_Detection_via_Hierarchical_Routing_Learning_CVPR_2026_paper.html)<br>Sun et al. | Layer- and token-level forgery cues | F+V | Adaptive depth/token routing + MoE | Score | CVPR |
| 06/2026 | QTFP | [Beyond &#91;CLS&#93; Token: Query-Driven Token-Level Forgery Purification for Generalizable Deepfake Detection](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_Beyond_CLS_Token_Query-Driven_Token-Level_Forgery_Purification_for_Generalizable_Deepfake_Detection_CVPR_2026_paper.html)<br>Wang et al. | Local forgery-token evidence | F+V | Query-driven token purification | Score | CVPR |
| 06/2026 | TSRL | [Tutor-Student Reinforcement Learning: A Dynamic Curriculum for Robust Deepfake Detection](https://openaccess.thecvf.com/content/CVPR2026/html/Lei_Tutor-Student_Reinforcement_Learning_A_Dynamic_Curriculum_for_Robust_Deepfake_Detection_CVPR_2026_paper.html)<br>Lei et al. | Hard-but-learnable samples under shift | F+V | PPO tutor + dynamic curriculum | Score | CVPR |
| 06/2026 | Forensic Rewiring | [Forensic Rewiring: Circuit-Level Shortcut Suppression for Generalizable Deepfake Detection](https://openaccess.thecvf.com/content/CVPR2026W/AIMS/html/A_Forensic_Rewiring_Circuit-Level_Shortcut_Suppression_for_Generalizable_Deepfake_Detection_CVPRW_2026_paper.html)<br>Nishitha A et al. | Dataset-specific attention shortcuts | F+V | Head attribution + selective gradient masking | Score | CVPRW |
| 06/2026 | Seeing the Unseen | [Seeing the Unseen: Enhancing Synthetic Video Detector Transferability to New AI Video Generation Models via Virtual Generators](https://doi.org/10.1145/3785353.3815083)<br>Vahdati et al. | Transferable forensic microstructures | F+V | Virtual generators + autoregressive trace learning | Score | ACM IH&MMSec |
| 03/2026 | DFA | [Deepfake Forensics Adapter: A Dual-Stream Network for Generalizable Deepfake Detection](https://doi.org/10.48550/ARXIV.2603.01450)<br>Liao et al. | Global-local intrinsic anomalies | F+V | CLIP adapter + local anomaly stream | Score | ICDF2C 2025 |
| 08/2025 | GenD | [Deepfake Detection that Generalizes Across Benchmarks](https://openaccess.thecvf.com/content/WACV2026/papers/Yermakov_Deepfake_Detection_that_Generalizes_Across_Benchmarks_WACV_2026_paper.pdf)<br>Yermakov et al. | Cross-benchmark distribution shift | F+V | LN tuning + hyperspherical metric learning | Score | WACV 2026 |
| 12/2024 | Leave Deepfake Data Behind | [Can we leave deepfake data behind in training deepfake detector?](https://doi.org/10.52202/079017-0691)<br>Cheng et al. | Real-only training for robustness under shift | V | Real-only training paradigm | Score | NeurIPS |
| 10/2024 | Fake It Till You Make It | [Fake It till You Make It: Curricular Dynamic Forgery Augmentations Towards General Deepfake Detection](https://doi.org/10.1007/978-3-031-73016-0_7)<br>Lin et al. | Curriculum-based forgery augmentation | V | Curriculum forgery augmentation | Score | ECCV |
| 06/2024 | LSDA | [Transcending Forgery Specificity with Latent Space Augmentation for Generalizable Deepfake Detection](https://doi.org/10.1109/CVPR52733.2024.00858)<br>Yan et al. | Cross-generator transfer | V | Latent-space augmentation for transfer | Score | CVPR |
| 06/2024 | Style Latent Flows | [Exploiting style latent flows for generalizing deepfake video detection](https://doi.org/10.1109/cvpr52733.2024.00114)<br>Choi et al. | Abnormal style-latent trajectories | V | Style-flow modeling + contrastive loss | Score | CVPR |
| 06/2024 | Turns Out I'm Not Real | [Turns Out I'm Not Real: Towards Robust Detection of AI-Generated Videos](https://arxiv.org/abs/2406.09601)<br>Liu et al. | Robust intrinsic cues for AI-generated video | V | Robust training under generator diversity | Score | arXiv |
| 10/2023 | SeeABLE | [Seeable: Soft discrepancies and bounded contrastive learning for exposing deepfakes](https://doi.org/10.1109/iccv51070.2023.01921)<br>Larue et al. | Soft discrepancies under shifts | F | Real-only bounded contrastive learning | Score | ICCV |
| 10/2023 | QAD | [Quality-agnostic deepfake detection with intra-model collaborative learning](https://doi.org/10.1109/iccv51070.2023.02045)<br>Le et al. | Compression-robust representations | F | Quality-aware regularization | Score | ICCV |
| 12/2022 | OST | [Ost: Improving generalization of deepfake detection via one-shot test-time training](https://doi.org/10.52202/068431-1786)<br>Chen et al. | Domain shift and compression sensitivity | F | One-shot test-time adaptation | Score | NeurIPS |
| 10/2020 | Locality-Aware Autoencoder | [Towards generalizable deepfake detection with locality-aware autoencoder](https://doi.org/10.1145/3340531.3411892)<br>Du et al. | Local anomaly reconstruction under shift | F | Locality-aware autoencoder | Score | CIKM |

<details>
<summary>Additional cited works discussed in this layer</summary>

- [On Using rPPG Signals for DeepFake Detection: A Cautionary Note](https://doi.org/10.1007/978-3-031-43153-1_20) (D'Amelio et al. · ICIAP)
- [ID-Reveal: Identity-aware DeepFake Video Detection](https://doi.org/10.1109/ICCV48922.2021.01483) (Cozzolino et al. · ICCV)

</details>
