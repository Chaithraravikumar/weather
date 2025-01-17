import requests
from django.http import JsonResponse
from django.views import View

class WeatherView(View):
    def get(self, request):
        city = request.GET.get('city', 'India')
        api_key = '40269b9328c376abfb2648ee6ad60b63'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()

            weather_info = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
            }
            return JsonResponse(weather_info)
        except requests.exceptions.HTTPError as http_err:
            return JsonResponse({'error': str(http_err)}, status=response.status_code)
        except requests.exceptions.RequestException as req_err:
            return JsonResponse({'error': 'Network error occurred'}, status=500)
        except KeyError:
            return JsonResponse({'error': 'Unexpected data format'}, status=500)