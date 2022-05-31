# USZ Log Handler

This package is for logging your functions. It can be extended with messages (e-mail) if error occurs.
If you want to have the `rdf_logging.log` entries in the DB, then you should look into project `ust_db_connector`.


Decorate your functions with:
`@LogDecorator(a_message)`

Set your logging level in: `options.py`

### Set Up
For set up new projects or PyCharm read the following Wiki entries:
- https://wiki.usz.ch/display/MDM/Setup+PyCharm
- https://wiki.usz.ch/display/MDM/Setup+New+Project

>Important: activate environment!
