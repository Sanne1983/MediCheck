import subprocess
import time
import unittest
import requests

class TestInteractionsEndpoint(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Start der API
        cls.app_process = subprocess.Popen(
            ["python", "api.py"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        time.sleep(2)  # Warten bis der Server bereit ist

    def test_get_interactions_success(self):
        # Test mit Daten aus der Datenbank
        response = requests.get('http://127.0.0.1:8080/interactions?pzn1=64738228&pzn2=46758392')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"interaktion": "Gleichzeitige Einnahme nicht empfohlen! Die Wirkung von anderen Arzneimitteln wird durch das Medikament mit der PZN 64738228 abgeschwächt. Bitte halten Sie einen Abstand von 2 Stunden bei der Einnahme ein. "})

if __name__ == "__main__":
    unittest.main()