# AIGC-V Paradigms

[Back to home](../README.md)

<p align="center">
  <a href="../figures/paradigms.pdf">
    <img src="../figures/paradigms.png" width="100%" alt="AIGC-V paradigms" />
  </a>
</p>

The survey groups mainstream AIGC-V pipelines into three generation paradigms: **Local Manipulation**, **Audio-Visual Editing**, and **Generative Video Synthesis**.
The tables below collect representative systems cited directly in the paradigm section of the survey.

## Where the Evidence Lives

- **Local Manipulation** starts from a real recorded video and edits selected regions, identities, or attributes, so the strongest clues are often local, residual, and compression-sensitive.
- **Audio-Visual Editing** is driven by speech or performance control, so the most useful evidence often comes from lip-sync, speaker identity, and cross-modal timing.
- **Generative Video Synthesis** creates the clip itself, which weakens local edit traces and shifts detection toward temporal coherence, semantic plausibility, and provenance.

## Local Manipulation

Methods in this paradigm keep an authentic video carrier and edit only specific regions, attributes, or identities. The strongest clues are often localized and residual rather than scene-wide.

| Date | System | Paper | Focus | Venue |
| --- | --- | --- | --- | --- |
| 2025 | FakeParts | [FakeParts: a New Family of AI-Generated DeepFakes](https://arxiv.org/abs/2508.21052)<br>Brison et al. | Localized part editing on an authentic carrier. | arXiv |
| 2025 | FakeChain | [FakeChain: Exposing Shallow Cues in Multi-Step Deepfake Detection](https://doi.org/10.1145/3746252.3761345)<br>Heo et al. | Multi-stage local editing with controlled refinement. | CIKM |
| 2025 | DynamicFace | [DynamicFace: High-quality and consistent face swapping for image and video using composable 3D facial priors](https://openaccess.thecvf.com/content/ICCV2025/html/Wang_DynamicFace_High-Quality_and_Consistent_Face_Swapping_for_Image_and_Video_ICCV_2025_paper.html)<br>Wang et al. | 3D-prior-based identity transfer with expression and pose control. | ICCV |
| 2024 | FuseAnyPart | [FuseAnyPart: Diffusion-Driven Facial Parts Swapping via Multiple Reference Images](https://arxiv.org/abs/2410.22771)<br>Wang et al. | Mask-guided latent fusion for facial element manipulation. | NeurIPS |

## Audio-Visual Editing

Methods in this paradigm use speech as an explicit control signal. Detection therefore leans heavily on lip-audio alignment, speaker identity coherence, and cross-modal timing.

| Date | System | Paper | Focus | Venue |
| --- | --- | --- | --- | --- |
| 2025 | SayAnything | [SayAnything: Audio-Driven Lip Synchronization with Conditional Video Diffusion](https://arxiv.org/abs/2502.11515)<br>Ma et al. | Diffusion-based, speech-conditioned talking-head generation. | arXiv |
| 2025 | Actalker | [Audio-visual Controlled Video Diffusion with Masked Selective State Spaces Modeling for Natural Talking Head Generation](https://arxiv.org/abs/2504.02542)<br>Hong et al. | Unified audio-guided talking-head synthesis with expressive motion. | arXiv |
| 2024 | Ditto | [Ditto: Motion-Space Diffusion for Controllable Realtime Talking Head Synthesis](https://arxiv.org/abs/2411.19509)<br>Li et al. | Lip-synced talking-head generation with stronger motion control. | arXiv |
| 2023 | GeneFace | [GeneFace: Generalized and High-Fidelity Audio-Driven 3D Talking Face Synthesis](https://arxiv.org/abs/2301.13430)<br>Ye et al. | 3D-aware audio-driven portrait animation. | arXiv |
| 2022 | VideoReTalking | [VideoReTalking: Audio-based Lip Synchronization for Talking Head Video Editing in the Wild](https://arxiv.org/abs/2211.14758)<br>Cheng et al. | Speech-driven talking-head redubbing with identity preservation. | SIGGRAPH Asia |

## Generative Video Synthesis

Methods in this paradigm synthesize full clips from text, image, or noise conditions. This weakens local edit traces and shifts detection toward long-range coherence, factual plausibility, and provenance.

| Date | System | Paper | Focus | Venue |
| --- | --- | --- | --- | --- |
| 2026 | Seedance 2.0 | [Official Launch of Seedance 2.0](https://seed.bytedance.com/en/seedance2_0)<br>ByteDance Seed | Recent industrial text-to-video system with stronger realism and control. | Official page |
| 2025 | Show-1 | [Show-1: Marrying pixel and latent diffusion models for text-to-video generation](https://doi.org/10.1007/s11263-024-02271-9)<br>Zhang et al. | Hybrid pixel-latent refinement for efficient video synthesis. | IJCV |
| 2025 | Kling | [Kling O1: Unified Multimodal Video Model](https://app.klingai.com/global/)<br>Kuaishou Technology | Commercial large-scale text-to-video system. | Official page |
| 2025 | Veo 3 | [Veo 3](https://deepmind.google/models/veo/)<br>Google DeepMind | Large-scale high-fidelity video generation with stronger world modeling. | Official page |
| 2024 | Grid Diffusion | [Grid diffusion models for text-to-video generation](https://doi.org/10.1109/cvpr52733.2024.00834)<br>Lee et al. | Unified 2D-grid modeling for spatiotemporal generation. | CVPR |
| 2024 | Sora 2 | [Sora 2](https://openai.com/sora/)<br>OpenAI | Industrial-scale open-domain text-to-video generation. | Official page |
| 2024 | Runway Gen-3 | [Introducing Gen-3 Alpha: A New Frontier for Video Generation](https://runwayml.com/research/introducing-gen-3-alpha)<br>Runway Research | Commercial high-fidelity controllable video generation. | Official page |
| 2024 | Dream Machine | [Dream Machine](https://lumalabs.ai/dream-machine)<br>Luma AI | Open-ended video generation for narrative and motion-heavy scenes. | Official page |
| 2023 | DiT | [Scalable Diffusion Models with Transformers](https://openaccess.thecvf.com/content/ICCV2023/papers/Peebles_Scalable_Diffusion_Models_with_Transformers_ICCV_2023_paper.pdf)<br>Peebles et al. | Transformer scaling recipe for diffusion backbones. | ICCV |
| 2022 | Video Diffusion Models | [Video Diffusion Models](https://arxiv.org/abs/2204.03458)<br>Ho et al. | Diffusion-based video generation with temporal modeling. | arXiv |
| 2022 | Imagen Video | [Imagen Video: High Definition Video Generation with Diffusion Models](https://arxiv.org/abs/2210.02303)<br>Ho et al. | Cascaded high-fidelity text-to-video generation. | arXiv |
| 2022 | Make-A-Video | [Make-A-Video: Text-to-Video Generation without Text-Video Data](https://arxiv.org/abs/2209.14792)<br>Singer et al. | Text-to-video generation with text-image and video priors. | arXiv |
