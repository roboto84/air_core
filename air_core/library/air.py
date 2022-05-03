# Air weather, pollution and pollen properties
from typing import Any
from .climate_cell_units import metric_units, imperial_units
from .types.types import Unit


class Air:
    def __init__(self, unit_choice: Unit = Unit.metric, weather_data: dict = None, date: str = 'n/a'):
        self.unit_choice = unit_choice
        if self.unit_choice == Unit.imperial:
            self.unit_standard: dict = imperial_units
        else:
            self.unit_standard: dict = metric_units

        self.weather: dict = {
            'date': date,
            'temperature': 'n/a',
            'temperatureApparent': 'n/a',
            'moonPhase': 'n/a',
            'humidity': 'n/a',
            'dewPoint': 'n/a',
            'weatherCode': 'n/a',
            'precipitationProbability': 'n/a',
            'precipitationType': 'n/a',
            'pressureSurfaceLevel': 'n/a',
            'epaIndex': 'n/a',
            'epaHealthConcern': 'n/a',
            'epaPrimaryPollutant': 'n/a',
            'particulateMatter10': 'n/a',
            'particulateMatter25': 'n/a',
            'pollutantCO': 'n/a',
            'pollutantNO2': 'n/a',
            'pollutantO3': 'n/a',
            'pollutantSO2': 'n/a',
            'grassIndex': 'n/a',
            'treeIndex': 'n/a',
            'weedIndex': 'n/a'
        }
        self.single_value_attributes: list[str] = ['grassIndex', 'treeIndex', 'weedIndex', 'date']
        self.single_value_mapped_attributes: list[str] = ['moonPhase', 'weatherCode', 'precipitationType',
                                                          'epaHealthConcern', 'epaPrimaryPollutant']

        if weather_data:
            for key in weather_data:
                self._set_weather_attribute(key, weather_data[key])

    def __str__(self) -> str:
        return f'{self._air_to_string("summary", self.weather)}'

    def _set_weather_attribute(self, attribute_type: str, attribute_value: Any) -> None:
        if attribute_type in self.single_value_attributes:
            self.weather[f'{attribute_type}'] = attribute_value
        elif attribute_type in self.single_value_mapped_attributes:
            if isinstance(attribute_value, int):
                self.weather[f'{attribute_type}'] = self.unit_standard[f'{attribute_type}'][f'{attribute_value}']
            else:
                self.weather[f'{attribute_type}'] = attribute_value
        else:
            self.weather[f'{attribute_type}'] = {}
            self.weather[f'{attribute_type}']['value'] = attribute_value
            self.weather[f'{attribute_type}']['unit'] = self.unit_standard[f'{attribute_type}']

    def _air_to_string(self, output_type: str, data: dict) -> str:
        data_as_string: str = ''
        for key in data:
            if key in self.single_value_attributes or key in self.single_value_mapped_attributes:
                if output_type == 'summary':
                    data_as_string += f'{key}: {data[key]},'
                else:
                    data_as_string += f'{data[key]},'
            else:
                if output_type == 'summary':
                    data_as_string += f'{key}: {data[key]["value"]}{data[key]["unit"]},'
                else:
                    data_as_string += f'{data[key]["value"]},'
        return data_as_string.rstrip(',')

    def _get_sub_dict(self, key_array) -> dict:
        return {key: self.weather[key] for key in key_array}

    def get_units(self, weather_unit_type: Unit = None):
        unit_type: Unit
        if weather_unit_type:
            unit_type = weather_unit_type
        else:
            unit_type = self.unit_choice

        unit_legend: dict = {}
        if unit_type == Unit.imperial:
            units = imperial_units
        else:
            units = metric_units

        for key in self.weather:
            if key not in self.single_value_attributes and key not in self.single_value_mapped_attributes:
                unit_legend[f'{key}'] = units[f'{key}']
        return unit_legend

    def set_weather_with_array(self, data_array: list[str]) -> None:
        weather_keys: list[str] = list(self.weather.keys())
        for index in range(len(data_array)):
            if data_array[index] != 'n/a':
                self._set_weather_attribute(weather_keys[index], data_array[index])

    def get_all_weather(self) -> dict:
        return self.weather

    def get_basic_weather(self) -> dict:
        return self._get_sub_dict(['date', 'temperature', 'temperatureApparent', 'moonPhase', 'humidity', 'dewPoint',
                                   'weatherCode', 'precipitationProbability', 'precipitationType',
                                   'pressureSurfaceLevel'])

    def get_pollution(self) -> dict:
        return self._get_sub_dict(['date', 'epaIndex', 'epaHealthConcern', 'epaPrimaryPollutant',
                                   'particulateMatter10', 'particulateMatter25', 'pollutantCO', 'pollutantNO2',
                                   'pollutantO3', 'pollutantSO2'])

    def get_pollen(self) -> dict:
        return self._get_sub_dict(['date', 'grassIndex', 'treeIndex', 'weedIndex'])

    def get_date(self) -> str:
        return self.weather['date']

    def data_to_csv_string(self) -> str:
        data_string: str = f'{self._air_to_string("csv", self.weather)}'
        return data_string

    def data_key_order(self) -> str:
        data_as_string: str = ''
        for index in self.weather:
            data_as_string += f'{index},'
        return data_as_string.rstrip(',')
