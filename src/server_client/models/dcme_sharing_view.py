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


class DCMESharingView(object):
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
    swagger_types = {"execution": "DCMESharingForExecutionView", "collaboration": "DCMESharingForCollaborationView"}

    attribute_map = {"execution": "execution", "collaboration": "collaboration"}

    def __init__(self, execution=None, collaboration=None, _configuration=None):  # noqa: E501
        """DCMESharingView - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._execution = None
        self._collaboration = None
        self.discriminator = None

        if execution is not None:
            self.execution = execution
        if collaboration is not None:
            self.collaboration = collaboration

    @property
    def execution(self):
        """Gets the execution of this DCMESharingView.  # noqa: E501


        :return: The execution of this DCMESharingView.  # noqa: E501
        :rtype: DCMESharingForExecutionView
        """
        return self._execution

    @execution.setter
    def execution(self, execution):
        """Sets the execution of this DCMESharingView.


        :param execution: The execution of this DCMESharingView.  # noqa: E501
        :type: DCMESharingForExecutionView
        """

        self._execution = execution

    @property
    def collaboration(self):
        """Gets the collaboration of this DCMESharingView.  # noqa: E501


        :return: The collaboration of this DCMESharingView.  # noqa: E501
        :rtype: DCMESharingForCollaborationView
        """
        return self._collaboration

    @collaboration.setter
    def collaboration(self, collaboration):
        """Sets the collaboration of this DCMESharingView.


        :param collaboration: The collaboration of this DCMESharingView.  # noqa: E501
        :type: DCMESharingForCollaborationView
        """

        self._collaboration = collaboration

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
        if issubclass(DCMESharingView, dict):
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
        if not isinstance(other, DCMESharingView):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DCMESharingView):
            return True

        return self.to_dict() != other.to_dict()
