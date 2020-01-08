# coding: utf-8

"""
    localhost:8088

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 4.0.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class BuildInfo(object):
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
        '_date': 'str',
        'kernel': 'str',
        'machine': 'str',
        'options': 'str',
        'os': 'str',
        'user': 'str'
    }

    attribute_map = {
        '_date': 'date',
        'kernel': 'kernel',
        'machine': 'machine',
        'options': 'options',
        'os': 'os',
        'user': 'user'
    }

    def __init__(self, _date=None, kernel=None, machine=None, options=None, os=None, user=None):  # noqa: E501
        """BuildInfo - a model defined in Swagger"""  # noqa: E501

        self.__date = None
        self._kernel = None
        self._machine = None
        self._options = None
        self._os = None
        self._user = None
        self.discriminator = None

        self._date = _date
        self.kernel = kernel
        self.machine = machine
        self.options = options
        self.os = os
        self.user = user

    @property
    def _date(self):
        """Gets the _date of this BuildInfo.  # noqa: E501

        Date and time when Asterisk was built.  # noqa: E501

        :return: The _date of this BuildInfo.  # noqa: E501
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this BuildInfo.

        Date and time when Asterisk was built.  # noqa: E501

        :param _date: The _date of this BuildInfo.  # noqa: E501
        :type: str
        """
        if _date is None:
            raise ValueError("Invalid value for `_date`, must not be `None`")  # noqa: E501

        self.__date = _date

    @property
    def kernel(self):
        """Gets the kernel of this BuildInfo.  # noqa: E501

        Kernel version Asterisk was built on.  # noqa: E501

        :return: The kernel of this BuildInfo.  # noqa: E501
        :rtype: str
        """
        return self._kernel

    @kernel.setter
    def kernel(self, kernel):
        """Sets the kernel of this BuildInfo.

        Kernel version Asterisk was built on.  # noqa: E501

        :param kernel: The kernel of this BuildInfo.  # noqa: E501
        :type: str
        """
        if kernel is None:
            raise ValueError("Invalid value for `kernel`, must not be `None`")  # noqa: E501

        self._kernel = kernel

    @property
    def machine(self):
        """Gets the machine of this BuildInfo.  # noqa: E501

        Machine architecture (x86_64, i686, ppc, etc.)  # noqa: E501

        :return: The machine of this BuildInfo.  # noqa: E501
        :rtype: str
        """
        return self._machine

    @machine.setter
    def machine(self, machine):
        """Sets the machine of this BuildInfo.

        Machine architecture (x86_64, i686, ppc, etc.)  # noqa: E501

        :param machine: The machine of this BuildInfo.  # noqa: E501
        :type: str
        """
        if machine is None:
            raise ValueError("Invalid value for `machine`, must not be `None`")  # noqa: E501

        self._machine = machine

    @property
    def options(self):
        """Gets the options of this BuildInfo.  # noqa: E501

        Compile time options, or empty string if default.  # noqa: E501

        :return: The options of this BuildInfo.  # noqa: E501
        :rtype: str
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this BuildInfo.

        Compile time options, or empty string if default.  # noqa: E501

        :param options: The options of this BuildInfo.  # noqa: E501
        :type: str
        """
        if options is None:
            raise ValueError("Invalid value for `options`, must not be `None`")  # noqa: E501

        self._options = options

    @property
    def os(self):
        """Gets the os of this BuildInfo.  # noqa: E501

        OS Asterisk was built on.  # noqa: E501

        :return: The os of this BuildInfo.  # noqa: E501
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        """Sets the os of this BuildInfo.

        OS Asterisk was built on.  # noqa: E501

        :param os: The os of this BuildInfo.  # noqa: E501
        :type: str
        """
        if os is None:
            raise ValueError("Invalid value for `os`, must not be `None`")  # noqa: E501

        self._os = os

    @property
    def user(self):
        """Gets the user of this BuildInfo.  # noqa: E501

        Username that build Asterisk  # noqa: E501

        :return: The user of this BuildInfo.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this BuildInfo.

        Username that build Asterisk  # noqa: E501

        :param user: The user of this BuildInfo.  # noqa: E501
        :type: str
        """
        if user is None:
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501

        self._user = user

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(BuildInfo, dict):
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
        if not isinstance(other, BuildInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
