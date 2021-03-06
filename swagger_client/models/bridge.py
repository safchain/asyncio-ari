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


class Bridge(object):
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
        'bridge_class': 'str',
        'bridge_type': 'str',
        'bridgevars': 'object',
        'channels': 'list[str]',
        'creationtime': 'date',
        'creator': 'str',
        'id': 'str',
        'name': 'str',
        'technology': 'str',
        'video_mode': 'str',
        'video_source_id': 'str'
    }

    attribute_map = {
        'bridge_class': 'bridge_class',
        'bridge_type': 'bridge_type',
        'bridgevars': 'bridgevars',
        'channels': 'channels',
        'creationtime': 'creationtime',
        'creator': 'creator',
        'id': 'id',
        'name': 'name',
        'technology': 'technology',
        'video_mode': 'video_mode',
        'video_source_id': 'video_source_id'
    }

    def __init__(self, bridge_class=None, bridge_type=None, bridgevars=None, channels=None, creationtime=None, creator=None, id=None, name=None, technology=None, video_mode=None, video_source_id=None):  # noqa: E501
        """Bridge - a model defined in Swagger"""  # noqa: E501

        self._bridge_class = None
        self._bridge_type = None
        self._bridgevars = None
        self._channels = None
        self._creationtime = None
        self._creator = None
        self._id = None
        self._name = None
        self._technology = None
        self._video_mode = None
        self._video_source_id = None
        self.discriminator = None

        self.bridge_class = bridge_class
        self.bridge_type = bridge_type
        if bridgevars is not None:
            self.bridgevars = bridgevars
        self.channels = channels
        self.creationtime = creationtime
        self.creator = creator
        self.id = id
        self.name = name
        self.technology = technology
        if video_mode is not None:
            self.video_mode = video_mode
        if video_source_id is not None:
            self.video_source_id = video_source_id

    @property
    def bridge_class(self):
        """Gets the bridge_class of this Bridge.  # noqa: E501

        Bridging class  # noqa: E501

        :return: The bridge_class of this Bridge.  # noqa: E501
        :rtype: str
        """
        return self._bridge_class

    @bridge_class.setter
    def bridge_class(self, bridge_class):
        """Sets the bridge_class of this Bridge.

        Bridging class  # noqa: E501

        :param bridge_class: The bridge_class of this Bridge.  # noqa: E501
        :type: str
        """
        if bridge_class is None:
            raise ValueError("Invalid value for `bridge_class`, must not be `None`")  # noqa: E501

        self._bridge_class = bridge_class

    @property
    def bridge_type(self):
        """Gets the bridge_type of this Bridge.  # noqa: E501

        Type of bridge technology  # noqa: E501

        :return: The bridge_type of this Bridge.  # noqa: E501
        :rtype: str
        """
        return self._bridge_type

    @bridge_type.setter
    def bridge_type(self, bridge_type):
        """Sets the bridge_type of this Bridge.

        Type of bridge technology  # noqa: E501

        :param bridge_type: The bridge_type of this Bridge.  # noqa: E501
        :type: str
        """
        if bridge_type is None:
            raise ValueError("Invalid value for `bridge_type`, must not be `None`")  # noqa: E501

        self._bridge_type = bridge_type

    @property
    def bridgevars(self):
        """Gets the bridgevars of this Bridge.  # noqa: E501

        Channel variables  # noqa: E501

        :return: The bridgevars of this Bridge.  # noqa: E501
        :rtype: object
        """
        return self._bridgevars

    @bridgevars.setter
    def bridgevars(self, bridgevars):
        """Sets the bridgevars of this Bridge.

        Channel variables  # noqa: E501

        :param bridgevars: The bridgevars of this Bridge.  # noqa: E501
        :type: object
        """

        self._bridgevars = bridgevars

    @property
    def channels(self):
        """Gets the channels of this Bridge.  # noqa: E501

        Ids of channels participating in this bridge  # noqa: E501

        :return: The channels of this Bridge.  # noqa: E501
        :rtype: list[str]
        """
        return self._channels

    @channels.setter
    def channels(self, channels):
        """Sets the channels of this Bridge.

        Ids of channels participating in this bridge  # noqa: E501

        :param channels: The channels of this Bridge.  # noqa: E501
        :type: list[str]
        """
        if channels is None:
            raise ValueError("Invalid value for `channels`, must not be `None`")  # noqa: E501

        self._channels = channels

    @property
    def creationtime(self):
        """Gets the creationtime of this Bridge.  # noqa: E501

        Timestamp when bridge was created  # noqa: E501

        :return: The creationtime of this Bridge.  # noqa: E501
        :rtype: date
        """
        return self._creationtime

    @creationtime.setter
    def creationtime(self, creationtime):
        """Sets the creationtime of this Bridge.

        Timestamp when bridge was created  # noqa: E501

        :param creationtime: The creationtime of this Bridge.  # noqa: E501
        :type: date
        """
        if creationtime is None:
            raise ValueError("Invalid value for `creationtime`, must not be `None`")  # noqa: E501

        self._creationtime = creationtime

    @property
    def creator(self):
        """Gets the creator of this Bridge.  # noqa: E501

        Entity that created the bridge  # noqa: E501

        :return: The creator of this Bridge.  # noqa: E501
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this Bridge.

        Entity that created the bridge  # noqa: E501

        :param creator: The creator of this Bridge.  # noqa: E501
        :type: str
        """
        if creator is None:
            raise ValueError("Invalid value for `creator`, must not be `None`")  # noqa: E501

        self._creator = creator

    @property
    def id(self):
        """Gets the id of this Bridge.  # noqa: E501

        Unique identifier for this bridge  # noqa: E501

        :return: The id of this Bridge.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Bridge.

        Unique identifier for this bridge  # noqa: E501

        :param id: The id of this Bridge.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this Bridge.  # noqa: E501

        Name the creator gave the bridge  # noqa: E501

        :return: The name of this Bridge.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Bridge.

        Name the creator gave the bridge  # noqa: E501

        :param name: The name of this Bridge.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def technology(self):
        """Gets the technology of this Bridge.  # noqa: E501

        Name of the current bridging technology  # noqa: E501

        :return: The technology of this Bridge.  # noqa: E501
        :rtype: str
        """
        return self._technology

    @technology.setter
    def technology(self, technology):
        """Sets the technology of this Bridge.

        Name of the current bridging technology  # noqa: E501

        :param technology: The technology of this Bridge.  # noqa: E501
        :type: str
        """
        if technology is None:
            raise ValueError("Invalid value for `technology`, must not be `None`")  # noqa: E501

        self._technology = technology

    @property
    def video_mode(self):
        """Gets the video_mode of this Bridge.  # noqa: E501

        The video mode the bridge is using. One of 'none', 'talker', or 'single'.  # noqa: E501

        :return: The video_mode of this Bridge.  # noqa: E501
        :rtype: str
        """
        return self._video_mode

    @video_mode.setter
    def video_mode(self, video_mode):
        """Sets the video_mode of this Bridge.

        The video mode the bridge is using. One of 'none', 'talker', or 'single'.  # noqa: E501

        :param video_mode: The video_mode of this Bridge.  # noqa: E501
        :type: str
        """

        self._video_mode = video_mode

    @property
    def video_source_id(self):
        """Gets the video_source_id of this Bridge.  # noqa: E501

        The ID of the channel that is the source of video in this bridge, if one exists.  # noqa: E501

        :return: The video_source_id of this Bridge.  # noqa: E501
        :rtype: str
        """
        return self._video_source_id

    @video_source_id.setter
    def video_source_id(self, video_source_id):
        """Sets the video_source_id of this Bridge.

        The ID of the channel that is the source of video in this bridge, if one exists.  # noqa: E501

        :param video_source_id: The video_source_id of this Bridge.  # noqa: E501
        :type: str
        """

        self._video_source_id = video_source_id

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
        if issubclass(Bridge, dict):
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
        if not isinstance(other, Bridge):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
