# home-assistant-no-cloud-custom-component
Use default_config: without the cloud integration


This thing only exists since as of now (2020-10-11) it is impossible to customize the `default_config:` option of Home Assistant.
Therefore, the only way to get rid of the cloud without manually adding everything added by `default_config` is to override the unwanted components.

This repository will be archived as soon as this changes.

You should be able to add this as a custom repository URL to HACS.
This will however not be added to the default HACS repository since it makes sense for regular users to not override the cloud and updater components.
If you really want to do this, you should be "advanced" enough to add a custom repository.


Do note that this also modifies the `get_config` handler of the core webhook integration to remove the `cloud` component from the list
of active integrations, because the frontend enables stuff such as the almond automation dialog when it detects that.

This _could_ be destructive and break other things. Please don't complain about that in the Home Assistant Issue tracker.
Instead, complain about the fact that there's no way to customize `default_config`.

Also, feel free to check out [the updater: counterpart](https://github.com/Hypfer/home-assistant-no-updater-custom-component)