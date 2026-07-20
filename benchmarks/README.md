# Benchmarks and Diagnostics

[Back to home](../README.md)

Benchmarks in the survey follow three main families: **Local Manipulation Video (LMV)**, **Audio-Visual Editing (AVE)**, and **Generative Video Synthesis (GVS)**. They then extend into a broader diagnostic landscape that stresses physics, world dynamics, and explanation quality.

## Benchmark Families

| Family | Resources | Main question | Page |
| --- | --- | --- | --- |
| Local Manipulation Video (LMV) | 21 | Localized forensic residue, compression robustness, cross-dataset transfer. | [Open](local-manipulation-video.md) |
| Audio-Visual Editing (AVE) | 17 | Lip-audio alignment, speaker-content consistency, localization. | [Open](audio-visual-editing.md) |
| Generative Video Synthesis (GVS) | 30 | Cross-generator transfer, plausibility, semantically fabricated scenarios. | [Open](generative-video-synthesis.md) |
| Diagnostics and audits | 25 | Physics, world dynamics, explanations, detector robustness controls, and human judgments. | [Open](adjacent-diagnostics.md) |

## Reading Note

- **Local Manipulation Video (LMV)** remains the deepest protocol tradition and is especially useful for compression robustness, transfer, and localized forensic residue.
- **Audio-Visual Editing (AVE)** is smaller but more tightly aligned with lip-sync, speaker identity, multimodal consistency, and temporal localization.
- **Generative Video Synthesis (GVS)** changes fastest because stronger generators keep resetting the detection problem and demand broader cross-model transfer.
- **Diagnostics and audits** matter because future evaluation increasingly depends on physical plausibility, world consistency, grounded explanations, and explicit shortcut controls rather than a single clip label.
