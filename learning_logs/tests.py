from django.test import TestCase
from learning_logs.models import Topic, Entry

class TopicModelTestCase(TestCase):

    def setUp(self):
        self.topic = Topic.objects.create(text='Test Topic')

    def test_topic_creation(self):
        self.assertEqual(self.topic.text, 'Test Topic')
        self.assertIsNotNone(self.topic.date_added)

    def test_topic_str(self):
        self.assertEqual(str(self.topic), 'Test Topic')


class EntryModelTestCase(TestCase):

    def setUp(self):
        self.topic = Topic.objects.create(text='Test Topic')
        self.entry = Entry.objects.create(topic=self.topic, text='Test Entry Text')

    def test_entry_creation(self):
        self.assertEqual(self.entry.topic, self.topic)
        self.assertEqual(self.entry.text, 'Test Entry Text')
        self.assertIsNotNone(self.entry.date_added)

    def test_entry_str(self):
        self.assertEqual(str(self.entry), 'Test Entry Text'[:50])

    def test_entries_related_to_topic(self):
        entry2 = Entry.objects.create(topic=self.topic, text='Another Entry Text')
        self.assertEqual(self.topic.entry_set.count(), 2)
        self.assertIn(self.entry, self.topic.entry_set.all())
        self.assertIn(entry2, self.topic.entry_set.all())
