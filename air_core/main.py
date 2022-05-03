
from typing import NoReturn
from library.air import Air
from library.types.types import Unit


def print_out_air(air_record: Air) -> NoReturn:
    print(air_record.get_basic_weather(), '\n')
    print(air_record.get_pollution(), '\n')
    print(air_record.get_pollen(), '\n')
    print(air_record.data_to_csv_string(), '\n')


if __name__ == '__main__':
    air_data: dict = {
        'dewPoint': 34.2,
        'humidity': 83,
        'precipitationProbability': 53.9,
        'precipitationType': 1,
        'pressureSurfaceLevel': 29.68,
        'temperature': 38.98,
        'temperatureApparent': 27.41,
        'weatherCode': 1001,
        'epaHealthConcern': 1,
        'epaIndex': 70,
        'epaPrimaryPollutant': 0,
        'particulateMatter10': 1.03,
        'particulateMatter25': 0.58,
        'pollutantCO': 1.16,
        'pollutantNO2': 22.6,
        'pollutantO3': 16.97,
        'pollutantSO2': 1.96,
        'grassIndex': 0,
        'treeIndex': 0,
        'weedIndex': 0
    }
    air_array = ['2021-02-27T14:08:00-05:00', '83.98', '83.91', 'n/a', '38', '55.71', 'Mostly Clear', '0', 'Rain',
                 '30', '41', 'Good', 'O3', '0.32', '0.24', '3.58', '4.01', '45.68', '3.76', '0', '0', '0']

    air_from_array = Air(Unit.imperial)
    air_from_array.set_weather_with_array(air_array)
    print('air_from_array:')
    print_out_air(air_from_array)

    air_from_dict = Air(Unit.imperial, air_data, '2021-02-27T14:08:00-05:00')
    print('air_from_dict:')
    print_out_air(air_from_dict)

    empty_air = Air()
    print(f'Metric Units:\n{empty_air.get_units()}')
    print(f'\nImperial Units:\n{empty_air.get_units(Unit.imperial)}')
    print(f'\nMetric Units:\n{empty_air.get_units(Unit.metric)}')
