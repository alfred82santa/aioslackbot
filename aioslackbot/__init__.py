from asyncio import get_event_loop
from logging import getLogger

import weakref
from service_client import ServiceClient
from service_client.plugins import QueryParams
from service_client.utils import build_parameter_object

from aioslackbot.models import *
from aioslackbot.utils import return_model

__version__ = '0.1.0'

SLACK_BOT_API_BASEPATH = 'https://slack.com/api'


class BaseModule:
    def __init__(self, parent, method_prefix=''):
        self._parent = weakref.ref(parent)
        self._method_prefix = method_prefix + self.__name__[:-len('Module')]

    @property
    def parent(self):
        return self._parent()


class APIModule(BaseModule):
    @build_parameter_object
    @return_model
    async def test(self, request: ApiTestRequest) -> ApiTestResponse:
        """
        This method helps you test your calling code.
        
        .. seealso:: https://api.slack.com/methods/api.test
        
        :param request: Request model.      
        :return: Any key argument used on method call should be included in response.
        """
        pass


class AuthModule(BaseModule):
    @build_parameter_object
    @return_model
    async def revoke(self, request: AuthRevokeRequest) -> AuthRevokeResponse:
        """
        This method revokes an access token. Use it when you no longer need a token. 
        For example, with a Sign In With Slack app, call this to log a user out.
        
        .. seealso:: https://api.slack.com/methods/auth.revoke
        
        :param request: Request model.
        :return: Response model.
        """
        pass

    @build_parameter_object
    @return_model
    async def test(self, request: AuthTestRequest) -> AuthTestResponse:
        """
        This method checks authentication and tells you who you are.

        .. seealso:: https://api.slack.com/methods/auth.test

        :param request: Request model.
        :return: Response model.
        """
        pass


class BotsModule(BaseModule):
    @build_parameter_object
    @return_model
    async def info(self, request: BotsInfoRequest) -> BotsInfoResponse:
        """
        This method returns information about a bot user.

        bot_id is returned from bot_message message events 
        and in the response of methods like channels.history.

        Use this method to look up the username and icons for those bot users. 
        Use the app_id field to identify whether a bot belongs to your Slack app.
        
        :param request: Request model.
        :return: Response model.
        """
        pass


