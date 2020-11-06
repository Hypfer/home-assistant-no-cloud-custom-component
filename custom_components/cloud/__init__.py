import voluptuous as vol
from homeassistant.exceptions import HomeAssistantError
from homeassistant.core import callback
from homeassistant.loader import bind_hass
from homeassistant.components import websocket_api


DOMAIN = "cloud"


WS_TYPE_STATUS = "cloud/status"
SCHEMA_WS_STATUS = websocket_api.BASE_COMMAND_MESSAGE_SCHEMA.extend(
    {vol.Required("type"): WS_TYPE_STATUS}
)

WS_TYPE_GET_CONFIG = "get_config"
SCHEMA_WS_GET_CONFIG = websocket_api.BASE_COMMAND_MESSAGE_SCHEMA.extend(
    {vol.Required("type"): WS_TYPE_GET_CONFIG}
)


async def async_setup(hass, config):
    async_register_command = hass.components.websocket_api.async_register_command
    async_register_command(WS_TYPE_STATUS, websocket_cloud_status, SCHEMA_WS_STATUS)

    async_register_command(WS_TYPE_GET_CONFIG, handle_get_config, SCHEMA_WS_GET_CONFIG)

    hass.async_create_task(reregister_get_config(hass))
    # Return boolean to indicate that initialization was successful.
    return True


async def reregister_get_config(hass):
    """Since there apparently can be a race-condition here, we're just trying to re-register later
        Yes, this is terrible but what can you do?
    """
    async_register_command = hass.components.websocket_api.async_register_command

    async_register_command(WS_TYPE_GET_CONFIG, handle_get_config, SCHEMA_WS_GET_CONFIG)


class CloudNotAvailable(HomeAssistantError):
    """Raised when an action requires the cloud but it's not available."""


@bind_hass
@callback
def async_remote_ui_url(hass) -> str:
    """Get the remote UI URL."""
    raise CloudNotAvailable


@callback
def websocket_cloud_status(hass, connection, msg):
    """Handle request for account info.
    Async friendly.
    """

    connection.send_message(
        websocket_api.result_message(msg["id"], {"logged_in": False, "cloud": "disconnected"})
    )


@callback
def handle_get_config(hass, connection, msg):
    """Handle get config command."""

    current_config = hass.config.as_dict()
    if DOMAIN in current_config['components']:
        current_config['components'].remove(DOMAIN)

    connection.send_message(websocket_api.result_message(msg["id"], current_config))


@bind_hass
@callback
def async_active_subscription(hass) -> bool:
    """Test if user has an active subscription."""
    return False


@bind_hass
@callback
def async_is_logged_in(hass) -> bool:
    """Test if user is logged in."""
    return False
