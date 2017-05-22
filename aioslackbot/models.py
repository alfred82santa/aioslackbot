from enum import Enum

from dirty_models.fields import StringIdField, BooleanField, ModelField, StringField, DateTimeField, ArrayField, \
    IntegerField, EnumField, MultiTypeField, HashMapField
from dirty_models.models import FastDynamicModel, BaseModel


class BaseEntity(BaseModel):
    id = StringIdField(read_only=True)


class Icons(BaseModel):
    image_36 = StringIdField()
    image_48 = StringIdField()
    image_72 = StringIdField()


class Topic(BaseModel):
    value = StringField()
    creator = StringIdField()
    last_set = DateTimeField()


class Edited(BaseModel):
    user = StringIdField()
    ts = DateTimeField()


class MessageSubtypeEnum(Enum):
    BOT_MESSAGE = 'bot_message'
    """
    A message was posted by an integration
    """

    CHANNEL_ARCHIVE = 'channel_archive'
    """
    A channel was archived
    """

    CHANNEL_JOIN = 'channel_join'
    """
    A team member joined a channel
    """

    CHANNEL_LEAVE = 'channel_leave'
    """
    A team member left a channel
    """

    CHANNEL_NAME = 'channel_name'
    """
    A channel was renamed
    """

    CHANNEL_PURPOSE = 'channel_purpose'
    """
    A channel purpose was updated
    """

    CHANNEL_TOPIC = 'channel_topic'
    """
    A channel topic was updated
    """

    CHANNEL_UNARCHIVE = 'channel_unarchive'
    """
    A channel was unarchived
    """

    FILE_COMMENT = 'file_comment'
    """
    A comment was added to a file
    """

    FILE_MENTION = 'file_mention'
    """
    A file was mentioned in a channel
    """

    FILE_SHARE = 'file_share'
    """
    A file was shared into a channel
    """

    GROUP_ARCHIVE = 'group_archive'
    """
    A group was archived
    """

    GROUP_JOIN = 'group_join'
    """
    A team member joined a group
    """

    GROUP_LEAVE = 'group_leave'
    """
    A team member left a group
    """

    GROUP_NAME = 'group_name'
    """
    A group was renamed
    """

    GROUP_PURPOSE = 'group_purpose'
    """
    A group purpose was updated
    """

    GROUP_TOPIC = 'group_topic'
    """
    A group topic was updated
    """

    GROUP_UNARCHIVE = 'group_unarchive'
    """
    A group was unarchived
    """

    ME_MESSAGE = 'me_message'
    """
    A /me message was sent
    """

    MESSAGE_CHANGED = 'message_changed'
    """
    A message was changed
    """

    MESSAGE_DELETED = 'message_deleted'
    """
    A message was deleted
    """

    MESSAGE_REPLIED = 'message_replied'
    """
    A message thread received a reply
    """

    PINNED_ITEM = 'pinned_item'
    """
    An item was pinned in a channel
    """

    REPLY_BROADCAST = 'reply_broadcast'
    """
    A message thread's reply was broadcast to a channel
    """

    UNPINNED_ITEM = 'unpinned_item'
    """
    An item was unpinned from a channel
    """


class ItemTypeEnum(Enum):
    CHANNEL_MESSAGE = 'C'
    PRIVATE_GROUP_MESSAGE = 'G'
    FILE = 'F'
    FILE_COMMENT = 'Fc'


class ReplyInfo(BaseModel):
    user = StringIdField()
    ts = DateTimeField()


class Field(BaseModel):
    title = StringField()
    value = StringField()
    short = BooleanField()


class ActionStyleEnum(Enum):
    DEFAULT = 'default'
    PRIMARY = 'primary'
    DANGER = 'danger'


class ActionTypeEnum(Enum):
    BUTTON = 'button'
    SELECT = 'select'


class ActionConfirm(BaseModel):
    title = StringField()
    text = StringIdField()
    ok_text = StringField(default='Okay')
    dismiss_text = StringField(default='Cancel')


class ActionDataSourceEnum(Enum):
    STATIC = 'static'
    USERS = 'users'
    CHANNELS = 'channels'
    CONVERSATION = 'conversations'
    EXTERNAL = 'external'


class ActionOption(BaseModel):
    text = StringField()
    value = StringIdField()
    description = StringField()


class ActionOptionsGroup(BaseModel):
    text = StringField()
    options = ArrayField(field_type=ModelField(model_class=ActionOption))


class Action(BaseModel):
    name = StringIdField()
    text = StringField()
    style = EnumField(enum_class=ActionStyleEnum)
    type = EnumField(enum_class=ActionTypeEnum)
    value = StringIdField()
    confirm = ModelField(model_class=ActionConfirm)

    options = ArrayField(field_type=ModelField(model_class=ActionOption))
    options_groups = ArrayField(field_type=ModelField(model_class=ActionOptionsGroup))

    data_source = EnumField(enum_class=ActionDataSourceEnum)
    selected_options = ArrayField(field_type=ModelField(model_class=ActionOption))
    min_query_length = IntegerField(default=1)


class Attachment(BaseEntity):
    fallback = StringField()
    color = StringIdField()
    pretext = StringField()
    author_name = StringField()
    author_link = StringIdField()
    author_icon = StringIdField()
    title = StringField()
    title_link = StringIdField()
    text = StringField()
    fields = ArrayField(field_type=ModelField(model_class=Field))
    image_url = StringIdField()
    thumb_url = StringIdField()
    footer = StringField()
    footer_icon = StringIdField()
    ts = DateTimeField()

    callback_id = StringIdField()
    attachment_type = StringIdField()
    actions = ArrayField(field_type=ModelField(model_class=Action))


class FileTypeEnum(Enum):
    AUTO = 'auto'
    """
    Auto Detect Type
    """

    TEXT = 'text'
    """
    Plain Text
    """

    APPLESCRIPT = 'applescript'
    """
    AppleScript
    """

    BOXNOTE = 'boxnote'
    """
    BoxNote
    """

    C = 'c'
    """
    C
    """

    CSHARP = 'csharp'
    """
    C#
    """

    CPP = 'cpp'
    """
    C++
    """

    CSS = 'css'
    """
    CSS
    """

    CSV = 'csv'
    """
    CSV
    """

    CLOJURE = 'clojure'
    """
    Clojure
    """

    COFFEESCRIPT = 'coffeescript'
    """
    CoffeeScript
    """

    CFM = 'cfm'
    """
    Cold Fusion
    """

    D = 'd'
    """
    D
    """

    DART = 'dart'
    """
    Dart
    """

    DIFF = 'diff'
    """
    Diff
    """

    DOCKERFILE = 'dockerfile'
    """
    Docker
    """

    ERLANG = 'erlang'
    """
    Erlang
    """

    FSHARP = 'fsharp'
    """
    F#
    """

    FORTRAN = 'fortran'
    """
    Fortran
    """

    GO = 'go'
    """
    Go
    """

    GROOVY = 'groovy'
    """
    Groovy
    """

    HTML = 'html'
    """
    HTML
    """

    HANDLEBARS = 'handlebars'
    """
    Handlebars
    """

    HASKELL = 'haskell'
    """
    Haskell
    """

    HAXE = 'haxe'
    """
    Haxe
    """

    JAVA = 'java'
    """
    Java
    """

    JAVASCRIPT = 'javascript'
    """
    JavaScript/JSON
    """

    KOTLIN = 'kotlin'
    """
    Kotlin
    """

    LATEX = 'latex'
    """
    LaTeX/sTeX
    """

    LISP = 'lisp'
    """
    Lisp
    """

    LUA = 'lua'
    """
    Lua
    """

    MARKDOWN = 'markdown'
    """
    Markdown (raw)
    """

    MATLAB = 'matlab'
    """
    MATLAB
    """

    MUMPS = 'mumps'
    """
    MUMPS
    """

    OCAML = 'ocaml'
    """
    OCaml
    """

    OBJC = 'objc'
    """
    Objective-C
    """

    PHP = 'php'
    """
    PHP
    """

    PASCAL = 'pascal'
    """
    Pascal
    """

    PERL = 'perl'
    """
    Perl
    """

    PIG = 'pig'
    """
    Pig
    """

    POST = 'post'
    """
    Slack Post
    """

    POWERSHELL = 'powershell'
    """
    PowerShell
    """

    PUPPET = 'puppet'
    """
    Puppet
    """

    PYTHON = 'python'
    """
    Python
    """

    R = 'r'
    """
    R
    """

    RUBY = 'ruby'
    """
    Ruby
    """

    RUST = 'rust'
    """
    Rust
    """

    SQL = 'sql'
    """
    SQL
    """

    SASS = 'sass'
    """
    Sass
    """

    SCALA = 'scala'
    """
    Scala
    """

    SCHEME = 'scheme'
    """
    Scheme
    """

    SHELL = 'shell'
    """
    Shell
    """

    SMALLTALK = 'smalltalk'
    """
    Smalltalk
    """

    SWIFT = 'swift'
    """
    Swift
    """

    TSV = 'tsv'
    """
    TSV
    """

    VB = 'vb'
    """
    VB.NET
    """

    VBSCRIPT = 'vbscript'
    """
    VBScript
    """

    VELOCITY = 'velocity'
    """
    Velocity
    """

    VERILOG = 'verilog'
    """
    Verilog
    """

    XML = 'xml'
    """
    XML
    """

    YAML = 'yaml'
    """
    YAML
    """


