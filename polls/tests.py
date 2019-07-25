from django.test import TestCase

# Create your tests here.

import datetime

from django.test import TestCase
from django.test import Client
from django.utils import timezone

from .models import Question


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

class IndexViewTests(TestCase):
    def test_view_doesnt_display_future_question(self):
        """
        Verify that if there is a question with future date was created , it is not published in the view , with the granularity of days"
        """
        #Create a question with future view
        futuretime = timezone.now() + datetime.timedelta(days=1)
        futureQuestionText = "I am a futuristic question used for testing"
        future_question = Question(pub_date=futuretime,question_text=futureQuestionText)
        testclient = Client()
        # The content returned is in bytes , hence conversion needs to be made 
        # https://webkul.com/blog/string-and-bytes-conversion-in-python3-x/
        responsecontent = testclient.get("/polls/").content.decode()
        self.assertIs(responsecontent.find(futureQuestionText) < 0 , True)





