import logging.config
import os
from air_core.library.air import Air
from willow_core.library.sqlite_db import SqlLiteDb
from sqlite3 import Connection, Cursor, Error, Row
from typing import Any


class AirDb(SqlLiteDb):
    def __init__(self, logging_object: Any, db_location: str):
        self._logger: logging.Logger = logging_object.getLogger(type(self).__name__)
        self._logger.setLevel(logging.INFO)
        super().__init__(logging_object, db_location)
        self._check_db_schema()

    def _check_db_schema(self) -> None:
        if self._check_db_state(['CURRENT_WEATHER', 'FORECAST_WEATHER']):
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

    def clear_location_forecast_weather(self, lat_long: tuple[float, float]) -> None:
        try:
            conn: Connection = self._db_connect()
            db_cursor: Cursor = conn.cursor()
            with open(f'{os.path.dirname(__file__)}/sql/delete_forecast_weather.sql') as f:
                db_cursor.execute(f.read(), lat_long)
            self._db_close(conn)
        except Error as error:
            self._logger.info(f'Error occurred clearing forecast weather in Air_DB', error)

    def insert_forecast_weather(self, lat_long: tuple[float, float], air_data: Air) -> None:
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

    def get_forecast_weather(self) -> list[Row]:
        return self.get_weather('FORECAST_WEATHER')

    def get_current_weather(self) -> list[Row]:
        return self.get_weather('CURRENT_WEATHER')

    def get_weather(self, table_name: str) -> list[Row]:
        try:
            conn: Connection = self._db_connect()
            self.set_row_factory(conn)
            db_cursor: Cursor = conn.cursor()
            table_results: list = db_cursor.execute(
                f'select * from {table_name} ORDER BY id DESC;').fetchall()
            self._db_close(conn)
            return table_results
        except Error as error:
            self._logger.info(f'Error occurred getting table rows from Air_DB', error)