class BaseChannelsModule(BaseModule):
    """
    Get info on your team's Slack channels, create or archive channels, 
    invite users, set the topic and purpose, and mark a channel as read.
    """

    _base_method = 'channels'

    @build_parameter_object
    @return_model
    async def archive(self, request: ChannelsArchiveRequest) -> ChannelsArchiveResponse:
        """
        This method archives a channel.
        
        .. seealso:: https://api.slack.com/methods/channels.archive
        
        :param request: Request model.
        :return: Response model.
        """
        pass

    @build_parameter_object
    @return_model
    async def create(self, request: ChannelsCreateRequest) -> ChannelsCreateResponse:
        """
        This method is used to create a channel.

        To create a private channel, use groups.create.
        
        .. seealso:: https://api.slack.com/methods/channels.create
        
        .. note::
            
            Channel names can only contain lowercase letters, numbers, hyphens, and underscores, 
            and must be 21 characters or less. We will validate the submitted channel name and 
            modify it to meet the above criteria. When calling this method, we recommend storing 
            the channel's name value that is returned in the response.
        
        :param request: Request model.
        :return: Response model.
        """
        pass

    @build_parameter_object
    @return_model
    async def history(self, request: ChannelsHistoryRequest) -> ChannelsHistoryResponse:
        """
        This method returns a portion of message events from the specified public channel.

        To read the entire history for a channel, call the method with no latest or oldest arguments, 
        and then continue paging.
        
        To retrieve a single message, specify its ts value as latest, 
        set inclusive to true, and dial your count down to 1.
        
        .. seealso:: https://api.slack.com/methods/channels.history
        
        
        :param request: Request model.
        :return: Response model.
        """
        pass

    @build_parameter_object
    @return_model
    async def info(self, request: ChannelsInfoRequest) -> ChannelsInfoResponse:
        """
        This method returns information about a team channel.

        To retrieve information on a private channel, use groups.info.
        
        :param request: Request model.
        :return: Response model.
        """
        pass

    @build_parameter_object
    @return_model
    async def invite(self, request: ChannelsInviteRequest) -> ChannelsInviteResponse:
        """
        This method is used to invite a user to a channel. 
        The calling user must be a member of the channel.
        
        .. seealso:: https://api.slack.com/methods/channels.invite
        
        :param request: Request model.
        :return: Response model.
        """
        pass

    @build_parameter_object
    @return_model
    async def kick(self, request: ChannelsKickRequest) -> ChannelsKickResponse:
        """
        This method allows a user to remove another member from a team channel.
        
        .. seealso:: https://api.slack.com/methods/channels.kick
        
        :param request: Request model.
        :return: Response model.
        """
        pass

    @build_parameter_object
    @return_model
    async def leave(self, request: ChannelsLeaveRequest) -> ChannelsLeaveResponse:
        """
        This method is used to leave a channel.
        
        .. seealso:: https://api.slack.com/methods/channels.leave
        
        :param request: Request model.
        :return: Response model.
        """
        pass

    @build_parameter_object
    @return_model
    async def list(self, request: ChannelsListRequest) -> ChannelsListResponse:
        """
        This method returns a list of all channels in the team. This includes channels 
        the caller is in, channels they are not currently in, and archived channels but 
        does not include private channels. The number of (non-deactivated) members in 
        each channel is also returned.

        To retrieve a list of private channels, use groups.list.
        
        .. seealso:: https://api.slack.com/methods/channels.list
        
        :param request: Request model.
        :return: Response model.
        """
        pass

    @build_parameter_object
    @return_model
    async def mark(self, request: ChannelsMarkRequest) -> ChannelsMarkResponse:
        """
        This method moves the read cursor in a channel.
        
        .. seealso:: https://api.slack.com/methods/channels.mark
        
        :param request: Request model.
        :return: Response model.
        """
        pass

    @build_parameter_object
    @return_model
    async def rename(self, request: ChannelsRenameRequest) -> ChannelsRenameResponse:
        """
        This method renames a team channel.

        The only people who can rename a channel are Team Admins, or the person that 
        originally created the channel. Others will receive a "not_authorized" error.
        
        .. seealso:: https://api.slack.com/methods/channels.rename
        
        :param request: Request model.
        :return: Response model.
        """
        pass

    @build_parameter_object
    @return_model
    async def replies(self, request: ChannelsRepliesRequest) -> ChannelsRepliesResponse:
        """
        This method returns an entire thread (a message plus all the messages in reply to it).
        
        ..seealso:: https://api.slack.com/methods/channels.replies
        
        The channel and thread_ts arguments are always required. thread_ts must 
        be the timestamp of an existing message with 0 or more replies. If there 
        are no replies then just the single message referenced by thread_ts will 
        be returned - it is just an ordinary message.
        
        :param request: Request model.
        :return: Response model.
        """
        pass

    @build_parameter_object
    @return_model
    async def set_purpuse(self, request: ChannelsSetPurposeRequest) -> ChannelsSetPurposeResponse:
        """
        This method is used to change the purpose of a channel. 
        The calling user must be a member of the channel.
        
        ..seealso:: https://api.slack.com/methods/channels.setPurpose
        
        :param request: Request model.
        :return: Response model.
        """
        pass

    @build_parameter_object
    @return_model
    async def set_topic(self, request: ChannelsSetTopicRequest) -> ChannelsSetTopicResponse:
        """
        This method is used to change the topic of a channel. 
        The calling user must be a member of the channel.
        
        ..seealso:: https://api.slack.com/methods/channels.setTopic
        
        :param request: Request model.
        :return: Response model.
        """
        pass

    @build_parameter_object
    @return_model
    async def unarchive(self, request: ChannelsUnarchiveRequest) -> ChannelsUnarchiveResponse:
        """
        This method unarchives a channel. The calling user is added to the channel.
        
        .. seealso:: https://api.slack.com/methods/channels.unarchive
        
        :param request: Request model.
        :return: Response model.
        """
        pass


