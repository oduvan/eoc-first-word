from checkio_referee import RefereeRank, ENV_NAME



import settings_env
from tests import TESTS


class Referee(RefereeRank):
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    DEFAULT_FUNCTION_NAME = "first_word"
    FUNCTION_NAMES = {
        "python_3": "first_word",
        "js_node": "firstWord"
    }
    ENV_COVERCODE = {
        
    }