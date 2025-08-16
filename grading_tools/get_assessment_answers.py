import json
from typing import Any
from smolagents import tool
import os

@tool
def fetch_assessment_answers_by_assessment_id(assessment_id: str) -> Any:
    """
    Fetches and returns a mocked (hardcoded) assessment answer key.

    This function simulates fetching an assessment's answer key by its ID.
    Currently, it ignores the provided ID and always returns the same
    dataset for testing and development purposes.

    Args:
        assessment_id (str): The ID of the assessment to fetch (currently ignored).

    Returns:
        dict: A dictionary with the assessment data, including 'assessment_id',
              'quantity_of_questions', and 'correct_alternatives'.
    """
    mock_data = {
        "assessment_id": assessment_id,
        "assessment_name": "Sample Exam",
        "quantity_of_questions": 20,
        "correct_alternatives": {
               "1": ["D"], "2": ["B"], "3": ["B"], "4": ["B", "E"],
               "5": ["B"], "6": [], "7": ["D", "E"], "8": ["C"],
               "9": ["A"], "10": ["A"], "11": ["B"], "12": ["C"],
               "13": ["B"], "14": ["C"], "15": ["A", "B", "C"], "16": ["C"],
               "17": ["A"], "18": ["C"], "19": [], "20": ["A"]
        }
    }
    
    return mock_data