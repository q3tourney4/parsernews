def validate_paramters(order: str, offset: int, limit: int) -> bool:
    valid_parameter = True
    order_values = {"title", "url", "limit"}

    if order not in order_values:
        valid_parameter = False

    if not 0 <= offset <= 10:
        valid_parameter = False

    if not 1 <= limit <= 30:
        valid_parameter = False

    return valid_parameter
