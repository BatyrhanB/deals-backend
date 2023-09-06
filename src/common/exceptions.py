from rest_framework.exceptions import APIException


class ObjectNotFoundException(APIException):
    status_code = 404


class UniqueObjectException(APIException):
    status_code = 400


class NothingToDoException(APIException):
    status_code = 400


class AlreadyExist(APIException):
    status_code = 400


class SomethingGetWrongException(APIException):
    status_code = 500


class RequiredFieldException(APIException):
    status_code = 400


class RequiredQueryException(APIException):
    status_code = 400


class IncorrectFileFormat(APIException):
    status_code = 400
    message = "Only csv files can be uploaded"