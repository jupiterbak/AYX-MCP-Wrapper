# coding: utf-8

"""
Alteryx Server API V3

No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

OpenAPI spec version: 3

Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

from src.server_client.configuration import Configuration


class ReducedServerConnectionView(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {"id": "str", "name": "str", "connection_string": "str", "connection_type": "str"}

    attribute_map = {
        "id": "id",
        "name": "name",
        "connection_string": "connectionString",
        "connection_type": "connectionType",
    }

    def __init__(self, id=None, name=None, connection_string=None, connection_type=None, _configuration=None):  # noqa: E501
        """ReducedServerConnectionView - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._name = None
        self._connection_string = None
        self._connection_type = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.connection_string = connection_string
        self.connection_type = connection_type

    @property
    def id(self):
        """Gets the id of this ReducedServerConnectionView.  # noqa: E501


        :return: The id of this ReducedServerConnectionView.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ReducedServerConnectionView.


        :param id: The id of this ReducedServerConnectionView.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this ReducedServerConnectionView.  # noqa: E501


        :return: The name of this ReducedServerConnectionView.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ReducedServerConnectionView.


        :param name: The name of this ReducedServerConnectionView.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def connection_string(self):
        """Gets the connection_string of this ReducedServerConnectionView.  # noqa: E501


        :return: The connection_string of this ReducedServerConnectionView.  # noqa: E501
        :rtype: str
        """
        return self._connection_string

    @connection_string.setter
    def connection_string(self, connection_string):
        """Sets the connection_string of this ReducedServerConnectionView.


        :param connection_string: The connection_string of this ReducedServerConnectionView.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and connection_string is None:
            raise ValueError("Invalid value for `connection_string`, must not be `None`")  # noqa: E501

        self._connection_string = connection_string

    @property
    def connection_type(self):
        """Gets the connection_type of this ReducedServerConnectionView.  # noqa: E501


        :return: The connection_type of this ReducedServerConnectionView.  # noqa: E501
        :rtype: str
        """
        return self._connection_type

    @connection_type.setter
    def connection_type(self, connection_type):
        """Sets the connection_type of this ReducedServerConnectionView.


        :param connection_type: The connection_type of this ReducedServerConnectionView.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and connection_type is None:
            raise ValueError("Invalid value for `connection_type`, must not be `None`")  # noqa: E501

        self._connection_type = connection_type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict()) if hasattr(item[1], "to_dict") else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(ReducedServerConnectionView, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ReducedServerConnectionView):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReducedServerConnectionView):
            return True

        return self.to_dict() != other.to_dict()
