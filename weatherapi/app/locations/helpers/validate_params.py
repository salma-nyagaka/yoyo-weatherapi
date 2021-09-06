from rest_framework.serializers import ValidationError

from .serialization_errors import error_dict


def validate_params(params):
    """Function that validates if the aqi, q,  and 
    key have been passed in the parameters
    Args:
        params(dict): request parameters
    """

    if 'days' not in params:
        raise ValidationError(
            error_dict['required_params'].format("'day' is")
        )  