class ChannelsModule(BaseChannelsModule):
    """
    Get info on your team's Slack channels, create or archive channels, 
    invite users, set the topic and purpose, and mark a channel as read.
    """

    _base_method = 'channels'

    @build_parameter_object
    @return_model
    async def join(self, request: ChannelsJoinRequest) -> ChannelsJoinResponse:
        """
        This method is used to join a channel. If the channel does not exist, it is created.

        .. seealso:: https://api.slack.com/methods/channels.join

        :param name: Name of channel to join
        :param validate: Whether to return errors on invalid channel name instead 
                         of modifying it to meet the specified criteria.
        :return: Channel object
        """
        pass


class ChatModule(BaseModule):
    @build_parameter_object
    @return_model
    async def delete(self, request: ChatDeleteRequest) -> ChatDeleteResponse:
        """
        This method deletes a message from a channel.
        
        .. seealso:: https://api.slack.com/methods/chat.delete
        
        :param request: Request model.
        :return: Response model.
        """
        pass

    @build_parameter_object
    @return_model
    async def me_message(self, request: ChatMeMessageRequest) -> ChatMeMessageResponse:
        """
        This method sends a me message to a channel from the calling user.
        
        .. seealso:: https://api.slack.com/methods/chat.meMessage
        
        :param request: Request model.
        :return: Response model.
        """
        pass

    @build_parameter_object
    @return_model
    async def post_message(self, request: ChatPostMessageRequest) -> ChatPostMessageResponse:
        """
        This method posts a message to a public channel, private channel, 
        or direct message/IM channel.

        .. seealso:: https://api.slack.com/methods/chat.postMessage

        :param request: Request model.
        :return: Response model.
        """
        pass

    @build_parameter_object
    @return_model
    async def unfurl(self, request: ChatUnfurlRequest) -> ChatUnfurlResponse:
        """
        This method attaches Slack app unfurl behavior to a specified and 
        relevant message. A user token is required as this method does 
        not support bot user tokens.

        The first time this method is executed with a particular ts and 
        channel combination, the valid unfurls attachments you provide will 
        be attached to the message. Subsequent attempts with the same ts and 
        channel values will modify the same attachments, rather than adding more.
        
        .. seealso:: https://api.slack.com/methods/chat.unfurl

        :param request: Request model.
        :return: Response model.
        """
        pass

    @build_parameter_object
    @return_model
    async def update(self, request: ChatUpdateRequest) -> ChatUpdateResponse:
        """
        This method updates a message in a channel. Though related to 
        :meth:`~ChatModule.post_message`, some parameters of :meth:`~ChatModule.update` 
        are handled differently.
        
        .. seealso:: https://api.slack.com/methods/chat.unfurl

        :param request: Request model.
        :return: Response model.
        """
        pass


class DndModule(BaseModule):
    @build_parameter_object
    @return_model
    async def end_dnd(self, request: DndEndDndRequest) -> DndEndDndResponse:
        """
        Ends the user's currently scheduled Do Not Disturb session immediately.
        
        .. seealso:: https://api.slack.com/methods/dnd.endDnd

        :param request: Request model.
        :return: Response model.
        """
        pass

    @build_parameter_object
    @return_model
    async def end_snooze(self, request: DndEndSnoozeRequest) -> DndEndSnoozeResponse:
        """
        Ends the current user's snooze mode immediately.

        .. seealso:: https://api.slack.com/methods/dnd.endSnooze

        :param request: Request model.
        :return: Response model.
        """
        pass

    @build_parameter_object
    @return_model
    async def info(self, request: DndInfoRequest) -> DndInfoResponse:
        """
        Provides information about a user's current Do Not Disturb settings.

        .. seealso:: https://api.slack.com/methods/dnd.info

        :param request: Request model.
        :return: Response model.
        """
        pass

    @build_parameter_object
    @return_model
    async def set_snooze(self, request: DndSetSnoozeRequest) -> DndSetSnoozeResponse:
        """
        Adjusts the snooze duration for a user's Do Not Disturb settings. 
        If a snooze session is not already active for the user, invoking
        this method will begin one for the specified duration.

        .. seealso:: https://api.slack.com/methods/dnd.setSnooze

        :param request: Request model.
        :return: Response model.
        """
        pass

    @build_parameter_object
    @return_model
    async def team_info(self, request: DndTeamInfoRequest) -> DndTeamInfoResponse:
        """
        Provides information about the current Do Not Disturb
        settings for users of a Slack team.

        .. seealso:: https://api.slack.com/methods/dnd.teamInfo

        :param request: Request model.
        :return: Response model.
        """
        pass


