import pytest
from crewai_sec_class.main import ExampleFlow

def test_flow_initialization():
    flow = ExampleFlow()
    assert flow is not None

def test_flow_model():
    flow = ExampleFlow()
    assert flow.model == "gemini/gemini-2.0-flash-exp" 