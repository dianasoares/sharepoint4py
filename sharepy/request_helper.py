import requests
from .errors import SharePyRequestError


def get(session: requests.Session, url, **kwargs):
    try:
        response = session.get(url, **kwargs)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as err:
        raise SharePyRequestError("SharePy HTTP Get Failed", err)


def post(session: requests.Session, url, **kwargs):
    try:
        response = session.post(url, **kwargs)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as err:
        raise SharePyRequestError("SharePy HTTP Post Failed", err)



def delete(session: requests.Session, url, **kwargs):
    try:
        response = session.delete(url, **kwargs)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as err:
        raise SharePyRequestError("SharePy HTTP Post Failed", err)
