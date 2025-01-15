import requests
from django.http import JsonResponse
from django.views import View

class WeatherView(View):
    def get(self, request):
        city = request.GET.get('city', 'India')
        api_key = '6d1b899158d4149627e49d7003483c08 '
        
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