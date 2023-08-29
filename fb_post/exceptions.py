class InvalidUserException(Exception):
    def __init__(self, user_id):
        self.user_id = user_id

    def __str__(self):
        return f'Invalid user with id {self.user_id}'


class InvalidPostException(Exception):
    def __init__(self, post_id):
        self.post_id = post_id

    def __str__(self):
        return f'Invalid post with id {self.post_id}'


class InvalidCommentException(Exception):
    def __init__(self, comment_id):
        self.comment_id = comment_id

    def __str__(self):
        return f'Invalid comment with id {self.comment_id}'


class InvalidPostContent(Exception):
    def __str__(self):
        return "Post content not to be empty."


class InvalidCommentContent(Exception):
    def __str__(self):
        return "Comment content not to be empty"


class InvalidReplyContent(Exception):
    def __str__(self):
        return "Reply not to be Empty"


class UserCannotDeletePostException(Exception):
    def __str__(self):
        return "user cannot be delete another ones post"


class InvalidReactionTypeException(Exception):
    def __str__(self):
        return "Invalid Reaction type Exception"