class FileModeEnum(Enum):
    HOSTED = 'hosted'
    EXTERNAL = 'external'
    SNIPPET = 'snippet'
    POST = 'post'


class FileComment(BaseEntity):
    created = DateTimeField()
    timestamp = DateTimeField()
    user = StringIdField()
    comment = StringField()
    channel = StringIdField()
    reactions = ArrayField(field_type=ModelField(model_class=Reaction))


class Reaction(BaseModel):
    name = StringIdField()
    count = IntegerField()
    users = ArrayField(field_type=StringIdField())


class File(BaseEntity):
    created = DateTimeField()
    timestamp = DateTimeField()
    name = StringIdField()
    title = StringField()
    mimetype = StringIdField()
    filetype = EnumField(enum_class=FileTypeEnum)
    pretty_type = StringIdField()
    user = StringIdField()
    mode = EnumField(enum_class=FileModeEnum)
    editable = BooleanField()
    is_external = BooleanField()
    external_type = StringField()
    username = StringIdField()
    size = IntegerField()
    url_private = StringIdField()
    url_private_download = StringIdField()
    thumb_64 = StringIdField()
    thumb_80 = StringIdField()
    thumb_360 = StringIdField()
    thumb_360_gif = StringIdField()
    thumb_360_w = IntegerField()
    thumb_360_h = IntegerField()
    thumb_480 = StringIdField()
    thumb_480_w = IntegerField()
    thumb_480_h = IntegerField()
    thumb_160 = StringIdField()
    permalink = StringIdField()
    permalink_public = StringIdField()
    edit_link = StringIdField()
    preview = StringIdField()
    preview_highlight = StringIdField()
    lines = IntegerField()
    lines_more = IntegerField()
    is_public = BooleanField()
    public_url_shared = BooleanField()
    display_as_bot = BooleanField()
    channels = ArrayField(field_type=StringIdField())
    groups = ArrayField(field_type=StringIdField())
    ims = ArrayField(field_type=StringIdField())
    initial_comment = ModelField(model_class=FileComment)
    num_stars = IntegerField()
    is_starred = BooleanField()
    pinned_to = ArrayField(field_type=StringIdField())
    reactions = ArrayField(field_type=ModelField(model_class=Reaction))
    comments_count = IntegerField()


class Reminder(BaseEntity):
    creator = StringIdField()
    """
    User who created reminder.
    """

    user = StringIdField()
    """
    User to notify.
    """

    text = StringField()
    """
    Notification text.
    """

    recurring = BooleanField()
    """
    Whether reminder is recurrent.
    """

    time = DateTimeField()
    """
    Creation timestamp.
    """

    complete_ts = DateTimeField()
    """
    Complete timestamp.
    """


class EventTypeEnum(Enum):
    ACCOUNTS_CHANGED = 'accounts_changed'
    """
    The list of accounts a user is signed into has changed.
    """

    BOT_ADDED = 'bot_added'
    """
    An bot user was added.
    """

    BOT_CHANGED = 'bot_changed'
    """
    An bot user was changed.
    """

    CHANNEL_ARCHIVE = 'channel_archive'
    """
    A channel was archived.
    """

    CHANNEL_CREATED = 'channel_created'
    """
    A channel was created.
    """

    CHANNEL_DELETED = 'channel_deleted'
    """
    A channel was deleted.
    """

    CHANNEL_HISTORY_CHANGED = 'channel_history_changed'
    """
    Bulk updates were made to a channel's history.
    """

    CHANNEL_JOINED = 'channel_joined'
    """
    You joined a channel.
    """

    CHANNEL_LEFT = 'channel_left'
    """
    You left a channel.
    """

    CHANNEL_MARKED = 'channel_marked'
    """
    Your channel read marker was updated.
    """

    CHANNEL_RENAME = 'channel_rename'
    """
    A channel was renamed.
    """

    CHANNEL_UNARCHIVE = 'channel_unarchive'
    """
    A channel was unarchived.
    """

    COMMANDS_CHANGED = 'commands_changed'
    """
    A team slash command has been added or changed.
    """

    DND_UPDATED = 'dnd_updated'
    """
    Do not Disturb settings changed for the current user.
    """

    DND_UPDATED_USER = 'dnd_updated_user'
    """
    Do not Disturb settings changed for a team member.
    """

    EMAIL_DOMAIN_CHANGED = 'email_domain_changed'
    """
    The team email domain has changed.
    """

    EMOJI_CHANGED = 'emoji_changed'
    """
    A team custom emoji has been added or changed.
    """

    FILE_CHANGE = 'file_change'
    """
    A file was changed.
    """

    FILE_COMMENT_ADDED = 'file_comment_added'
    """
    A file comment was added.
    """

    FILE_COMMENT_DELETED = 'file_comment_deleted'
    """
    A file comment was deleted.
    """

    FILE_COMMENT_EDITED = 'file_comment_edited'
    """
    A file comment was edited.
    """

    FILE_CREATED = 'file_created'
    """
    A file was created.
    """

    FILE_DELETED = 'file_deleted'
    """
    A file was deleted.
    """

    FILE_PUBLIC = 'file_public'
    """
    A file was made public.
    """

    FILE_SHARED = 'file_shared'
    """
    A file was shared.
    """

    FILE_UNSHARED = 'file_unshared'
    """
    A file was unshared.
    """

    GOODBYE = 'goodbye'
    """
    The server intends to close the connection soon.
    """

    GROUP_ARCHIVE = 'group_archive'
    """
    A private channel was archived.
    """

    GROUP_CLOSE = 'group_close'
    """
    You closed a private channel.
    """

    GROUP_HISTORY_CHANGED = 'group_history_changed'
    """
    Bulk updates were made to a private channel's history.
    """

    GROUP_JOINED = 'group_joined'
    """
    You joined a private channel.
    """

    GROUP_LEFT = 'group_left'
    """
    You left a private channel.
    """

    GROUP_MARKED = 'group_marked'
    """
    A private channel read marker was updated.
    """

    GROUP_OPEN = 'group_open'
    """
    You opened a private channel.
    """

    GROUP_RENAME = 'group_rename'
    """
    A private channel was renamed.
    """

    GROUP_UNARCHIVE = 'group_unarchive'
    """
    A private channel was unarchived.
    """

    HELLO = 'hello'
    """
    The client has successfully connected to the server
    """

    IM_CLOSE = 'im_close'
    """
    You closed a DM.
    """

    IM_CREATED = 'im_created'
    """
    A DM was created.
    """

    IM_HISTORY_CHANGED = 'im_history_changed'
    """
    Bulk updates were made to a DM's history.
    """

    IM_MARKED = 'im_marked'
    """
    A direct message read marker was updated.
    """

    IM_OPEN = 'im_open'
    """
    You opened a DM.
    """

    LINK_SHARED = 'link_shared'
    """
    A message was posted containing one or more links 
    relevant to your application.
    """

    MANUAL_PRESENCE_CHANGE = 'manual_presence_change'
    """
    You manually updated your presence.
    """

    MEMBER_JOINED_CHANNEL = 'member_joined_channel'
    """
    A user joined a public or private channel.
    """

    MEMBER_LEFT_CHANNEL = 'member_left_channel'
    """
    A user left a public or private channel.
    """

    MESSAGE = 'message'
    """
    A message was sent to a channel.
    """

    PIN_ADDED = 'pin_added'
    """
    A pin was added to a channel.
    """

    PIN_REMOVED = 'pin_removed'
    """
    A pin was removed from a channel.
    """

    PREF_CHANGE = 'pref_change'
    """
    You have updated your preferences.
    """

    PRESENCE_CHANGE = 'presence_change'
    """
    A team member's presence changed.
    """

    REACTION_ADDED = 'reaction_added'
    """
    A team member has added an emoji reaction to an item.
    """

    REACTION_REMOVED = 'reaction_removed'
    """
    A team member removed an emoji reaction.
    """

    RECONNECT_URL = 'reconnect_url'
    """
    Experimental.
    """

    STAR_ADDED = 'star_added'
    """
    A team member has starred an item.
    """

    STAR_REMOVED = 'star_removed'
    """
    A team member removed a star.
    """

    SUBTEAM_CREATED = 'subteam_created'
    """
    A User Group has been added to the team.
    """

    SUBTEAM_SELF_ADDED = 'subteam_self_added'
    """
    You have been added to a User Group.
    """

    SUBTEAM_SELF_REMOVED = 'subteam_self_removed'
    """
    You have been removed from a User Group.
    """

    SUBTEAM_UPDATED = 'subteam_updated'
    """
    An existing User Group has been updated or its members changed.
    """

    TEAM_DOMAIN_CHANGE = 'team_domain_change'
    """
    The team domain has changed.
    """

    TEAM_JOIN = 'team_join'
    """
    A new team member has joined.
    """

    TEAM_MIGRATION_STARTED = 'team_migration_started'
    """
    The team is being migrated between servers.
    """

    TEAM_PLAN_CHANGE = 'team_plan_change'
    """
    The team billing plan has changed.
    """

    TEAM_PREF_CHANGE = 'team_pref_change'
    """
    A team preference has been updated.
    """

    TEAM_PROFILE_CHANGE = 'team_profile_change'
    """
    Team profile fields have been updated.
    """

    TEAM_PROFILE_DELETE = 'team_profile_delete'
    """
    Team profile fields have been deleted.
    """

    TEAM_PROFILE_REORDER = 'team_profile_reorder'
    """
    Team profile fields have been reordered.
    """

    TEAM_RENAME = 'team_rename'
    """
    The team name has changed.
    """

    URL_VERIFICATION = 'url_verification'
    """
    Verifies ownership of an Events API Request URL.
    """

    USER_CHANGE = 'user_change'
    """
    A team member's data has changed.
    """

    USER_TYPING = 'user_typing'
    """
    A channel member is typing a message.
    """


