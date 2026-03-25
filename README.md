# Detecting AI-Generated Video

A link-first companion repository for **"Detecting AI-Generated Video: A Vision-Language Dual-View Survey"**.
It turns the survey into a compact index of paradigms, methods, benchmarks, and core figures.

## Start Here

| Section | What it covers | Link |
| --- | --- | --- |
| Paradigms | How AI-generated videos are produced: local manipulation, audio-visual editing, and full video synthesis | [Open](paradigms/README.md) |
| Methods | How they are detected: visual evidence, cross-modal consistency, and world-grounded reasoning across four layers | [Open](methods/README.md) |
| Benchmarks | Datasets, evaluation families, and diagnostic resources for both detection and explanation | [Open](benchmarks/README.md) |

## Key Figures

### 1. Problem framing
<p align="center">
  <a href="figures/intro-fig.pdf">
    <img src="figures/intro-fig.png" width="100%" loading="lazy" decoding="async" alt="AIGC-V detection pipeline" />
  </a>
</p>

AI-generated video detection is framed as **factual fidelity verification**: not only whether a clip is synthetic, but which claim, identity, event, or segment fails consistency.

Read next:
- [Survey PDF](paper.pdf): original framing, full tables, and figure context.
- [Detection methods](methods/README.md): the four-layer detection structure introduced by the survey.
- [Benchmarks and diagnostics](benchmarks/README.md): datasets and evaluation settings for testing these claims.

### 2. AIGC-V paradigms
<p align="center">
  <a href="figures/paradigms.pdf">
    <img src="figures/paradigms.png" width="100%" loading="lazy" decoding="async" alt="AIGC-V paradigms" />
  </a>
</p>

The generation side is split into three settings: **Local Manipulation** edits parts of a real recorded video, **Audio-Visual Editing** changes speech-driven facial performance, and **Generative Video Synthesis** creates the clip itself. As the pipeline moves from local edits to fully generated video, detection relies less on residual artifacts and more on temporal, semantic, and provenance evidence.

Read next:
- [Paradigms overview](paradigms/README.md): the full generation-side taxonomy and representative systems.
- [Local Manipulation](paradigms/README.md#local-manipulation): swaps or localized edits on an authentic carrier.
- [Audio-Visual Editing](paradigms/README.md#audio-visual-editing): talking-head editing and speech-conditioned generation.
- [Generative Video Synthesis](paradigms/README.md#generative-video-synthesis): full-video generation from prompts, images, or noise.

### 3. Vision-language dual-view taxonomy
<p align="center">
  <a href="figures/dual-view.pdf">
    <img src="figures/dual-view.png" width="100%" loading="lazy" decoding="async" alt="Dual-view taxonomy" />
  </a>
</p>

The taxonomy moves from what can be seen directly in frames and motion to what must be verified across modalities and against external knowledge. **Layers 1-2** focus on visual evidence inside the video, while **Layers 3-4** test whether speech, text, events, and implied claims remain mutually and externally consistent.

Read next:
- [Methods overview](methods/README.md): the four-layer index and compact performance snapshot.
- [Layer 1 methods](methods/layer-1-intrinsic-cues.md): frame-level artifacts, geometry, physiology, and transfer cues.
- [Layer 2 methods](methods/layer-2-spatiotemporal.md): motion, physics, and behavior over time.
- [Layer 3 methods](methods/layer-3-cross-modal.md): audio-video-text agreement inside the clip.
- [Layer 4 methods](methods/layer-4-world-level-reasoning.md): world knowledge, tools, and explainable reasoning.

### 4. Method landscape
<p align="center">
  <a href="figures/landscape.pdf">
    <img src="figures/landscape.png" width="100%" loading="lazy" decoding="async" alt="Method landscape" />
  </a>
</p>

The field is shifting from artifact-centric screening toward multimodal verification, grounded localization, and explainable reasoning as generators become stronger and more realistic.

Read next:
- [Methods overview](methods/README.md): compare the four detection layers in one place.
- [Benchmarks overview](benchmarks/README.md): map methods to evaluation families and diagnostic needs.
- [Generative Video Synthesis benchmarks](benchmarks/generative-video-synthesis.md): the fastest-changing setting for modern detectors.
- [Adjacent diagnostics](benchmarks/adjacent-diagnostics.md): physical plausibility, world dynamics, and explanation-oriented evaluation.

## Detection Map

### [Layer 1: Intrinsic Visual Cues](methods/layer-1-intrinsic-cues.md)

**Goal:** Decide whether individual frames still carry the statistics of captured video rather than synthesis, blending, or tampering.  
**Evidence:** Frequency fingerprints, local texture artifacts, geometric inconsistencies, physiological traces, and distribution gaps.  
**Best fit:** Fast screening and local-manipulation settings where traces survive inside the frame.

**Boundary L1~2:** Layer 1 focuses on frame-level intrinsic distributional cues, whereas Layer 2 moves beyond frames to explicitly model spatiotemporal connections across the frame sequence and test whether sequence-level dynamics are consistent with real video formation.

### [Layer 2: Spatiotemporal Consistency](methods/layer-2-spatiotemporal.md)

**Goal:** Check whether motion, behavior, and physical transitions unfold like a real recorded sequence rather than a stitched or synthesized one.  
**Evidence:** Optical flow residuals, temporal frequency response, expression dynamics, interaction patterns, and physics-aware motion cues.  
**Best fit:** Video-level verification when realism depends on motion continuity, scene dynamics, or long-range temporal coherence.

**Boundary L2~3:** Layer 2 stays within the visual modality and evaluates within visual coherence, whereas Layer 3 goes beyond vision and treats the video as multimodal content, judging whether different modalities are mutually consistent in describing the same semantics.

### [Layer 3: Cross-Modal Consistency](methods/layer-3-cross-modal.md)

**Goal:** Test whether speech, lip motion, voice identity, captions, and visible events describe the same clip.  
**Evidence:** Lip-sync alignment, voice-face consistency, text-video semantics, multimodal grounding, and temporal localization of mismatch.  
**Best fit:** Audio-visual editing and multimodal misinformation settings where the failure is not visual texture but cross-modal contradiction.

**Boundary L3~4:** Layer 3 relies on within-video cross-modal agreement, whereas Layer 4 further requires external facts, commonsense, or physics for reasoning-based verification, even when the modalities appear mutually consistent.

### [Layer 4: World-Level Reasoning](methods/layer-4-world-level-reasoning.md)

**Goal:** Judge whether the clip's implied claims remain plausible when checked against external facts, commonsense, and structured evidence.  
**Evidence:** Vision-language prompting, retrieval, tool-augmented reasoning, evidence chains, and explanation-oriented post-training.  
**Best fit:** Full-video synthesis and high-realism cases where low-level artifacts fade but factual or causal consistency still breaks.
