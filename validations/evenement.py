from validations.common import validate_required, validate_alphanumeric, validate_date, validate_int, validate_float



def validate_chaine(my_str: str):
    if isinstance(v := validate_required(my_str), str):
        return v

    if isinstance(v := validate_alphanumeric(my_str), str):
        return v

    return True


# Validation alphanumérique pour titre, lieu, artiste
def validate_chaine(value: str):
    if isinstance(v := validate_required(value), str):
        return v
    if isinstance(v := validate_alphanumeric(value), str):
        return v
    return True

# Validation de la date (option future_only=True pour concerts)
def validate_date_concert(value: str):
    if isinstance(v := validate_required(value), str):
        return v
    if isinstance(v := validate_date(value, future_only=True), str):
        return v
    return True

# Validation du prix de base
def validate_prix_base(value: str):
    if isinstance(v := validate_required(value), str):
        return v
    if isinstance(v := validate_float(value), str):
        return v
    return True

# Validation de la capacité
def validate_capacite(value: str):
    if isinstance(v := validate_required(value), str):
        return v
    if isinstance(v := validate_int(value), str):
        return v
    return True