class ItemTypeEnum(Enum):
    MESSAGE = 'message'
    FILE = 'file'
    FILE_COMMENT = 'file_comment'


class Event(BaseModel):
    type = EnumField(enum_class=EventTypeEnum, read_only=True)


class Message(BaseModel):
    type = EnumField(enum_class=ItemTypeEnum, read_only=True)
    subtype = EnumField(enum_class=MessageSubtypeEnum)
    channel = StringIdField()
    user = StringIdField()
    text = StringField()
    ts = DateTimeField()
    deleted_ts = DateTimeField()
    thread_ts = DateTimeField()
    event_ts = DateTimeField()

    hidden = BooleanField(default=False)

    bot_id = StringIdField()
    username = StringIdField()
    icons = ModelField(model_class=Icons)

    members = ArrayField(field_type=StringIdField())

    inviter = StringIdField()

    old_name = StringIdField()
    name = StringIdField()

    purpose = StringField()
    topic = StringField()

    file = ModelField(model_class=File)
    comment = ModelField(model_class=FileComment)
    upload = BooleanField()

    members = ArrayField(field_type=StringIdField())

    message = ModelField()

    source_team = StringIdField()
    parent_user_id = StringIdField()
    reply_count = IntegerField()
    replies = ArrayField(field_type=ModelField(model_class=ReplyInfo))
    subscribed = BooleanField()
    last_read = DateTimeField()
    unread_count = IntegerField()

    attachments = ArrayField(field_type=ModelField(model_class=Attachment))

    item_type = EnumField(enum_class=ItemTypeEnum)
    item = MultiTypeField(field_types=[ModelField(),
                                       ModelField(model_class=File),
                                       ModelField(model_class=FileComment)])

    is_starred = BooleanField()
    pinned_to = ArrayField(field_type=StringIdField())
    reactions = ArrayField(field_type=ModelField(model_class=Reaction))


class Im(BaseEntity):
    """
    An IM object contains information about a direct message channel.
    """

    is_im = BooleanField()
    """
    Whether it is a direct message object.
    """

    user = StringIdField()
    """
    Other party user.
    """

    created = DateTimeField()
    """
    Timestamp when direct message was created.
    """

    is_user_deleted = BooleanField()
    """
    Whether other user was deleted.
    """

    is_open = BooleanField()
    """
    Whether the DM channel is open. 
    """

    last_read = DateTimeField()
    """
    It is the timestamp for the last message the calling user has read in this channel
    """

    latest = ModelField(model_class=Message)
    """
    It is the latest message in the channel.
    """

    unread_count = IntegerField()
    """
    It is a full count of visible messages that the calling user has yet to read.
    """

    unread_count_display = IntegerField()
    """
    It is a count of messages that the calling user has yet to read that 
    matter to them (this means it excludes things like join/leave messages). 
    """


class Mpim(BaseEntity):
    """
    An IM object contains information about a direct message channel.
    """

    name = StringIdField()
    """
    Indicates the name of the mpim.
    """

    is_mpim = BooleanField()
    """
    Whether it is a multiparty direct message object.
    """

    is_group = BooleanField()
    """
    Whether it is a group object.
    """

    created = DateTimeField()
    """
    Timestamp when multiparty direct message was created.
    """

    creator = StringIdField()
    """
    User who create multiparty direct message channel.
    """

    members = ArrayField(field_type=StringIdField())
    """
    Members of multiparty direct message channel.
    """

    last_read = DateTimeField()
    """
    It is the timestamp for the last message the calling user has read in this channel
    """

    latest = ModelField(model_class=Message)
    """
    It is the latest message in the channel.
    """

    unread_count = IntegerField()
    """
    It is a full count of visible messages that the calling user has yet to read.
    """

    unread_count_display = IntegerField()
    """
    It is a count of messages that the calling user has yet to read that 
    matter to them (this means it excludes things like join/leave messages). 
    """


class UserProfile(BaseModel):
    """
    User profile.
    """

    avatar_hash = StringIdField()
    status_emoji = StringField()
    status_text = StringField()
    first_name = StringIdField()
    last_name = StringField()
    real_name = StringField()
    email = StringField()
    skype = StringField()
    phone = StringIdField()
    image_24 = StringField()
    image_32 = StringField()
    image_48 = StringField()
    image_192 = StringField()
    image_512 = StringField()


class TwoFactorTypeEnum(Enum):
    """
    Two factor authorization types.
    """

    APP = 'app'
    """
    By App.
    """

    SMS = 'sms'
    """
    By SMS.
    """


class EnterpriseUser(BaseEntity):
    enterprise_id = StringIdField()
    """
    The unique ID for this particular Enterprise Organization.
    """

    enterprise_name = StringIdField()
    """
    The name of this umbrella organization.
    """

    is_admin = BooleanField(default=False)
    """
    A boolean value indicating whether this user administers this enterprise.
    """

    is_owner = BooleanField(default=False)
    """
    A boolean value indicating whether this user is the owner of this enterprise.
    """

    teams = ArrayField(field_type=StringIdField())
    """
    An array of team IDs within the containing enterprise that the user is a member of.
    """


class User(BaseEntity):
    name = StringIdField()
    deleted = BooleanField()
    color = StringIdField()
    is_admin = BooleanField(default=False)
    is_owner = BooleanField(default=False)
    is_primary_owner = BooleanField(default=False)
    is_restricted = BooleanField(default=False)
    is_ultra_restricted = BooleanField(default=False)
    updated = DateTimeField()
    has_2fa = BooleanField(default=False)
    two_factor_type = EnumField(enum_class=TwoFactorTypeEnum)

    enterprise_user = ModelField(model_class=EnterpriseUser)


class PinTypeEnum(Enum):
    MESSAGE = 'message'
    FILE = 'file'
    FILE_COMMENT = 'file_comment'


class Pin(BaseModel):
    type = EnumField(enum_class=PinTypeEnum, read_only=True)
    channel = StringIdField()
    message = ModelField(model_class=Message)
    file = ModelField(model_class=File)
    comment = ModelField(model_class=FileComment)
    created = DateTimeField()
    created_by = StringIdField()


class Bot(BaseEntity):
    app_id = StringIdField()
    deleted = BooleanField()
    name = StringField()
    icons = ModelField(model_class=Icons)


class BaseChannel(BaseEntity):
    """
    A channel object contains information about a team channel.
    
    These channel objects are not the same object type as private channels, 
    which are considered :class:`~Group` objects.
    """

    name = StringIdField()
    """
    This parameter indicates the name of the channel, without a leading hash sign.
    """

    is_channel = BooleanField()

    created = DateTimeField()
    """
    It is a unix timestamp.
    """

    creator = StringIdField()
    """
    It is the user ID of the member that created this channel.
    """

    is_archived = BooleanField()
    """
    It will be true if the channel is archived.
    """

    is_general = BooleanField()
    """
    It will be true if this channel is the "general" channel that 
    includes all regular team members. In most teams this is called 
    #general but some teams have renamed it.
    """

    is_org_shared = BooleanField()
    """
    It may appear set to true when the channel is part of a 
    shared channel between multiple teams of an Enterprise Grid. 
    """

    enterprise_id = StringIdField()
    """
    Enterprise Grid identifier.
    """

    members = ArrayField(field_type=StringIdField())
    """
    It is a list of user ids for all users in this channel. 
    This includes any disabled accounts that were in this 
    channel when they were disabled.
    """

    topic = ModelField(model_class=Topic)
    """
    It provides information about the channel topic.
    """

    purpose = ModelField(model_class=Topic)
    """
    It provides information about the channel purpose.
    """

    is_member = BooleanField()
    """
    It will be true if the calling member is part of the channel.
    """

    last_read = DateTimeField()
    """
    It is the timestamp for the last message the calling user has read in this channel
    """

    latest = ModelField(model_class=Message)
    """
    It is the latest message in the channel.
    """

    unread_count = IntegerField()
    """
    It is a full count of visible messages that the calling user has yet to read.
    """

    unread_count_display = IntegerField()
    """
    It is a count of messages that the calling user has yet to read that 
    matter to them (this means it excludes things like join/leave messages). 
    """


