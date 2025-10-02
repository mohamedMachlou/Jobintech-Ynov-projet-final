from validations.common import validate_gt, validate_lte, validate_required

def validate_buy_ticket_qty(q, max_qty):
    if isinstance(v := validate_required(q), str):
        return v

    if isinstance(v := validate_gt(q, 0), str):
        return v

    if isinstance(v := validate_lte(q, max_qty), str):
        return v

    return True
