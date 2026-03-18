# Experiment 001: One-Shot vs MultiStep

## Abstract

Based on my prior exploratory work with AI protocol reviews, I always included an intermediate step to convert a PDF to
text prior to conducting the clinical portion of the review. Now, models can work directly with the raw pdf file.
How does the performance change if no intermediate step is performed? I expect only a small change in performance, at
the cost of lower observability.

## Methods

I will run two tests on GPT 4.1 on the adult airway protocol and hand examine the results to get a basic sense of the
performance considerations before deciding on a project architecture.

### Control

1. Send PDF file to GPT 4.1 with [control prompt #1](./EXP_001/exp001_prompt_control.txt).
2. Send extracted text to GPT 4.1 with [control prompt #2](./EXP_001/exp001_prompt_control2.txt).

### Test

1. Send PDF file to GPT 4.1 with [test_prompt](./EXP_001/exp001_prompt_test.txt).

## Results

Test results are much less useful than the control. The test result primarily restates the existing protocol with the
conclusion "this is clinically sound." The control results are much more focused on identifying problems to be fixed.
There was one case identified where the control extraction process pre-emptively corrected a typo ("PROTCOL") which
meant that it did not show up in the multi-step process but was appropriately flagged by the oneshot review.

## Conclusion

No decision will be made until further testing is conducted. Can the oneshot process be made more useful by explicitly
stating that the process should focus on _problems_? Can the multistep process be fixed by an explicit instruction to
refrain from correcting typos?