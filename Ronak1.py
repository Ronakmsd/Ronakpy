def aggregate_weather_data(records):
    city_data = {}

    for record in records:
        city = record.get('city')
        temperature = record.get('temperature')
        humidity = record.get('humidity')

        if city not in city_data:
            city_data[city] = {
                'total_temperature': 0,
                'total_humidity': 0,
                'count': 0
            }

        if temperature is not None:
            city_data[city]['total_temperature'] += temperature
        if humidity is not None:
            city_data[city]['total_humidity'] += humidity

        city_data[city]['count'] += 1

    # Calculating averages
    averages = {}
    for city, data in city_data.items():
        count = data['count']
        avg_temp = data['total_temperature'] / count if count > 0 else None
        avg_humidity = data['total_humidity'] / count if count > 0 else None
        
        averages[city] = {
            'average_temperature': avg_temp,
            'average_humidity': avg_humidity
        }

    return averages

# Example usage:
records = [
    {'city': 'New York', 'temperature': 75, 'humidity': 60},
    {'city': 'Los Angeles', 'temperature': 85},
    {'city': 'New York', 'humidity': 55},
    {'city': 'Chicago', 'temperature': 70, 'humidity': 50},
    {'city': 'Los Angeles', 'humidity': 65},
]

result = aggregate_weather_data(records)
print(result)