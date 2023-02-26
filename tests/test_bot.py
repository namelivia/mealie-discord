from unittest import TestCase
from unittest.mock import patch
from mealie_discord.mealie import Mealie


class TestBot(TestCase):
    @patch("mealie_discord.mealie.requests")
    def test_meal_message_no_meal(self, m_requests):
        m_requests.get.return_value.json.return_value = {}
        message = Mealie.get_todays_meal_message(
            "mealie_token", "https://mealie.example.com"
        )
        m_requests.get.assert_called_once_with(
            "https://mealie.example.com/api/groups/mealplans/today",
            headers={"Authorization": "Bearer mealie_token"},
        )
        assert message == "No hay comida planificada para hoy"

    @patch("mealie_discord.mealie.requests")
    def test_meal_message_some_food(self, m_requests):
        m_requests.get.return_value.json.return_value = [
            {"entryType": "breakfast", "recipe": {"name": "Ice cream"}},
            {"entryType": "lunch", "recipe": {"name": "Pizza"}},
            {"entryType": "dinner", "recipe": {"name": "Hamburger"}},
        ]
        message = Mealie.get_todays_meal_message(
            "mealie_token", "https://mealie.example.com"
        )
        m_requests.get.assert_called_once_with(
            "https://mealie.example.com/api/groups/mealplans/today",
            headers={"Authorization": "Bearer mealie_token"},
        )
        assert (
            message
            == """Desayuno: Ice cream
Comida: Pizza
Cena: Hamburger
"""
        )
