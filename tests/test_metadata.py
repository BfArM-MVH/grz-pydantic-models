import importlib.resources
import itertools

import pytest

from . import resources
from grz_pydantic_models.submission.metadata.v1 import GrzSubmissionMetadata


@pytest.mark.parametrize(
    "dataset,version", itertools.product(["panel", "wes_tumor_germline", "wgs_tumor_germline"], ["1.1.1", "1.1.4"])
)
def test_examples(dataset: str, version: str):
    metadata_str = (
        importlib.resources.files(resources).joinpath("example_metadata", dataset, f"v{version}.json").read_text()
    )
    GrzSubmissionMetadata.model_validate_json(metadata_str)


def test_example_wgs_lr():
    metadata_str = (
        importlib.resources.files(resources).joinpath("example_metadata", "wgs_lr", f"v1.1.4.json").read_text()
    )
    GrzSubmissionMetadata.model_validate_json(metadata_str)
