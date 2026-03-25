# Detection Methods

[Back to home](../README.md)

<p align="center">
  <a href="../figures/landscape.pdf">
    <img src="../figures/landscape.png" width="100%" alt="Method landscape" />
  </a>
</p>

This section reorganizes the detection part of the survey into the **four-layer taxonomy**. Each layer page contains representative papers grouped by the same subcategories used in the paper tables, plus an extra list of additional cited works discussed in the text.

## Layer Index

| Layer | View | Representative methods | Subcategories | Page |
| --- | --- | --- | --- | --- |
| L1 | Visual | 28 | A. Pixel and geometric artifacts / B. Physiological features / C. Distribution discrepancy and robustness | [Open](layer-1-intrinsic-cues.md) |
| L2 | Visual | 39 | A. Temporal and motion inconsistencies / B. Physical and frequency artifacts / C. Human behavioral and interaction dynamics | [Open](layer-2-spatiotemporal.md) |
| L3 | Language | 33 | A. Audio-visual consistency detection / B. Text-video semantic consistency reasoning / C. Robust learning and temporal localization | [Open](layer-3-cross-modal.md) |
| L4 | Language | 19 | A. Prompts and adapters for representation calibration / B. Tool-augmented agents for evidence gathering / C. Post-training, preferences and rewards | [Open](layer-4-world-level-reasoning.md) |

## Protocol-Aware Performance Snapshot

The numbers below come from the survey's compact AUC table. They are useful as a quick anchor, but **cross-dataset (CD)** and **in-domain (ID)** results should not be compared as if they were one unified leaderboard.

| Method | Layer | Protocol | CDFv2 | DFDCP | DFDC |
| --- | --- | --- | --- | --- | --- |
| FreqBlender | L1 | CD | 94.6 | 87.6 | 74.6 |
| SeeABLE | L1 | CD | 87.3 | 86.3 | 75.9 |
| LSDA | L1 | CD | 83.0 | 81.5 | 73.6 |
| Style Latent Flows | L1 | CD | 89.0 | -- | -- |
| TALL-Swin | L2 | CD | 90.8 | -- | 76.8 |
| LipForensics | L2 | CD | 82.4 | -- | 73.5 |
| Two-branch | L2 | CD | 76.6 | -- | -- |
| MDS | L3 | ID | -- | -- | 90.6 |
| RepDFD | L4 | CD | 89.9 | 95.0 | 81.0 |
| LVLMDFD | L4 | CD | 94.3 | 92.4 | 77.0 |
