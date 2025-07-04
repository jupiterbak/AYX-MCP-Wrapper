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


class UpdateUserContract(object):
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
        "first_name": "str",
        "last_name": "str",
        "email": "str",
        "role": "str",
        "default_worker_tag": "str",
        "can_schedule_jobs": "bool",
        "can_prioritize_jobs": "bool",
        "can_assign_jobs": "bool",
        "can_create_collections": "bool",
        "is_api_enabled": "bool",
        "default_credential_id": "str",
        "is_account_locked": "bool",
        "is_active": "bool",
        "is_validated": "bool",
        "time_zone": "str",
        "language": "str",
        "can_create_and_update_dcm": "bool",
        "can_share_for_execution_dcm": "bool",
        "can_share_for_collaboration_dcm": "bool",
        "can_manage_generic_vaults_dcm": "bool",
    }

    attribute_map = {
        "id": "id",
        "first_name": "firstName",
        "last_name": "lastName",
        "email": "email",
        "role": "role",
        "default_worker_tag": "defaultWorkerTag",
        "can_schedule_jobs": "canScheduleJobs",
        "can_prioritize_jobs": "canPrioritizeJobs",
        "can_assign_jobs": "canAssignJobs",
        "can_create_collections": "canCreateCollections",
        "is_api_enabled": "isApiEnabled",
        "default_credential_id": "defaultCredentialId",
        "is_account_locked": "isAccountLocked",
        "is_active": "isActive",
        "is_validated": "isValidated",
        "time_zone": "timeZone",
        "language": "language",
        "can_create_and_update_dcm": "canCreateAndUpdateDcm",
        "can_share_for_execution_dcm": "canShareForExecutionDcm",
        "can_share_for_collaboration_dcm": "canShareForCollaborationDcm",
        "can_manage_generic_vaults_dcm": "canManageGenericVaultsDcm",
    }

    def __init__(
        self,
        id=None,
        first_name=None,
        last_name=None,
        email=None,
        role=None,
        default_worker_tag=None,
        can_schedule_jobs=None,
        can_prioritize_jobs=None,
        can_assign_jobs=None,
        can_create_collections=None,
        is_api_enabled=None,
        default_credential_id=None,
        is_account_locked=None,
        is_active=None,
        is_validated=None,
        time_zone=None,
        language=None,
        can_create_and_update_dcm=None,
        can_share_for_execution_dcm=None,
        can_share_for_collaboration_dcm=None,
        can_manage_generic_vaults_dcm=None,
        _configuration=None,
    ):  # noqa: E501
        """UpdateUserContract - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._first_name = None
        self._last_name = None
        self._email = None
        self._role = None
        self._default_worker_tag = None
        self._can_schedule_jobs = None
        self._can_prioritize_jobs = None
        self._can_assign_jobs = None
        self._can_create_collections = None
        self._is_api_enabled = None
        self._default_credential_id = None
        self._is_account_locked = None
        self._is_active = None
        self._is_validated = None
        self._time_zone = None
        self._language = None
        self._can_create_and_update_dcm = None
        self._can_share_for_execution_dcm = None
        self._can_share_for_collaboration_dcm = None
        self._can_manage_generic_vaults_dcm = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        self.email = email
        self.role = role
        self.default_worker_tag = default_worker_tag
        self.can_schedule_jobs = can_schedule_jobs
        self.can_prioritize_jobs = can_prioritize_jobs
        self.can_assign_jobs = can_assign_jobs
        self.can_create_collections = can_create_collections
        self.is_api_enabled = is_api_enabled
        self.default_credential_id = default_credential_id
        self.is_account_locked = is_account_locked
        self.is_active = is_active
        self.is_validated = is_validated
        self.time_zone = time_zone
        self.language = language
        if can_create_and_update_dcm is not None:
            self.can_create_and_update_dcm = can_create_and_update_dcm
        if can_share_for_execution_dcm is not None:
            self.can_share_for_execution_dcm = can_share_for_execution_dcm
        if can_share_for_collaboration_dcm is not None:
            self.can_share_for_collaboration_dcm = can_share_for_collaboration_dcm
        if can_manage_generic_vaults_dcm is not None:
            self.can_manage_generic_vaults_dcm = can_manage_generic_vaults_dcm

    @property
    def id(self):
        """Gets the id of this UpdateUserContract.  # noqa: E501

        The id of the user to be updated. Optional as will be set via the controller path parameter.  # noqa: E501

        :return: The id of this UpdateUserContract.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdateUserContract.

        The id of the user to be updated. Optional as will be set via the controller path parameter.  # noqa: E501

        :param id: The id of this UpdateUserContract.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def first_name(self):
        """Gets the first_name of this UpdateUserContract.  # noqa: E501

        This field is required on non windows authentication type.  # noqa: E501

        :return: The first_name of this UpdateUserContract.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this UpdateUserContract.

        This field is required on non windows authentication type.  # noqa: E501

        :param first_name: The first_name of this UpdateUserContract.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and first_name is not None and len(first_name) > 255:
            raise ValueError("Invalid value for `first_name`, length must be less than or equal to `255`")  # noqa: E501
        if self._configuration.client_side_validation and first_name is not None and len(first_name) < 0:
            raise ValueError("Invalid value for `first_name`, length must be greater than or equal to `0`")  # noqa: E501

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this UpdateUserContract.  # noqa: E501

        This field is required on non windows authentication type.  # noqa: E501

        :return: The last_name of this UpdateUserContract.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this UpdateUserContract.

        This field is required on non windows authentication type.  # noqa: E501

        :param last_name: The last_name of this UpdateUserContract.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and last_name is not None and len(last_name) > 255:
            raise ValueError("Invalid value for `last_name`, length must be less than or equal to `255`")  # noqa: E501
        if self._configuration.client_side_validation and last_name is not None and len(last_name) < 0:
            raise ValueError("Invalid value for `last_name`, length must be greater than or equal to `0`")  # noqa: E501

        self._last_name = last_name

    @property
    def email(self):
        """Gets the email of this UpdateUserContract.  # noqa: E501


        :return: The email of this UpdateUserContract.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UpdateUserContract.


        :param email: The email of this UpdateUserContract.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def role(self):
        """Gets the role of this UpdateUserContract.  # noqa: E501


        :return: The role of this UpdateUserContract.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this UpdateUserContract.


        :param role: The role of this UpdateUserContract.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and role is None:
            raise ValueError("Invalid value for `role`, must not be `None`")  # noqa: E501
        allowed_values = ["NoAccess", "Viewer", "Member", "Artisan", "Curator", "Evaluated"]  # noqa: E501
        if self._configuration.client_side_validation and role not in allowed_values:
            raise ValueError(
                "Invalid value for `role` ({0}), must be one of {1}".format(role, allowed_values)  # noqa: E501
            )

        self._role = role

    @property
    def default_worker_tag(self):
        """Gets the default_worker_tag of this UpdateUserContract.  # noqa: E501


        :return: The default_worker_tag of this UpdateUserContract.  # noqa: E501
        :rtype: str
        """
        return self._default_worker_tag

    @default_worker_tag.setter
    def default_worker_tag(self, default_worker_tag):
        """Sets the default_worker_tag of this UpdateUserContract.


        :param default_worker_tag: The default_worker_tag of this UpdateUserContract.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and default_worker_tag is None:
            raise ValueError("Invalid value for `default_worker_tag`, must not be `None`")  # noqa: E501

        self._default_worker_tag = default_worker_tag

    @property
    def can_schedule_jobs(self):
        """Gets the can_schedule_jobs of this UpdateUserContract.  # noqa: E501


        :return: The can_schedule_jobs of this UpdateUserContract.  # noqa: E501
        :rtype: bool
        """
        return self._can_schedule_jobs

    @can_schedule_jobs.setter
    def can_schedule_jobs(self, can_schedule_jobs):
        """Sets the can_schedule_jobs of this UpdateUserContract.


        :param can_schedule_jobs: The can_schedule_jobs of this UpdateUserContract.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and can_schedule_jobs is None:
            raise ValueError("Invalid value for `can_schedule_jobs`, must not be `None`")  # noqa: E501

        self._can_schedule_jobs = can_schedule_jobs

    @property
    def can_prioritize_jobs(self):
        """Gets the can_prioritize_jobs of this UpdateUserContract.  # noqa: E501


        :return: The can_prioritize_jobs of this UpdateUserContract.  # noqa: E501
        :rtype: bool
        """
        return self._can_prioritize_jobs

    @can_prioritize_jobs.setter
    def can_prioritize_jobs(self, can_prioritize_jobs):
        """Sets the can_prioritize_jobs of this UpdateUserContract.


        :param can_prioritize_jobs: The can_prioritize_jobs of this UpdateUserContract.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and can_prioritize_jobs is None:
            raise ValueError("Invalid value for `can_prioritize_jobs`, must not be `None`")  # noqa: E501

        self._can_prioritize_jobs = can_prioritize_jobs

    @property
    def can_assign_jobs(self):
        """Gets the can_assign_jobs of this UpdateUserContract.  # noqa: E501


        :return: The can_assign_jobs of this UpdateUserContract.  # noqa: E501
        :rtype: bool
        """
        return self._can_assign_jobs

    @can_assign_jobs.setter
    def can_assign_jobs(self, can_assign_jobs):
        """Sets the can_assign_jobs of this UpdateUserContract.


        :param can_assign_jobs: The can_assign_jobs of this UpdateUserContract.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and can_assign_jobs is None:
            raise ValueError("Invalid value for `can_assign_jobs`, must not be `None`")  # noqa: E501

        self._can_assign_jobs = can_assign_jobs

    @property
    def can_create_collections(self):
        """Gets the can_create_collections of this UpdateUserContract.  # noqa: E501


        :return: The can_create_collections of this UpdateUserContract.  # noqa: E501
        :rtype: bool
        """
        return self._can_create_collections

    @can_create_collections.setter
    def can_create_collections(self, can_create_collections):
        """Sets the can_create_collections of this UpdateUserContract.


        :param can_create_collections: The can_create_collections of this UpdateUserContract.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and can_create_collections is None:
            raise ValueError("Invalid value for `can_create_collections`, must not be `None`")  # noqa: E501

        self._can_create_collections = can_create_collections

    @property
    def is_api_enabled(self):
        """Gets the is_api_enabled of this UpdateUserContract.  # noqa: E501


        :return: The is_api_enabled of this UpdateUserContract.  # noqa: E501
        :rtype: bool
        """
        return self._is_api_enabled

    @is_api_enabled.setter
    def is_api_enabled(self, is_api_enabled):
        """Sets the is_api_enabled of this UpdateUserContract.


        :param is_api_enabled: The is_api_enabled of this UpdateUserContract.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and is_api_enabled is None:
            raise ValueError("Invalid value for `is_api_enabled`, must not be `None`")  # noqa: E501

        self._is_api_enabled = is_api_enabled

    @property
    def default_credential_id(self):
        """Gets the default_credential_id of this UpdateUserContract.  # noqa: E501


        :return: The default_credential_id of this UpdateUserContract.  # noqa: E501
        :rtype: str
        """
        return self._default_credential_id

    @default_credential_id.setter
    def default_credential_id(self, default_credential_id):
        """Sets the default_credential_id of this UpdateUserContract.


        :param default_credential_id: The default_credential_id of this UpdateUserContract.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and default_credential_id is None:
            raise ValueError("Invalid value for `default_credential_id`, must not be `None`")  # noqa: E501

        self._default_credential_id = default_credential_id

    @property
    def is_account_locked(self):
        """Gets the is_account_locked of this UpdateUserContract.  # noqa: E501


        :return: The is_account_locked of this UpdateUserContract.  # noqa: E501
        :rtype: bool
        """
        return self._is_account_locked

    @is_account_locked.setter
    def is_account_locked(self, is_account_locked):
        """Sets the is_account_locked of this UpdateUserContract.


        :param is_account_locked: The is_account_locked of this UpdateUserContract.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and is_account_locked is None:
            raise ValueError("Invalid value for `is_account_locked`, must not be `None`")  # noqa: E501

        self._is_account_locked = is_account_locked

    @property
    def is_active(self):
        """Gets the is_active of this UpdateUserContract.  # noqa: E501


        :return: The is_active of this UpdateUserContract.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this UpdateUserContract.


        :param is_active: The is_active of this UpdateUserContract.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and is_active is None:
            raise ValueError("Invalid value for `is_active`, must not be `None`")  # noqa: E501

        self._is_active = is_active

    @property
    def is_validated(self):
        """Gets the is_validated of this UpdateUserContract.  # noqa: E501


        :return: The is_validated of this UpdateUserContract.  # noqa: E501
        :rtype: bool
        """
        return self._is_validated

    @is_validated.setter
    def is_validated(self, is_validated):
        """Sets the is_validated of this UpdateUserContract.


        :param is_validated: The is_validated of this UpdateUserContract.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and is_validated is None:
            raise ValueError("Invalid value for `is_validated`, must not be `None`")  # noqa: E501

        self._is_validated = is_validated

    @property
    def time_zone(self):
        """Gets the time_zone of this UpdateUserContract.  # noqa: E501


        :return: The time_zone of this UpdateUserContract.  # noqa: E501
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this UpdateUserContract.


        :param time_zone: The time_zone of this UpdateUserContract.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and time_zone is None:
            raise ValueError("Invalid value for `time_zone`, must not be `None`")  # noqa: E501

        self._time_zone = time_zone

    @property
    def language(self):
        """Gets the language of this UpdateUserContract.  # noqa: E501

        Supported Language values are "de-de", "en-us", "es-es", "fr-fr", "it-it", 
        "ja-jp", "pt-br", "zh-cn"  # noqa: E501

        :return: The language of this UpdateUserContract.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this UpdateUserContract.

        Supported Language values are "de-de", "en-us", "es-es", "fr-fr", "it-it", 
        "ja-jp", "pt-br", "zh-cn"  # noqa: E501

        :param language: The language of this UpdateUserContract.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and language is None:
            raise ValueError("Invalid value for `language`, must not be `None`")  # noqa: E501

        self._language = language

    @property
    def can_create_and_update_dcm(self):
        """Gets the can_create_and_update_dcm of this UpdateUserContract.  # noqa: E501


        :return: The can_create_and_update_dcm of this UpdateUserContract.  # noqa: E501
        :rtype: bool
        """
        return self._can_create_and_update_dcm

    @can_create_and_update_dcm.setter
    def can_create_and_update_dcm(self, can_create_and_update_dcm):
        """Sets the can_create_and_update_dcm of this UpdateUserContract.


        :param can_create_and_update_dcm: The can_create_and_update_dcm of this UpdateUserContract.  # noqa: E501
        :type: bool
        """

        self._can_create_and_update_dcm = can_create_and_update_dcm

    @property
    def can_share_for_execution_dcm(self):
        """Gets the can_share_for_execution_dcm of this UpdateUserContract.  # noqa: E501


        :return: The can_share_for_execution_dcm of this UpdateUserContract.  # noqa: E501
        :rtype: bool
        """
        return self._can_share_for_execution_dcm

    @can_share_for_execution_dcm.setter
    def can_share_for_execution_dcm(self, can_share_for_execution_dcm):
        """Sets the can_share_for_execution_dcm of this UpdateUserContract.


        :param can_share_for_execution_dcm: The can_share_for_execution_dcm of this UpdateUserContract.  # noqa: E501
        :type: bool
        """

        self._can_share_for_execution_dcm = can_share_for_execution_dcm

    @property
    def can_share_for_collaboration_dcm(self):
        """Gets the can_share_for_collaboration_dcm of this UpdateUserContract.  # noqa: E501


        :return: The can_share_for_collaboration_dcm of this UpdateUserContract.  # noqa: E501
        :rtype: bool
        """
        return self._can_share_for_collaboration_dcm

    @can_share_for_collaboration_dcm.setter
    def can_share_for_collaboration_dcm(self, can_share_for_collaboration_dcm):
        """Sets the can_share_for_collaboration_dcm of this UpdateUserContract.


        :param can_share_for_collaboration_dcm: The can_share_for_collaboration_dcm of
        this UpdateUserContract.  # noqa: E501
        :type: bool
        """

        self._can_share_for_collaboration_dcm = can_share_for_collaboration_dcm

    @property
    def can_manage_generic_vaults_dcm(self):
        """Gets the can_manage_generic_vaults_dcm of this UpdateUserContract.  # noqa: E501


        :return: The can_manage_generic_vaults_dcm of this UpdateUserContract.  # noqa: E501
        :rtype: bool
        """
        return self._can_manage_generic_vaults_dcm

    @can_manage_generic_vaults_dcm.setter
    def can_manage_generic_vaults_dcm(self, can_manage_generic_vaults_dcm):
        """Sets the can_manage_generic_vaults_dcm of this UpdateUserContract.


        :param can_manage_generic_vaults_dcm: The can_manage_generic_vaults_dcm of this
        UpdateUserContract.  # noqa: E501
        :type: bool
        """

        self._can_manage_generic_vaults_dcm = can_manage_generic_vaults_dcm

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
        if issubclass(UpdateUserContract, dict):
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
        if not isinstance(other, UpdateUserContract):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateUserContract):
            return True

        return self.to_dict() != other.to_dict()
