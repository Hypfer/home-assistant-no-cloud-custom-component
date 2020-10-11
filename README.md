# home-assistant-no-cloud-custom-component
Use default_config: without the cloud integration


This thing only exists since as of now (2020-10-11) it is impossible to customize the `default_config:` option of Home Assistant.
Therefore, the only way to get rid of the cloud without manually adding everything added by `default_config` is to override the unwanted components.

This repository will be archived as soon as this changes.

You should be able to add this as a custom repository URL to HACS.
This will however not be added to the default HACS repository since it makes sense for regular users to not override the cloud and updater components.
If you really want to do this, you should be "advanced" enough to add a custom repository.

Also, feel free to check out [the updater: counterpart](https://github.com/Hypfer/home-assistant-no-updater-custom-component)