class EmojiModule(BaseModule):
    @build_parameter_object
    @return_model
    async def list(self, request: EmojiListRequest) -> EmojiListResponse:
        """
        This method lists the custom emoji for a team.
        
        .. seealso:: https://api.slack.com/methods/emoji.list

        :param request: Request model.
        :return: Response model.
        """
        pass


class FilesModule(BaseModule):
    def __init__(self, parent):
        super(FilesModule, self).__init__(parent)
        self.comments = FilesCommentsModule(parent, method_prefix=self._method_prefix + '__')

    @build_parameter_object
    @return_model
    async def delete(self, request: FilesDeleteRequest) -> FilesDeleteResponse:
        """
        This method deletes a file from your team.

        .. seealso:: https://api.slack.com/methods/files.delete

        :param request: Request model.
        :return: Response model.
        """
        pass

    @build_parameter_object
    @return_model
    async def info(self, request: FilesInfoRequest) -> FilesInfoResponse:
        """
        This method returns information about a file in your team.

        .. seealso:: https://api.slack.com/methods/files.info

        :param request: Request model.
        :return: Response model.
        """
        pass

    @build_parameter_object
    @return_model
    async def list(self, request: FilesListRequest) -> FilesListResponse:
        """
        This method returns a list of files within the team. 
        It can be filtered and sliced in various ways.

        .. seealso:: https://api.slack.com/methods/files.list

        :param request: Request model.
        :return: Response model.
        """
        pass

    @build_parameter_object
    @return_model
    async def revoke_public_url(self, request: FilesRevokePublicURLRequest) -> FilesRevokePublicURLResponse:
        """
        This method disables public/external sharing for a file.

        .. seealso:: https://api.slack.com/methods/files.revokePublicURL

        :param request: Request model.
        :return: Response model.
        """
        pass

    @build_parameter_object
    @return_model
    async def shared_public_url(self, request: FilesSharedPublicURLRequest) -> FilesSharedPublicURLResponse:
        """
        This method enables public/external sharing for a file.

        .. seealso:: https://api.slack.com/methods/files.sharedPublicURL

        :param request: Request model.
        :return: Response model.
        """
        pass

    @build_parameter_object
    @return_model
    async def upload(self, request: FilesUploadRequest) -> FilesUploadResponse:
        """
        This method allows you to create or upload an existing file.

        .. seealso:: https://api.slack.com/methods/files.upload

        :param request: Request model.
        :return: Response model.
        """
        pass


class FilesCommentsModule(BaseModule):
    @build_parameter_object
    @return_model
    async def add(self, request: FilesCommentsAddRequest) -> FilesCommentsAddResponse:
        """
        Add a comment to an existing file.

        .. seealso:: https://api.slack.com/methods/files.comments.add

        :param request: Request model.
        :return: Response model.
        """
        pass

    @build_parameter_object
    @return_model
    async def delete(self, request: FilesCommentsDeleteRequest) -> FilesCommentsDeleteResponse:
        """
        Delete an existing comment on a file. Only the original author of the
        comment or a Team Administrator may delete a file comment.

        .. seealso:: https://api.slack.com/methods/files.comments.delete

        :param request: Request model.
        :return: Response model.
        """
        pass

    @build_parameter_object
    @return_model
    async def edit(self, request: FilesCommentsEditRequest) -> FilesCommentsEditResponse:
        """
        Edit an existing comment on a file. Only the user who created a comment may make edits.
        Teams may configure a limited time window during which file comment edits are allowed.

        .. seealso:: https://api.slack.com/methods/files.comments.edit

        :param request: Request model.
        :return: Response model.
        """
        pass


