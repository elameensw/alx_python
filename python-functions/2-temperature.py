def convert_to_celsius(fahrenheit):
    result = ((fahrenheit - 32)/9)* 5
    round_result = round(result, 2)
    return round_result