class Channel(BaseChannel):
    """
    A channel object contains information about a team channel.

    These channel objects are not the same object type as private channels, 
    which are considered :class:`~Group` objects.
    """

    is_channel = BooleanField()

    is_general = BooleanField()
    """
    It will be true if this channel is the "general" channel that 
    includes all regular team members. In most teams this is called 
    #general but some teams have renamed it.
    """

    is_org_shared = BooleanField()
    """
    It may appear set to true when the channel is part of a 
    shared channel between multiple teams of an Enterprise Grid. 
    """

    enterprise_id = StringIdField()
    """
    Enterprise Grid identifier.
    """


class Group(BaseChannel):
    """
    A group object contains information about a private channel. 
    Private channels were once known as "private groups." C
    onsider a group object the same thing as a private channel object.
    """

    is_group = BooleanField()

    is_mpim = BooleanField()
    """
    Indicates if a multiparty im (mpim) is being emulated as a private channel.
    For compatibility with older clients, mpims can appear as private channels 
    unless rtm.start is called with mpim_aware=1.
    """

    parent_group = StringIdField()
    """
    Parent group.
    """


class ThreadInfo(BaseModel):
    complete = BooleanField()
    count = IntegerField()


class Paging(BaseModel):
    count = IntegerField()
    total = IntegerField()
    page = IntegerField()
    pages = IntegerField()


class TeamInfo(BaseEntity):
    name = StringField()
    email_domain = StringField()
    domain = StringIdField()
    icon = ModelField(model_class=Icons)
    msg_edit_window_mins = IntegerField()
    over_storage_limit = BooleanField()
    prefs = ModelField(model_class=FastDynamicModel)
    plan = StringIdField()
    enterprise_id = StringIdField()
    enterprise_name = StringField()


class SelfInfo(BaseEntity):
    name = StringField()
    prefs = ModelField(model_class=FastDynamicModel)
    created = DateTimeField()
    manual_presence = BooleanField()


class BaseRequest(BaseModel):
    pass


class BaseResponse(BaseModel):
    ok = BooleanField()


class ApiTestRequest(FastDynamicModel):
    """
    Request for :meth:`~aioslackbot.APIModule.test`.
    """

    error = StringIdField()


class ApiTestResponse(BaseResponse):
    """
    Response for :meth:`~aioslackbot.APIModule.test`.
    """

    error = StringIdField()
    args = ModelField(model_class=FastDynamicModel)


class AuthRevokeRequest(BaseRequest):
    """
    Request for :meth:`~aioslackbot.AuthModule.revoke`.
    """

    test = BooleanField()


class AuthRevokeResponse(BaseResponse):
    """
    Response for :meth:`~aioslackbot.AuthModule.revoke`.
    """

    revoked = BooleanField()


class AuthTestRequest(BaseRequest):
    """
    Request for :meth:`~aioslackbot.AuthModule.test`.
    """

    pass


class AuthTestResponse(BaseResponse):
    """
    Response for :meth:`~aioslackbot.AuthModule.test`.
    """

    url = StringIdField()
    team = StringField()
    user = StringField()
    team_id = StringIdField()
    user_id = StringIdField()


class BotsInfoRequest(BaseRequest):
    """
    Request for :meth:`~aioslackbot.BotsModule.info`.
    """

    bot = StringIdField()


class BotsInfoResponse(BaseResponse):
    """
    Response for :meth:`~aioslackbot.BotsModule.info`.
    """

    bot = ModelField(model_class=Bot)


class ChannelsArchiveRequest(BaseRequest):
    """
    Request for :meth:`~aioslackbot.ChannelsModule.archive`.
    """

    channel = StringIdField()


class ChannelsArchiveResponse(BaseResponse):
    """
    Response for :meth:`~aioslackbot.ChannelsModule.archive`.
    """
    pass


class ChannelsCreateRequest(BaseRequest):
    """
    Request for :meth:`~aioslackbot.ChannelsModule.create`.
    """

    name = StringIdField()
    validate = BooleanField()


class ChannelsCreateResponse(BaseResponse):
    """
    Response for :meth:`~aioslackbot.ChannelsModule.create`.
    """
    channel = ModelField(model_class=Channel)


class ChannelsHistoryRequest(BaseRequest):
    """
    Request for :meth:`~aioslackbot.ChannelsModule.history`.
    """

    channel = StringIdField()
    """
    Channel to fetch history for.
    """

    latest = DateTimeField()
    """
    End of time range of messages to include in results.
    """

    oldest = DateTimeField(default=0)
    """
    Start of time range of messages to include in results.
    """

    inclusive = BooleanField(default=False)
    """
    Include messages with latest or oldest timestamp in results.
    """

    count = IntegerField(default=100)
    """
    Number of messages to return, between 1 and 1000.
    """

    unreads = BooleanField(default=False)
    """
    Include unread_count_display in the output?
    """


class ChannelsHistoryResponse(BaseResponse):
    """
    Response for :meth:`~aioslackbot.ChannelsModule.history`.
    """

    latest = DateTimeField()
    messages = ArrayField(field_type=ModelField(model_class=Message))
    """
    The messages array contains up to 100 messages between latest and oldest.
    """

    has_more = BooleanField()
    """
    If there were more than 100 messages between latest and oldest, 
    then has_more will be true.
    """


class ChannelsInfoRequest(BaseRequest):
    """
    Request for :meth:`~aioslackbot.ChannelsModule.info`.
    """

    channel = StringIdField()
    """
    Channel to get info on
    """


class ChannelsInfoResponse(BaseResponse):
    """
    Response for :meth:`~aioslackbot.ChannelsModule.info`.
    """

    channel = ModelField(model_class=Channel)


class ChannelsInviteRequest(BaseRequest):
    """
    Request for :meth:`~aioslackbot.ChannelsModule.invite`.
    """

    channel = StringIdField()
    """
    Channel to invite user to.
    """

    user = StringIdField()
    """
    User to invite to channel.
    """


class ChannelsInviteResponse(BaseResponse):
    """
    Response for :meth:`~aioslackbot.ChannelsModule.invite`.
    """

    channel = ModelField(model_class=Channel)


class ChannelsJoinRequest(BaseRequest):
    """
    Request for :meth:`~aioslackbot.ChannelsModule.join`.
    """

    name = StringIdField()
    """
    Name of channel to join.
    """

    validate = BooleanField()
    """
    Whether to return errors on invalid channel name instead of 
    modifying it to meet the specified criteria.
    """


class ChannelsJoinResponse(BaseResponse):
    """
    Response for :meth:`~aioslackbot.ChannelsModule.join`.
    """

    already_in_channel = BooleanField(default=False)
    channel = ModelField(model_class=Channel)


class ChannelsKickRequest(BaseRequest):
    """
    Request for :meth:`~aioslackbot.ChannelsModule.kick`.
    """

    channel = StringIdField()
    """
    Channel to remove user from.
    """

    user = StringIdField()
    """
    User to remove from channel.
    """


class ChannelsKickResponse(BaseResponse):
    """
    Response for :meth:`~aioslackbot.ChannelsModule.kick`.
    """
    pass


class ChannelsLeaveRequest(BaseRequest):
    """
    Request for :meth:`~aioslackbot.ChannelsModule.leave`.
    """

    channel = StringIdField()
    """
    Channel to leave.
    """


class ChannelsLeaveResponse(BaseResponse):
    """
    Response for :meth:`~aioslackbot.ChannelsModule.leave`.
    """

    not_in_channel = BooleanField(default=False)


class BaseChannelsListRequest(BaseRequest):
    """
    Request for :meth:`~aioslackbot.ChannelsModule.list`.
    """

    exclude_archived = BooleanField(default=False)
    """
    Exclude archived channels from the list.
    """


class ChannelsListRequest(BaseChannelsListRequest):
    """
    Request for :meth:`~aioslackbot.ChannelsModule.list`.
    """

    exclude_members = BooleanField(default=False)
    """
    Exclude the members collection from each channel.
    """


class ChannelsListResponse(BaseResponse):
    """
    Response for :meth:`~aioslackbot.ChannelsModule.list`.
    """

    channels = ArrayField(field_type=ModelField(model_class=Channel))


class ChannelsMarkRequest(BaseRequest):
    """
    Request for :meth:`~aioslackbot.ChannelsModule.mark`.
    """

    channel = StringIdField()
    """
    Channel to set reading cursor in.
    """

    ts = DateTimeField()
    """
    Timestamp of the most recently seen message.
    """


class ChannelsMarkResponse(BaseResponse):
    """
    Response for :meth:`~aioslackbot.ChannelsModule.mark`.
    """

    channels = ArrayField(field_type=ModelField(model_class=Channel))