class GroupsModule(BaseChannelsModule):
    """
    Get info on your team's private channels.
    """

    _base_method = 'groups'

    @build_parameter_object
    @return_model
    async def create(self, request: GroupsCreateRequest) -> GroupsCreateResponse:
        """
        This method creates a private channel.
        
        .. seealso:: https://api.slack.com/methods/groups.create
        
        :param request: Request model.
        :return: Response model.
        """
        pass

    @build_parameter_object
    @return_model
    async def create_child(self, request: GroupsCreateChildRequest) -> GroupsCreateChildResponse:
        """
        This method takes an existing private channel and performs the following steps:

        * Renames the existing private channel (from "example" to "example-archived").
        * Archives the existing private channel.
        * Creates a new private channel with the name of the existing private channel.
        * Adds all members of the existing private channel to the new private channel.
    
        This is useful when inviting a new member to an existing private channel while 
        hiding all previous chat history from them. In this scenario you can call 
        :meth:`GroupsModule.create_child followed by groups.invite.
        
        The new private channel will have a special parent_group property pointing to 
        the original archived private channel. This will only be returned for members 
        of both private channels, so will not be visible to any newly invited members.
        
        .. seealso:: https://api.slack.com/methods/groups.createChild

        :param request: Request model.
        :return: Response model.
        """
        pass

    @build_parameter_object
    @return_model
    async def info(self, request: GroupsInfoRequest) -> GroupsInfoResponse:
        """
        This method returns information about a private channel.
        
        .. seealso:: https://api.slack.com/methods/groups.info

        :param request: Request model.
        :return: Response model.
        """
        pass

    @build_parameter_object
    @return_model
    async def invite(self, request: GroupsInviteRequest) -> GroupsInviteResponse:
        """
        This method is used to invite a user to a private channel. The calling user 
        must be a member of the private channel.

        To invite a new member to a private channel without giving them access 
        to the archives of the private channel, call the :meth:`GroupsModule.create_child`
        method before inviting.
        
        .. seealso:: https://api.slack.com/methods/groups.invite

        :param request: Request model.
        :return: Response model.
        """
        pass

    @build_parameter_object
    @return_model
    async def list(self, request: GroupsListRequest) -> GroupsListResponse:
        """
        This method returns a list of private channels in the team that the caller 
        is in and archived groups that the caller was in. The list of (non-deactivated) 
        members in each private channel is also returned.
        
        .. seealso:: https://api.slack.com/methods/groups.list

        :param request: Request model.
        :return: Response model.
        """
        pass

    @build_parameter_object
    @return_model
    async def open(self, request: GroupsOpenRequest) -> GroupsOpenResponse:
        """
        This method opens a private channel.
        
        .. seealso:: https://api.slack.com/methods/groups.open

        :param request: Request model.
        :return: Response model.
        """
        pass

    @build_parameter_object
    @return_model
    async def close(self, request: GroupsCloseRequest) -> GroupsCloseResponse:
        """
        This method closes a private channel.

        .. seealso:: https://api.slack.com/methods/groups.close

        :param request: Request model.
        :return: Response model.
        """
        pass

    @build_parameter_object
    @return_model
    async def rename(self, request: GroupsRenameRequest) -> GroupsRenameResponse:
        """
        This method renames a private channel.
        
        .. seealso:: https://api.slack.com/methods/groups.rename

        :param request: Request model.
        :return: Response model.
        """
        pass


