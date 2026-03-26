# Layer 1: Intrinsic Cues Analysis

[Back to methods](README.md) · [Back to home](../README.md)

Frame-level forensic evidence. The detector tests whether low-level visual signals still look like real captured video, including frequency fingerprints, local geometry, physiological traces, and cross-generator distribution gaps.

## Subcategory Guide

- **A. Pixel and geometric artifacts**: Frequency, texture, localization, and geometric plausibility cues.
- **B. Physiological features**: Blink, rPPG, heart-rate, and biological rhythm inconsistencies.
- **C. Distribution discrepancy and robustness**: Transfer-oriented modeling, adaptation, and robustness under shift.

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
| 03/2026 | DFA | [Deepfake Forensics Adapter: A Dual-Stream Network for Generalizable Deepfake Detection](https://doi.org/10.48550/ARXIV.2603.01450)<br>Liao et al. | Global-local intrinsic anomalies | F+V | CLIP adapter + local anomaly stream | Score | arXiv |
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
