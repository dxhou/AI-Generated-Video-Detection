# Layer 2: Spatiotemporal Consistency

[Back to methods](README.md) · [Back to home](../README.md)

Sequence-level visual verification. The detector checks whether motion, physical transitions, and human behavior evolve in a temporally and physically plausible way.

## Subcategory Guide

- **A. Temporal and motion inconsistencies**: Clip-level coherence, motion residuals, and temporal naturalness.
- **B. Physical and frequency artifacts**: Transform-domain dynamics, physics constraints, and non-physical trajectories.
- **C. Human behavioral and interaction dynamics**: Expression, gaze, identity, and interaction realism over time.

## A. Temporal and motion inconsistencies

Clip-level coherence, motion residuals, and temporal naturalness.

| Date | Method | Paper | Cue | Mechanism | Output | Venue |
| --- | --- | --- | --- | --- | --- | --- |
| 07/2020 | FS-Spotter | [Fsspotter: Spotting face-swapped video by spatial and temporal clues](https://doi.org/10.1109/icme46284.2020.9102914)<br>Chen et al. | Spatiotemporal swap artifacts | Fuse spatial+temporal cues | Score | ICME |
| 10/2020 | Two-Branch Recurrent Network | [Two-branch recurrent network for isolating deepfakes in videos](https://doi.org/10.1007/978-3-030-58571-6_39)<br>Masi et al. | Recurrent temporal inconsistency across clips | Two-branch recurrent isolation of forged dynamics | Score | ECCV |
| 10/2020 | Sharp Multiple Instance Learning | [Sharp multiple instance learning for deepfake video detection](https://doi.org/10.1145/3394171.3414034)<br>Li et al. | Sparse temporal evidence aggregation | Multiple-instance learning over clips | Score | ACM MM |
| 01/2021 | Dynamic Prototypes | [Interpretable and trustworthy deepfake detection via dynamic prototypes](https://doi.org/10.1109/wacv48630.2021.00202)<br>Trinh et al. | Transferable spatiotemporal evidence | Dynamic prototypes + predictive learning | Score | WACV |
| 08/2021 | Temporal Dropout 3DCNN | [Detecting Deepfake Videos with Temporal Dropout 3DCNN](https://doi.org/10.24963/ijcai.2021/178)<br>Zhang et al. | Frame-rate dependent temporal artifacts | 3D CNN + temporal dropout | Score | IJCAI |
| 08/2021 | Dynamic Inconsistency-aware Detection | [Dynamic Inconsistency-aware DeepFake Video Detection](https://doi.org/10.24963/ijcai.2021/102)<br>Hu et al. | Local temporal inconsistency under manipulation | Dynamic inconsistency modeling | Score | IJCAI |
| 10/2021 | STIL | [Spatiotemporal inconsistency learning for deepfake video detection](https://doi.org/10.1145/3474085.3475508)<br>Gu et al. | Short-clip spatiotemporal inconsistency | Clip encoder for ST inconsistency | Score | ACM MM |
| 02/2022 | Delving into the Local | [Delving into the local: Dynamic inconsistency learning for deepfake video detection](https://doi.org/10.1609/aaai.v36i1.19955)<br>Gu et al. | Fine-grained local temporal mismatch | Dynamic local inconsistency learning | Score | AAAI |
| 05/2022 | EfficientNet-ViT Ensemble | [Combining efficientnet and vision transformers for video deepfake detection](https://doi.org/10.1007/978-3-031-06433-3_19)<br>Coccomini et al. | Robust temporal features | CNN and ViT ensemble | Score | ICIAP |
| 07/2022 | Region-Aware Temporal Inconsistency | [Region-Aware Temporal Inconsistency Learning for DeepFake Video Detection](https://doi.org/10.24963/ijcai.2022/129)<br>Gu et al. | Region-wise dynamics anomalies | Region-aware learning + maps | Score+loc. | IJCAI |
| 10/2023 | Dynamic Difference Learning | [Dynamic difference learning with spatio--temporal correlation for deepfake video detection](https://doi.org/10.1109/tifs.2023.3290752)<br>Yin et al. | Spatiotemporal correlation gaps | Dynamic difference learning | Score | IEEE TIFS |
| 10/2023 | TALL | [Tall: Thumbnail layout for deepfake video detection](https://doi.org/10.1109/iccv51070.2023.02071)<br>Xu et al. | Cross-frame inconsistency | Thumbnail layout + 2D backbone | Score | ICCV |
| 02/2024 | DeCoF | [Decof: Generated video detection via frame consistency](https://arxiv.org/abs/2402.02085)<br>Ma et al. | Frame-to-frame consistency failures | Consistency modeling across generated frames | Score | arXiv |
| 06/2024 | Thumbnail Layout IJCV | [Learning spatiotemporal inconsistency via thumbnail layout for face deepfake detection](https://doi.org/10.1007/s11263-024-02054-2)<br>Xu et al. | Thumbnail-based sequence inconsistency | Spatiotemporal inconsistency via layout modeling | Score | IJCV |
| 11/2024 | Natural Consistency Representation | [Learning natural consistency representation for face forgery video detection](https://doi.org/10.1007/978-3-031-73010-8_24)<br>Zhang et al. | Temporal naturalness deviations | SSL consistency + fine-tune | Score | ECCV |
| 01/2025 | Vulnerability-Aware Learning | [Vulnerability-Aware Spatio-Temporal Learning for Generalizable and Interpretable Deepfake Video Detection](https://arxiv.org/abs/2501.01184)<br>Nguyen et al. | Cross-generator vulnerability patterns | Vulnerability-aware transfer | Score | arXiv |
| 06/2025 | GC-ConsFlow | [GC-ConsFlow: Leveraging Optical Flow Residuals and Global Context for Robust Deepfake Detection](https://arxiv.org/abs/2501.13435)<br>Chen et al. | Optical-flow residual inconsistency | Flow residuals + global context | Score | arXiv |
| 06/2025 | Plug-and-Play Adapters | [Generalizing deepfake video detection with plug-and-play: Video-level blending and spatiotemporal adapter tuning](https://doi.org/10.1109/cvpr52734.2025.01177)<br>Yan et al. | Generalization under generator shift | Video blending + ST adapters | Score | CVPR |

## B. Physical and frequency artifacts

Transform-domain dynamics, physics constraints, and non-physical trajectories.

| Date | Method | Paper | Cue | Mechanism | Output | Venue |
| --- | --- | --- | --- | --- | --- | --- |
| 06/2020 | Face Geometry Consistency | [Towards untrusted social video verification to combat deepfakes via face geometry consistency](https://doi.org/10.1109/cvprw50498.2020.00335)<br>Tursman et al. | Geometry consistency over time | Face-geometry verification across sequence | Score | CVPR |
| 12/2024 | DIP | [DIP: diffusion learning of inconsistency pattern for general deepfake detection](https://doi.org/10.1109/tmm.2024.3521766)<br>Nie et al. | Temporal frequency response anomalies | Transform-domain temporal spectra | Score | IEEE TMM |
| 11/2024 | Quality-Centric Framework | [A quality-centric framework for generic deepfake detection](https://arxiv.org/abs/2411.05335)<br>Song et al. | Quality-aware temporal degradation patterns | Quality-centric forensic modeling | Score | arXiv |
| 01/2025 | DiffFake | [DiffFake: Exposing Deepfakes using Differential Anomaly Detection](https://doi.org/10.1109/wacvw65960.2025.00079)<br>Stamnas et al. | Differential anomaly patterns | Differential anomaly detection | Score | WACV |
| 03/2025 | VoD | [VoD: Learning Volume of Differences for Video-Based Deepfake Detection](https://arxiv.org/abs/2503.07607)<br>Xu et al. | Volumetric difference cues | Volume-of-differences modeling | Score | arXiv |
| 06/2025 | Forensic-Oriented Augmentation | [Seeing What Matters: Generalizable AI-generated Video Detection with Forensic-Oriented Augmentation](https://arxiv.org/abs/2506.16802)<br>Corvi et al. | Forensic cue amplification under shift | Forensic-oriented augmentation | Score | arXiv |
| 07/2025 | ReStraV (Perceptual Straightening) | [AI-Generated Video Detection via Perceptual Straightening](https://openreview.net/forum?id=LsmUgStXby)<br>Interno et al. | Non-physical motion and trajectory irregularities | Perceptual straightening | Score | NeurIPS |
| 07/2025 | Beyond RGB | [Beyond Spatial Frequency: Pixel-wise Temporal Frequency-based Deepfake Video Detection](https://arxiv.org/abs/2507.02398)<br>Kim et al. | Stable descriptors beyond raw RGB | Transformed descriptors | Score | arXiv |
| 07/2025 | Pre-Trained Visual Models | [Leveraging Pre-Trained Visual Models for AI-Generated Video Detection](https://arxiv.org/abs/2507.13224)<br>Veeramachaneni et al. | Strong visual priors for temporal forensics | Adaptation of pre-trained visual backbones | Score | arXiv |
| 07/2025 | De-Fake | [De-Fake: Style based Anomaly Deepfake Detection](https://arxiv.org/abs/2507.03334)<br>Padhi et al. | Style-space anomaly over time | Style-based anomaly detection | Score | arXiv |
| 10/2025 | D3 | [D3: Training-Free AI-Generated Video Detection Using Second-Order Features](https://openaccess.thecvf.com/content/ICCV2025/html/Zheng_D3_Training-Free_AI-Generated_Video_Detection_Using_Second-Order_Features_ICCV_2025_paper.html)<br>Zheng et al. | Second-order spatiotemporal statistics | Training-free second-order features | Score | ICCV |
| 10/2025 | Physics-Driven ST Modeling | [Physics-Driven Spatiotemporal Modeling for AI-Generated Video Detection](https://openreview.net/forum?id=HiBoJLCyEo)<br>Zhang et al. | Physics constraints on spatiotemporal flow | Physics-driven ST modeling | Score | NeurIPS |
| 01/2026 | MPF-Net | [MPF-Net: Exposing High-Fidelity AI-Generated Video Forgeries via Hierarchical Manifold Deviation and Micro-Temporal Fluctuations](https://doi.org/10.48550/ARXIV.2601.21408)<br>He et al. | Off-manifold residuals + micro-temporal fluctuations | Hierarchical manifold deviation + temporal filtering | Score | arXiv |

## C. Human behavioral and interaction dynamics

Expression, gaze, identity, and interaction realism over time.

| Date | Method | Paper | Cue | Mechanism | Output | Venue |
| --- | --- | --- | --- | --- | --- | --- |
| 03/2020 | Emotions Don't Lie | [Emotions Don't Lie: An Audio-Visual Deepfake Detection Method Using Affective Cues](https://arxiv.org/abs/2003.06711)<br>Mittal et al. | Affective audio-visual cue coherence | Siamese audio-visual model + triplet loss | Score | arXiv |
| 12/2020 | Appearance and Behavior | [Detecting deep-fake videos from appearance and behavior](https://doi.org/10.1109/wifs49906.2020.9360904)<br>Agarwal et al. | Appearance and behavior realism over time | Behavior-aware temporal features | Score | WIFS |
| 12/2020 | Identity-Driven Detection | [Identity-driven deepfake detection](https://arxiv.org/abs/2012.03930)<br>Dong et al. | Identity dynamics consistency | Track identity dynamics | Score | arXiv |
| 06/2021 | Lips Don't Lie | [Lips Don't Lie: A Generalisable and Robust Approach To Face Forgery Detection](https://doi.org/10.1109/cvpr46437.2021.00500)<br>Haliassos et al. | Behavioral realism in mouth motion | Lip dynamics modeling | Score | CVPR |
| 10/2023 | Complementary Dynamic Incoherence | [Exploiting complementary dynamic incoherence for deepfake video detection](https://doi.org/10.1109/tcsvt.2023.3238517)<br>Wang et al. | Complementary behavior and motion incoherence | Multi-branch dynamic modeling | Score | IEEE TCSVT |
| 06/2025 | Action Unit-Guided Representations | [Detecting Localized Deepfake Manipulations Using Action Unit-Guided Video Representations](https://doi.org/10.1109/cvprw67362.2025.00419)<br>Anand et al. | Expression and action-unit inconsistency | Action-unit-guided video representations | Score+loc. | CVPR |
| 08/2025 | GNN Framework | [When Deepfake Detection Meets Graph Neural Network: a Unified and Lightweight Learning Framework](https://arxiv.org/abs/2508.05526)<br>Liu et al. | Relational dynamics across face regions | Graph-based temporal reasoning | Score | arXiv |
| 09/2025 | Gaze Tracking | [DeepFake Detection in Dyadic Video Calls using Point of Gaze Tracking](https://arxiv.org/abs/2509.25503)<br>Kohler et al. | Gaze dynamics | Gaze features for dyadic calls | Score | arXiv |

<details>
<summary>Additional cited works discussed in this layer</summary>

- [Deepfake Detection Using Deep Convolutional Neural Network and Long Short-Term Memory](https://doi.org/10.1007/s11042-026-21375-7) (Bahadure et al. · Multimedia Tools and Applications)
- [Deepfake Detection Using Spatiotemporal Methods and Vision-Language Models](https://doi.org/10.1145/3726302.3730234) (Tong et al. · KDD-UMC’25)
- [One detector to rule them all: Towards a general deepfake attack detection framework](https://arxiv.org/abs/2105.00187) (Tariq et al. · WWW)
- [Video anomaly detection via self-supervised and spatio-temporal proxy tasks learning](https://doi.org/10.1016/j.patcog.2024.111021) (Yang et al. · Pattern Recognition)
- [Self-supervised video forensics by audio-visual anomaly detection](https://doi.org/10.1109/cvpr52729.2023.01011) (Feng et al. · CVPR)

</details>