class ChannelsRenameRequest(BaseRequest):
    """
    Request for :meth:`~aioslackbot.ChannelsModule.rename`.
    """

    channel = StringIdField()
    """
    Channel to rename.
    """

    name = StringIdField()
    """
    New name for channel.
    """

    validate = BooleanField(default=False)
    """
    Whether to return errors on invalid channel name instead 
    of modifying it to meet the specified criteria.
    """


class ChannelsRenameResponse(BaseResponse):
    """
    Response for :meth:`~aioslackbot.ChannelsModule.rename`.
    """

    channel = ModelField(model_class=Channel)
    """
    Channel renamed.
    """


class ChannelsRepliesRequest(BaseRequest):
    """
    Request for :meth:`~aioslackbot.ChannelsModule.replies`.
    """

    channel = StringIdField()
    """
    Channel to fetch thread from.
    """

    thread_ts = DateTimeField()
    """
    Unique identifier of a thread's parent message
    """


class ChannelsRepliesResponse(BaseResponse):
    """
    Response for :meth:`~aioslackbot.ChannelsModule.replies`.
    """

    messages = ArrayField(field_type=ModelField(model_class=Message))
    thread_info = ModelField(model_class=ThreadInfo)


class ChannelsSetPurposeRequest(BaseRequest):
    """
    Request for :meth:`~aioslackbot.ChannelsModule.set_purpose`.
    """

    channel = StringIdField()
    """
    Channel to set the purpose of.
    """

    purpose = StringField()
    """
    The new purpose.
    """


class ChannelsSetPurposeResponse(BaseResponse):
    """
    Response for :meth:`~aioslackbot.ChannelsModule.set_purpose`.
    """

    purpose = StringField()
    """
    The new purpose.
    """


class ChannelsSetTopicRequest(BaseRequest):
    """
    Request for :meth:`~aioslackbot.ChannelsModule.set_topic`.
    """

    channel = StringIdField()
    """
    Channel to set the topic of.
    """

    topic = StringField()
    """
    The new topic.
    """


class ChannelsSetTopicResponse(BaseResponse):
    """
    Response for :meth:`~aioslackbot.ChannelsModule.set_topic`.
    """

    topic = StringField()
    """
    The new topic.
    """


class ChannelsUnarchiveRequest(BaseRequest):
    """
    Request for :meth:`~aioslackbot.ChannelsModule.unarchive`.
    """

    channel = StringIdField()
    """
    Channel to unarchive.
    """


class ChannelsUnarchiveResponse(BaseResponse):
    """
    Response for :meth:`~aioslackbot.ChannelsModule.unarchive`.
    """
    pass


class ChatDeleteRequest(BaseRequest):
    """
    Request for :meth:`~aioslackbot.ChatModule.delete`.
    """

    ts = DateTimeField()
    """
    Timestamp of the message to be deleted.
    """

    channel = StringIdField()
    """
    Channel containing the message to be deleted.
    """

    as_user = BooleanField(default=False)
    """
    Pass true to delete the message as the authed user. 
    Bot users in this context are considered authed users.
    """


class ChatDeleteResponse(BaseResponse):
    """
    Response for :meth:`~aioslackbot.ChatModule.delete`.
    """

    s = DateTimeField()
    """
    Timestamp of the message deleted.
    """

    channel = StringIdField()
    """
    Channel containing the message deleted.
    """


class ChatMeMessageRequest(BaseRequest):
    """
    Request for :meth:`~aioslackbot.ChatModule.me_message`.
    """

    channel = StringIdField()
    """
    Channel to send message to. Can be a public channel, private group
    or IM channel. Can be an encoded ID, or a name.
    """

    text = StringField()
    """
    Text of the message to send.
    """


class ChatMeMessageResponse(BaseResponse):
    """
    Response for :meth:`~aioslackbot.ChatModule.me_message`.
    """

    s = DateTimeField()
    """
    Timestamp of the message sent.
    """

    channel = StringIdField()
    """
    Channel containing the message sent.
    """


class TextParse(Enum):
    FULL = 'full'
    NONE = 'none'


class ChatPostMessageRequest(BaseRequest):
    """
    Request for :meth:`~aioslackbot.ChatModule.post_message`.
    """

    s = DateTimeField()
    """
    Timestamp of the message sent.
    """

    channel = StringIdField()
    """
    Channel containing the message sent.
    """

    parse = EnumField(enum_class=TextParse, default=TextParse.NONE)
    """
    Change how messages are treated.
    """

    link_names = BooleanField(default=False)
    """
    Find and link channel names and usernames.
    """

    attachments = ArrayField(field_type=ModelField(model_class=Attachment))
    """
    Structured message attachments.
    """

    unfurl_links = BooleanField(default=False)
    """
    Pass true to enable unfurling of primarily text-based content.
    """

    unfurl_media = BooleanField(default=True)
    """
    Pass false to disable unfurling of media content.
    """

    username = StringIdField()
    """
    Set your bot's user name. Must be used in conjunction 
    with ``as_user`` set to false, otherwise ignored. See authorship below.
    """

    as_user = BooleanField(default=False)
    """
    Pass true to post the message as the authed user, instead of as a bot.
    """

    icon_url = StringIdField()
    """
    URL to an image to use as the icon for this message. Must be used in 
    conjunction with ``as_user`` set to false, otherwise ignored.
    """

    icon_emoji = StringIdField()
    """
    Emoji to use as the icon for this message. Overrides ``icon_url``. Must be 
    used in conjunction with as_user set to false, otherwise ignored.
    """

    thread_ts = DateTimeField()
    """
    Provide another message's ts value to make this message a reply. 
    Avoid using a reply's ts value; use its parent instead.
    """

    reply_broadcast = BooleanField(default=False)
    """
    Used in conjunction with thread_ts and indicates whether reply 
    should be made visible to everyone in the channel or conversation.
    """


class ChatPostMessageResponse(BaseResponse):
    """
    Response for :meth:`~aioslackbot.ChatModule.post_message`.
    """

    ts = DateTimeField()
    """
    Message timestamp.
    """

    channel = StringIdField()
    """
    Channel, private group, or IM channel message was sent to. 
    """

    message = ModelField(model_class=Message)
    """
    Message sent.
    """


class ChatUnfurlRequest(BaseRequest):
    """
    Request for :meth:`~aioslackbot.ChatModule.unfurl`.
    """

    channel = StringIdField()
    """
    Channel ID of the message.
    """

    ts = DateTimeField()
    """
    Timestamp of the message to add unfurl behavior to.
    """

    unfurls = HashMapField(field_type=ModelField(model_class=Attachment))
    """
    JSON mapping a set of URLs from the message to their unfurl attachments.
    """

    user_auth_required = BooleanField(default=False)
    """
    Set to true or 1 to indicate the user must install your 
    Slack app to trigger unfurls for this.
    """


class ChatUnfurlResponse(BaseResponse):
    """
    Response for :meth:`~aioslackbot.ChatModule.unfurl`.
    """
    pass


class ChatUpdateRequest(BaseRequest):
    """
    Request for :meth:`~aioslackbot.ChatModule.update`.
    """

    ts = DateTimeField()
    """
    Timestamp of the message to be updated.
    """

    channel = StringIdField()
    """
    Channel containing the message to be updated.
    """

    text = StringField()
    """
    New text for the message, using the default formatting rules.
    """

    attachments = ArrayField(field_type=ModelField(model_class=Attachment))
    """
    Structured message attachments.
    """

    parse = EnumField(enum_class=TextParse)
    """
    Change how messages are treated. Defaults to client, unlike chat.postMessage.
    """

    link_names = BooleanField()
    """
    Find and link channel names and usernames. Defaults to none. This parameter 
    should be used in conjunction with parse. To set link_names to 1, specify a 
    parse mode of full.
    """

    as_user = BooleanField(default=False)
    """
    Pass true to update the message as the authed user. Bot users in this context are 
    considered authed users.
    """


class ChatUpdateResponse(BaseResponse):
    """
    Response for :meth:`~aioslackbot.ChatModule.update`.
    """

    channel = StringIdField()
    """
    Channel where message was updated.
    """

    ts = DateTimeField()
    """
    Message timestamp.
    """

    text = StringField()
    """
    New message text.
    """


class DndInfo(BaseModel):
    """
    Do not distrub info structure.
    
    """
    dnd_enabled = BooleanField()
    """
    Whether Do not disturb is enabled.
    """

    next_dnd_start_ts = DateTimeField()
    """
    Timestamp dnd next start. 
    """

    next_dnd_end_ts = DateTimeField()
    """
    Timestamp dnd next end. 
    """


class DndEndDndRequest(BaseRequest):
    """
    Request for :meth:`~aioslackbot.DndModule.end_dnd`.
    """
    pass


class DndEndDndResponse(BaseResponse):
    """
    Response for :meth:`~aioslackbot.DndModule.end_dnd`.
    """
    pass


