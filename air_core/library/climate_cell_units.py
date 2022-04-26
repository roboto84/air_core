# Climacell attribute units

pollen_index_scale: dict = {
    '0': 'None',
    '0.5': 'Extremely Low',
    '1': 'Very Low',
    '1.5': 'Very Low',
    '2': 'Low',
    '2.5': 'Low',
    '3': 'Medium',
    '3.5': 'Medium',
    '4': 'High',
    '4.5': 'Very High',
    '5': 'Extremely High'
}

health_concern_scale: dict = {
    '0': 'Good',
    '1': 'Moderate',
    '2': 'Unhealthy for Sensitive Groups',
    '3': 'Unhealthy',
    '4': 'Very Unhealthy',
    '5': 'Hazardous'
}

primary_pollutants: dict = {
    '0': 'PM2.5',
    '1': 'PM10',
    '2': 'O3',
    '3': 'NO2',
    '4': 'CO',
    '5': 'SO2'
}

moon_phase_scale: dict = {
    '0': 'New',
    '1': 'Waxing Crescent',
    '2': 'First Quarter',
    '3': 'Waxing Gibbous',
    '4': 'Full',
    '5': 'Waning Gibbous',
    '6': 'Third Quarter',
    '7': 'Waning Crescent'
}

precipitation_type: dict = {
    '0': 'N/A',
    '1': 'Rain',
    '2': 'Snow',
    '3': 'Freezing Rain',
    '4': 'Ice Pellets'
}

weather_code: dict = {
    '0': 'Unknown',
    '1000': 'Clear',
    '1001': 'Cloudy',
    '1100': 'Mostly Clear',
    '1101': 'Partly Cloudy',
    '1102': 'Mostly Cloudy',
    '2000': 'Fog',
    '2100': 'Light Fog',
    '3000': 'Light Wind',
    '3001': 'Wind',
    '3002': 'Strong Wind',
    '4000': 'Drizzle',
    '4001': 'Rain',
    '4200': 'Light Rain',
    '4201': 'Heavy Rain',
    '5000': 'Snow',
    '5001': 'Flurries',
    '5100': 'Light Snow',
    '5101': 'Heavy Snow',
    '6000': 'Freezing Drizzle',
    '6001': 'Freezing Rain',
    '6200': 'Light Freezing Rain',
    '6201': 'Heavy Freezing Rain',
    '7000': 'Ice Pellets',
    '7101': 'Heavy Ice Pellets',
    '7102': 'Light Ice Pellets',
    '8000': 'Thunderstorm'
}

weather_code_emojis: dict = {
    'Unknown': '🌡️',
    'Clear': '🌞️',
    'Cloudy': '🌥️️',
    'Mostly Clear': '🌞',
    'Partly Cloudy': '🌥️',
    'Mostly Cloudy': '🌥️',
    'Fog': '🌫',
    'Light Fog': '🌫',
    'Light Wind': '🌬',
    'Wind': '🌬',
    'Strong Wind': '🌬',
    'Drizzle': '☔',
    'Rain': '☔',
    'Light Rain': '☔',
    'Heavy Rain': '☔',
    'Snow': '❄️',
    'Flurries': '❄️',
    'Light Snow': '❄️',
    'Heavy Snow': '❄',
    'Freezing Drizzle': '❄',
    'Freezing Rain': '❄',
    'Light Freezing Rain': '❄',
    'Heavy Freezing Rain': '❄',
    'Ice Pellets': '❄',
    'Heavy Ice Pellets': '❄',
    'Light Ice Pellets': '❄',
    'Thunderstorm': '⛈'
}

general_weather_scales: dict = {
    'cloudCover': '%',
    'epaHealthConcern': health_concern_scale,
    'epaIndex': 'EPA AQI',
    'epaPrimaryPollutant': primary_pollutants,
    'fireIndex': 'FWI',
    'grassGrassIndex': pollen_index_scale,
    'grassIndex': pollen_index_scale,
    'hailBinary': 'Binary Prediction',
    'humidity': '%',
    'mepHealthConcern': health_concern_scale,
    'mepIndex': 'MEP AQI',
    'mepPrimaryPollutant': primary_pollutants,
    'moonPhase': moon_phase_scale,
    'pollutantCO': 'ppb',
    'pollutantNO2': 'ppb',
    'pollutantO3': 'ppb',
    'pollutantSO2': 'ppb',
    'precipitationProbability': '%',
    'precipitationType': precipitation_type,
    'treeAcacia': pollen_index_scale,
    'treeAsh': pollen_index_scale,
    'treeBeech': pollen_index_scale,
    'treeBirch': pollen_index_scale,
    'treeCedar': pollen_index_scale,
    'treeCottonwood': pollen_index_scale,
    'treeCypress': pollen_index_scale,
    'treeElder': pollen_index_scale,
    'treeElm': pollen_index_scale,
    'treeHemlock': pollen_index_scale,
    'treeHickory': pollen_index_scale,
    'treeIndex': pollen_index_scale,
    'treeJuniper': pollen_index_scale,
    'treeMahagony': pollen_index_scale,
    'treeMaple': pollen_index_scale,
    'treeMulberry': pollen_index_scale,
    'treeOak': pollen_index_scale,
    'treePine': pollen_index_scale,
    'treeSpruce': pollen_index_scale,
    'treeSycamore': pollen_index_scale,
    'treeWalnut': pollen_index_scale,
    'treeWillow': pollen_index_scale,
    'weatherCode': weather_code,
    'weedGrassweedIndex': pollen_index_scale,
    'weedIndex': pollen_index_scale,
    'windDirection': 'degrees'
}

metric_units_core: dict = {
    'cloudBase': 'km',
    'cloudCeiling': 'km',
    'dewPoint': '°C',
    'particulateMatter10': 'μg/m³',
    'particulateMatter25': 'μg/m³',
    'precipitationIntensity': 'mm/hr',
    'pressureSeaLevel': 'hPa',
    'pressureSurfaceLevel': 'hPa',
    'solarDIF': 'W/m²',
    'solarDIR': 'W/m²',
    'solarGHI': 'W/m²',
    'temperature': '°C',
    'temperatureApparent': '°C',
    'visibility': 'km',
    'windDirection': 'degrees',
    'windGust': 'm/s',
    'windSpeed': 'm/s'
}

imperial_units_core: dict = {
    'cloudBase': 'mi',
    'cloudCeiling': 'mi',
    'dewPoint': '°F',
    'particulateMatter10': 'μg/ft³',
    'particulateMatter25': 'μg/ft³',
    'precipitationIntensity': 'in/hr',
    'pressureSeaLevel': 'inHg',
    'pressureSurfaceLevel': 'inHg',
    'solarDIF': 'Btu/ft²',
    'solarDIR': 'Btu/ft²',
    'solarGHI': 'Btu/ft²',
    'temperature': '°F',
    'temperatureApparent': '°F',
    'visibility': 'mi',
    'windGust': 'mph',
    'windSpeed': 'mph'
}

metric_units = {**metric_units_core, **general_weather_scales}
imperial_units = {**imperial_units_core, **general_weather_scales}