class ImModule(BaseModule):
    """
    Get info on your direct messages.
    """

    @build_parameter_object
    @return_model
    async def close(self, request: ImCloseRequest) -> ImCloseResponse:
        """
        This method closes a direct message channel.

        .. seealso:: https://api.slack.com/methods/im.close

        :param request: Request model.
        :return: Response model.
        """
        pass

    @build_parameter_object
    @return_model
    async def history(self, request: ImHistoryRequest) -> ImHistoryResponse:
        """
        This method returns a portion of messages/events from the specified 
        direct message channel. To read the entire history for a direct 
        message channel, call the method with no latest or oldest arguments, 
        and then continue paging using the instructions below.

        .. seealso:: https://api.slack.com/methods/im.history

        :param request: Request model.
        :return: Response model.
        """
        pass

    @build_parameter_object
    @return_model
    async def list(self, request: ImListRequest) -> ImListResponse:
        """
        This method returns a list of all im channels that the user has.

        .. seealso:: https://api.slack.com/methods/im.list

        :param request: Request model.
        :return: Response model.
        """
        pass

    @build_parameter_object
    @return_model
    async def mark(self, request: ImMarkRequest) -> ImMarkResponse:
        """
        This method moves the read cursor in a direct message channel.

        .. seealso:: https://api.slack.com/methods/im.mark

        :param request: Request model.
        :return: Response model.
        """
        pass

    @build_parameter_object
    @return_model
    async def open(self, request: ImOpenRequest) -> ImOpenResponse:
        """
        This method opens a direct message channel with another member 
        of your Slack team.

        .. seealso:: https://api.slack.com/methods/im.open

        :param request: Request model.
        :return: Response model.
        """
        pass

    @build_parameter_object
    @return_model
    async def replies(self, request: ImRepliesRequest) -> ImRepliesResponse:
        """
        This method returns an entire thread (a message plus all the 
        messages in reply to it).

        .. seealso:: https://api.slack.com/methods/im.replies

        :param request: Request model.
        :return: Response model.
        """
        pass


class MpimModule(BaseModule):
    """
    Get info on your multiparty direct messages.
    """

    @build_parameter_object
    @return_model
    async def close(self, request: MpimCloseRequest) -> MpimCloseResponse:
        """
        Closes a multiparty direct message channel.

        .. seealso:: https://api.slack.com/methods/mpim.close

        :param request: Request model.
        :return: Response model.
        """
        pass

    @build_parameter_object
    @return_model
    async def history(self, request: MpimHistoryRequest) -> MpimHistoryResponse:
        """
        This method returns a portion of messages/events from the specified 
        multiparty direct message channel. To read the entire history for a 
        multiparty direct message, call the method with no latest or oldest arguments, 
        and then continue paging using the instructions below.

        .. seealso:: https://api.slack.com/methods/mpim.history

        :param request: Request model.
        :return: Response model.
        """
        pass

    @build_parameter_object
    @return_model
    async def list(self, request: MpimListRequest) -> MpimListResponse:
        """
        This method returns a list of all multiparty direct message channels 
        that the user has.

        .. seealso:: https://api.slack.com/methods/mpim.list

        :param request: Request model.
        :return: Response model.
        """
        pass

    @build_parameter_object
    @return_model
    async def mark(self, request: MpimMarkRequest) -> MpimMarkResponse:
        """
        This method moves the read cursor in a multiparty direct message channel.

        .. seealso:: https://api.slack.com/methods/mpim.mark

        :param request: Request model.
        :return: Response model.
        """
        pass

    @build_parameter_object
    @return_model
    async def open(self, request: MpimOpenRequest) -> MpimOpenResponse:
        """
        This method opens a multiparty direct message.

        Opening a multiparty direct message takes a list of up-to 8 encoded 
        user ids. If there is no MPIM already created that includes that 
        exact set of members, a new MPIM will be created. Subsequent calls 
        to :meth:`MpimModule.open` with the same set of users will return 
        the already existing MPIM conversation.

        .. seealso:: https://api.slack.com/methods/mpim.open

        :param request: Request model.
        :return: Response model.
        """
        pass

    @build_parameter_object
    @return_model
    async def replies(self, request: MpimRepliesRequest) -> MpimRepliesResponse:
        """
        This method returns an entire thread (a message plus all the 
        messages in reply to it).

        .. seealso:: https://api.slack.com/methods/mpim.replies

        :param request: Request model.
        :return: Response model.
        """
        pass


