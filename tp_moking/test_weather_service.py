"""Test sans MOCKING"""

# import unittest
# from weather_service import get_temperature

# class testWeatherService(unittest.TestCase):
    
#     def test_get_temperature(self):
#         """Test basique qui va poser problème"""
#         temp = get_temperature
#         #Comment tester ça ? L'API peut être en panne, lente, différente...
#         self.assertIsNotNone(temp)
        
# if __name__ == '__main__':
#     unittest.main()

"""Test avec MOCKING"""
import unittest
import requests, json
from requests.exceptions import RequestException
from unittest.mock import patch, Mock
from weather_service import get_temperature, save_weather_report

class TestWeatherService(unittest.TestCase):
    
    def setUp(self):
        self.weather_data = {
            'main': {
                'temp': 25.5
            }
        }
        self.test_city = 'Paris'
        pass
    
    @patch('weather_service.requests.get')
    def test_get_temperature_success(self, mock_get):
        # 1. Créez un objet Mock pour simuler la réponse de l'API
        mock = Mock()
        mock.status_code = 200
        
        # 2. Créez les données JSON que l'API renverrait
        mock.json.return_value = self.weather_data

        # 3. Configurez le mock pour retourner la réponse simulée
        mock_get.return_value = mock

        # 4. Appelez la fonction que vous testez
        temperature = get_temperature(self.test_city)

        # 5. Vérifiez que la température est correcte
        #TODO: Vérifiez que la température retournée est bien 25.5
        self.assertEqual(temperature, self.weather_data['main']['temp'])  
        
        # 6 Vérifiez que requests.get a été appelé avec les bons paramètres
        #TODO: Utilisez mock_get.assert_called_once_with pour vérifier l'url et les paramètres
        mock_get.assert_called_once_with(
            'http://api.openweathermap.org/data/2.5/weather',
            params={
                'q': self.test_city,
                'appid': '441f54eb9b8819b3a05d1674294bb055', 
                'units': 'metric'
            }
        )
    
    @patch('weather_service.requests.get')
    def test_get_temperature_failure(self, mock_get):
        mock = Mock()
        mock.status_code = 404
        mock_get.return_value = mock
        temperature = get_temperature('Metrocity')
        self.assertIsNone(temperature)
        pass
    
    @patch('weather_service.requests.get')
    def test_get_temperature_network_error(self, mock_get):
        mock_get.side_effect = RequestException("Network error")
        temperature = get_temperature('Atlantis')
        self.assertIsNone(temperature)
        pass
    
class TestWeatherReport(unittest.TestCase):
    
    def setUp(self):
        self.test_city = 'Paris'
        self.test_filename = 'test_weather_log.json'
        pass
    
    @patch('weather_service.datetime')
    @patch('builtins.open', new_callable=unittest.mock.mock_open, read_data='[]')
    @patch('weather_service.get_temperature')
    
    def test_save_weather_report_success(self, mock_get_temp, mock_file, mock_datetime):
        mock_get_temp.return_value = 25.5
        mock_datetime.now.return_value.isoformat.return_value = '2025-06-20T12:00:00'
        
        result = save_weather_report(self.test_city, self.test_filename)
        
        # Vérifiez que le résultat est True
        self.assertTrue(result)
        mock_file.assert_called_with(self.test_filename, 'w')
        
        # Vérifiez que get_temperature a été appelé avec la bonne ville
        mock_get_temp.assert_called_once_with(self.test_city)
        
        #Vérifiez que le fichier a été ouvert en lecture puis en écriture
        mock_file.assert_called_with(self.test_filename, 'w')
        
        pass
  

if __name__ == '__main__':
    unittest.main()