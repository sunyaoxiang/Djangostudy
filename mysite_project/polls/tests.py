# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

import datetime
from django.test import TestCase
from django.utils import timezone

from .models import Question,Choice
from django.urls import reverse

class QuestionModelsTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        # was_published_recently() 应该对 pub_date 字段值是将来的那些问题返回 False
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date = time)
        self.assertIs(future_question.was_published_recently(),False)

    def test_was_published_recently_with_old_question(self):
        time = timezone.now() + datetime.timedelta(days=1,seconds=1)
        old_question = Question(pub_date = time)
        self.assertIs(old_question.was_published_recently(),False)

    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=23,minutes=59,seconds=59)
        recent_question = Question(pub_date = time)
        self.assertIs(recent_question.was_published_recently(),True)


def create_question(question_text,days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text = question_text,pub_date = time,pub_time = '00:00:00')


class QuestionIndexViewTests(TestCase):
    def test_no_questin(self):
        """
        如果数据库里没有保存问题，应该显示一个合适的提示信息。
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"No Polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'],[])

    def test_past_question(self):
        """
        值 pub_date 是过去的，问题应该被显示在主页上。
        """
        create_question(question_text="Past question.",days=-30)
        response =self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )

    def test_future_question(self):
        """
        值 pub_date 是将来的，问题不应该被显示在主页上。
        """
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No Polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_future_question_and_past_question(self):
        """
        如果数据库里同时存有过去和将来的投票，那么只应该显示过去那些。
        """
        create_question(question_text="Past question.", days=-30)
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )

    def test_two_past_questions(self):
        """
        问题索引页应该可以显示多个问题。
        """
        create_question(question_text="Past question 1.", days=-30)
        create_question(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question 2.>', '<Question: Past question 1.>']
        )


def create_choice(choice_text,votes,question):
    time = timezone.now() + datetime.timedelta(days=-1)
    return Choice.objects.create(choice_text = choice_text,cho_date = time,votes = votes,question_id=question.id)

class QuestionResultsViewTests(TestCase):

    def test_vote_is_than_one(self):
        votes_text1 = u'翻译的好'
        votes_text2 = u'坏'
        votes_num1 = 33
        votes_num2 = 22
        question = create_question(question_text="Test_For_Choice",days=-1)
        create_choice(choice_text=votes_text1,votes=votes_num1,question=question)
        create_choice(choice_text=votes_text2,votes=votes_num2,question=question)
        response = self.client.get(reverse('polls:results',args=(question.id,)))
        self.assertContains(response,votes_text1)
        self.assertContains(response,votes_text2)
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'<td><a>{}</a></td>'.format(votes_num1))
        self.assertContains(response,'<td><a>{}</a></td>'.format(votes_num2))


from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
class TestByselenium(StaticLiveServerTestCase):
    # python manage.py dumpdata --natural-primary -o fire.json
    fixtures = ['fire.json']

    @classmethod
    def setUpClass(cls):
        # question = create_question(question_text="Test_For_Choice",days=-1)
        super(TestByselenium, cls).setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(1)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(TestByselenium, cls).tearDownClass()

    def test_login(self):
        self.selenium.get('%s%s' % (self.live_server_url,reverse("polls:index")))
        pass