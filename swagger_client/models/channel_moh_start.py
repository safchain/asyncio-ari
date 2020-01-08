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


class ChannelMohStart(object):
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
        'channel': 'Channel',
        'moh_class': 'str'
    }

    attribute_map = {
        'channel': 'channel',
        'moh_class': 'moh_class'
    }

    def __init__(self, channel=None, moh_class=None):  # noqa: E501
        """ChannelMohStart - a model defined in Swagger"""  # noqa: E501

        self._channel = None
        self._moh_class = None
        self.discriminator = None

        self.channel = channel
        self.moh_class = moh_class

    @property
    def channel(self):
        """Gets the channel of this ChannelMohStart.  # noqa: E501

        The channel on which the MOH started.  # noqa: E501

        :return: The channel of this ChannelMohStart.  # noqa: E501
        :rtype: Channel
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this ChannelMohStart.

        The channel on which the MOH started.  # noqa: E501

        :param channel: The channel of this ChannelMohStart.  # noqa: E501
        :type: Channel
        """
        if channel is None:
            raise ValueError("Invalid value for `channel`, must not be `None`")  # noqa: E501

        self._channel = channel

    @property
    def moh_class(self):
        """Gets the moh_class of this ChannelMohStart.  # noqa: E501

        The name of the MOH class that started  # noqa: E501

        :return: The moh_class of this ChannelMohStart.  # noqa: E501
        :rtype: str
        """
        return self._moh_class

    @moh_class.setter
    def moh_class(self, moh_class):
        """Sets the moh_class of this ChannelMohStart.

        The name of the MOH class that started  # noqa: E501

        :param moh_class: The moh_class of this ChannelMohStart.  # noqa: E501
        :type: str
        """
        if moh_class is None:
            raise ValueError("Invalid value for `moh_class`, must not be `None`")  # noqa: E501

        self._moh_class = moh_class

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
        if issubclass(ChannelMohStart, dict):
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
        if not isinstance(other, ChannelMohStart):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
