"""
Setup for different kinds of Tuya climate devices
"""
from homeassistant.const import CONF_HOST
from custom_components.tuya_local import (
    DOMAIN, CONF_TYPE, CONF_TYPE_HEATER, CONF_TYPE_DEHUMIDIFIER, CONF_TYPE_FAN, CONF_TYPE_KOGAN_HEATER
)
from custom_components.tuya_local.heater.lock import GoldairHeaterChildLock
from custom_components.tuya_local.dehumidifier.lock import GoldairDehumidifierChildLock


def setup_platform(hass, config, add_devices, discovery_info=None):
    """Set up the Goldair climate device according to its type."""
    device = hass.data[DOMAIN][discovery_info[CONF_HOST]]
    if discovery_info[CONF_TYPE] == CONF_TYPE_HEATER:
        add_devices([GoldairHeaterChildLock(device)])
    if discovery_info[CONF_TYPE] == CONF_TYPE_DEHUMIDIFIER:
        add_devices([GoldairDehumidifierChildLock(device)])
    if discovery_info[CONF_TYPE] == CONF_TYPE_FAN:
        raise ValueError('Goldair fans do not support Child Lock.')
    if discovery_info[CONF_TYPE] == CONF_TYPE_KOGAN_HEATER:
        raise ValueError('Kogan Heaters do not support Child Lock.')