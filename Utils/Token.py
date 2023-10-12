import io
import jwt
from datetime import datetime, timedelta, timezone


def generate_expiration_date(day=0, hours=0, minutes=0, seconds=0):
    actual_date = datetime.now(tz=timezone.utc)
    expiration_time = timedelta(
        days=day, hours=hours, minutes=minutes, seconds=seconds
    )
    expiration_time = datetime.timestamp(actual_date + expiration_time)
    return Out_response(data=expiration_time)


# Function to generate token
def generate_token(user_token, pass_token):
    try:
        expiration_time = generate_expiration_date(day=2)["token"]
        payload = {
            "exp": expiration_time,
            "user_id": user_token,
            "user_pass": pass_token,
        }
        token = jwt.encode(payload, "KOPAYTOKEN", algorithm="HS256")
        return Out_response(False, "Token generated", data=token)

    except Exception as err:
        error_message = str(err)  # Extract the error message as a string
        error_args = err.args  # Extract any error arguments if needed
        return Out_response(error=True, message=error_message, data=error_args)


# Function to verify the token
def verify_token(token):
    try:
        token_verify = jwt.decode(token, "KOPAYTOKEN", algorithms="HS256")
        if token_verify:
            res = {
                "error": False,
                "message": "Valid token"
            }
            return res
        else:
            return Error_response(True, "Invalid token", 101)
    except Exception as err:
        return Error_response(err, "Expired token", 101)
    except jwt.ExpiredSignatureError as err:
        return Error_response(err, "Expired token", 101)
    except jwt.exceptions.InvalidSignatureError as err:
        return Error_response(err, "Invalid token signature", 102)
    except jwt.exceptions.InvalidTokenError as err:
        return Error_response(err, "Invalid token", 102)
    except jwt.exceptions.DecodeError as err:
        return Error_response(err, "Unable to decode token", 103)
    except jwt.exceptions.InvalidKeyError as err:
        return Error_response(err, "Invalid secret key", 102)
    except jwt.exceptions.InvalidAlgorithmError as err:
        return Error_response(err, "Invalid algorithm token", 102)


def Out_response(
    error=False,
    message="Success",
    data=None,
):

    res = {
        "error": error,
        "message": message,
        "token": data,
    }
    return res


# Function for exceptions
def Error_response(err, message, error_code=None):

    if len(err.args) > 1:

        res = {
            "error": True,
            # "message": f"Error interno en el servidor al procesar esta solicitud",
            "message": f"{message}",
            "token": f"""Codigo interno:{error_code}
\n

                Codigo Error: {err.args[0]}
\n

                Mensaje Error: {err.args[1]}
""",
        }

    else:

        res = {
            "error": True,
            "message": error_code,
            "data": {"Codigo interno": error_code, "Mensaje Error": err.args[0]},
        }

    return res
