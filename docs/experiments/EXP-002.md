# Experiment 002: Repeatability and Variance

## Abstract

How many trials are required to get a reliable sense of model performance? What is the expected variation between trials
of a model query? I expect significant variability in wording between runs, but the underlying reasoning and clinical
knowledge should be similar between runs.

## Methods

I will run 5 tests each of the oneshot, extraction-only, and review-only queries on the airway protocol and compare the
outputs. If necessary, I will run further sets of tests until results stabilize. I will run 3 sets of review-only
queries on different extraction results to determine the presence of any downstream effects / compounding errors in the
workflow. Primary evaluation metric will be the 'eyeball test', with note given to the number of false positives and
false negatives. Scripts and prompts are in the [EXP-002 folder](./EXP_002).

## Results

### Test 1: Text extraction

Each of the 5 sample runs demonstrated some deviations from the pdf protocol. Common failure modes included:

1. Adding non-existent text (copied from prompt or fully hallucinated)
2. Combining unrelated instructions
3. Duplicating items
4. Erroneously correcting typos
5. Failure to reproduce branching treatment pathways

| File | Quality | Ranking | Notes                       |
|------|---------|---------|-----------------------------|
| 0    | low     | 5       | errors: 1(many), 2, 3, 4, 5 |
| 1    | medium  | 3       | errors: 1                   |
| 2    | low     | 4       | errors: 1, 3, 4             |
| 3    | high    | 1       | errors: 3                   |
| 4    | medium  | 2       | errors: 1, 2, 4             |

### Test 2: Oneshot evaluation

Only 1 of the one-shot runs included similar behavior to EXP-001 -- where the results emphasized the positive aspects of
the protocol. Most of the results included a majority of irrelevant suggestions in all categories. Runs 3 and 4 failed
to identify both typos. Examples of harmful suggestions included erroneously linking esophageal _disease_ with
esophageal _obstruction_, suggesting that EMTs should exceed their scope in providing airways, and suggesting that
providers should provide cricothyrotomies without approval.

| File | Quality  | Ranking | clinical | operational | wording |
|------|----------|---------|----------|-------------|---------|
| 0    | moderate | 1       | 3/3      | 0/3         | 1/5     |
| 1    | low      | 2       | 1/2      | 0/4         | 4/5     |
| 2    | very low | 5       | 0/4      | 1/4         | 3/8     |
| 3    | very low | 4       | 1/3 *    | 0/4         | 1/2 *   |
| 4    | low      | 3       | 1/3      | 1/3 *       | 1/4     |

"*" indicates harmful or hallucinated suggestions

### Test 3: Text evaluation

#### Sub-test 3.1: Text evaluation from best extraction

| File | Quality | Ranking | clinical | operational | wording |
|------|---------|---------|----------|-------------|---------|
| 0    | medium  | 2       | 2/7      | 0/5         | 6/11    |
| 1    | low     | 4       | 0/3      | 1/3         | 4/5     |
| 2    | medium  | 1       | 4/5      | 2/5         | 2/11    |
| 3    | medium  | 3       | 1/3      | 2/5         | 4/8     |
| 4    | low     | 5       | 0/4      | 1/4         | 5/6     |

As a whole, there were some very good points in this round of outputs. I would say that this round noticeably
outperformed the oneshot evaluations. I noticed that the models are currently producing way more (at least 2x)
suggestions than would be optimal. Many of those suggestions are duplicative or extremely minor. I find that the model
has great clinical knowledge but struggles to reason logically about real operational scenarios (eg should you apply
capnography before or after getting an airway). I feel like different runs "focus" on different aspects of the prompt -
some runs are very clinically focused and others are very formatting/wording focused. This phenomenon would need
additional research, but it might indicate that a multi-agent system is required for optimal results. (This architecture
could be similar to results published by the major AI health research teams.)

#### Sub-test 3.2: Text evaluation from worst extraction

| File | Quality  | Ranking | clinical | operational | wording |
|------|----------|---------|----------|-------------|---------|
| 0    | low      | 3       | 2/5      | 0/5         | 4/6     |
| 1    | very low | 4       | 0/2      | 2/3         | 2/9     |
| 2    | very low | 5       | 0/3      | 3/4         | 0/4     |
| 3    | medium   | 1       | 4/7      | 1/6         | 2/6     |
| 4    | medium   | 2       | 4/5      | 0/4         | 3/9     |

There was a noticeable increase in the number of "extraction artifacts" noticed in the LLM output. It is tough to say,
but I believe the quality of the other outputs also suffered.

#### Sub-test 3.3: Comparison of outputs from 2, 3.1, 3.2

As mentioned previously, I believe that the outputs from test 3.1 were significantly better in depth and breadth than
3.2 or the one-shot evaluations.

## Conclusion

I think it is clear that the multi-step process is beneficial for model outputs. There may be a way to include the one-shot evaluation as a check for typos that may have gotten wiped away by the LLM. Further experiments of interest include:
* testing the potential prompt changes noticed during the review process
* testing various multi-agent architectures
* testing other models and platforms