class OauthModule(BaseModule):
    """
    Oauth module
    """

    @build_parameter_object
    @return_model
    async def access(self, request: OauthAccessRequest) -> OauthAccessResponse:
        """
        This method allows you to exchange a temporary OAuth code for an 
        API access token. This is used as part of the OAuth authentication flow.

        As discussed in RFC 6749 it is possible to supply the Client ID and 
        Client Secret using the HTTP Basic authentication scheme. If HTTP Basic 
        authentication is used you do not need to supply the client_id and 
        client_secret parameters as part of the request.
        
        **Keep your tokens secure.** Do not share tokens with users or anyone else.

        .. seealso:: https://api.slack.com/methods/oauth.access

        :param request: Request model.
        :return: Response model.
        """
        pass


class PinsModule(BaseModule):
    """
    Pins module
    """

    @build_parameter_object
    @return_model
    async def add(self, request: PinsAddRequest) -> PinsAddResponse:
        """
        This method pins an item (file, file comment, channel message, or group message) 
        to a particular channel. The channel argument is required and one of file, 
        file_comment, or timestamp must also be specified.
        
        .. seealso:: https://api.slack.com/methods/pins.add

        :param request: Request model.
        :return: Response model.
        """
        pass

    @build_parameter_object
    @return_model
    async def list(self, request: PinsListRequest) -> PinsListResponse:
        """
        This method lists the items pinned to a channel.

        .. seealso:: https://api.slack.com/methods/pins.list

        :param request: Request model.
        :return: Response model.
        """
        pass

    @build_parameter_object
    @return_model
    async def remove(self, request: PinsRemoveRequest) -> PinsRemoveResponse:
        """
        This method un-pins an item (file, file comment, channel message, or group message) 
        from a channel. The channel argument is required and one of file, file_comment, 
        or timestamp must also be specified.

        .. seealso:: https://api.slack.com/methods/pins.remove

        :param request: Request model.
        :return: Response model.
        """
        pass


class ReactionsModule(BaseModule):
    """
    Reactions module
    """

    @build_parameter_object
    @return_model
    async def add(self, request: ReactionsAddRequest) -> ReactionsAddResponse:
        """
        his method adds a reaction (emoji) to an item (file, file comment, 
        channel message, group message, or direct message). One of file, 
        file_comment, or the combination of channel and timestamp must be specified.

        .. seealso:: https://api.slack.com/methods/reactions.add

        :param request: Request model.
        :return: Response model.
        """
        pass

    @build_parameter_object
    @return_model
    async def get(self, request: ReactionsGetRequest) -> ReactionsGetResponse:
        """
        This method returns a list of all reactions for a single item (file, 
        file comment, channel message, group message, or direct message).

        .. seealso:: https://api.slack.com/methods/reactions.get

        :param request: Request model.
        :return: Response model.
        """
        pass

    @build_parameter_object
    @return_model
    async def list(self, request: ReactionsListRequest) -> ReactionsListResponse:
        """
        This method returns a list of all items (file, file comment, 
        channel message, group message, or direct message) reacted to by a user.

        .. seealso:: https://api.slack.com/methods/reactions.list

        :param request: Request model.
        :return: Response model.
        """
        pass

    @build_parameter_object
    @return_model
    async def remove(self, request: ReactionsRemoveRequest) -> ReactionsRemoveResponse:
        """
        This method removes a reaction (emoji) from an item (file, file comment, channel message, 
        group message, or direct message). One of file, file_comment, or the combination 
        of channel and timestamp must be specified.

        .. seealso:: https://api.slack.com/methods/reactions.remove

        :param request: Request model.
        :return: Response model.
        """
        pass


