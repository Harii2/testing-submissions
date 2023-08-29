import pytest
from .models import User, Post, Comment, Reaction
from .utils import *


@pytest.fixture(autouse=True)
def user_and_post():
    User.objects.create(name="test", profile_pic="test")
    test_user = get_user_by_id(1)
    create_post(test_user.id, "test")
    post = get_post_by_id(1)
    return test_user, post


@pytest.fixture(autouse=True)
def user_and_post_and_comment(user_and_post):
    test_user, post = user_and_post
    create_comment(test_user.id, post.id, "test comment")
    comment = get_comment_by_id(1)
    return test_user, post, comment


@pytest.mark.django_db
def test_my_user():
    User.objects.create(name="test", profile_pic="test")
    # with pytest.raises(InvalidUserException):
    #     me = get_user_by_id(1)

    me = get_user_by_id(1)
    assert me.id == 1


@pytest.mark.django_db
def test_get_post_by_id():
    User.objects.create(name='test', profile_pic='test')
    test_user = get_user_by_id(1)

    with pytest.raises(InvalidPostException):
        get_post_by_id(1)

    with pytest.raises(InvalidPostContent):
        create_post(1, "")

    create_post(1, "test")

    post = get_post_by_id(1)
    assert post.id == 1


@pytest.mark.django_db
def test_creating_comment_and_getting_comment(user_and_post):
    test_user, post = user_and_post

    with pytest.raises(InvalidCommentContent):
        create_comment(1, 1, "")

    create_comment(test_user.id, post.id, "test comment")
    comment = Comment.objects.get(id=1)
    assert comment.id == 1


@pytest.mark.django_db
def test_creating_reply_to_comment_and_accesing_comment(user_and_post_and_comment):
    test_user, post, comment = user_and_post_and_comment

    with pytest.raises(InvalidReplyContent):
        reply_to_comment(1, 1, "")

    create_comment(test_user.id, post.id, "test comment 2")
    reply_to_comment(test_user.id, comment.id, "test reply")
    reply_comment = Comment.objects.get(id=3)
    assert reply_comment.parent_comment_id == 1


@pytest.mark.django_db
def test_reaction_to_post(user_and_post):
    test_user, post = user_and_post
    with pytest.raises(InvalidReactionTypeException):
        react_to_post(test_user.id, post.id, "test")

    react_to_post(test_user.id, post.id, "WOW")
    reaction = Reaction.objects.get(reacted_by=test_user, post=post)
    assert reaction.reaction == "WOW"

    react_to_post(test_user.id, post.id, "LOVE")
    reaction = Reaction.objects.get(reacted_by=test_user, post=post)
    assert reaction.reaction == "LOVE"

    react_to_post(test_user.id, post.id, "LOVE")

    with pytest.raises(ObjectDoesNotExist):
        reaction = Reaction.objects.get(reacted_by=test_user, post=post)


@pytest.mark.django_db
def test_reaction_to_comment(user_and_post_and_comment):
    test_user, post, comment = user_and_post_and_comment
    with pytest.raises(InvalidReactionTypeException):
        react_to_comment(test_user.id, comment.id, "test")

    react_to_comment(test_user.id, comment.id, "WOW")
    reaction = Reaction.objects.get(reacted_by=test_user, comment=comment)
    assert reaction.reaction == "WOW"

    react_to_comment(test_user.id, comment.id, "LOVE")
    reaction = Reaction.objects.get(reacted_by=test_user, comment=comment)
    assert reaction.reaction == "LOVE"

    react_to_comment(test_user.id, comment.id, "LOVE")
    with pytest.raises(ObjectDoesNotExist):
        reaction = Reaction.objects.get(reacted_by=test_user, comment=comment)


@pytest.mark.django_db
def test_total_reactions_count(user_and_post_and_comment):
    test_user, post, comment = user_and_post_and_comment
    react_to_post(test_user.id, post.id, "LOVE")
    total_reactions_for_post = get_reactions_for_post_by_post_object(post)
    assert total_reactions_for_post["reactions"] == ["LOVE"]


@pytest.mark.django_db
def test_reaction_metrics(user_and_post_and_comment):
    test_user, post, comment = user_and_post_and_comment
    User.objects.create(name='test2', profile_pic='test2')
    User.objects.create(name='test3', profile_pic='test3')

    test_user_2 = User.objects.get(name='test2')
    test_user_3 = User.objects.get(name='test3')

    react_to_post(test_user_2.id, post.id, "LOVE")
    react_to_post(test_user_3.id, post.id, "WOW")

    metrics = get_reaction_metrics(post.id)
    assert metrics['LOVE'] == 1
    assert metrics['WOW'] == 1


@pytest.mark.django_db
def test_delete_post(user_and_post):
    test_user, post = user_and_post

    with pytest.raises(UserCannotDeletePostException):
        delete_post(2, post.id)

    delete_post(test_user.id, post.id)
    with pytest.raises(InvalidPostException):
        post = get_post_by_id(post.id)


@pytest.mark.django_db
def test_get_posts_with_more_positive_reactions(user_and_post):
    test_user, post = user_and_post
    react_to_post(test_user.id, post.id, "LOVE")

    create_post(test_user.id, "test2")
    post2 = get_post_by_id(2)

    create_post(test_user.id, "test3")
    post3 = get_post_by_id(3)

    create_post(test_user.id, "test4")
    post4 = get_post_by_id(4)

    react_to_post(test_user.id, post2.id, "LOVE")
    react_to_post(test_user.id, post3.id, "ANGRY")
    react_to_post(test_user.id, post4.id, "SAD")

    posts = get_posts_with_more_positive_reactions()
    assert len(posts) == 2


@pytest.mark.django_db
def test_get_posts_reacted_by_user(user_and_post_and_comment):
    test_user, post, comment = user_and_post_and_comment
    react_to_post(test_user.id, post.id, "LOVE")
    posts = get_posts_reacted_by_user(test_user.id)
    print(posts)
    assert len(posts) == 1


@pytest.mark.django_db
def test_get_reactions_to_post(user_and_post):
    test_user, post = user_and_post
    react_to_post(test_user.id, post.id, "LOVE")

    User.objects.create(name='test2', profile_pic='test2')
    u2 = User.objects.get(name='test2')

    User.objects.create(name='test3', profile_pic='test3')
    u3 = User.objects.get(name='test3')

    react_to_post(u2.id, post.id, "LOVE")
    react_to_post(u3.id, post.id, "LOVE")

    reactions = get_reactions_to_post(post.id)
    assert len(reactions) == 3


@pytest.mark.django_db
def test_get_post(user_and_post):
    test_user, post = user_and_post

    User.objects.create(name='test2', profile_pic='test2')
    u2 = User.objects.get(name='test2')

    create_comment(u2.id, post.id, "Hey Happy BirthDay")
    comment = get_comment_by_id(1)
    reply_to_comment(test_user.id, comment.id, "Thank you")

    react_to_comment(test_user.id, comment.id, "LOVE")

    post_object = get_post(post.id)

    print(post_object)


@pytest.mark.django_db
def test_get_replies_for_comment(user_and_post_and_comment):
    test_user, post, comment = user_and_post_and_comment
    react_to_comment(test_user.id, comment.id, "LOVE")
    reply_to_comment(test_user.id, comment.id, "Thank you")
    reply = get_replies_for_comment(comment.id)
    assert len(reply) == 1