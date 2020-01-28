## Sample db connection app

This is a simple Flask + oslo.config example app that attempts
to connect to a database and tells if it was successful or not.

The app expects a config file like the following one:

```ini
[app]
host=0.0.0.0
port=5000

[db]
hostname=localhost
username=postgres
password=changeme
```