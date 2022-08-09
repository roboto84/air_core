#  Configuration for different plotting perspectives
from .types.types import Unit

UNITS = Unit.imperial
TIMEZONE = 'UTC'
file_settings: dict = {
    'live_data': {
        'data_file': 'liveData.csv'
    },
    'next_days': {
        'data_file': 'forecastData.csv'
    }
}
