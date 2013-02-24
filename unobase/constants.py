from settings import DEFAULT_IMAGE_CATEGORY_CHOICES

STATE_PUBLISHED = 0
STATE_UNPUBLISHED = 1
STATE_STAGED = 2
STATE_DELETED = 3

STATE_CHOICES = ((STATE_PUBLISHED, 'Published'),
                 (STATE_UNPUBLISHED, 'Unpublished'),
                 (STATE_STAGED, 'Staged'),
                 (STATE_DELETED, 'Deleted'),
                )


ACTIVITY_LOGIN = 'logged in'
ACTIVITY_LOGOUT = 'logged out'
ACTIVITY_ACTION_CREATE = 'created'
ACTIVITY_ACTION_UPDATE = 'updated'
ACTIVITY_ACTION_COMMENT = 'commented'
ACTIVITY_MODERATE_APPROVE = 'approved comment'
ACTIVITY_MODERATE_UNAPPROVE = 'unapproved comment'
ACTIVITY_MODERATE_SPAM = 'marked as spam'
ACTIVITY_MODERATE_BLACKLIST = 'blacklisted'
ACTIVITY_MODERATE_UNBLACKLIST = 'unblacklisted'
ACTIVITY_RESEND_USER_WELCOME_EMAIL = 'resent user welcome email'

ACTION_CHOICES = ((ACTIVITY_LOGIN, 'logged in'),
                  (ACTIVITY_LOGOUT, 'logged out'),
                  (ACTIVITY_ACTION_CREATE, 'created'),
                  (ACTIVITY_ACTION_UPDATE, 'updated'),
                  (ACTIVITY_ACTION_COMMENT, 'commented on'),
                  (ACTIVITY_MODERATE_APPROVE, 'updated the status to "Approved"'),
                  (ACTIVITY_MODERATE_UNAPPROVE, 'updated the status to "Unapproved"'),
                  (ACTIVITY_MODERATE_SPAM, 'updated the status to "Spam"'),
                  (ACTIVITY_MODERATE_BLACKLIST, 'blacklisted'),
                  (ACTIVITY_MODERATE_UNBLACKLIST, 'unblacklisted'),
                  (ACTIVITY_RESEND_USER_WELCOME_EMAIL, 'resent user welcome email'),
    )

MODERATION_ACTIONS = [ACTIVITY_MODERATE_APPROVE,
                      ACTIVITY_MODERATE_UNAPPROVE,
                      ACTIVITY_MODERATE_SPAM]