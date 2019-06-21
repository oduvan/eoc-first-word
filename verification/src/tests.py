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
            "input": "Hello world",
            "answer": "Hello"
        },
        {
            "input": " a word ",
            "answer": "a",
            "explanation": "starts with space"
        },
        {
            "input": "don't touch it",
            "answer": "don't",
            "explanation": "apostrophe can be a part of a word"
        },
        {
            "input": "greetings, friends",
            "answer": "greetings",
            "explanation": "comma is not a part of a word"
        },
        {
            "input": "... and so on ...",
            "answer": "and",
            "explanation": "text starts with dots"
        },
        {
            "input": "hi",
            "answer": "hi",
            "explanation": "text consists of only one word"
        }
    ],
    "Extra": [
        {
            "input": "Holy Edison",
            "answer": "Holy"
        },
        {
            "input": "Don't speak... I know just what you're saying",
            "answer": "Don't"
        },
        {
            "input": "Hello.World",
            "answer": "Hello"
        }
    ]
}
