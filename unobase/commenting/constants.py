__author__ = 'michael'

COMMENT_STATE_PENDING = 'pending'
COMMENT_STATE_APPROVED = 'approved'
COMMENT_STATE_UNAPPROVED = 'unapproved'
COMMENT_STATE_SPAM = 'spam'

COMMENT_STATE_CHOICES = ((COMMENT_STATE_PENDING, 'Pending'),
                         (COMMENT_STATE_APPROVED, 'Approved'),
                         (COMMENT_STATE_UNAPPROVED, 'Unapproved'),
                         (COMMENT_STATE_SPAM, 'Spam'),
    )

COMMENT_SETTING_ALL_APPROVED = 'approved'
COMMENT_SETTING_NEEDS_APPROVAL = 'needs approval'
COMMENT_SETTING_ALL_UNAPPROVED = 'unapproved'

COMMENT_SETTING_CHOICES = ((COMMENT_SETTING_ALL_APPROVED, 'All comments by default are approved (public)'),
                           (COMMENT_SETTING_NEEDS_APPROVAL, 'All comments by default need approval before being public'),
                           (COMMENT_SETTING_ALL_UNAPPROVED, 'All comments by default are unapproved (not public)'),
    )

COMMENT_VISIBLE_TO_EVERYONE = 0
COMMENT_VISIBLE_TO_STAFF = 1
COMMENT_VISIBLE_TO_ADMIN = 2

COMMENT_VISIBLE_TO_CHOICES = ((COMMENT_VISIBLE_TO_EVERYONE, 'Everyone'),
                              (COMMENT_VISIBLE_TO_STAFF, 'Staff only'),
                              (COMMENT_VISIBLE_TO_STAFF, 'Site administrators only'),
                              )

COMMENT_VISIBLE_TO_CHOICES_STAFF = ((COMMENT_VISIBLE_TO_EVERYONE, 'Everyone'),
                                    (COMMENT_VISIBLE_TO_STAFF, 'Staff only'),
                                    )
