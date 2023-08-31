"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": ["abcabcbb"],
            "answer": 3
        },
        {
            "input": ["bbbbb"],
            "answer": 1
        },
        {
            "input": ["pwwkew"],
            "answer": 3
        },
        {
            "input": ["abcdef"],
            "answer": 6
        },
        {
            "input": [""],
            "answer": 0
        },
        {
            "input": ["au"],
            "answer": 2
        },
        {
            "input": ["dvdf"],
            "answer": 3
        },
    ],
    "Extra": [
        {
            "input": ["anviaj"],
            "answer": 5
        },
        {
            "input": ["ohomm"],
            "answer": 3
        },
    ]
}
