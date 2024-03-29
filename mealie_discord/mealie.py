import requests
import logging

logger = logging.getLogger(__name__)


class Mealie:
    @staticmethod
    def _translate_entry_type(entryType):
        return {
            "breakfast": "Desayuno",
            "lunch": "Comida",
            "dinner": "Cena",
        }[entryType]

    @staticmethod
    def _no_food_message():
        return "No hay comida planificada para hoy"

    @staticmethod
    def _get_headers(token):
        return {"Authorization": f"Bearer {token}"}

    @staticmethod
    def get_todays_meal_message(token, url):
        try:
            response = requests.get(
                f"{url}/api/groups/mealplans/today", headers=Mealie._get_headers(token)
            )
            response.raise_for_status()
            data = response.json()
            if len(data) == 0:
                return Mealie._no_food_message()

            message = ""
            for entry in data:
                message += f"{Mealie._translate_entry_type(entry['entryType'])}: "
                message += f"{entry['recipe']['name']}\n"
            return message
        except requests.RequestException as e:
            logger.error(f"Request failed: {e}")
            raise
