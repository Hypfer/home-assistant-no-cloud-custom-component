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


async def async_setup(hass, config):
    async_register_command = hass.components.websocket_api.async_register_command
    async_register_command(WS_TYPE_STATUS, websocket_cloud_status, SCHEMA_WS_STATUS)

    # Return boolean to indicate that initialization was successful.
    return True


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
