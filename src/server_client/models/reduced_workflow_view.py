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


class ReducedWorkflowView(object):
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
    swagger_types = {
        "id": "str",
        "source_app_id": "str",
        "name": "str",
        "owner_id": "str",
        "date_created": "datetime",
        "published_version_number": "int",
        "is_amp": "bool",
        "execution_mode": "str",
    }

    attribute_map = {
        "id": "id",
        "source_app_id": "sourceAppId",
        "name": "name",
        "owner_id": "ownerId",
        "date_created": "dateCreated",
        "published_version_number": "publishedVersionNumber",
        "is_amp": "isAmp",
        "execution_mode": "executionMode",
    }

    def __init__(
        self,
        id=None,
        source_app_id=None,
        name=None,
        owner_id=None,
        date_created=None,
        published_version_number=None,
        is_amp=None,
        execution_mode=None,
        _configuration=None,
    ):  # noqa: E501
        """ReducedWorkflowView - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._source_app_id = None
        self._name = None
        self._owner_id = None
        self._date_created = None
        self._published_version_number = None
        self._is_amp = None
        self._execution_mode = None
        self.discriminator = None

        self.id = id
        self.source_app_id = source_app_id
        self.name = name
        self.owner_id = owner_id
        self.date_created = date_created
        self.published_version_number = published_version_number
        self.is_amp = is_amp
        self.execution_mode = execution_mode

    @property
    def id(self):
        """Gets the id of this ReducedWorkflowView.  # noqa: E501


        :return: The id of this ReducedWorkflowView.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ReducedWorkflowView.


        :param id: The id of this ReducedWorkflowView.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def source_app_id(self):
        """Gets the source_app_id of this ReducedWorkflowView.  # noqa: E501


        :return: The source_app_id of this ReducedWorkflowView.  # noqa: E501
        :rtype: str
        """
        return self._source_app_id

    @source_app_id.setter
    def source_app_id(self, source_app_id):
        """Sets the source_app_id of this ReducedWorkflowView.


        :param source_app_id: The source_app_id of this ReducedWorkflowView.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and source_app_id is None:
            raise ValueError("Invalid value for `source_app_id`, must not be `None`")  # noqa: E501

        self._source_app_id = source_app_id

    @property
    def name(self):
        """Gets the name of this ReducedWorkflowView.  # noqa: E501


        :return: The name of this ReducedWorkflowView.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ReducedWorkflowView.


        :param name: The name of this ReducedWorkflowView.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def owner_id(self):
        """Gets the owner_id of this ReducedWorkflowView.  # noqa: E501


        :return: The owner_id of this ReducedWorkflowView.  # noqa: E501
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this ReducedWorkflowView.


        :param owner_id: The owner_id of this ReducedWorkflowView.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and owner_id is None:
            raise ValueError("Invalid value for `owner_id`, must not be `None`")  # noqa: E501

        self._owner_id = owner_id

    @property
    def date_created(self):
        """Gets the date_created of this ReducedWorkflowView.  # noqa: E501


        :return: The date_created of this ReducedWorkflowView.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this ReducedWorkflowView.


        :param date_created: The date_created of this ReducedWorkflowView.  # noqa: E501
        :type: datetime
        """
        if self._configuration.client_side_validation and date_created is None:
            raise ValueError("Invalid value for `date_created`, must not be `None`")  # noqa: E501

        self._date_created = date_created

    @property
    def published_version_number(self):
        """Gets the published_version_number of this ReducedWorkflowView.  # noqa: E501


        :return: The published_version_number of this ReducedWorkflowView.  # noqa: E501
        :rtype: int
        """
        return self._published_version_number

    @published_version_number.setter
    def published_version_number(self, published_version_number):
        """Sets the published_version_number of this ReducedWorkflowView.


        :param published_version_number: The published_version_number of this ReducedWorkflowView.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and published_version_number is None:
            raise ValueError("Invalid value for `published_version_number`, must not be `None`")  # noqa: E501

        self._published_version_number = published_version_number

    @property
    def is_amp(self):
        """Gets the is_amp of this ReducedWorkflowView.  # noqa: E501


        :return: The is_amp of this ReducedWorkflowView.  # noqa: E501
        :rtype: bool
        """
        return self._is_amp

    @is_amp.setter
    def is_amp(self, is_amp):
        """Sets the is_amp of this ReducedWorkflowView.


        :param is_amp: The is_amp of this ReducedWorkflowView.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and is_amp is None:
            raise ValueError("Invalid value for `is_amp`, must not be `None`")  # noqa: E501

        self._is_amp = is_amp

    @property
    def execution_mode(self):
        """Gets the execution_mode of this ReducedWorkflowView.  # noqa: E501


        :return: The execution_mode of this ReducedWorkflowView.  # noqa: E501
        :rtype: str
        """
        return self._execution_mode

    @execution_mode.setter
    def execution_mode(self, execution_mode):
        """Sets the execution_mode of this ReducedWorkflowView.


        :param execution_mode: The execution_mode of this ReducedWorkflowView.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and execution_mode is None:
            raise ValueError("Invalid value for `execution_mode`, must not be `None`")  # noqa: E501
        allowed_values = ["Safe", "SemiSafe", "Standard"]  # noqa: E501
        if self._configuration.client_side_validation and execution_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `execution_mode` ({0}), must be one of {1}".format(execution_mode, allowed_values)  # noqa: E501
            )

        self._execution_mode = execution_mode

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
        if issubclass(ReducedWorkflowView, dict):
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
        if not isinstance(other, ReducedWorkflowView):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReducedWorkflowView):
            return True

        return self.to_dict() != other.to_dict()
