from deepeval.evaluate import evaluate
from dotenv import load_dotenv
from deepeval.metrics import GEval
from deepeval.test_case import LLMTestCaseParams, LLMTestCase

def load_file(filename):
    with open(f'test/{filename}', 'r') as f:
        return f.read()

def test_example_output():
    load_dotenv()

    correctness_metric = GEval(
        name="Correctness",
        criteria="Evaluate the helpfulness of the protocol review based on correctness and completeness.",
        # NOTE: you can only provide either criteria or evaluation_steps, and not both
        evaluation_steps=[
            "Check whether the actual output contains the recommendations in the expected output.",
            "Penalize extraneous or hallucinated recommendations.",
        ],
        evaluation_params=[LLMTestCaseParams.INPUT, LLMTestCaseParams.ACTUAL_OUTPUT, LLMTestCaseParams.EXPECTED_OUTPUT],
    )

    test_case_bad = LLMTestCase(
        input=load_file('example_prompt.txt'),
        actual_output=load_file('example_bad.csv'),
        expected_output=load_file('gold_standard.csv')
    )

    test_case_good = LLMTestCase(
        input=load_file('example_prompt.txt'),
        actual_output=load_file('example_good.csv'),
        expected_output=load_file('gold_standard.csv')
    )

    print('bad example:\n')
    correctness_metric.measure(test_case_bad)
    print(correctness_metric.score, correctness_metric.reason)

    print('good example:\n')
    correctness_metric.measure(test_case_good)
    print(correctness_metric.score, correctness_metric.reason)

    evaluate(test_cases=[test_case_good], metrics=[correctness_metric])