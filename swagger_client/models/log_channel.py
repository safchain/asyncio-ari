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


class LogChannel(object):
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
        'channel': 'str',
        'configuration': 'str',
        'status': 'str',
        'type': 'str'
    }

    attribute_map = {
        'channel': 'channel',
        'configuration': 'configuration',
        'status': 'status',
        'type': 'type'
    }

    def __init__(self, channel=None, configuration=None, status=None, type=None):  # noqa: E501
        """LogChannel - a model defined in Swagger"""  # noqa: E501

        self._channel = None
        self._configuration = None
        self._status = None
        self._type = None
        self.discriminator = None

        self.channel = channel
        self.configuration = configuration
        self.status = status
        self.type = type

    @property
    def channel(self):
        """Gets the channel of this LogChannel.  # noqa: E501

        The log channel path  # noqa: E501

        :return: The channel of this LogChannel.  # noqa: E501
        :rtype: str
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this LogChannel.

        The log channel path  # noqa: E501

        :param channel: The channel of this LogChannel.  # noqa: E501
        :type: str
        """
        if channel is None:
            raise ValueError("Invalid value for `channel`, must not be `None`")  # noqa: E501

        self._channel = channel

    @property
    def configuration(self):
        """Gets the configuration of this LogChannel.  # noqa: E501

        The various log levels  # noqa: E501

        :return: The configuration of this LogChannel.  # noqa: E501
        :rtype: str
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """Sets the configuration of this LogChannel.

        The various log levels  # noqa: E501

        :param configuration: The configuration of this LogChannel.  # noqa: E501
        :type: str
        """
        if configuration is None:
            raise ValueError("Invalid value for `configuration`, must not be `None`")  # noqa: E501

        self._configuration = configuration

    @property
    def status(self):
        """Gets the status of this LogChannel.  # noqa: E501

        Whether or not a log type is enabled  # noqa: E501

        :return: The status of this LogChannel.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this LogChannel.

        Whether or not a log type is enabled  # noqa: E501

        :param status: The status of this LogChannel.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def type(self):
        """Gets the type of this LogChannel.  # noqa: E501

        Types of logs for the log channel  # noqa: E501

        :return: The type of this LogChannel.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this LogChannel.

        Types of logs for the log channel  # noqa: E501

        :param type: The type of this LogChannel.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

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
        if issubclass(LogChannel, dict):
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
        if not isinstance(other, LogChannel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