class DndEndSnoozeRequest(BaseRequest):
    """
    Request for :meth:`~aioslackbot.DndModule.end_snooze`.
    """
    pass


class DndEndSnoozeResponse(BaseResponse, DndInfo):
    """
    Response for :meth:`~aioslackbot.DndModule.end_snooze`.
    """

    snooze_enabled = BooleanField()
    """
    Whether snooze is enabled.
    """


class DndInfoRequest(BaseRequest):
    """
    Request for :meth:`~aioslackbot.DndModule.info`.
    """

    user = StringIdField()
    """
    User to fetch status for (defaults to current user).
    """


class DndInfoResponse(BaseResponse, DndInfo):
    """
    Response for :meth:`~aioslackbot.DndModule.info`.
    """

    snooze_enabled = BooleanField()
    """
    Whether snooze is enabled.
    """

    snooze_endtime = DateTimeField()
    """
    Timestamp snooze end.
    """

    snooze_remaining = IntegerField()
    """
    Snooze remaining minutes.
    """


class DndSetSnoozeRequest(BaseRequest):
    """
    Request for :meth:`~aioslackbot.DndModule.set_snooze`.
    """

    num_minutes = IntegerField()
    """
    Number of minutes, from now, to snooze until.
    """


class DndSetSnoozeResponse(BaseResponse):
    """
    Response for :meth:`~aioslackbot.DndModule.set_snooze`.
    """

    snooze_enabled = BooleanField()
    """
    Whether snooze is enabled.
    """

    snooze_endtime = DateTimeField()
    """
    Timestamp snooze end.
    """

    snooze_remaining = IntegerField()
    """
    Snooze remaining minutes.
    """


class DndTeamInfoRequest(BaseRequest):
    """
    Request for :meth:`~aioslackbot.DndModule.team_info`.
    """

    users = ArrayField(field_type=StringIdField(),
                       autolist=True)
    """
    Comma-separated list of users to fetch Do Not Disturb status for.
    """


class DndTeamInfoResponse(BaseResponse):
    """
    Response for :meth:`~aioslackbot.DndModule.team_info`.
    """

    users = HashMapField(field_type=ModelField(model_class=DndInfo))


class EmojiListRequest(BaseRequest):
    """
    Request for :meth:`~aioslackbot.EmojiModule.list`.
    """
    pass


class EmojiListResponse(BaseResponse):
    """
    Response for :meth:`~aioslackbot.EmojiModule.list`.
    """

    emoji = HashMapField(field_type=StringIdField())
    """
    Contains a map of name/url pairs, one for each custom emoji used by the team. 
    The alias: pseudo-protocol will be used where the emoji is an alias, the 
    string following the colon is the name of the other emoji this emoji is an alias to.
    """


class FilesDeleteRequest(BaseRequest):
    """
    Request for :meth:`~aioslackbot.FilesModule.delete`.
    """

    file = StringIdField()
    """
    ID of file to delete.
    """


class FilesDeleteResponse(BaseResponse):
    """
    Response for :meth:`~aioslackbot.FilesModule.delete`.
    """
    pass


class FilesInfoRequest(BaseRequest):
    """
    Request for :meth:`~aioslackbot.FilesModule.info`.
    """

    file = StringIdField()
    """
    Specify a file by providing its ID.
    """

    count = IntegerField()
    """
    Number of items to return per page.
    """

    page = IntegerField()
    """
    Page number of results to return.
    """


class FilesInfoResponse(BaseResponse):
    """
    Response for :meth:`~aioslackbot.FilesModule.info`.
    """

    file = ModelField(model_class=File)
    """
    File object that was asked for.
    """

    comments = ArrayField(field_type=ModelField(model_class=FileComment))
    """
    File comment list using pagination.
    """

    paging = ModelField(model_class=Paging)
    """
    Comment pagination info.
    """


class FilesTypeFilterEnum(Enum):
    ALL = 'all'
    """
    All files
    """

    SPACES = "spaces"
    """
    Posts
    """

    SNIPPETS = "snippets"
    """
    Snippets
    """

    IMAGES = "images"
    """
    Image files
    """

    GDOCS = "gdocs"
    """
    Google docs
    """

    ZIPS = "zips"
    """
    Zip files"
    """

    PDFS = "pdfs"
    """
    PDF files
    """


class FilesListRequest(BaseRequest):
    """
    Request for :meth:`~aioslackbot.FilesModule.list`.
    """

    user = StringIdField()
    """
    Filter files created by a single user.
    """

    channel = StringIdField()
    """
    Filter files appearing in a specific channel, indicated by its ID.
    """

    ts_from = DateTimeField()
    """
    Filter files created after this timestamp (inclusive).
    """

    ts_to = DateTimeField()
    """
    Filter files created before this timestamp (inclusive).
    """

    types = ArrayField(field_type=EnumField(enum_class=FilesTypeFilterEnum),
                       default=[FilesTypeFilterEnum.ALL],
                       autolist=True)
    """
    You can pass multiple values in the types argument. Comma-separated values.
    """

    count = IntegerField()
    """
    Number of items to return per page.
    """

    page = IntegerField()
    """
    Page number of results to return.
    """


class FilesListResponse(BaseResponse):
    """
    Response for :meth:`~aioslackbot.FilesModule.list`.
    """

    files = ArrayField(field_type=ModelField(model_class=File))
    """
    File object list that was asked for.
    """

    paging = ModelField(model_class=Paging)
    """
    Files pagination info.
    """


class FilesRevokePublicURLRequest(BaseRequest):
    """
    Request for :meth:`~aioslackbot.FilesModule.revoke_public_url`.
    """

    file = StringIdField()
    """
    File to revoke.
    """


class FilesRevokePublicURLResponse(BaseResponse):
    """
    Response for :meth:`~aioslackbot.FilesModule.revoke_public_url`.
    """

    file = ModelField(model_class=File)
    """
    File object.
    """


class FilesSharedPublicURLRequest(BaseRequest):
    """
    Request for :meth:`~aioslackbot.FilesModule.shared_public_url`.
    """

    file = StringIdField()
    """
    File to share.
    """


class FilesSharedPublicURLResponse(BaseResponse):
    """
    Response for :meth:`~aioslackbot.FilesModule.shared_public_url`.
    """

    file = ModelField(model_class=File)
    """
    File object.
    """


class FilesUploadRequest(BaseRequest):
    """
    Request for :meth:`~aioslackbot.FilesModule.upload`.
    """

    file = StringIdField()
    """
    File contents via multipart/form-data. If omitting this parameter, 
    you must submit content. Used for binary files.
    """

    content = StringIdField()
    """
    File contents via a POST variable. If omitting this parameter, 
    you must provide a file. Used for text files.
    """

    filetype = EnumField(enum_class=FileTypeEnum)
    """
    A file type identifier.
    """

    filename = StringIdField()
    """
    Filename of file.
    """

    title = StringField()
    """
    Title of file.
    """

    initial_comment = StringField()
    """
    Initial comment to add to file.
    """

    channels = ArrayField(field_type=StringIdField(), autolist=True)
    """
    Comma-separated list of channel names or IDs where the file will be shared.
    """


class FilesUploadResponse(BaseResponse):
    """
    Response for :meth:`~aioslackbot.FilesModule.upload`.
    """

    file = ModelField(model_class=File)
    """
    File object uploaded.
    """


class FilesCommentsAddRequest(BaseRequest):
    """
    Request for :meth:`~aioslackbot.FilesCommentsModule.add`.
    """

    file = StringIdField()
    """
    File to add a comment to.
    """

    comment = StringField()
    """
    Text of the comment to add.
    """


class FilesCommentsAddResponse(BaseResponse):
    """
    Response for :meth:`~aioslackbot.FilesCommentsModule.add`.
    """

    comment = ModelField(model_class=FileComment)
    """
    Comment added.
    """


class FilesCommentsDeleteRequest(BaseRequest):
    """
    Request for :meth:`~aioslackbot.FilesCommentsModule.delete`.
    """

    file = StringIdField()
    """
    File to delete a comment from.
    """

    id = StringIdField()
    """
    The comment to delete.
    """


class FilesCommentsDeleteResponse(BaseResponse):
    """
    Response for :meth:`~aioslackbot.FilesCommentsModule.delete`.
    """
    pass


class FilesCommentsEditRequest(BaseRequest):
    """
    Request for :meth:`~aioslackbot.FilesCommentsModule.edit`.
    """

    file = StringIdField()
    """
    File containing the comment to edit.
    """

    id = StringIdField()
    """
    The comment to edit.
    """

    comment = StringField()
    """
    Text of the comment to edit.
    """


class FilesCommentsEditResponse(BaseResponse):
    """
    Response for :meth:`~aioslackbot.FilesCommentsModule.edit`.
    """

    comment = ModelField(model_class=FileComment)
    """
    Comment object edited.
    """


class GroupsCreateRequest(ChannelsCreateRequest):
    """
    Request for :meth:`~aioslackbot.GroupsModule.create`.
    """
    pass


