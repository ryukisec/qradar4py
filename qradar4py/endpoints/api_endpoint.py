import requests


class QRadarAPIEndpoint:
    """"
    The parent class for a QRadar API endpoints providing a constructor and several classmethods.
    """
    def __init__(self, baseurl, header, verify):
        self._baseurl = baseurl
        self._header = header
        self._verify = verify

    def get_header(self):
        """
        Return the header to use in API calls.
        :return: The header defined while constructing the class.
        """
        return self._header

    def _call(self, method, url, response_type='json', **kwargs):
        """
        Wrapper around the requests request method.
        :param method:  The HTTP method to use.
        :param url:     The url to query.
        :param kwargs:  The arguments to pass to requests.
        :return:        The status code and the response in JSON.
        """
        header = self._header.copy()
        header.update(kwargs.pop('headers', {}))
        header.update(kwargs.pop('mime_type', {}))
        if response_type == 'json':
            response = requests.request(method, url, headers=header, verify=self._verify, **kwargs)
            return response.status_code, response.json()

        header.update({'Accept': response_type})
        response = requests.request(method, url, headers=header, verify=self._verify, **kwargs)
        return response.status_code, response.text


def header_vars(*valid_header_fields):
    """
    Decorator maker to assign variables to the header field.
    :param valid_header_fields: The variables to move from **kwargs to header.
    :return:                    A decorator that checks for the passed variables and moves them to the header var.
    """
    def decorator(func):
        def wrapped(self, *args, **all_args):
            header = all_args.pop('headers', {})
            valid_header = {key: all_args[key] for key in all_args if key in valid_header_fields}

            header.update(valid_header)

            return func(self, *args, headers=header, **all_args)
        return wrapped
    return decorator


def request_vars(*valid_param_fields):
    """
        Decorator maker to assign variables to the params field.
        :param valid_param_fields:  The variables to move from **kwargs to params.
        :return:                    A decorator that checks for the passed variables and moves them to the params var.
        """
    def decorator(func):
        def wrapped(self, *args, **all_args):
            params = all_args.pop('params', {})
            valid_params = {key: all_args[key] for key in all_args if key in valid_param_fields}

            params.update(valid_params)

            return func(self, *args, params=params, **all_args)
        return wrapped
    return decorator
