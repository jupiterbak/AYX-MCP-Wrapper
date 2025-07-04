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


class Member(object):
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
        "active_directory_object": "ADObject",
        "user_id": "str",
        "date_added_to_group": "datetime",
        "added_by_user_id": "str",
    }

    attribute_map = {
        "active_directory_object": "activeDirectoryObject",
        "user_id": "userId",
        "date_added_to_group": "dateAddedToGroup",
        "added_by_user_id": "addedByUserId",
    }

    def __init__(
        self,
        active_directory_object=None,
        user_id=None,
        date_added_to_group=None,
        added_by_user_id=None,
        _configuration=None,
    ):  # noqa: E501
        """Member - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._active_directory_object = None
        self._user_id = None
        self._date_added_to_group = None
        self._added_by_user_id = None
        self.discriminator = None

        if active_directory_object is not None:
            self.active_directory_object = active_directory_object
        if user_id is not None:
            self.user_id = user_id
        if date_added_to_group is not None:
            self.date_added_to_group = date_added_to_group
        if added_by_user_id is not None:
            self.added_by_user_id = added_by_user_id

    @property
    def active_directory_object(self):
        """Gets the active_directory_object of this Member.  # noqa: E501


        :return: The active_directory_object of this Member.  # noqa: E501
        :rtype: ADObject
        """
        return self._active_directory_object

    @active_directory_object.setter
    def active_directory_object(self, active_directory_object):
        """Sets the active_directory_object of this Member.


        :param active_directory_object: The active_directory_object of this Member.  # noqa: E501
        :type: ADObject
        """

        self._active_directory_object = active_directory_object

    @property
    def user_id(self):
        """Gets the user_id of this Member.  # noqa: E501


        :return: The user_id of this Member.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this Member.


        :param user_id: The user_id of this Member.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def date_added_to_group(self):
        """Gets the date_added_to_group of this Member.  # noqa: E501


        :return: The date_added_to_group of this Member.  # noqa: E501
        :rtype: datetime
        """
        return self._date_added_to_group

    @date_added_to_group.setter
    def date_added_to_group(self, date_added_to_group):
        """Sets the date_added_to_group of this Member.


        :param date_added_to_group: The date_added_to_group of this Member.  # noqa: E501
        :type: datetime
        """

        self._date_added_to_group = date_added_to_group

    @property
    def added_by_user_id(self):
        """Gets the added_by_user_id of this Member.  # noqa: E501


        :return: The added_by_user_id of this Member.  # noqa: E501
        :rtype: str
        """
        return self._added_by_user_id

    @added_by_user_id.setter
    def added_by_user_id(self, added_by_user_id):
        """Sets the added_by_user_id of this Member.


        :param added_by_user_id: The added_by_user_id of this Member.  # noqa: E501
        :type: str
        """

        self._added_by_user_id = added_by_user_id

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
        if issubclass(Member, dict):
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
        if not isinstance(other, Member):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Member):
            return True

        return self.to_dict() != other.to_dict()
