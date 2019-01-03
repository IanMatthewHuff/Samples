import unittest
from survey import AnonSurvey

class TestAnonSurvey(unittest.TestCase):
    """ Tests for anon survey """

    def setUp(self):
        """ Create survey and initial responses """
        question = "What language did you first learn to speak?"
        self.my_survey = AnonSurvey(question)
        self.responses = ['English', 'Spanish', 'Japanese']

    def test_store_single_response(self):
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

unittest.main()
