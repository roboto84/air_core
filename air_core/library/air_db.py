import logging.config
import os
from air_core.library.air import Air
from willow_core.library.sqlite_db import SqlLiteDb
from sqlite3 import Connection, Cursor, Error, Row
from typing import Any, Optional


class AirDb(SqlLiteDb):
    def __init__(self, logging_object: Any, db_location: str):
        self._logger: logging.Logger = logging_object.getLogger(type(self).__name__)
        self._logger.setLevel(logging.INFO)
        super().__init__(logging_object, db_location)
        self._check_db_schema()

    def _check_db_schema(self) -> None:
        if self._check_db_state(['WEATHER', 'WEATHER_FORECAST']):
            self._logger.info(f'DB schema looks good')
        else:
            self._logger.info(f'Tables not found')
            self._create_db_schema()

    def _create_db_schema(self) -> None:
        try:
            conn: Connection = self._db_connect()
            db_cursor: Cursor = conn.cursor()
            with open(f'{os.path.dirname(__file__)}/sql/schema.sql') as f:
                db_cursor.executescript(f.read())
            self._logger.info(f'Initializing Air_DB schema')
            self._db_close(conn)
            self._logger.info(f'Database has been initialized')
        except Error as error:
            self._logger.info(f'Error occurred initializing Air_DB', error)

    def clear_location_weather_forecast(self, lat_long: tuple[float, float]) -> None:
        try:
            conn: Connection = self._db_connect()
            db_cursor: Cursor = conn.cursor()
            query: str = f'DELETE FROM WEATHER_FORECAST WHERE latitude = ? and longitude = ?;'
            db_cursor.execute(query, lat_long)
            self._db_close(conn)
        except Error as error:
            self._logger.info(f'Error occurred clearing forecast weather in Air_DB', error)

    def insert_weather_forecast(self, lat_long: tuple[float, float], air_data: Air) -> None:
        self._insert_weather(f'{os.path.dirname(__file__)}/sql/insert_into_forecast_weather.sql', lat_long, air_data)

    def insert_current_weather(self, lat_long: tuple[float, float], air_data: Air) -> None:
        self._insert_weather(f'{os.path.dirname(__file__)}/sql/insert_into_current_weather.sql', lat_long, air_data)

    def _insert_weather(self, sql_path: str, lat_long: tuple[float, float], air_data: Air) -> None:
        weather: dict = air_data.get_all_weather()
        latitude: float = lat_long[0]
        longitude: float = lat_long[1]

        try:
            conn: Connection = self._db_connect()
            db_cursor: Cursor = conn.cursor()
            self._logger.info(f'Inserting weather data into Air_DB')
            with open(sql_path, 'r') as file:
                db_cursor.execute(
                    file.read(),
                    (latitude, longitude, weather['date'],
                     weather['temperature']['value'], weather['temperature']['unit'],
                     weather['temperatureApparent']['value'], weather['temperatureApparent']['unit'],
                     weather['moonPhase'],
                     weather['humidity']['value'], weather['humidity']['unit'],
                     weather['dewPoint']['value'], weather['dewPoint']['unit'],
                     weather['weatherCode'],
                     weather['precipitationProbability']['value'], weather['precipitationProbability']['unit'],
                     weather['precipitationType'],
                     weather['pressureSurfaceLevel']['value'], weather['pressureSurfaceLevel']['unit'],
                     weather['epaIndex']['value'], weather['epaIndex']['unit'],
                     weather['epaHealthConcern'], weather['epaPrimaryPollutant'],
                     weather['particulateMatter10']['value'], weather['particulateMatter10']['unit'],
                     weather['particulateMatter25']['value'], weather['particulateMatter25']['unit'],
                     weather['pollutantCO']['value'], weather['pollutantCO']['unit'],
                     weather['pollutantNO2']['value'], weather['pollutantNO2']['unit'],
                     weather['pollutantO3']['value'], weather['pollutantO3']['unit'],
                     weather['pollutantSO2']['value'], weather['pollutantSO2']['unit'],
                     weather['grassIndex'], weather['treeIndex'], weather['weedIndex']))
                self._db_close(conn)
        except IOError as e:
            self._logger.info(f'IOError was thrown', e)
        except Exception as e:
            self._logger.exception(f'Exception was thrown', e)

    def get_weather_history(self, number_of_records: int) -> list[dict]:
        weather_history: list[Row] = self.get_weather(None, number_of_records)
        weather_history_dicts: list[dict] = [self._table_row_to_dict(row) for row in weather_history]
        return weather_history_dicts

    def get_current_weather(self) -> dict:
        current_weather: list[Row] = self.get_weather('CURRENT_WEATHER')
        return self._table_row_to_dict(current_weather[0])

    def get_weather_forecast(self) -> list[dict]:
        weather_forecast: list[Row] = self.get_weather('WEATHER_FORECAST')
        weather_forecast_dicts: list[dict] = [self._table_row_to_dict(row) for row in weather_forecast]
        return weather_forecast_dicts

    def get_weather(self, query_type: Optional[str] = None, query_record_limit: Optional[int] = 0) -> list[Row]:
        base_query: str = f'select * from WEATHER ORDER BY id DESC'
        if query_record_limit > 0:
            query = f'{base_query} LIMIT {query_record_limit}'
        elif query_type == 'CURRENT_WEATHER':
            query = f'{base_query} LIMIT 1'
        elif query_type == 'WEATHER_FORECAST':
            query = f'select * from WEATHER_FORECAST ORDER BY id'
        else:
            query = base_query
        try:
            conn: Connection = self._db_connect()
            self.set_row_factory(conn)
            db_cursor: Cursor = conn.cursor()
            table_results: list = db_cursor.execute(query).fetchall()
            self._db_close(conn)
            return table_results
        except Error as error:
            self._logger.info(f'Error occurred getting table rows from Air_DB', error)

    @staticmethod
    def _table_row_to_dict(row: Row) -> dict:
        data: dict = dict(row)
        return {
            'date': data['date'],
            'temperature': {data['temp_value']},
            'temperatureApparent': {data['temp_apparent_value']},
            'moonPhase': data['moon_phase'],
            'humidity': {data['humidity_value']},
            'dewPoint': {data['dew_point_value']},
            'weatherCode': data['weather_code'],
            'precipitationProbability': {data['precipitation_probability_value']},
            'precipitationType': data['precipitation_type'],
            'pressureSurfaceLevel': {data['pressure_surface_level_value']},
            'epaIndex': {data['epa_index_value']},
            'epaHealthConcern': data['epa_health_concern'],
            'epaPrimaryPollutant': data['epa_primary_pollutant'],
            'particulateMatter10': {data['particulate_matter10_value']},
            'particulateMatter25': {data['particulate_matter25_value']},
            'pollutantCO': {data['pollutant_CO_value']},
            'pollutantNO2': {data['pollutant_NO2_value']},
            'pollutantO3': {data['pollutant_O3_value']},
            'pollutantSO2': {data['pollutant_SO2_value']},
            'grassIndex': {data['grass_index']},
            'treeIndex': {data['tree_index']},
            'weedIndex': {data['weed_index']}
        }
