from enum import Enum

class ExperimentType(Enum):
    Correlation = 1

class Experiment:
    def __init__(self, type: ExperimentType, prompt: str, options: List):
        self.type = type
        self.prompt = prompt
        self.options = options


AllExperiments = [
    Experiment(
        ExperimentType.Correlation,
        "",
        [],
    )
]