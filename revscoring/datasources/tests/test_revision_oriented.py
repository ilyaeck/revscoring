from ..revision_oriented import revision
from .util import check_datasource


def test_revision():
    check_datasource(revision.id)
    check_datasource(revision.timestamp)
    check_datasource(revision.comment)
    check_datasource(revision.byte_len)
    check_datasource(revision.minor)
    check_datasource(revision.content_model)
    check_datasource(revision.content_format)
    check_datasource(revision.text)
    check_datasource(revision.bytes)
    assert hasattr(revision, "parent")
    assert hasattr(revision, "user")
    assert hasattr(revision, "page")
    assert hasattr(revision, "diff")

    # revision.parent
    check_datasource(revision.parent.id)
    assert hasattr(revision.parent, "user")
    check_datasource(revision.parent.user.id)
    check_datasource(revision.parent.user.text)
    assert not hasattr(revision.parent.user, "groups")
    check_datasource(revision.parent.timestamp)
    check_datasource(revision.parent.comment)
    check_datasource(revision.parent.byte_len)
    check_datasource(revision.parent.minor)
    check_datasource(revision.parent.content_model)
    check_datasource(revision.parent.content_format)
    check_datasource(revision.parent.text)
    check_datasource(revision.parent.bytes)
    assert not hasattr(revision.parent, "page")
    assert not hasattr(revision.parent, "parent")
    assert not hasattr(revision.parent, "diff")

    # revision.page
    check_datasource(revision.page.id)
    assert hasattr(revision.page, "namespace")
    check_datasource(revision.page.namespace.id)
    check_datasource(revision.page.namespace.name)
    check_datasource(revision.page.title)
    assert hasattr(revision.page, "creation")
    check_datasource(revision.page.creation.id)
    assert hasattr(revision.page.creation, "user")
    check_datasource(revision.page.creation.user.id)
    check_datasource(revision.page.creation.user.text)
    assert not hasattr(revision.page.creation, "groups")
    check_datasource(revision.page.creation.timestamp)
    check_datasource(revision.page.creation.comment)
    check_datasource(revision.page.creation.byte_len)
    check_datasource(revision.page.creation.minor)
    check_datasource(revision.page.creation.content_model)
    check_datasource(revision.page.creation.content_format)
    assert not hasattr(revision.page.creation, "page")
    assert not hasattr(revision.page.creation, "text")
    assert not hasattr(revision.page.creation, "bytes")
    assert not hasattr(revision.page.creation, "diff")

    # revision.user
    check_datasource(revision.user.id)
    check_datasource(revision.user.text)
    check_datasource(revision.user.editcount)
    check_datasource(revision.user.registration)
    check_datasource(revision.user.groups)
    check_datasource(revision.user.emailable)
    check_datasource(revision.user.gender)
    check_datasource(revision.user.block_id)
    check_datasource(revision.user.blocked_by)
    check_datasource(revision.user.blocked_by_id)
    check_datasource(revision.user.blocked_timestamp)
    check_datasource(revision.user.block_reason)
    check_datasource(revision.user.block_expiry)
    assert hasattr(revision.user, "last_revision")
    check_datasource(revision.user.last_revision.id)
    check_datasource(revision.user.last_revision.parent_id)
    assert hasattr(revision.user.last_revision, "page")
    check_datasource(revision.user.last_revision.page.id)
    assert hasattr(revision.user.last_revision.page, "namespace")
    check_datasource(revision.user.last_revision.page.namespace.id)
    check_datasource(revision.user.last_revision.page.namespace.name)
    check_datasource(revision.user.last_revision.page.title)
    assert not hasattr(revision.user.last_revision.page, "creation")
    check_datasource(revision.user.last_revision.timestamp)
    check_datasource(revision.user.last_revision.comment)
    check_datasource(revision.user.last_revision.byte_len)
    check_datasource(revision.user.last_revision.minor)
    check_datasource(revision.user.last_revision.content_model)
    check_datasource(revision.user.last_revision.content_format)
    assert not hasattr(revision.user.last_revision, "user")
    assert not hasattr(revision.user.last_revision, "parent")
    assert not hasattr(revision.user.last_revision, "text")
    assert not hasattr(revision.user.last_revision, "bytes")
    assert not hasattr(revision.user.last_revision, "diff")