class GroupsCreateResponse(BaseResponse):
    """
    Response for :meth:`~aioslackbot.GroupsModule.create`.
    """

    group = ModelField(model_class=Group)
    """
    Group object created.
    """


class GroupsCreateChildRequest(BaseRequest):
    """
    Request for :meth:`~aioslackbot.GroupsModule.create_child`.
    """

    channel = StringIdField()
    """
    Private channel to clone and archive.
    """


class GroupsCreateChildResponse(BaseResponse):
    """
    Response for :meth:`~aioslackbot.GroupsModule.create_child`.
    """

    group = ModelField(model_class=Group)
    """
    Child group object created.
    """


class GroupsInfoRequest(ChannelsInfoRequest):
    """
    Request for :meth:`~aioslackbot.GroupsModule.info`.
    """
    pass


class GroupsInfoResponse(BaseResponse):
    """
    Response for :meth:`~aioslackbot.GroupsModule.info`.
    """

    group = ModelField(model_class=Group)
    """
    Group object.
    """


class GroupsInviteRequest(ChannelsInviteRequest):
    """
    Request for :meth:`~aioslackbot.GroupsModule.invite`.
    """
    pass


class GroupsInviteResponse(BaseResponse):
    """
    Response for :meth:`~aioslackbot.GroupsModule.invite`.
    """

    group = ModelField(model_class=Group)
    """
    Child group object created.
    """


class GroupsListRequest(BaseChannelsListRequest):
    """
    Request for :meth:`~aioslackbot.GroupsModule.list`.
    """
    pass


class GroupsListResponse(BaseResponse):
    """
    Response for :meth:`~aioslackbot.GroupsModule.list`.
    """

    groups = ArrayField(field_type=ModelField(model_class=Group))
    """
    Groups list.
    """


class GroupsOpenRequest(BaseRequest):
    """
    Request for :meth:`~aioslackbot.GroupsModule.open`.
    """

    channel = StringIdField()
    """
    Private channel to open.
    """


class GroupsOpenResponse(BaseResponse):
    """
    Response for :meth:`~aioslackbot.GroupsModule.open`.
    """

    no_op = BooleanField(default=False)
    """
    Whether an operation was performed. Usually it come with ``already_open``
    parameter.
    """

    already_open = BooleanField(default=False)
    """
    Whether group was already opened.
    """


class GroupsCloseRequest(BaseRequest):
    """
    Request for :meth:`~aioslackbot.GroupsModule.close`.
    """

    channel = StringIdField()
    """
    Private channel to close.
    """


class GroupsCloseResponse(BaseResponse):
    """
    Response for :meth:`~aioslackbot.GroupsModule.close`.
    """

    no_op = BooleanField(default=False)
    """
    Whether an operation was performed. Usually it come with ``already_closed``
    parameter.
    """

    already_closed = BooleanField(default=False)
    """
    Whether group was already closed.
    """


class GroupsRenameRequest(ChannelsRenameRequest):
    """
    Request for :meth:`~aioslackbot.GroupsModule.rename`.
    """
    pass


class GroupsRenameResponse(ChannelsRenameResponse):
    """
    Response for :meth:`~aioslackbot.GroupsModule.rename`.
    """

    channel = ModelField(model_class=Group)
    """
    Group renamed.
    """


class ImCloseRequest(BaseRequest):
    """
    Request for :meth:`~aioslackbot.ImModule.close`.
    """

    channel = StringIdField()
    """
    Direct message channel to close.
    """


class ImCloseResponse(BaseResponse):
    """
    Response for :meth:`~aioslackbot.ImModule.close`.
    """

    no_op = BooleanField(default=False)
    """
    Whether an operation was performed. Usually it come with ``already_closed``
    parameter.
    """

    already_closed = BooleanField(default=False)
    """
    Whether direct message was already closed.
    """


class ImHistoryRequest(ChannelsHistoryRequest):
    """
    Request for :meth:`~aioslackbot.ImModule.history`.
    """
    pass


class ImHistoryResponse(ChannelsHistoryResponse):
    """
    Response for :meth:`~aioslackbot.ImModule.history`.
    """
    pass


class ImListRequest(BaseRequest):
    """
    Request for :meth:`~aioslackbot.ImModule.list`.
    """
    pass


class ImListResponse(BaseResponse):
    """
    Response for :meth:`~aioslackbot.ImModule.list`.
    """

    ims = ArrayField(field_type=ModelField(model_class=Im))


class ImMarkRequest(ChannelsMarkRequest):
    """
    Request for :meth:`~aioslackbot.ImModule.mark`.
    """
    pass


class ImMarkResponse(ChannelsMarkResponse):
    """
    Response for :meth:`~aioslackbot.ImModule.mark`.
    """
    pass


class ImOpenRequest(BaseRequest):
    """
    Request for :meth:`~aioslackbot.ImModule.open`.
    """

    user = StringIdField()
    """
    User to open a direct message channel with.
    """

    return_im = BooleanField(default=False)
    """
    Indicates you want the full IM channel definition in the response.
    """


class ImOpenResponse(BaseResponse):
    """
    Response for :meth:`~aioslackbot.ImModule.open`.
    """

    no_op = BooleanField(default=False)
    """
    Whether an operation was performed. Usually it come with ``already_open``
    parameter.
    """

    already_open = BooleanField(default=False)
    """
    Whether direct message was already opened.
    """

    channel = ModelField(model_class=Im)


class ImRepliesRequest(ChannelsRepliesRequest):
    """
    Request for :meth:`~aioslackbot.ImModule.replies`.
    """
    pass


class ImRepliesResponse(BaseResponse):
    """
    Response for :meth:`~aioslackbot.ImModule.replies`.
    """
    pass


class MpimCloseRequest(BaseRequest):
    """
    Request for :meth:`~aioslackbot.MpimModule.close`.
    """

    channel = StringIdField()
    """
    Multiparty direct message channel to close.
    """


class MpimCloseResponse(BaseResponse):
    """
    Response for :meth:`~aioslackbot.MpimModule.close`.
    """

    no_op = BooleanField(default=False)
    """
    Whether an operation was performed. Usually it come with ``already_closed``
    parameter.
    """

    already_closed = BooleanField(default=False)
    """
    Whether direct message was already closed.
    """


class MpimHistoryRequest(ChannelsHistoryRequest):
    """
    Request for :meth:`~aioslackbot.MpimModule.history`.
    """
    pass


class MpimHistoryResponse(ChannelsHistoryResponse):
    """
    Response for :meth:`~aioslackbot.MpimModule.history`.
    """
    pass


class MpimListRequest(BaseRequest):
    """
    Request for :meth:`~aioslackbot.MpimModule.list`.
    """
    pass


class MpimListResponse(BaseResponse):
    """
    Response for :meth:`~aioslackbot.MpimModule.list`.
    """

    groups = ArrayField(field_type=ModelField(model_class=Mpim))


class MpimMarkRequest(ChannelsMarkRequest):
    """
    Request for :meth:`~aioslackbot.MpimModule.mark`.
    """
    pass


class MpimMarkResponse(ChannelsMarkResponse):
    """
    Response for :meth:`~aioslackbot.MpimModule.mark`.
    """
    pass


class MpimOpenRequest(BaseRequest):
    """
    Request for :meth:`~aioslackbot.MpimModule.open`.
    """

    users = ArrayField(field_type=StringIdField(), autolist=True)
    """
    Comma separated lists of users. The ordering of the users is 
    preserved whenever a MPIM group is returned.
    """


class MpimOpenResponse(BaseResponse):
    """
    Response for :meth:`~aioslackbot.MpimModule.open`.
    """

    group = ModelField(model_class=Mpim)


class MpimRepliesRequest(ChannelsRepliesRequest):
    """
    Request for :meth:`~aioslackbot.MpimModule.replies`.
    """
    pass


class MpimRepliesResponse(BaseResponse):
    """
    Response for :meth:`~aioslackbot.MpimModule.replies`.
    """
    pass


class OauthAccessRequest(BaseRequest):
    """
    Request for :meth:`~aioslackbot.OauthModule.access`.
    """

    client_id = StringIdField()
    """
    Issued when you created your application.
    """

    client_secret = StringIdField()
    """
    Issued when you created your application.
    """

    code = StringIdField()
    """
    The code param returned via the OAuth callback.
    """

    redirect_uri = StringIdField()
    """
    This must match the originally submitted URI (if one was sent).
    """


class OauthAccessResponse(BaseResponse):
    """
    Response for :meth:`~aioslackbot.OauthModule.access`.
    """

    access_token = StringIdField()
    scope = StringIdField()


class PinsAddRequest(BaseRequest):
    """
    Request for :meth:`~aioslackbot.PinsModule.add`.
    """

    channel = StringIdField()
    """
    Channel to pin the item in.
    """

    file = StringIdField()
    """
    File to pin.
    """

    file_comment = StringIdField()
    """
    File comment to pin.
    """

    timestamp = DateTimeField()
    """
    Timestamp of the message to pin.
    """