class RemindersModule(BaseModule):
    """
    Reminders module
    """

    @build_parameter_object
    @return_model
    async def add(self, request: RemindersAddRequest) -> RemindersAddResponse:
        """
        This method creates a reminder.
        
        .. seealso:: https://api.slack.com/methods/reminders.add

        :param request: Request model.
        :return: Response model.
        """
        pass

    @build_parameter_object
    @return_model
    async def complete(self, request: RemindersCompleteRequest) -> RemindersCompleteResponse:
        """
        This method completes a reminder.

        .. seealso:: https://api.slack.com/methods/reminders.complete

        :param request: Request model.
        :return: Response model.
        """
        pass

    @build_parameter_object
    @return_model
    async def delete(self, request: RemindersDeleteRequest) -> RemindersDeleteResponse:
        """
        This method deletes a reminder.

        .. seealso:: https://api.slack.com/methods/reminders.delete

        :param request: Request model.
        :return: Response model.
        """
        pass

    @build_parameter_object
    @return_model
    async def info(self, request: RemindersInfoRequest) -> RemindersInfoResponse:
        """
        This method returns information about a reminder.

        .. seealso:: https://api.slack.com/methods/reminders.info

        :param request: Request model.
        :return: Response model.
        """
        pass

    @build_parameter_object
    @return_model
    async def list(self, request: RemindersListRequest) -> RemindersListResponse:
        """
        This method lists all reminders created by or for a given user.

        .. seealso:: https://api.slack.com/methods/reminders.list

        :param request: Request model.
        :return: Response model.
        """
        pass


class RtmModule(BaseModule):
    """
    RTM module
    """

    @build_parameter_object
    @return_model
    async def connect(self, request: RtmConnectRequest) -> RtmConnectResponse:
        """
        This method begins a Real Time Messaging API session and reserves your application 
        a specific URL with which to connect via websocket.

        Unlike rtm.start, this method is focused only on connecting to the RTM API.
        
        Use this method in conjunction with other Web API methods like channels.list, 
        users.list, and team.info to build a full picture of the team or workspace
        you're connecting on behalf of.
        
        Please consult the RTM API documentation for full details on using the RTM API.

        .. seealso:: https://api.slack.com/methods/rtm.connect

        :param request: Request model.
        :return: Response model.
        """
        pass

    @build_parameter_object
    @return_model
    async def start(self, request: RtmStartRequest) -> RtmStartResponse:
        """
        This method begins a Real Time Messaging API session and reserves your application 
        a specific URL with which to connect via websocket.

        It's user-centric and team-centric: your app connects as a specific user or bot 
        user on a specific team. Many apps will find the Events API's subscription model 
        more scalable when working against multiple teams.
        
        This method also returns a smorgasbord of data about the team, 
        its channels, and members. Some times more information than can be 
        provided in a timely or helpful manner.
        
        Please use rtm.connect instead, especially when connecting on behalf 
        of an Enterprise Grid customer.
        
        Consult the RTM API documentation for full details on using the RTM API. 
        You'll also find our changelog entry useful.

        .. seealso:: https://api.slack.com/methods/rtm.start

        :param request: Request model.
        :return: Response model.
        """
        pass

class Bot:
    def __init__(self, token, base_path=SLACK_BOT_API_BASEPATH,
                 client_name='SlackBot', spec=None, logger=None, loop=None):
        from .slack_api_spec import spec as default_spec
        spec = spec or default_spec

        self.loop = loop or get_event_loop()
        self.logger = logger or getLogger('slack-bot')
        plugins = [QueryParams()]

        self.service_client = ServiceClient(name=client_name,
                                            spec=spec,
                                            base_path=base_path,
                                            plugins=plugins)

        self.api = APIModule(self)
        self.auth = AuthModule(self)
        self.bots = BotsModule(self)
        self.channels = ChannelsModule(self)
        self.chat = ChatModule(self)
        self.dnd = DndModule(self)
        self.emoji = EmojiModule(self)
        self.files = FilesModule(self)
        self.groups = GroupsModule(self)
        self.im = ImModule(self)
        self.mpim = MpimModule(self)
        self.oauth = OauthModule(self)
        self.pins = PinsModule(self)
