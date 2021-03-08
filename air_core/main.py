from library.air import Air

if __name__ == '__main__':
    air_array = ['2021-02-27T14:08:00-05:00', '83.98', '83.91', 'n/a', '38', '55.71', 'Mostly Clear', '0', 'Rain',
                 '30', '41', 'Good', 'O3', '0.32', '0.24', '3.58', '4.01', '45.68', '3.76', 'None', 'Very High', 'None']

    new_air = Air('imperial')
    new_air.set_weather_with_array(air_array)

    print(new_air.get_basic_weather(), '\n')
    print(new_air.get_pollution(), '\n')
    print(new_air.get_pollen(), '\n')

