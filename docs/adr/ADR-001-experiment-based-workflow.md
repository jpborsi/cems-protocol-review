# ADR 001: Experiment-Based Workflow

## Status

Implemented. 2026-03-11.

## Context

"Prompt-Hacking" is recognized as a serious problem in LLM-based research
projects [(Kosch, 2026)](https://dl.acm.org/doi/10.1145/3744911). It is very tempting to massage system prompts until
you achieve your desired results. Unfortunately, this provides no insight into the fragility, variability, and pitfalls
in the prompt-space.

## Decision

The gold standard for LLM-based research projects is pre-registered prompts with documentation for any prompt changes.
Because of the exploratory nature of this project, it is not feasible to use pre-registration. But it is absolutely
possible to provide transparent, reproducible evidence in support of our research findings. This project will proceed by
saving all relevant data, code, and methodologies in the `docs/experiments` folder. Package code should be structured to
support backwards compatability for previous experiments.

## Consequences

The documentation and backward-compatibility requirements are substantial costs that will slow development. The
transparency and reproducibility provided, however, are essential to this project.