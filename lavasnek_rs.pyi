import typing as t

class Info:
    title: str
    is_seekable: bool
    indetifier: str
    is_stream: bool
    author: str
    length: int
    position: int
    uri: str

class ConnectionInfo:
    guild_id: int
    channel_id: int
    endpoint: int
    token: str
    session_id: str

class PlaylistInfo:
    selected_track: t.Optional[int]
    name: t.Optional[str]

class Track:
    info: Info
    track: str

class Tracks:
    tracks: t.List[Track]
    load_type: str
    playlist_info: PlaylistInfo

class TrackQueue:
    start_time: int
    requester: int
    track: Track
    end_time: int

class Node:
    volume: int
    is_on_loops: bool
    guild: int
    now_playing: t.Optional[TrackQueue]
    is_paused: bool
    queue: t.List[TrackQueue]
    async def get_data(self): ...
    async def set_data(self, data: t.Union[t.Any, t.Dict]): ...

class Band:
    gain: int
    band: int

class Stats:
    frame_stats_deficit: t.Optional[int]
    frame_stats_nulled: t.Optional[int]
    frame_stats_sent: t.Optional[int]
    playing_players: int
    memory_reservable: int
    memory_allocated: int
    cpu_cores: int
    memory_used: int
    cpu_lavalink_load: float
    memory_free: int
    op: str
    players: int
    uptime: int
    cpu_system_load: float

class PlayerUpdate:
    guild_id: int
    state_time: int
    state_position: int
    op: str

class TrackStart:
    track_start_type: str
    guild_id: int
    track: str
    op: str

class TrackFinish:
    reason: str
    op: str
    track_finish_type: str
    guild_id: int
    track: str

class TrackException:
    error: str
    op: str
    track: str
    track_exception_type: str
    exception_message: str
    guild_id: int
    exception_cause: str
    exception_severity: str

class NoSessionPresent(Exception): ...
class NetworkError(Exception): ...
class WebsocketClosed(Exception): ...
class PlayerDestroyed(Exception): ...

class PlayBuilder:
    async def start(self) -> None: ...
    async def queue(self) -> None: ...
    def to_track_queue(self) -> TrackQueue: ...
    def requester(self, requester: int) -> PlayBuilder: ...
    def replace(self, replace: bool) -> PlayBuilder: ...
    def start_time_secs(self, start: int) -> PlayBuilder: ...
    def finish_time_secs(self, finish: int) -> PlayBuilder: ...
    def start_time_millis(self, start: int) -> PlayBuilder: ...
    def finish_time_millis(self, finish: int) -> PlayBuilder: ...

class Lavalink:
    async def start_discord_gateway(self, wait_time: int) -> None: ...
    async def join(self, guild_id: int, channel_id: int) -> ConnectionInfo: ...
    async def leave(self, guild_id: int) -> None: ...
    async def create_session(self, connection_info: ConnectionInfo) -> None: ...
    async def destory(self, guild_id: int) -> None: ...
    async def play(self, track: Track) -> PlayBuilder: ...
    async def get_tracks(self, query: str) -> Tracks: ...
    async def auto_search_tracks(self, query: str) -> Tracks: ...
    async def search_tracks(self, query: str) -> Tracks: ...
    async def skip(self, guild_id: int) -> t.Optional[TrackQueue]: ...
    async def stop(self, guild_id: int) -> None: ...
    async def set_pause(self, guild_id: int, pause: bool) -> None: ...
    async def pause(self, guild_id: int) -> None: ...
    async def resume(self, guild_id: int) -> None: ...
    async def seek_secs(self, guild_id: int, time: int) -> None: ...
    async def jump_to_time_secs(self, guild_id: int, time: int) -> None: ...
    async def scrub_secs(self, guild_id: int, time: int) -> None: ...
    async def seek_millis(self, guild_id: int, time: int) -> None: ...
    async def jump_to_time_millis(self, guild_id: int, time: int) -> None: ...
    async def scrub_millis(self, guild_id: int, time: int) -> None: ...
    async def volume(self, guild_id: int, volume: int) -> None: ...
    async def equalize_all(self, guild_id: int, bands: t.List[float]) -> None: ...
    async def equalize_dynamic(self, guild_id: int, bands: t.List[Band]) -> None: ...
    async def equalize_band(self, guild_id: int, band: Band) -> None: ...
    async def equalize_reset(self, guild_id: int) -> None: ...
    async def remove_guild_from_loops(self, guild_id: int) -> None: ...
    async def remove_guild_node(self, guild_id: int) -> None: ...
    async def get_guild_node(self, guild_id: int) -> t.Optional[Node]: ...
    async def set_guild_node(self, guild_id: int, node: Node) -> None: ...
    async def get_guild_gateway_connection_info(
        self, guild_id: int
    ) -> t.Optional[ConnectionInfo]: ...
    async def wait_for_full_connection_info_insert(
        self, guild_id: int, event_count: int = 10
    ) -> ConnectionInfo: ...
    async def wait_for_connection_info_remove(
        self, guild_id: int, event_count: int = 10
    ) -> None: ...
    async def raw_handle_event_voice_server_update(
        self, guild_id: int, endpoint: str, token: str
    ) -> None: ...
    async def raw_handle_event_voice_state_update(
        self, guild_id: int, user_id: int, session_id: str, channel_id: int
    ) -> None: ...

class LavalinkBuilder:
    async def build(self, event_handler: LavalinkEventHandler) -> Lavalink: ...
    def set_host(self, host: str) -> LavalinkBuilder: ...
    def set_port(self, port: int) -> LavalinkBuilder: ...
    def set_addr(self, address: str) -> LavalinkBuilder: ...
    def set_password(self, password: str) -> LavalinkBuilder: ...
    def set_shard_count(self, shard_count: int) -> LavalinkBuilder: ...
    def set_bot_id(self, bot_id: int) -> LavalinkBuilder: ...
    def set_bot_token(self, bot_token: str) -> LavalinkBuilder: ...
    def set_is_ssl(self, is_ssl: bool) -> LavalinkBuilder: ...
    def set_start_gateway(self, start_gateway: bool) -> LavalinkBuilder: ...
    def set_gateway_start_wait_time_secs(self, time: int) -> LavalinkBuilder: ...
    def set_gateway_start_wait_time_millis(self, time: int) -> LavalinkBuilder: ...

class LavalinkEventHandler:
    async def stats(self, client: Lavalink, event: Stats) -> None: ...
    async def player_update(self, client: Lavalink, event: PlayerUpdate) -> None: ...
    async def track_start(self, client: Lavalink, event: TrackStart) -> None: ...
    async def track_finish(self, client: Lavalink, event: TrackFinish) -> None: ...
    async def track_exception(
        self, client: Lavalink, event: TrackException
    ) -> None: ...
    async def websocket_closed(
        self, client: Lavalink, event: WebsocketClosed
    ) -> None: ...
    async def player_destroyed(
        self, client: Lavalink, event: PlayerDestroyed
    ) -> None: ...
