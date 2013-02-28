Changelog
=========

0.0.1 (2013-02-18)
------------------
#. Initial addition of files

0.0.2 (2013-02-24)
------------------
#. Changed publish_on to publish_date_time
#. Changed retract_on to retract_date_time
#. Added code in StateModel's save method to set publish_date_time to timezone.now() if not set and state is set to 'published'
#. Fixed license
#. Added author email addresses
#. Dropped README.md

0.0.3 (2013-02-25)
------------------
#. Fixed distinct on tags

0.0.4 (2013-02-26)
------------------
#. Fixed the ordering of StateModel and removed the auto Manager assignment

0.0.5 (2013-02-28)
------------------
#. Added description to ContentModel