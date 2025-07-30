def format_number(value, specifier):
    result = format(value, specifier)
    return result

formatted_result = format_number(145, 'o')
print("Formatted Result:", formatted_result)