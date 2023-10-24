from django.test import TestCase

import datetime
from django.utils import timezone

from .models import Question

from django.urls import reverse

# Create your tests here.

def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionModelTest(TestCase):
    
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions 
        whose pub_date is in the future
        """
        future_time = timezone.now() + datetime.timedelta(days =30)
        future_question = Question(pub_date=future_time)

        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        time = timezone.now() - datetime.timedelta(hours=24, seconds=1)
        old_question = Question(pub_date = time)

        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        old_question = Question(pub_date = time)

        self.assertIs(old_question.was_published_recently(), True)

class QuestionIndexViewTests(TestCase):

    def test_no_questions(self):
        '''
        no question exist -> show message
        '''
        response = self.client.get(reverse("polls:index"))
        # print(response.content)
        self.assertContains(response, 'No polls are available')
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_question(self):
        '''
        pub_data in past -> display 
        '''
        question = create_question(question_text='past question', days = -30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], [question])

    def test_future_question(self):
        '''
        pub_data in future -> do not display
        '''
        create_question(question_text='future q', days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_future_and_past_question(self):
        question = create_question(question_text='past question', days = -30)
        create_question(question_text='future q', days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], [question])

    def test_2_past_questions(self):
        question_1 = create_question(question_text='past question 1', days = -30)
        question_2 = create_question(question_text='past question 2', days = -5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], [question_2, question_1])

    def test_show_only_3_when_more_questions(self):
        question_1 = create_question(question_text='past question 1', days = -30)
        question_2 = create_question(question_text='past question 2', days = -15)
        question_3 = create_question(question_text='past question 3', days = -10)
        question_4 = create_question(question_text='past question 4', days = -5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], [question_4, question_3, question_2])
        self.assertCountEqual(response.context['latest_question_list'], [question_3, question_2, question_4])

class QuestionDetailViewTests(TestCase):

    def test_future_question(self):
        '''
        Detail future question -> 404 error
        '''
        future_question = create_question(question_text='future q', days=5)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        '''
        Detail past question
        '''
        past_question = create_question(question_text='past question', days=-5)
        url = reverse('polls:detail', args=(past_question.id, ))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)
