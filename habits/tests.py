from django.test import TestCase
from users.models import User, Profile
from .models import Habit


class HabitTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="habituser", password="pass")

    def test_habit_creation(self):
        """Создание привычки и связь с пользователем."""
        habit = Habit.objects.create(
            owner=self.user,
            action="Read 10 pages",
            time="10:00",
            is_rewarding=True,
            is_public=False,
            periodicity_days=1
        )
        self.assertEqual(habit.owner, self.user)
        self.assertEqual(str(habit), habit.action)

    def test_habit_list_filter(self):
        """Проверка фильтров и булевых полей."""
        Habit.objects.create(owner=self.user, action="Run", time="08:00", is_rewarding=True, is_public=True)
        Habit.objects.create(owner=self.user, action="Sleep", time="22:00", is_rewarding=False, is_public=False)
        rewarding = Habit.objects.filter(is_rewarding=True)
        public = Habit.objects.filter(is_public=True)
        self.assertEqual(rewarding.count(), 1)
        self.assertEqual(public.count(), 1)