class PinsAddResponse(BaseResponse):
    """
    Response for :meth:`~aioslackbot.PinsModule.add`.
    """
    pass


class PinsListRequest(BaseRequest):
    """
    Request for :meth:`~aioslackbot.PinsModule.list`.
    """

    channel = StringIdField()
    """
    Channel to get pinned items for.
    """


class PinsListResponse(BaseResponse):
    """
    Response for :meth:`~aioslackbot.PinsModule.list`.
    """

    items = ArrayField(field_type=ModelField(model_class=Pin))


class PinsRemoveRequest(BaseRequest):
    """
    Request for :meth:`~aioslackbot.PinsModule.remove`.
    """

    channel = StringIdField()
    """
    Channel to pin the item in.Channel where the item is pinned to.
    """

    file = StringIdField()
    """
    File to un-pin.
    """

    file_comment = StringIdField()
    """
    File comment to un-pin.
    """

    timestamp = DateTimeField()
    """
    Timestamp of the message to un-pin.
    """


class PinsRemoveResponse(BaseResponse):
    """
    Response for :meth:`~aioslackbot.PinsModule.remove`.
    """
    pass


class ReactionsAddRequest(BaseRequest):
    """
    Request for :meth:`~aioslackbot.ReactionsModule.add`.
    """

    name = StringIdField()
    """
    Reaction(emoji) name.
    """

    channel = StringIdField()
    """
    Channel where the message to add reaction to was posted.
    """

    file = StringIdField()
    """
    File to add reaction to.
    """

    file_comment = StringIdField()
    """
    File comment to add reaction to.
    """

    timestamp = DateTimeField()
    """
    Timestamp of the message to add reaction to.
    """


class ReactionsAddResponse(BaseResponse):
    """
    Response for :meth:`~aioslackbot.ReactionsModule.add`.
    """
    pass


class ReactionsGetRequest(BaseRequest):
    """
    Request for :meth:`~aioslackbot.ReactionsModule.get`.
    """

    channel = StringIdField()
    """
    Channel where the message to get reactions for was posted.
    """

    file = StringIdField()
    """
    File to get reactions for.
    """

    file_comment = StringIdField()
    """
    File comment to get reactions for.
    """

    timestamp = DateTimeField()
    """
    Timestamp of the message to get reactions for.
    """

    full = BooleanField(default=False)
    """
    If true always return the complete reaction list.
    """


class ReactionsGetResponse(BaseResponse):
    """
    Response for :meth:`~aioslackbot.ReactionsModule.get`.
    """

    channel = StringIdField()
    message = ModelField(model_class=Message)
    file = ModelField(model_class=File)
    file_comment = ModelField(model_class=FileComment)


class ReactionsListRequest(BaseRequest):
    """
    Request for :meth:`~aioslackbot.ReactionsModule.list`.
    """

    user = StringIdField()
    """
    Show reactions made by this user. Defaults to the authed user.
    """

    full = BooleanField(default=False)
    """
    If true always return the complete reaction list.
    """

    count = IntegerField()
    """
    Number of items to return per page.
    """

    page = IntegerField()
    """
    Page number of results to return.
    """


class ReactionsListResponse(BaseResponse):
    """
    Response for :meth:`~aioslackbot.ReactionsModule.list`.
    """

    items = ArrayField(field_type=ModelField(model_class=Message))

    paging = ModelField(model_class=Paging)


class ReactionsRemoveRequest(BaseRequest):
    """
    Request for :meth:`~aioslackbot.ReactionsModule.remove`.
    """

    name = StringIdField()
    """
    Reaction (emoji) name.
    """

    file = StringIdField()
    """
    File to remove reaction from.
    """

    file_comment = StringIdField()
    """
    File comment to remove reaction from.
    """

    channel = StringIdField()
    """
    Channel where the message to remove reaction from was posted.
    """

    timestamp = DateTimeField()
    """
    Timestamp of the message to remove reaction from.
    """


class ReactionsRemoveResponse(BaseResponse):
    """
    Response for :meth:`~aioslackbot.ReactionsModule.remove`.
    """
    pass


class RemindersAddRequest(BaseRequest):
    """
    Request for :meth:`~aioslackbot.RemindersModule.add`.
    """

    text = StringField()
    """
    The content of the reminder.
    """

    time = MultiTypeField(field_types=[DateTimeField(),
                                       StringIdField()])
    """
    When this reminder should happen: the Unix timestamp (up to five years from now), 
    the number of seconds until the reminder (if within 24 hours), or a natural 
    language description (Ex. "in 15 minutes," or "every Thursday")
    """

    user = StringIdField()
    """
    The user who will receive the reminder. If no user is specified, the reminder 
    will go to user who created it.
    """


class RemindersAddResponse(BaseResponse):
    """
    Response for :meth:`~aioslackbot.RemindersModule.add`.
    """
    pass


class RemindersCompleteRequest(BaseRequest):
    """
    Request for :meth:`~aioslackbot.RemindersModule.complete`.
    """

    reminder = StringIdField()
    """
    The ID of the reminder to be marked as complete.
    """


class RemindersCompleteResponse(BaseResponse):
    """
    Response for :meth:`~aioslackbot.RemindersModule.complete`.
    """
    pass


class RemindersDeleteRequest(BaseRequest):
    """
    Request for :meth:`~aioslackbot.RemindersModule.delete`.
    """

    reminder = StringIdField()
    """
    The ID of the reminder.
    """


class RemindersDeleteResponse(BaseResponse):
    """
    Response for :meth:`~aioslackbot.RemindersModule.delete`.
    """
    pass


class RemindersInfoRequest(BaseRequest):
    """
    Request for :meth:`~aioslackbot.RemindersModule.info`.
    """

    reminder = StringIdField()
    """
    The ID of the reminder.
    """


class RemindersInfoResponse(BaseResponse):
    """
    Response for :meth:`~aioslackbot.RemindersModule.info`.
    """

    reminder = ModelField(model_class=Reminder)


class RemindersListRequest(BaseRequest):
    """
    Request for :meth:`~aioslackbot.RemindersModule.list`.
    """
    pass


class RemindersListResponse(BaseResponse):
    """
    Response for :meth:`~aioslackbot.RemindersModule.list`.
    """

    reminders = ArrayField(field_type=ModelField(model_class=Reminder))


class RtmConnectRequest(BaseRequest):
    """
    Request for :meth:`~aioslackbot.RtmModule.connect`.
    """
    pass


class RtmConnectResponse(BaseResponse):
    """
    Response for :meth:`~aioslackbot.RtmModule.connect`.
    """

    url = StringIdField()
    """
    URL to connect via websocket.
    """

    team = ModelField(model_class=TeamInfo)

    self = ModelField(model_class=SelfInfo)



class RtmStartRequest(BaseRequest):
    """
    Request for :meth:`~aioslackbot.RtmModule.start`.
    """
    simple_latest = BooleanField()
    """
    Return timestamp only for latest message object of each channel (improves performance).
    """

    no_unreads = BooleanField()
    """
    Skip unread counts for each channel (improves performance).
    """

    mpim_aware = BooleanField()
    """
    Returns MPIMs to the client in the API response.
    """

    no_latest = BooleanField(default=False)
    """
    Exclude latest timestamps for channels, groups, mpims, and ims. Automatically sets no_unreads to 1
    """


class RtmStartResponse(BaseResponse):
    """
    Response for :meth:`~aioslackbot.RtmModule.start`.
    """

    url = StringIdField()
    """
    URL to connect via websocket.
    """

    team = ModelField(model_class=TeamInfo)
    """
    Contains details on the authenticated user's team. 
    If a team has not yet set a custom icon, the value of 
    team.icon.image_default will be true.
    """

    self = ModelField(model_class=SelfInfo)
    """
    Contains details on the authenticated user.
    """

    users = ArrayField(field_type=ModelField(model_class=User))
    """
    Contains a list of user objects, one for every member of the team.
    """

    channels = ArrayField(field_type=ModelField(model_class=Channel))
    """
    List of channel objects, one for every channel visible to 
    the authenticated user. For regular or administrator accounts 
    this list will include every team channel. The is_member 
    property indicates if the user is a member of this channel. 
    If true then the channel object will also include the topic, 
    purpose, member list and read-state related information. The 
    latest attribute is deprecated and will soon be removed from 
    this method's response.
    """

    groups = ArrayField(field_type=ModelField(model_class=Group))
    """
    List of group objects, one for every group the authenticated user is in.
    """

    mpims = ArrayField(field_type=ModelField(model_class=Mpim))
    """
    List of mpims objects, one for every group the authenticated user is in. 
    MPIMs are only returned to the client if mpim_aware is set when calling 
    rtm.start. Otherwise, mpims are emulated using the groups API.
    """

    ims = ArrayField(field_type=ModelField(model_class=Im))
    """
    List of IM objects, one for every direct message channel visible 
    to the authenticated user.
    """

    bots = ArrayField(field_type=ModelField(model_class=FastDynamicModel))
    """
    Gives details of the integrations set up on this team.
    """


