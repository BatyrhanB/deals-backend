from rest_framework.exceptions import APIException


class ObjectNotFoundException(APIException):
    status_code = 404


class UniqueObjectException(APIException):
    status_code = 400

class NothingToDoException(APIException):
    status_code = 400

class ObjectDeletedException(APIException):
    status_code = 400


class TypeErrorException(APIException):
    status_code = 400


class IncorrectPasswordException(APIException):
    status_code = 400


class AlreadyExist(APIException):
    status_code = 400


class SomethingGetWrongException(APIException):
    status_code = 500


class RequiredFieldException(APIException):
    status_code = 400


class RequiredQueryException(APIException):
    status_code = 400
