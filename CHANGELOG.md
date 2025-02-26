# Changelog

## streamlink 2.27.4.0 (2022-08-13)

```text
Billy2011 <kschmidt2007@googlemail.com> (57):
      plugins.mildom: fix/update (#4531)
      stream.hls: refactor segment decryption (#4533)
      plugins.useetv: geo+subscription error messages (#4550)
      stream.hls: parse M3U8 from Response obj directly (#4552)
      plugins.nicolive: fix email logins (#4553)
      stream.hls: cache parsed multivariant playlist (#4568)
      stream.hls: add methods for fetching playlists (#4571)
      plugins.filmon: rewrite plugin (#4573)
      cli: list all dependencies in debug output (#4575)
      plugins.mediavitrina: fix invalid url_json (#4584)
      plugins.idf1: fix plugin (#4585)
      cli: fix pluginerror in handle_url if json is True (#4590)
      plugins.pandalive: update/fix (#4591)
      plugins.telefe: fix livestream (#4592)
      plugin.api.websocket: don't join current thread (#4605)
      plugin.api.websocket: fix typing, export opcodes (#4608)
      plugins.twitcasting: fix websocket stream data (#4608)
      plugins.twitch: fix stream weight (#4625)
      plugins.twitcasting: discard text frames(#4628)
      plugins.rtve: rewrite plugin (#4632)
      stream.segmented: add AwaitableMixin(#4630)
      stream.dash: update DASHStreamWorker.iter_segments(#4630)
      stream.dash: update DASHStreamWriter.fetch(#4630)
      plugins.trovo: update URL matching, tests(#4636)
      plugins.vk: add support for WAF cookie(#4638)
      stream.hls: turn url_master into property(#4643)
      cli: refactor nested argparse argument groups(#4651)
      utils.l10n: switch to locale.getlocale()(#4654)
      docs: use single-backtick inline code block(#4659)
      stream.ffmpegmux: cache executable lookups(#4660)
      plugins.nbcnews: fix plugin(#4668)
      stream.ffmpegmux: rewrite tests(#4669)
      plugins.livestream: rewrite and fix plugin(#4679)
      plugins.huya: rewrite and fix plugin(#4685)
      plugin.api.validate: more DRY schema definitions(#4691)
      plugin.api.validate: add ListSchema(#4691)
      plugin.api.validate: add NoneOrAllSchema(#4691)
      plugins.ard_mediathek: fix plugin(#4703)
      plugins.zdf_mediathek: replace regex with XPath(#4704)
      plugin.api.validate: fix pattern input type(#4708)
      plugin.api.validate: add RegexSchema(#4709)
      plugin.api.http_session: suppress type error(#4710)
      plugins: refactor validation schemas(#4702)
      plugins: move and refactor validation schemas(#4702)
      plugins.dlive: refactor(#4713)
      plugins.cmmedia: refactor(#4711)
      plugins.ltv_lsm_lv: fix plugin(#4712)
      plugins.olympicchannel: rewrite(#4717)
      plugins.btv: rewrite(#4716)
      plugins.blazetv: refactor(#4714)
      plugins: call schema.validate(value)(#4718)
      plugins.deutschewelle: rewrite and fix plugin(#4725)
      plugins.picarto: fix streams and VODs (#4729)
      Update .removed

Ian Cameron <1661072+mkbloke@users.noreply.github.com> (5):
      plugins.useetv: new plugin
      plugins.blazetv: new plugin
      plugin.api: update useragents
      plugins.aloula: new plugin
      plugins.vk: fix

Mozi <29089388+pzhlkj6612@users.noreply.github.com> (7):
      plugins.nicolive: docs: apply bold style to "--timeshift-offset"
      docs: use valid or full-length options to create links
      docs: use bulleted list to organize content
      docs: include the option itself in its example
      docs: apply option links in indented lines
      docs: add names for special characters
      docs: put inline code to code blocks in examples

NeedMilk! <xiaoyu960522@sina.com> (1):
      plugins.atpchallenger: new plugin (#4700)

back-to <backto@protonmail.ch> (2):
      plugins.rtpa: fix 401 error, added self.title
      plugins.eltrecetv: removed

bastimeyer <mail@bastimeyer.de> (14):
      plugins.tvtoya: rewrite plugin
      plugins.youtube: fix InitialPlayerResponse regex
      stream.ffmpegmux: close sub-streams concurrently
      plugins.vidio: rewrite plugin
      plugins.vidio: fix referer HTTP header
      stream.ffmpegmux: add ffmpeg-verbose{,-path} tests
      plugins.tv360: rewrite plugin
      plugins.huajiao: rewrite and fix plugin
      plugins.cinergroup: rewrite and fix plugin
      plugins.raiplay: refactor
      plugins.bloomberg: fix default US live stream
      plugins.theplatform: remove plugin
      plugins.nbc: remove plugin
      plugins.nbcsports: remove plugin

streamlinkbot <streamlinkbot@users.noreply.github.com> (2):
      plugin.api: update useragents
      plugin.api: update useragents
```


## streamlink 2.27.3.0 (2022-05-16)

```text
Alexis Murzeau <amubtdx@gmail.com> (1):
      tests: mock user euid to be able to run tests as root

Billy2011 <kschmidt2007@googlemail.com> (30):
      plugins.teamliquid: plugin removal (#4393)
      chore: clean up some imports (#4394)
      plugins.dash: add support for parameters (#4434)
      plugins.cdnbg: rewrite plugin (#4456)
      plugins.vrtbe: remove plugin (#4459)
      plugins.senategov: remove plugin (#4458)
      plugins.garena: remove plugin (#4460)#
      plugins.facebook: replace itertags (#4465)
      cli: add support for --record=- (#4462)
      plugins.showroom: fix plugin (#4473)
      plugins.youtube: fix consent dialog (#4515)
      Update youtube.py
      stream.segmented: join worker+writer on close (#4517)
      plugin.api.validate: fix xml_element (#4514)
      plugin.api.validate: refactor all + any (#4514)
      plugin.api.validate: refactor get (#4514)
      plugin.api.validate: refactor callable (#4514)
      plugin.api.validate: refactor Schema class (#4514)
      Update compat.py
      Update validate.py
      plugin.api.validate: turn module into package (#4514)
      plugin.api.validate: truncate error messages (#4514)
      plugin.api.validate: rewrite tests (#4514)
      http_session: don't disable InsecureRequestWarning (#4525)
      plugin.api.http_session: add prepare_new_request (#4521)
      stream: refactor to_url and string representation (#4521)
      stream.hls_filtered: simplify discard logic in writer
      docs: rewrite API guide (#4527)

Ekang Monyet <ekangmonyet@posteo.net> (1):
      plugins.nicolive: fix timeshift-offset option

Ian Cameron <1661072+mkbloke@users.noreply.github.com> (8):
      plugins: add missing "description" metadata tags
      plugins.cmmedia: new plugin
      plugins.htv: new plugin
      plugins.trovo: new plugin
      cli.argparser: update help with dir/subdir creation info
      plugins.rotana: plugin removal
      plugins.hiplayer: new plugin
      plugins.crunchyroll: update/fix

Mozi <29089388+pzhlkj6612@users.noreply.github.com> (1):
      cli: add "overwrite" to --force help text (#4396)

back-to <backto@protonmail.ch> (2):
      plugins.oneplusone: fix iframe
      plugins.tlctr: remove plugin

bastimeyer <mail@bastimeyer.de> (3):
      docs: fix CLI argument line breaks
      plugins.funimationnow: replace itertags
      tests: move FileStream tests

code-review-doctor <72647856+code-review-doctor@users.noreply.github.com> (1):
      tests: fix accidental URL string concatenation (#4387)

iwconfig <snelhingst@gmail.com> (1):
      plugins.svtplay: oppetarkiv.se is not functional anymore (#4443)

takayuki <nirasawa@gmail.com> (1):
      plugins.linelive: fix API URL
```


## streamlink 2.27.2.0 (2022-03-08)

```text
Billy2011 <kschmidt2007@googlemail.com> (20):
      plugins.skylinewebcams: fix source extraction
      cli: log absolute file output path
      cli.main: prevent py2 UnicodeDecodeError
      plugin.api.http_session: add class TLSSecLevel1Adapter() (#4345)
      plugins.filmon: fix/update (#4335)
      plugins.pandalive: fix plugin (#4338)
      docs: correct minor typo (#4351)
      plugins.ard_live: fix live.daserste.de inputs (#4355)
      tests.plugins: test URL capture groups (#4363)
      tests: rewrite TestPlugins using pytest fixtures (#4372)
      tests: add parametrized TestPluginTests (#4372)
      tests: add parametrized TestRemovedPluginsFile (#4372)
      tests: move global plugin arguments test (#4372)
      plugins.mildom: get token for livestream (#4375)
      plugins: add metadata header comments (#4374)
      docs: dynamically build list of plugins (#4374)
      plugins.nicolive: fix login via email (#4380)
      Update .travis.yml

Dylan <71848660+dylan-roussin@users.noreply.github.com> (1):
      typo of "steams" to "streams" in opencv-face.py

Justinas Stankevičius <justinas@users.noreply.github.com> (1):
      plugins.lnk: add new plugin (#4364)

bastimeyer <mail@bastimeyer.de> (10):
      plugins.pluzz: fix workflow value in API schema
      plugins.rtpa: add new plugin
      tests.plugins: implement should_match_groups
      plugins.goltelevision: fix API URL
      docs: update Streamlink Twitch GUI image
      docs: fix GithubReferences transform
      docs: add icon to external links
      docs: rename plugin_matrix to plugins
      docs: update developing page
      docs: fix plugin metadata example

fireattack <human.peng@gmail.com> (1):
      plugins.openrectv: get URLs from subs_trial_media (#4349)
```


## streamlink 2.27.1.0 (2022-01-28)

```text
Billy2011 <kschmidt2007@googlemail.com> (38):
      cli.output: remove MPV title variable escape logic (#4206)
      plugin: add 'id' metadata property (#4203)
      plugins.youtube: add 'id' metadata (#4203)
      plugins.twitch: add 'id' metadata (#4203)
      docs: add dedicated metadata variables section (#4207)
      CLI: fix file output
      utils.parse: parse invalid XHTML5 documents (#4210)
      cli: prioritize --help and fix its output (#4213)
      plugins.youtube: add category metadata (#4214)
      plugins.youtube: fix metadata on /live URLs (#4222)
      stream.hls: read and discard filtered sequences properly
      plugins.abematv: fix HLS filtering
      plugins.steam: refactor plugin (#4244)
      plugins.onetv: added support for channel with different timezone +4 (#4247)
      plugins.pluto: rewrite/fix (#4232)
      plugins.stadium: rewrite (#4246)
      cli: create file output before opening the stream (#4252)
      plugins.albavision: fix/update (#4254)
      plugins.pluto: make ads filtering optional
      cli.console: ignore msg() calls if json=True
      plugins.ceskatelevize: Fix Livestreams (#4260)
      plugins.mediavitrina: better support for different channel names (#4259)
      plugins.live_russia_tv: removed outdated plugin (#4263)
      plugins.liveme: removed (#4264)
      plugins.vtvgo: remove itertags (#4266)
      plugins.vk: rewrite and remove itertags (#4267)
      plugins.ard_mediathek: fix encode error
      plugins.streann: remove itertags (#4268)
      plugins.abweb: removed (#4270)
      plugins.nos: remove itertags (#4272)
      tests: rewrite plugins_meta tests (#4274)
      2022
      plugins.delfi: rewrite plugin (#4273)
      stream.hls: fix byterange parser (#4301)

Christian Kündig <christian@kuendig.info> (1):
      plugins.yupptv: override encoding, set Origin header (#4261)

Ian Cameron <1661072+mkbloke@users.noreply.github.com> (1):
      plugins.albavision: update plugin_matrix.rst

Mozi <29089388+pzhlkj6612@users.noreply.github.com> (1):
      cli: tell users the stream could be saved or piped

back-to <backto@protonmail.ch> (3):
      stream.dash: sort video duplicated resolutions by bandwidth
      plugins.dogus: update and cleanup
      plugins.twitcasting: Fix error messages

bastimeyer <mail@bastimeyer.de> (5):
      plugins.ustreamtv: fix websocket address
      tests: fix named pipe being created in CLI tests
      plugins.latina: remove plugin
      plugins.foxtr: fix regex
      plugins.twitch: fix pluginmatcher regex

zappepappe <zappepappe@users.noreply.github.com> (1):
      plugins.svtplay: fix live channel URL matching (#4219)
```


## streamlink 2.27.0.0 (2021-11-23)

```text
Billy2011 <kschmidt2007@googlemail.com> (34):
      plugins.viasat: removed (#4087)
      plugin.api: remove StreamMapper (#4088)
      plugins.okru: rewrite plugin, drop RTMP (#4090)
      plugin: trim metadata strings (#4117)
      plugins.brightcove: add more HLS source types (#4119)
      setup: remove NO_DEPS env var (#4115)
      cli: deprecate the --https-proxy option as well as the Session options (#4120)
      plugins.earthcam: fix hls_url
      plugins.openrectv: be able to get subscription video (#4130)
      plugins.tga: remove plugin (#4129)
      plugins.ltv_lsm_lv: update the plugin for the new page layout (#4138)
      logger: fix warning import and trace export (#4151)
      plugin.api: implement WebsocketClient (#4153)
      plugins.twitcasting: re-implement websocket client (#4154)
      plugins.twitch: new plugin command --twitch-api-header (#4156)
      plugins.nicolive: re-implement plugin (#4155)
      revert: stream.hls: remove hls-segment-stream-data option (#4159)
      plugins.attheshore: fix camid
      plugin.api.websocket: add reconnect method (#4164)
      stream.http: fix custom method argument (#4171)
      streams: remove HDS/AkamaiHD
      plugins.ustreamtv: re-implement plugin
      stream.flvconcat: remove
      remove flashmedia
      cli: override default signal handlers (#4190)
      plugins.twitch: set playerType back to embed (#4194)
      session.resolve_url: return plugin class + URL
      plugins.ard_mediathek: rewrite plugin (#4200)
      Update .travis.yml
      Update cli.rst
      utils.parse: fix encoding in parse_html (#4201)
      plugins.ard_mediathek: fix plugin (#4202)

Ian Cameron <1661072+mkbloke@users.noreply.github.com> (2):
      plugins.facebook: update onion address
      plugins.picarto: update URL regex and logic

back-to <backto@protonmail.ch> (7):
      plugins.tv999: use parse_html
      plugins.ssh101: use parse_html
      plugins.app17: remove RTMPStream, cleanup
      plugins.twitch: add device-id headers (#4086)
      plugin.api: update useragents
      plugins.goltelevision: fix api url and update plugin url
      plugins.tviplayer: new plugin

bastimeyer <mail@bastimeyer.de> (4):
      plugins.twitch: remove device-id headers
      ci.github: check for unicode bidi control chars
      plugins.twitch: refactor api-headers
      plugins.twitch: avg duration for prefetch segments

kyldery <kyldery@protonmail.com> (1):
      plugins.crunchyroll: add metadata attributes (#4185)

nnrm <91910832+nnrm@users.noreply.github.com> (1):
      plugins.nicolive: add support for community urls
```


## streamlink 1.27.8.0 (2021-10-09)

```text
Billy2011 <kschmidt2007@googlemail.com> (31):
      docs.install.rst: changed python 3.5 to 3.6
      docs: bump furo docs req to 2021.09.08 (#4000)
      http_session: override urllib3 percent-encoding (#4003)
      plugins.ardlive: rewrite plugin (#4005)
      utils: replace LazyFormatter with new Formatter (#4008)
      utils: move all URL methods to utils.url (#4016)
      plugins.viutv: removed (#4018)
      tests: fix Accept-Encoding headers in stream_json (#4022)
      plugins: clean up imports of parse_* utils (#4023)
      utils: split into submodules and fix imports (#4025)
      plugins.artetv: rewrite plugin using v2 API (#4029)
      plugins.bloomberg: rewrite plugin (#4031)
      stream: clean up imports (#4034)
      plugins.bbciplayer: remove HDSStream, upgrade scheme (#4041)
      plugins.earthcam: rewrite plugin, remove rtmp (#4043)
      plugins.skylinewebcams: add yt supp.
      plugins.oneplusone: cleanup and add auto session reload (#4049)
      plugins.picarto: fix HLS URL hostname (#4052)
      plugins.wetter: fix hls streams
      utils.url: make update_scheme always update target (#4053)
      plugins: fix update_scheme calls (#4053)
      plugins.bfmtv: rewrite plugin using XPath (#4061)
      plugins.youtube: replace itertags with XPath (#4060)
      plugins.youtube: better API age-gate bypassing (#4058)
      plugins.pandalive: new plugin (#4064)
      plugins.showroom: cleanup (#4065)
      session: move from http to https as default scheme (#4068)
      plugins.brightcove: rewrite plugin (#4070)
      plugins.tv5monde: re-implement plugin (#4077)

back-to <backto@protonmail.ch> (2):
      stream.hls: Fix error msg for 'Unable to decrypt cipher ...'
      plugins.webcast_india_gov: removed

bastimeyer <mail@bastimeyer.de> (9):
      docs: fix CLI argument example in manpage
      tests: fix typo in pytest skipif marker
      plugins.pluzz: rewrite plugin
      tests: move tests/streams to tests/stream
      tests: fix partial coverage in can_handle_url
      session: don't override https-proxy scheme
      utils.parse: fix ignore_ns in parse_xml
      script: fix update-removed-plugins bash script
      plugins.tv5monde: re-implement plugin
```


## streamlink 1.27.7.0 (2021-09-07)

```text
Billy2011 <kschmidt2007@googlemail.com> (31):
      docs: fix / update deprecations page
      session: deprecate options for spec. stream types (#3893)
      stream.hls: remove hls-segment-stream-data option (#3894)
      stream.hls: except more errors raised by requests (#3902)
      plugins.raiplay: use 'res.encoding = "UTF-8"' (#3904)
      plugins.rtve: update for /play/ URLs (#3905)
      plugins.zattoo: fix HLS stream, added more debug details
      plugins.nbcnews: fix stream URL extraction (#3909)
      docs: update python-requests version comment (#3928)
      plugins.twitch: replace remaining kraken API calls (#3929)
      plugins.twitch: refactor TwitchAPI class methods (#3929)
      setup: update requests version (#3880)>=2.26.0
      plugins.huomao: plugin removal (#3932)
      plugins.sportschau: fix audio streams (#3947)
      plugins.animelab: removed (#3951)
      plugins.svtplay: fix plugin video id (#3949)
      vendor: add lxml dependency (#3952)
      plugins.deutschewelle: rewrite plugin (#3953)
      plugins.gardenersworld: remove plugin (#3966)
      plugin.api.validate: switch to lxml.etree (#3967)
      plugins.booyah: add support for source stream (#3969)
      plugin.api.validate: add args+kwargs to transform (#3972)
      plugin.api.validate: add parse_{json,html,xml,qsd} (#3972)
      plugin: metadata attributes (#3970)
      plugins.deutschewelle: validate.parse_html (#3975)
      plugins.reuters: rewrite and fix using XPath (#3977)
      plugins.euronews: rewrite and fix using XPath (#3976)
      utils.__init__: make typing optional
      stream.ffmpegmux: always clean up named pipes (#3992)

Ian Cameron <1661072+mkbloke@users.noreply.github.com> (1):
      plugins.pluto: fix URL match for 2 letter language codes

back-to <backto@protonmail.ch> (1):
      plugins.abematv: skip invalid ad segments

bastimeyer <mail@bastimeyer.de> (6):
      docs: reorganize stream transport options
      tests: fix Plugin.bind(session) calls
      plugin: fix cookie related error messages
      plugins.euronews: add API fallback requests
      plugins: fix utils imports
      plugins.welt: rewrite and simplify using XPath

steven7851 <steven7851@msn.com> (1):
      plugins.app17: fix API_URL and URL match (#3989)
```


## streamlink 1.27.6.0 (2021-07-27)

```text
Billy2011 <kschmidt2007@googlemail.com> (28):
      plugins.youtube: translate embed_live URLs (#3804)
      plugins.youtube: added API fallback (#3809)
      plugins.periscope: remove plugin (#3813)
      plugins.vlive: fixed livestream (#3820)
      plugins.PowerApp: removed (#3816)
      plugins.TeleclubZoom: removed (#3817)
      Update pluto.py
      plugins.mediaklikk: rewrite plugin (#3825)
      stream.hls_playlist: refactor
      plugin: new matchers API (#3821)
      plugins: update protocol plugins (#3821)
      plugins: update basic plugins (#3821)
      plugins: update plugins with URL capture groups (#3821)
      plugins: update plugins with spec. can_handle_url (#3821)
      plugins: update plugins with multiple URL matchers (#3821)
      plugins: update plugins with URL translations (#3821)
      session: resolve deprecated plugins (#3821)
      plugins.zdf_mediathek: refactor plugin, drop HDS (#3832)
      plugins.cdnbg: Fix regex and referer issues (#3838)
      plugins.CanalPlus: removed (#3841)
      plugins.liveedu: removed (#3845)
      plugins.openrectv: update HLS URLs (#3850)
      plugin.plugin: make typing optional
      plugins.youtube: detect Livestreams with 'isLive' (#3872)
      plugins.nimotv: use 'mStreamPkg' (#3882)
      stream.hls: set fallback playlist reload time to 6 seconds (#3887)
      setup: add future dep for py2

back-to <backto@protonmail.ch> (7):
      plugins.rtvs: fixed livestream
      plugins.nos: Fixed Livestream and VOD
      plugins.Tigerdile: removed
      plugins.Dommune: removed
      plugins.rtlxl: removed
      plugins.Streamingvideoprovider: removed
      plugin.api: update useragents

bastimeyer <mail@bastimeyer.de> (4):
      docs: add deprecations page
      plugins.tv8: remove API, find HLS via simple regex
      plugins.youtube: find videoId on channel pages
      tests: fix unnecessary hostname lookup in cli_main

gustaf <gustaf@protonmail.ch> (1):
      plugins.tv4play: fix plugin URL regex
```


## streamlink 1.27.5.0 (2021-06-19)

```text
Billy2011 <kschmidt2007@googlemail.com> (25):
      v1.27.4.0-dev
      utils.url: add encoding options to update_qsd (#3746)
      plugins.tf1: fixed api_url (#3748)
      plugins.onetv: cleanup (#3743)
      plugins.mediavitrina: new plugin (#3743)
      use range() from streamlink.compat
      plugins.olympics: fix / rewrite
      utils.url: fix update_scheme with implicit schemes (#3765)
      plugins.bfmtv: fix/find Brightcove video data in JS (#3662)
      plugins.skylinewebcams: fix hls url
      tests: refactor TestCLIMainLogging (#3753)
      plugins.zattoo: change api to hello_v3
      plugin.api.validate: add nested lookups to get() (#3774)
      plugin.api.validate: implement union_get() (#3774)
      plugins.ine: removed (#3781)
      plugins.zattoo: cleanup, fix other domains  master (#3780)
      plugins.twitch: tidy up API calls (#3778)
      stream.hls: replace custom PKCS#7 unpad function (#3770)
      utils.named_pipe: rewrite named pipes (#3709)
      cli: implement logfile
      plugins.youtube: clean up a bit
      plugins.youtube: update URL regex, translate URLs (#3797)
      plugins.youtube: replace private API calls (#3797)
      plugins.youtube: unescape consent form values (#3797)
      prepare 1.27.5.0

FaceHiddenInsideTheDark <wesleywitz@gmail.com> (1):
      plugins.funimationnow: fix subtitle language (#3752)

Ian Cameron <1661072+mkbloke@users.noreply.github.com> (1):
      plugins.booyah: new plugin

back-to <backto@protonmail.ch> (2):
      plugin.api: update useragents, remove EDGE
      plugins.playtv: removed - SEC_ERROR_EXPIRED_CERTIFICATE (#3798)

bastimeyer <mail@bastimeyer.de> (6):
      docs: set man_make_section_directory to false
      tests.hls: test headers on segment+key requests
      cli.argparser: fix description text
      plugins.twitch: add access token to clips
      plugins.twitch: fix clips URL regex
      plugins.twitch: query hosted channels on GQL

shirokumacode <79662880+shirokumacode@users.noreply.github.com> (1):
      plugins.mildom: new plugin for mildom.com (#3584)
```


## streamlink 1.27.4.0 (2021-05-21)

Release highlights:

- Added: skylinewebcams plugin
- Fixed: youtube 404 errors ([#3732](https://github.com/streamlink/streamlink/pull/3732))
- Fixed: euronews plugin ([#3698](https://github.com/streamlink/streamlink/pull/3698))
- Fixed: bbciplayer plugin ([#3725](https://github.com/streamlink/streamlink/pull/3725))
- Fixed: missing removed-plugins-file in `setup.py build` ([#3653](https://github.com/streamlink/streamlink/pull/3653))
- Changed: HLS streams to use rounded bandwidth names ([#3721](https://github.com/streamlink/streamlink/pull/3721))


```text
Billy2011 <kschmidt2007@googlemail.com> (7):
      plugins.euronews: rewrite and fix live streams (#3698)
      plugins.nicolive: fix proxy arguments (streamlink#3710) 
      plugins.skylinewebcams: add new plugin
      plugins.mediaklikk: improve _url_re
      plugins.mitele: use '_{bitrate}' and remove duplicates (#3722)
      prepare 1.27.4.0

Ian Cameron <1661072+mkbloke@users.noreply.github.com> (1):
      plugins.bbciplayer: fix/update state_re regex

Kagamia <amethyst50504724@msn.com> (1):
      plugins.nicolive: fix proxy arguments (#3710)

Yavuz Kömeçoğlu <komecoglu.yavuz@gmail.com> (1):
      plugins.youtube: add html5=1 parameter (#3732)

back-to <backto@protonmail.ch> (1):
      stream.hls_playlist: round BANDWIDTH and parse as int (#3721)
```


## streamlink 1.27.3.0 (2021-04-19)

Release highlights:

- Added: plugin for livespotting.tv
- Fixed: various plugins issues (see detailed changelog down below)
- Removed: plugin for hitbox.tv (#3686) (https://github.com/streamlink/streamlink/pull/3686)
- Removed: plugin for tvplayer.com (#3673) (https://github.com/streamlink/streamlink/pull/3673)

```text
Billy2011 <kschmidt2007@googlemail.com> (11):
      plugins.youtube: fix consent issue
      plugins.picarto: rewrite/fix (#3661)
      plugins.youtube: add short video URLs (#3677)
      plugins.livespotting: new plugin
      plugins.hitbox: remove plugin (#3686)
      plugins.livespotting: fix location cams
      plugins.wetter: add mp4 stream type
      plugins.tvplayer: plugin removal (#3673)
      plugins.livespotting: improve _url_re

bastimeyer <mail@bastimeyer.de> (1):
      chore: remove square brackets from issue titles

bururaku <rakuburu@gmail.com> (1):
      plugins.abematv: Fixed download problem again. (#3658)
```


## streamlink 1.27.2.1 (2021-03-26)

Patch release:

- Fixed: test failure due to missing removed plugins file in sdist tarball (#3644).

```text
Billy2011 <kschmidt2007@googlemail.com> (29):
      build: don't build sdist/bdist quietly (#3645)
      build: include removed plugins file in sdist
```


## streamlink 1.27.2.0 (2021-03-23)

Release highlights:

- Added: `--interface`, `-4` / `--ipv4` and `-6` / `--ipv6` ([#3483](https://github.com/streamlink/streamlink/pull/3483))
- Added: `--niconico-purge-credentials` ([#3434](https://github.com/streamlink/streamlink/pull/3434))
- Added: `--twitcasting-password` ([#3505](https://github.com/streamlink/streamlink/pull/3505))
- Added: plugin for ahaber.com.tr and atv.com.tr ([#3484](https://github.com/streamlink/streamlink/pull/3484)), nimo.tv ([#3508](https://github.com/streamlink/streamlink/pull/3508))
- Added: plugin for auftanken.tv
- Fixed: `--player-http` / `--player-continuous-http` HTTP server being bound to all interfaces ([#3450](https://github.com/streamlink/streamlink/pull/3450))
- Fixed: handling of languages without alpha_2 code when using pycountry ([#3518](https://github.com/streamlink/streamlink/pull/3518))
- Fixed: memory leak when calling `streamlink.streams()` ([#3486](https://github.com/streamlink/streamlink/pull/3486))
- Fixed: race condition in HLS related tests ([#3454](https://github.com/streamlink/streamlink/pull/3454))
- Fixed: `--player-fifo` issues on Windows with VLC or MPV ([#3619](https://github.com/streamlink/streamlink/pull/3619))
- Fixed: various plugins issues (see detailed changelog down below)
- Removed: plugin for micous.com ([#3457](https://github.com/streamlink/streamlink/pull/3457)), ntvspor.net ([#3485](https://github.com/streamlink/streamlink/pull/3485)), btsports ([#3636](https://github.com/streamlink/streamlink/pull/3636))
- Dependencies: set `websocket-client` to `>=0.58.0` ([#3634](https://github.com/streamlink/streamlink/pull/3634))

```text
Billy2011 <kschmidt2007@googlemail.com> (29):
      stream.hls: open reader from class attribute
      tools: force LF line endings via .gitattributes
      tests.hls: await all filtered-HLS writer calls
      plugins.twitch: fix access_token on invalid inputs
      2021
      plugins.stadium: adaptions for new player api
      plugins.dogan: py2 fix
      plugins.pluto:  py2 fix
      plugins.streann:  py2 fix
      plugins.twitcasting: add support for  private/password-protected streams (#3505)
      plugins.bloomberg: fix and refactor plugin (#3514)
      session: implement --interface, --ipv4 and --ipv6 (#3483)
      tests: Add / fix tests
      plugins.afreeca: use 'gs_cdn_pc_web' and 'common' (#3549)
      plugins: fix invalid plugin class names (#3533)
      tests.plugins: parametrize can_handle_url tests (#3533)
      [Patch] tests: fix test code coverage (#3547)
      plugins.wetter: add vod support
      utils.crypto: add py2 compat. pad, unpad
      plugins.mjunoon: rewrite/fix (#3577)
      plugins.ustvnow: update pad, unpad
      plugins.openrectv: update/fix (#3583)
      plugins.abematv: Update abematv.py (#3617)
      plugins.auftanken: new plugin
      setup.py: require websocket-client>=0.58.0 (#3634)
      plugins.nicolive: fixed websocket-client (#3634)
      plugins.btsports: remove plugin (#3636)
      cli: debug-log arguments set by the user (#3639)
      utils: remove custom memoize decorator (#3486)

Ian Cameron <1661072+mkbloke@users.noreply.github.com> (6):
      plugins.mico: plugin removal
      plugins.turkuvaz: add channels and URL tests
      plugins.dogus: remove channel and update test
      plugins.tvtoya: fix playlist regex
      plugins.nimotv: new plugin
      plugins.tvtoya: minor fixes

Jefffrey <22608443+Jefffrey@users.noreply.github.com> (1):
      plugins.Nicolive: login before getting wss api url

Miguel Valadas <mvaladas@gmail.com> (1):
      plugins.rtpplay: add schema and fix HLS URL (#3627)

Vladimir Stavrinov <9163352+vstavrinov@users.noreply.github.com> (1):
      plugins.oneplusone: fix iframe url pattern (#3503)

back-to <backto@protonmail.ch> (7):
      cli.main: use *_args, **_kwargs for create_http_server (#3450)
      plugins.nicolive: added --niconico-purge-credentials
      docs: remove outdated gst-player example
      plugins.facebook: Add 'Log into Facebook' error message.
      stream.dash: Fix static playlist - refresh_wait - Pipe copy aborted - Read timeout
      plugin.api: update useragents (#3637)
      plugins.zattoo: use 'dash' as default stream

bastimeyer <mail@bastimeyer.de> (10):
      docs: add minimalist code of conduct
      http_session: remove HTTPAdapterWithReadTimeout
      docs: fix description of `--ffmpeg-fout`
      utils/l10n: fix langs without alpha_2 in pycountry
      docs: remove CLI tutorial from man page
      plugins.vtvgo: ignore duplicate params
      chore: reorder and improve issue templates
      plugins: fix and update removed plugins list
      cli.output: fix named pipe player input on Windows
      cli: refactor log_current_versions and add tests

onde2rock <onde2rock@users.noreply.github.com> (1):
      plugins.bfmtv : fix rmcstory and rmcdecouverte (#3471)
```


## streamlink 1.27.1.0 (2020-12-22)

Release highlights:

- BREAKING: removed all deprecated CLI arguments ([#3277](https://github.com/streamlink/streamlink/pull/3277), [#3349](https://github.com/streamlink/streamlink/pull/3349))
  - `--http-cookies`, `--http-headers`, `--http-query-params`
  - `--no-version-check`
  - `--rtmpdump-proxy`
  - `--cmdline`, `-c`
  - `--errorlog`, `-e`
  - `--errorlog-path`
  - `--btv-username`, `--btv-password`
  - `--crunchyroll-locale`
  - `--pixiv-username`, `--pixiv-password`
  - `--twitch-oauth-authenticate`, `--twitch-oauth-token`, `--twitch-cookie`
  - `--ustvnow-station-code`
  - `--youtube-api-key`
- BREAKING: replaced various subtitle muxing CLI arguments with `--mux-subtitles` ([#3324](https://github.com/streamlink/streamlink/pull/3324))
  - `--funimationnow-mux-subtitles`
  - `--pluzz-mux-subtitles`
  - `--rtve-mux-subtitles`
  - `--svtplay-mux-subtitles`
  - `--vimeo-mux-subtitles`
- BREAKING: sideloading faulty plugins will now raise an `Exception` ([#3366](https://github.com/streamlink/streamlink/pull/3366))
- BREAKING/API: removed deprecated parameters from `HLSStream.parse_variant_playlist` ([#3347](https://github.com/streamlink/streamlink/pull/3347))
- BREAKING/API: removed `plugin.api.support_plugin` ([#3398](https://github.com/streamlink/streamlink/pull/3398))
- Added: new plugin for pluto.tv ([#3363](https://github.com/streamlink/streamlink/pull/3363))
- Added: support for HLS master playlist URLs to `--stream-url` / `--json` ([#3300](https://github.com/streamlink/streamlink/pull/3300))
- Added: `--ffmpeg-fout` for changing the output format of muxed streams ([#2892](https://github.com/streamlink/streamlink/pull/2892))
- Added: `--ffmpeg-copyts` and `--ffmpeg-start-at-zero` ([#3404](https://github.com/streamlink/streamlink/pull/3404), [#3413](https://github.com/streamlink/streamlink/pull/3413))
- Added: `--streann-url` for iframe referencing ([#3356](https://github.com/streamlink/streamlink/pull/3356))
- Added: `--niconico-timeshift-offset` ([#3425](https://github.com/streamlink/streamlink/pull/3425))
- Fixed: duplicate stream names in DASH inputs ([#3410](https://github.com/streamlink/streamlink/pull/3410))
- Fixed: youtube live playback ([#3268](https://github.com/streamlink/streamlink/pull/3268), [#3372](https://github.com/streamlink/streamlink/pull/3372), [#3428](https://github.com/streamlink/streamlink/pull/3428))
- Fixed: `--twitch-disable-reruns` ([#3375](https://github.com/streamlink/streamlink/pull/3375))
- Fixed: various plugins issues (see detailed changelog down below)
- Changed: `{filename}` variable in `--player-args` / `-a` to `{playerinput}` and made both optional ([#3313](https://github.com/streamlink/streamlink/pull/3313))
- Changed: MPV's automated `--title` argument to `--force-media-title` ([#3405](https://github.com/streamlink/streamlink/pull/3405))
- Changed: HTML documentation theme to [furo](https://github.com/pradyunsg/furo) ([#3335](https://github.com/streamlink/streamlink/pull/3335))
- Removed: plugins for `skai`, `kingkong`, `ellobo`, `trt`/`trtspor`, `tamago`, `streamme`, `metube`, `cubetv`, `willax`

```text
Billy2011 <kschmidt2007@googlemail.com> (49):
      cli.main: improvements
      release-27 mods
      release: 1.27.0.0
      plugins.youtube: fix live playback
      check for valid canonical URL
      remove User-Agent
      replace self.logger calls in plugins/updates
      chore: remove deprecated CLI arguments
      docs changes
      update workflow
      update github.io url's
      Update deploy-docs.sh
      update cli.main
      plugins.skai: plugin removal
      update import order
      plugins.trt/trtspor: remove plugins
      cli: optional player-args input variable
      cli: add support for stream manifest URL output
      plugin.api.useragents: update User-Agent and removed FIREFOX User-Agent imports
      Create .travis.yml
      Create deploy_key_doctr.enc
      plugins.bfmtv: fix ID & embed re, use Dailymotion
      plugins.abweb: fixed login issues
      update docs
      plugins.cdnbg: simplify and fix iframes without schema
      docs: add autosectionlabel Sphinx extension
      docs: fix most http links
      Update README.md
      plugin: implement global plugin arguments
      plugins.earthcam: change rtmp stream prio
      streamlink.session: remove py2 deprecated warning
      plugins.mitele: update plugin to support new website APIs
      plugins.tamago: removed dead plugin
      plugins.streamme: removed dead plugin
      plugins.cubetv: removed dead plugin
      cli.utils: remove named_pipe.py file, use streamlink.utils
      fix str validates for py2 compat.
      plugins.willax: removed plugin, they use streann
      plugins.streann: allow different source URLs
      docs: split CLI args in HTML output into rows
      Update author email to shared email
      plugin.api: remove support_plugin
      stream.dash: allow '_alt' streams with the same resolution
      docs: switch theme to furo, bump sphinx to >=3.0
      docs: remove custom sphinx_rtd_theme_violet
      cli.output: replace MPV player title parameter
      plugins.pluto: new plugin for https://pluto.tv/
      stream.ffmpegmux: add --ffmpeg-copyts option (#3404)
      packages.requests_file: update import order

Ian Cameron <1661072+mkbloke@users.noreply.github.com> (6):
      plugins.kingkong: plugin removal
      plugins.cnews: fix video ID search, add schema
      plugins.ellobo: plugin removal
      plugins.filmon: mitigate for non-JSON data response
      plugins.schoolism: fix and test for colon in title (#3421)
      plugins.dogan: fix/update

Jon Bergli Heier <snakebite@jvnv.net> (1):
      plugins.nrk: fix/rewrite plugin (#3318)

Mark Ignacio <mark@ignacio.io> (1):
      plugins.NicoLive: add --niconico-timeshift-offset option (#3425)

Martin Buck <mb-tmp-tvguho.pbz@gromit.dyndns.org> (1):
      plugins.zdf_mediathek: also support 3sat mediathek

Sean Greenslade <sean@seangreenslade.com> (1):
      plugins.picarto: explicitly detect and fail on private streams

Seonjae Hyeon <hsj106@mju.ac.kr> (1):
      plugins.vlive: fix URL regex and plugin (#3315)

azizLIGHT <azizLIGHT@users.noreply.github.com> (1):
      docs: fix mpv property-list link in --title description (#3342)

back-to <backto@protonmail.ch> (13):
      plugin.api.useragents: update User-Agent
      plugins.huya: use FLV stream with multiple mirrors
      plugin.api.useragents: update User-Agent's
      plugins.metube: removed dead plugin
      plugins.pixiv: set headers for stream data, fixed login issue
      plugins.twitch: fix --twitch-disable-reruns
      plugins.twitch: fix ads
      plugins.youtube: quickfix for "/live" URL
      plugins.afreeca: update '_get_channel_info' with 'bno', plugin cleanup (#3408)
      plugins.plugin: use the same cls.logger 'plugins'
      stream.ffmpegmux: disable -start_at_zero for -copyts as default (#3413)
      plugin.api.useragents: update User-Agent
      plugins.youtube: Fix 'ytInitialData' for channel pages

bastimeyer <mail@bastimeyer.de> (23):
      chore: remove old LIVESTREAMER_VERSION constant
      ci.github: run lint step before test step
      flake8: add import-order linting config
      plugins.twitch: player_type access token parameter
      plugins: turn mux-subtitles into a global argument
      plugins.twitch: remove player_type parameter
      plugins.twitch: move access_token request to GQL
      chore: remove HLS variant playlist compat params
      chore: remove old rtmpdump/subprocess CLI args
      stream.ffmpegmux: only close FFMPEGMuxer once
      chore: fix deprecated logging.Logger.warn calls
      docs: fix CLI page
      docs: add warning to plugin sideloading section
      tools: update editorconfig for docs theme files
      docs: add index page to toctree
      docs: add custom stylesheet and customize sidebar
      docs: change/fix fonts, brand colors and spacings
      docs: add version warning message
      docs: fix applications and donate pages
      cli: move plugin args into their own args group
      docs: fix scrollbar issues in both sidebars
      cli: move --stream-url to different args group
      cache: catch OverflowError in set()

beardypig <beardypig@protonmail.com> (2):
      tests: validate all plugins' global arguments
      stream.ffmpegmux: Add support for specifying output file format and audio sync option (#2892)

smallbomb <rockon590+git@gmail.com> (1):
      plugins: fix radiko.py url (#3394)
```


## streamlink 1.27.0.0 (2020-10-18)

This is the first Python 2.7 compatibel release created from the streamlink/streamlink base version 1.7.0

- renamed streamlink to streamlink-27
- added wetter plugin
- added attheshore plugin
- added ozolio plugin
- added cli-main-update-1


## streamlink 1.7.0 (2020-10-18)

Release highlights:

- Added: new plugins for micous.com, tv999.bg and cbsnews.com
- Added: new embedded ad detection for Twitch streams ([#3213](https://github.com/streamlink/streamlink/pull/3213))
- Fixed: a few broken plugins and minor plugin issues (see changelog down below)
- Fixed: arguments in config files were read too late before taking effect ([#3255](https://github.com/streamlink/streamlink/pull/3255))
- Fixed: Arte plugin returning too many streams and overriding primary ones ([#3228](https://github.com/streamlink/streamlink/pull/3228))
- Fixed: Twitch plugin error when stream metadata API response is empty ([#3223](https://github.com/streamlink/streamlink/pull/3223))
- Fixed: Zattoo login issues ([#3202](https://github.com/streamlink/streamlink/pull/3202))
- Changed: plugin request and submission guidelines ([#3244](https://github.com/streamlink/streamlink/pull/3244))
- Changed: refactored and cleaned up Twitch plugin ([#3227](https://github.com/streamlink/streamlink/pull/3227))
- Removed: `platform=_` stream token request parameter from Twitch plugin (again) ([#3220](https://github.com/streamlink/streamlink/pull/3220))
- Removed: plugins for itvplayer, aljazeeraen, srgssr and dingittv


```text
Alexis Murzeau <amubtdx@gmail.com> (1):
      docs: use recommonmark as an extension

Billy2011 <kschmidt2007@googlemail.com> (3):
      plugins.zattoo: use hello api v2 for zattoo.com (#3202)
      plugins.dlive: rewrite plugin (#3239)
      utils.l10n: use DEFAULT_LANGUAGE_CODE if locale lookup fails (#3055)

Forrest <gravyboat@users.noreply.github.com> (1):
      plugins.itvplayer: remove due to DRM (#2934)

Ian Cameron <1661072+mkbloke@users.noreply.github.com> (8):
      plugins.mico: new plugin for http://www.micous.com/ (#3188)
      plugins.cdnbg: update url_re, plugin test, plugin matrix (#3205)
      plugins.tv999: new plugin for http://tv999.bg/live.html (#3199)
      plugins.aljazeeraen: plugin removal (#3207)
      plugins.srgssr: plugin removal
      plugins.tv3cat: update URL match, test and plugin matrix
      chore: update issue templates (#3250)
      docs: add plugin addition/removal infos (#3249)

Sebastian Meyer <mail@bastimeyer.de> (2):
      Improve coverage reports on codecov (#3200)
      plugins.twitch: remove platform access token param (#3220)

back-to <backto@protonmail.ch> (4):
      plugin.api.useragents: update User-Agent
      plugins.livestream: remove AkamaiHDStream, use only secure HLSStream (#3243)
      plugins.dingittv: removed, website is unmaintained
      plugins: mark some plugins as broken (#3262)

bastimeyer <mail@bastimeyer.de> (21):
      ci.coverage: increase threshold of tests status
      tests: add stream_hls mixin for testing HLSStreams
      stream.hls_filtered: refactor tests, use mixin
      plugins.twitch: refactor tests, use mixin
      stream.hls: refactor reload time tests, use mixin
      stream.hls: separate variant playlist tests
      stream.hls: separate default and encrypted tests
      stream.hls_playlist: implement EXT-X-DATERANGE tag
      plugins.twitch: filter ads by EXT-X-DATERANGE tag
      plugins.twitch: fix metadata API response handling
      ci: add python 3.9 test runners
      tests: fix early writer close in stream_hls mixin
      stream.segmented: gracefully shut down thread pool
      plugins.twitch: remove video-type distinction
      plugins.twitch: refactor Twitch API related code
      plugins.twitch: refactor _get_hls_streams
      plugins.twitch: remove stream weights and clean up
      docs: fix working tree check in deploy script
      docs: update plugin guidelines
      docs: add developing menu with basic setup steps
      docs: add generic pull request template

beardypig <beardypig@protonmail.com> (3):
      plugins.cbsnews: support for live streams from CBS News (#3251)
      plugins.artetv: only pick the first variant of the stream (#3228)
      cli: make config based args available during early setup (#3255)
```


## streamlink 1.6.0 (2020-09-22)

Release highlights:

- Fixed: lots of broken plugins and minor plugin issues (see changelog down below)
- Fixed: embedded ads on Twitch with an ads workaround, removing pre-roll and mid-stream ads ([#3173](https://github.com/streamlink/streamlink/pull/3173))
- Fixed: read timeout error when filtering out HLS segments ([#3187](https://github.com/streamlink/streamlink/pull/3187))
- Fixed: twitch plugin logging incorrect low-latency status when pre-roll ads exist ([#3169](https://github.com/streamlink/streamlink/pull/3169))
- Fixed: crunchyroll auth logic ([#3150](https://github.com/streamlink/streamlink/pull/3150))
- Added: the `--hls-playlist-reload-time` parameter for customizing HLS playlist reload times ([#2925](https://github.com/streamlink/streamlink/pull/2925))
- Added: `python -m streamlink` invocation style support ([#3174](https://github.com/streamlink/streamlink/pull/3174))
- Added: plugin for mrt.com.mk ([#3097](https://github.com/streamlink/streamlink/pull/3097))
- Changed: yupptv plugin and replaced email+pass with id+token authentication ([#3116](https://github.com/streamlink/streamlink/pull/3116))
- Removed: plugins for vaughnlive, pandatv, douyutv, cybergame, europaplus and startv


```text
Ian Cameron <1661072+mkbloke@users.noreply.github.com> (11):
      docs: update turkuvaz plugin matrix entry (#3114)
      docs: Add reuters.com for reuters plugin entry in plugin matrix (#3124)
      Fix formatting for reuters plugin entry
      plugins.huomao: fix/rewrite (#3126)
      plugins.drdk: fix livestreams (#3115)
      plugins.tvplayer: update regex and tests for /uk/ URLs
      plugins.tv360: fix HLS URL regex and plugin (#3185)
      plugins: fix unescaped literal dots in url_re entries (#3192)
      plugins.svtplay: rewrite/fix (#3155)
      plugins.yupptv: fix/minor rewrite (#3116)
      plugins.ine: fix unescaped literal dots in js_re (#3196)

Il Harper <afanyiyu@hotmail.com> (2):
      Add OBS-Streamlink into thirdparty.rst
      Apply suggestions from code review

PleasantMachine9 <65126927+PleasantMachine9@users.noreply.github.com> (1):
      support `python -m` cli invocation

Sebastian Meyer <mail@bastimeyer.de> (4):
      plugins.bloomberg: fix regex module anchor (#3131)
      plugins.sportschau: rewrite and fix plugin (#3142)
      plugins.raiplay: rewrite and fix plugin (#3147)
      plugins.twitch: refactor worker, parser and tests (#3169)

Tr4sK <tr4sk+github@biboum.fr> (1):
      plugins.mrtmk: new plugin for http://play.mrt.com.mk/ (#3097)

Yahya <5457202+anakaiti@users.noreply.github.com> (1):
      docs: update reference to minimum VLC version

back-to <backto@protonmail.ch> (9):
      plugins.vaughnlive: removed
      plugins.pandatv: removed
      plugins.douyutv: removed
      plugins.tv8: fix plugin with new api
      plugins.cybergame: removed
      plugins.europaplus: remove plugin
      plugins.vk: remove '\' from data
      plugins.nicolive: fix quality
      plugins.wasd: fixed plugin (#3139)

bastimeyer <mail@bastimeyer.de> (8):
      stream.hls: customizable playlist reload times
      plugins.twitch: platform=_ in access_token request
      docs: fix NixOS link
      docs: replace easy_install macOS entry with pip
      docs: add comment regarding pip/pip3 differences
      stream.hls_filtered: implement FilteredHLSStream
      plugins.twitch: use FilteredHLS{Writer,Reader}
      stream.hls_filtered: fix tests

beardypig <beardypig@protonmail.com> (1):
      plugins.crunchyroll: update auth logic

derFogel <derFogel@users.noreply.github.com> (1):
      plugins.zattoo: fix quantum tv streaming (#3108)

hymer-up <34783904+hymer-up@users.noreply.github.com> (2):
      plugins.startv: remove plugin (#3163)
      plugins.dogus: add startv URL (#3161)
```


## streamlink 1.5.0 (2020-07-07)

A minor release with fixes for `pycountry==20.7.3` ([#3057](https://github.com/streamlink/streamlink/pull/3057)) and a few plugin additions and removals.

And of course the usual plugin fixes and upgrades, which you can see in the git shortlog down below. Thank you to everyone involved!

Support for Python2 has not been dropped yet (contrary to the comment in the last changelog), but will be in the near future.


```text
Alexis Murzeau <amubtdx@gmail.com> (1):
      docs: update debian install instructions

Billy2011 <kschmidt2007@googlemail.com> (8):
      plugins.nbcsports: fix embed_url_re (#2980)
      plugins.olympicchannel: fix/rewrite (#2981)
      plugins.foxtr: fix playervars_re (#3013)
      plugins.huya: fix _hls_re (#3007)
      plugins.ceskatelevize: add new api for some links (#2991)
      plugins.beattv: remove plugin (#3053)
      plugins.ard_live: fix / rewrite (#3052)
      plugins.ard_mediathek: fix / update (#3049)

Code <60588434+superusercode@users.noreply.github.com> (1):
      Streamlink was added to Windows Package Manager

Ian Cameron <1661072+mkbloke@users.noreply.github.com> (6):
      plugins.tvplayer: Add missing platform key in the GET for stream_url (#2989)
      plugins.btv: remove login and fix API URL (#3019)
      plugins.n13tv: new plugin - replaces plugins.reshet (#3034)
      plugins.reshet: plugin removal (#3000)
      plugins.tvnbg: plugin removal (#3056)
      plugins.adultswim: fix/rewrite (#2952)

Sebastian Meyer <mail@bastimeyer.de> (3):
      ci: no test/documentation jobs on scheduled run (#3012)
      cli.main: fix msecs format in logging output (#3025)
      utils.l10n: fix pycountry language lookup (#3057)

Vladimir Stavrinov <9163352+vstavrinov@users.noreply.github.com> (1):
      plugins.nbcnews: new plugin for http://nbcnews.com/now (#2927)

back-to <backto@protonmail.ch> (11):
      plugins.showroom: use normal HLSStreams
      docs: remove unimportant note / file
      plugins.viasat: remove play.nova.bg domain
      actions: fixed incorrect versions and use names for codecov (#2932)
      plugins.filmon: use /tv/ url and raise PluginError for invalid channels
      flake8: E741 ambiguous variable name
      plugins.youtube: Fix isLive and signatureCipher (#3026)
      plugins.facebook: use meta og:video:url and added basic title support (#3024)
      plugins.picarto: fixed vod url detection
      ci: fix pycountry issue temporarily with a fixed version
      plugin.api.useragents: update User-Agent

bastimeyer <mail@bastimeyer.de> (3):
      docs/install: fix Windows package manager
      plugins.mixer: remove plugin
      ci: run scheduled tests, ignore coverage report

beardypig <beardypig@protonmail.com> (1):
      plugins.cdnbg: update plugin to support new sites, and remove old sites (#2912)

lanroth <github.com@lanroth.com> (1):
      plugins.radionet: fix plugin so it works with new page format (#3018)

resloved <bfriesen95@gmail.com> (1):
      fixed typo

steven7851 <steven7851@msn.com> (1):
      plugins.app17: update API (#2969)

tnira <tnira@users.noreply.github.com> (1):
      Plugin.nicolive:resolve API format change (#3061)

unavailable <51099894+EnterGin@users.noreply.github.com> (1):
      plugins.twitch: fix call_subdomain (#2958)

wiresp33d <66558220+wiresp33d@users.noreply.github.com> (2):
      plugins.bigo: use API for video URL (#3016)
      plugins.nicolive: resolve new api format (#3039)
```


## streamlink 1.4.1 (2020-04-24)

No code changes. [See the full `1.4.0` changelog here.](https://github.com/streamlink/streamlink/releases/tag/1.4.0)


```text
beardypig <beardypig@protonmail.com> (1):
      build: include correct signing key: 0xE3DB9E282E390FA0
```


## streamlink 1.4.0 (2020-04-22)

This will be the last release with support for Python 2, as it has finally reached its EOL at the beginning of this year.

Streamlink 1.4.0 comes with lots of plugin fixes/improvements, as well as some new features and plugins, and also a few plugin removals.

Notable changes:

- New: low latency streaming on Twitch via `--twitch-low-latency` ([#2513](https://github.com/streamlink/streamlink/pull/2513))
- New: output HLS segment data immediately via `--hls-segment-stream-data` ([#2513](https://github.com/streamlink/streamlink/pull/2513))
- New: always show download progress via `--force-progress` ([#2438](https://github.com/streamlink/streamlink/pull/2438))
- New: URL template support for `--hls-segment-key-uri` ([#2821](https://github.com/streamlink/streamlink/pull/2821))
- Removed: Twitch auth logic, `--twitch-oauth-token`, `--twitch-oauth-authenticate`, `--twitch-cookie` ([#2846](https://github.com/streamlink/streamlink/pull/2846))
- Fixed: Youtube plugin ([#2858](https://github.com/streamlink/streamlink/pull/2858))
- Fixed: Crunchyroll plugin ([#2788](https://github.com/streamlink/streamlink/pull/2788))
- Fixed: Pixiv plugin ([#2840](https://github.com/streamlink/streamlink/pull/2840))
- Fixed: TVplayer plugin ([#2802](https://github.com/streamlink/streamlink/pull/2802))
- Fixed: Zattoo plugin ([#2887](https://github.com/streamlink/streamlink/pull/2887))
- Changed: set Firefox User-Agent HTTP header by default ([#2795](https://github.com/streamlink/streamlink/pull/2795))
- Changed: upgraded bundled FFmpeg to `4.2.2` in Windows installer ([#2916](https://github.com/streamlink/streamlink/pull/2916))


```text
Adam Baxter <github@voltagex.org> (1):
      stream.hls_playlist: Add extra logging for invalid #EXTM3U line (#2479)

Alexis Murzeau <amubtdx@gmail.com> (1):
      docs: fix duplicate object description of streamlink in api docs

Colas Broux <colas.broux@free.fr> (2):
      plugins.youtube: Fix for new Youtube VOD API (#2858)
      Updating README Applying changes from 1402fb0 to the README Closes #2880

Finn <finn@finn.io> (1):
      plugins.invintus: Add support for Invintus Media live streams and VOD (#2845)

Ian Cameron <1661072+mkbloke@users.noreply.github.com> (3):
      Fix tvplayer plugin and tests (#2802)
      plugins.piczel: Added HLS, Removed RTMP (#2815)
      plugins.reuters: fix (#2811)

Mohamed El Morabity <melmorabity@users.noreply.github.com> (1):
      plugins.tf1: use new API to retrieve DASH streams (#2759)

Riolu <16816842+iucario@users.noreply.github.com> (1):
      plugins.radiko: Add support for radiko.jp (#2826)

Uinden <25625733+Uinden@users.noreply.github.com> (1):
      plugins.wasd: new plugin for WASD.TV (#2641)

YYY <yyy3752@gmail.com> (1):
      plugins.nicolive: new plugin for Niconico Live (#2651)

Yavuz Kömeçoğlu <komecoglu.yavuz@gmail.com> (1):
      plugins.galatasaraytv: Add support for GALATASARAY SK TV (#2760)

Zhenyu Hu <andyhuzhill@users.noreply.github.com> (1):
      plugins.kugou:  Add Kugou Fanxing live plugin (#2794)

back-to <backto@protonmail.ch> (17):
      plugin.api: use Firefox as default User-Agent instead of python-requests
      plugins.filmon: retry for 50X errors
      cli: New command --force-progress (#2438)
      travis-ci: don't run doctr on pull requests
      plugins.bilibili: ignore unavailable URLs (#2818)
      plugins.mlgtv: remove plugin they use DRM for Livestreams (#2829)
      plugins.twitch: Fixed clips (#2843)
      plugins.showroom: Fix HLS missing segments
      plugins.kanal7: Removed Plugin they use static URLs
      plugins.rotana: new plugin for rotana.net (#2838)
      plugins.pixiv: removed not working login process via username (#2840)
      plugins.abema: support for Abema overseas version
      plugins.younow: remove plugin
      plugin.api.useragents: update User-Agent
      plugins.zattoo: fix app token and new recording URL
      plugins.zeenews: new plugin for https://zeenews.india.com/live-tv
      AUTHORS: removed unused script and removed outdated list (#2889)

bastimeyer <mail@bastimeyer.de> (58):
      plugins.twitch: fix rerun validation schema
      flake8: E303
      flake8: E111
      flake8: E117
      flake8: E121
      flake8: E122
      flake8: E126, E127, E128
      flake8: E203, E226, E231, E241, E261
      flake8: E265
      flake8: E302, E305
      flake8: E402
      flake8: E712
      flake8: W291, W292, W293, W391
      flake8: F401, F403
      flake8: F405
      flake8: F811
      flake8: F841
      flake8: W504
      flake8: E741
      flake8: E501
      flake8: F601
      flake8: E722
      flake8: F821
      flake8: F812
      flake8: add flake8 to TravisCI
      cleanup: remove unnecessary unittest.main() calls
      cleanup: remove unnecessary python shebangs
      PEP263: use consistent utf-8 coding header comment
      tools: add .editorconfig
      stream.hls: add hls-segment-stream-data parameter
      plugins.twitch: low latency
      plugins.twitch: disable LL when filtering ads
      plugins.twitch: print info msg if stream is not LL
      plugins.bloomberg: fix vods and live streams
      plugins.twitch: remove cookie auth
      plugins.twitch: remove oauth token login
      docs: fix multiple options on the same line
      ci.github: implement main workflow
      ci.github: add release config and rewrite scripts
      ci.github: add scheduled nightly builds
      ci.github: deploy documentation
      ci: show extra test summary info
      ci: remove old CI configs
      ci.github: fix codecov uploads
      cleanup: change build badge and link in README.md
      cleanup: remove TravisCI from deploy scripts
      ci: remove macOS test runners
      codecov: wait before notifying
      docs: rewrite windows nightly builds section
      docs: rewrite pip/source install section
      docs: fix and rewrite index page
      docs: reformat donation page
      ci.github: fix continue on error
      installer: rewrite / clean up makeinstaller script
      installer: download ffmpeg+rtmpdump assets
      installer: delete locally included binary files
      plugins.twitch: rewrite disable ads logic
      Release 1.4.0

beardypig <beardypig@protonmail.com> (10):
      update release signing key
      update docs deployment key
      plugins.tv360: updated URL and HLS stream extraction method
      util: fix some encoding issue when setting unicode/utf8 titles in py2
      cli.output: make sure the player arguments are properly encoded
      utils: update_qsd to leave blank values unchanged (#2869)
      plugins.eurocom: remove eurocom plugin
      plugins.tv1channel: remove tv1channel plugin
      actions: no need to use a secret for the PyPI username
      add python 2.7 deprecation warning

danieljpiazza <daniel.joseph.piazza@gmail.com> (1):
      Update Crunchyroll access token. Fixes streamlink/streamlink issue #2785.

malvinas2 <malvinas2@gmx.de> (3):
      plugins.latina: new plugin for https://www.latina.pe/tvenvivo (#2793)
      plugins.albavision: Added support for ATV and ATVMas (#2801)
      plugins.rtve: Added support for clan tve, children's channel of RTVE (#2875)

steven7851 <steven7851@msn.com> (1):
      plugins.app17: fix for new layout (#2833)

tarkah <cforsstrom18@gmail.com> (1):
      stream.hls: add templating for hls-segment-key-uri option (#2821)
```


## streamlink 1.3.1 (2020-01-27)

A small patch release that addresses the removal of [MPV's legacy option syntax](https://mpv.io/manual/master/#legacy-option-syntax), also with fixes of several plugins, the addition of the `--twitch-disable-reruns` parameter and dropped support for Python 3.4.


```text
Hunter Peavey <krathalan@disroot.org> (4):
      Add wtwitch to list of thirdparty programs
      Try adding an image
      Move image position
      Make requested changes

Vladimir Stavrinov <9163352+vstavrinov@users.noreply.github.com> (1):
      plugins.nhkworld: the site migrates from xml to json stream data

back-to <backto@protonmail.ch> (6):
      docs/tests: remove python 3.4, use 3.8 and nightly for travis-ci
      plugins.bilibili: fix Livestreams with status 1 (set Referer)
      plugins.youtube: Remove itag 303
      plugins.ustream: Added support for video.ibm.com
      plugins.bbciplayer: Fixed login params
      plugins.bbciplayer: remove test_extract_nonce

bastimeyer <mail@bastimeyer.de> (5):
      plugins.twitch: use python logging module
      plugins.twitch: fix rerun detection
      cli.output: fix mpv player parameter format
      2020
      docs: fix MPV parameters on common issues page

skulblakka <pascal.romahn@mailbox.org> (1):
      Allow to disable twitch reruns (#2722)
```


## streamlink 1.3.0 (2019-11-22)

A new release with plugin updates and fixes, including Twitch.tv (see [#2680](https://github.com/streamlink/streamlink/issues/2680)), which had to be delayed due to back and forth API changes.

The Twitch.tv workarounds mentioned in [#2680](https://github.com/streamlink/streamlink/issues/2680) don't have to be applied anymore, but authenticating via `--twitch-oauth-token` has been disabled, regardless of the origin of the OAuth token (via `--twitch-oauth-authenticate` or the Twitch website). In order to not introduce breaking changes, both parameters have been kept in this release and the user name will still be logged when using an OAuth token, but receiving item drops or accessing restricted streams is not possible anymore.

Plugins for the following sites have also been added:
  - albavision
  - news.now.com
  - twitcasting.tv
  - viu.tv
  - vlive.tv
  - willax.tv


```text
Alexis Murzeau <amubtdx@gmail.com> (1):
      plugins.pixiv: fix doc typo thats -> that's

Mohamed El Morabity <melmorabity@fedoraproject.org> (1):
      plugins.idf1: HTTPS support

Mohamed El Morabity <melmorabity@users.noreply.github.com> (1):
      plugins.playtv: Fix for new stream data API (#2388)

Ozan Karaali <ozan.karaali@gmail.com> (1):
      plugins.foxtr: Extended support

Ozan Karaali <ozankaraali@users.noreply.github.com> (1):
      plugins.cinergroup: #2390 fix (#2629)

Troogle <Troogle@users.noreply.github.com> (1):
      plugins.bilibili: fix resolution issue

Werner Robitza <werner.robitza@gmail.com> (1):
      remove direct installation instructions, link to docs

back-to <backto@protonmail.ch> (6):
      setup.cfg: added flake8 settings
      plugins.vk: use html_unescape for HLS streams
      plugins.willax: new plugin for http://willax.tv/en-vivo/
      plugins.zattoo: _url_re update for some new urls
      plugin.api.useragents: update CHROME and FIREFOX User-Agent
      stream.hls: Fix UnicodeDecodeError for log msg and name_prefix for stream_name

bastimeyer <mail@bastimeyer.de> (3):
      ci/travis: install pynsist 2.4
      plugins.twitch: fix API issue - 410 gone error
      docs.cli: fix and reword the tutorial section

beardypig <beardypig@protonmail.com> (10):
      plugins.bbciplayer: update API URL to use https
      plugins.nownews: added support for the HK news site news.now.com
      plugins.tv8: update regex for the stream url
      plugins.bbciplayer: fix issue with nonce extraction
      plugins.bbciplayer: extract master brand/channel id from the state json
      plugins.itvplayer: Use flash streams for ITV1/ITV4
      plugins.viutv: support for the viu.tv live stream
      plugins.albavision: support for some albavision live streams
      plugins.bloomberg: fix issue where the incorrect playlist could be used
      stream.streamprocess: check that a process is usable before using it

derrod <xlnedder@gmail.com> (1):
      plugins.vlive: Add support for V LIVE live streams

printempw <printempw@gmail.com> (1):
      plugins.twitcasting: new plugin for TwitCasting.tv

ssaqua <ssaqua@users.noreply.github.com> (1):
      plugins.linelive: update to support VOD/archived streams
```


## streamlink 1.2.0 (2019-08-18)

Here are the changes for this month's release

- Multiple plugin fixes
- Fixed single hyphen params at the beginning of --player-args (#2333)
- `--http-proxy` will set the default value of `--https-proxy` to same as `--http-proxy`. (#2536)
- DASH Streams will handle headers correctly (#2545)
- the timestamp for FFMPEGMuxer streams will start with zero (#2559)


```text
Davi Guimarães <davi.guimaraesleite@gmail.com> (1):
      plugins.cubetv: base url changes (#2430)

Forrest <gravyboat@users.noreply.github.com> (1):
      Add a sponsor button (#2478)

Jiting <jiting@jtcat.com> (1):
      plugin.youtube: bug fix for YouTube live streams check

Juan Ramirez <jramirez@encompass.tv> (2):
      Invalid use of console.logger in CLI
      Too many arguments for logging format string

Mohamed El Morabity <melmorabity@fedoraproject.org> (9):
      plugins.vimeo: new plugin for Vimeo streams
      plugins.vimeo: add subtitle support for vimeo plugin
      plugins.vimeo: fix alphabetical order in plugin matrix
      Use class parameter instead of class name in class method
      [plugins.bfmtv] Fix player regex
      [plugins.idf1] Update for new website layout
      plugins.gulli: enable HTTPS support
      plugins.gulli: fix live stream fetching
      plugins.tvrplus: fix for new website layout

Mohamed El Morabity <melmorabity@users.noreply.github.com> (1):
      plugins.clubbingtv: new plugin for Clubbing TV website (#2569)

Viktor Kálmán <kviktor@users.noreply.github.com> (1):
      plugins.mediaklikk: update broken plugin (#2401)

Vladimir Stavrinov <vstavrinov@gmail.com> (2):
      plugins.live_russia_tv: adjust to site changes (#2523)
      plugins.oneplusone: fix site changes (#2425)

YuuichiMizuoka <32476209+YuuichiMizuoka@users.noreply.github.com> (1):
      add login posibility for pixiv using sessionid and devicetoken

aqxa1 <asheldon55@gmail.com> (1):
      Handle keyboard interrupts in can_handle_url checks (#2318)

back-to <backto@protonmail.ch> (12):
      cli.argparser: Fix single hyphen params at the beginning of --player-args
      plugins.reuters: New Plugin
      plugins: Removed rte and tvcatchup
      utils.__init__: remove cElementTree, it's just an alias for ElementTree
      plugins.teamliquid: New domain, fix stream_weight
      plugins.vimeo: Fixed DASH Livestreams
      plugin.api.useragents: update CHROME and FIREFOX User-Agent
      ffmpegmux: use -start_at_zero with -copyts
      plugins.youtube: fixed reason msg, updated _url_re
      plugins.TV1Channel: Fixed new livestream iframe
      plugins.npo: removed due to DRM
      plugins.lrt: fixed livestreams

bastimeyer <mail@bastimeyer.de> (1):
      plugins.welt: fix plugin

beardypig <beardypig@protonmail.com> (13):
      plugins.bbciplayer: small change to where the VPID is extracted from (#2376)
      plugins.goodgame: fix for debug logging error
      plugins.cdnbg: fix for bstv url
      plugins.ustvnow: updated to handle new auth, and site design
      plugin.schoolism: bug fix for videos with subtitles (#2524)
      stream.dash: use the stream args in the writer and worker
      session: default https-proxy to the same as http-proxy, can be overridden
      plugins.beattv: partial fix for the be-at.tv streams
      tests: test the behaviour of setting http-proxy and https-proxy
      plugins.twitch: support for different clips URL
      plugins.wwenetwork: support for new site
      plugins.ustreamtv: add support for proxying WebSocket connections
      plugins.wwenetwork: update for small page/api change

skulblakka <pascal.romahn@mailbox.org> (1):
      plugins.DLive: New Plugin for dlive.tv (#2419)

ssaqua <ssaqua@users.noreply.github.com> (1):
      plugins.linelive: new plugin for LINE LIVE (live.line.me) (#2574)
```


## streamlink 1.1.1 (2019-04-02)

This is just a small patch release which fixes a build/deploy issue with the new special wheels for Windows on PyPI. (#2392)

[Please see the full changelog of the `1.1.0` release!](https://github.com/streamlink/streamlink/releases/tag/1.1.0)


```text
Forrest <gravyboat@users.noreply.github.com> (1):
      build: remove cygwin from wheels for Windows (#2393)
```


## streamlink 1.1.0 (2019-03-31)

These are the highlights of Streamlink's first minor release after the 1.0.0 milestone:

- several plugin fixes, improvements and new plugin implementations
- addition of the `--twitch-disable-ads` parameter for filtering out advertisement segments from Twitch.tv streams (#2372)
- DASH stream improvements (#2285)
- documentation enhancements (#2292, #2293)
- addition of the `{url}` player title variable (#2232)
- default player title config for PotPlayer (#2224)
- new `streamlinkw` executable on Windows (wheels + installer) (#2326)
- Github release assets simplification (#2360)


```text
Brian Callahan <bcallah@openbsd.org> (1):
      Add OpenBSD to the installation docs

Peter Rowlands (변기호) <peter@pmrowla.com> (2):
      streams.dash: Support manifest strings in addition to manifest urls (#2285)
      plugins.facebook: Support manifest strings and tahoe player urls (#2286)

Roman Kornev <w.romankornev@gmail.com> (2):
      cli.main: Add {url} argument to window --title (#2232)
      cli.output: Add window title for PotPlayer (#2224)

Sebastian Meyer <mail@bastimeyer.de> (1):
      Build additional "streamlinkw" launcher on Windows (#2326)

Steve Oswald <30654895+SteveOswald@users.noreply.github.com> (1):
      plugins.zattoo: Added support for www.1und1.tv (#2274)

Vladimir Stavrinov <vstavrinov@gmail.com> (2):
      plugins.ntv: new Plugin for ntv.ru (#2351)
      plugins.live_russia_tv: fix iframe format differences (#2375)

back-to <backto@protonmail.ch> (13):
      plugins.atresplayer: Fixed HLSStream
      plugins.streamme: Fixed source quality, added title and author
      plugins.atresplayer: update for new api schema
      plugins.mitele: plugin update
      plugins.ustreamtv: handle stream names better, allow '_alt' streams (#2267)
      plugins.rtve: Fixed content_id search (#2300)
      plugins.streamme: Fixed null error for 'origin'
      tests: detect unsupported versions for itertags
      plugins.pluzz: Fixed Video ID and logging update
      plugins.pluzz: Fixed regex, they use quotes now.
      plugins.cdnbg: New domain videochanel.bstv.bg
      plugins.tf1: Fixed python2.7 ascii error
      plugins.okru: Fixed Plugin (#2374)
      plugins.rtpplay: fix _m3u8_re and plugin cleanup

bastimeyer <mail@bastimeyer.de> (13):
      docs/install: git+makepkg instead of AUR helper
      docs/install: rewrite source code and pip section
      docs/install: shell code blocks, remove prompts
      docs/install: simplify pip user/system table
      docs/install: rewrite virtual env section
      docs/install: move Windows and macOS to the top
      Add force_verify=true to Twitch OAuth URL
      plugins.twitch: platform=_ in access_token request
      TravisCI: don't publish wheels on Github releases
      stream.hls: refactor M3U8Parser
      stream.hls: refactor HLSStream{,Worker}
      plugins.twitch: implement disable-ads parameter
      Release 1.1.0

beardypig <beardypig@protonmail.com> (2):
      plugins.dogus: support for YouTube embedded streams
      plugins.bbciplayer: do not try to authenticate when not required

lon <rliouke@gmail.com> (1):
      plugins.crunchyroll: Allow CR's multilingual URLs to be handled (#2304)
```


## streamlink 1.0.0 (2019-01-30)

The celebratory release of Streamlink 1.0.0!

*A lot* of hard work has gone into getting Streamlink to where it is. Not only is Streamlink used across multiple applications and platforms, but companies as well. 

Streamlink started from the inaugural [fork of Livestreamer](https://github.com/chrippa/livestreamer/issues/1427) on September 17th, 2016. 

Since then, We've hit multiple milestones:

 - Over 886 PRs
 - Hit 3,000 commits in Streamlink
 - Obtaining our first sponsors as well as backers of the project
 - The creation of our own logo (https://github.com/streamlink/streamlink/issues/1123)

Thanks to everyone who has contributed to Streamlink (and our backers)! Without you, we wouldn't be where we are today.

**Without further ado, here are the changes in release 1.0.0:**

  - We have a new icon / logo for Streamlink! (https://github.com/streamlink/streamlink/pull/2165)
  - Updated dependencies (https://github.com/streamlink/streamlink/pull/2230)
  - A *ton* of plugin updates. Have a look at [this search query](https://github.com/streamlink/streamlink/pulls?utf8=%E2%9C%93&q=is%3Apr+is%3Aclosed+plugins.+) for all the recent updates.
  - You can now provide a custom key URI to override HLS streams (https://github.com/streamlink/streamlink/pull/2139). For example: `--hls-segment-key-uri <URI>`
  - User agents for API communication have been updated (https://github.com/streamlink/streamlink/pull/2194)
  - Special synonyms have been added to sort "best" and "worst" streams (https://github.com/streamlink/streamlink/pull/2127). For example: `streamlink --stream-sorting-excludes '>=480p' URL best,best-unfiltered`
  - Process output will no longer show if tty is unavailable (https://github.com/streamlink/streamlink/pull/2090)
  - We've removed BountySource in favour of our OpenCollective page. If you have any features you'd like to request, please open up an issue with the request and possibly consider backing us!
  - Improved terminal progress display for wide characters (https://github.com/streamlink/streamlink/pull/2032)
  - Fixed a bug with dynamic playlists on playback (https://github.com/streamlink/streamlink/pull/2096)
  - Fixed makeinstaller.sh (https://github.com/streamlink/streamlink/pull/2098)
  - Old Livestreamer deprecations and API references were removed (https://github.com/streamlink/streamlink/pull/1987)
  - Dependencies have been updated for Python (https://github.com/streamlink/streamlink/pull/1975)
  - Newer and more common User-Agents are now used (https://github.com/streamlink/streamlink/pull/1974)
  - DASH stream bitrates now round-up to the nearest 10, 100, 1000, etc. (https://github.com/streamlink/streamlink/pull/1995)
  - Updated documentation on issue templates (https://github.com/streamlink/streamlink/pull/1996)
  - URL have been added for better processing of HTML tags (https://github.com/streamlink/streamlink/pull/1675)
  - Fixed sort and prog issue (https://github.com/streamlink/streamlink/pull/1964)
  - Reformatted issue templates (https://github.com/streamlink/streamlink/pull/1966)
  - Fixed crashing bug with player-continuous-http option (https://github.com/streamlink/streamlink/pull/2234)
  - Make sure all dev dependencies (https://github.com/streamlink/streamlink/pull/2235)
  - -r parameter has been replaced for --rtmp-rtmpdump (https://github.com/streamlink/streamlink/pull/2152)

**Breaking changes:**

  - A large number of unmaintained or NSFW plugins have been removed. You can find the PR that implemented that change here: https://github.com/streamlink/streamlink/pull/2003 . See our [CONTRIBUTING.md](https://github.com/streamlink/streamlink/blob/130489c6f5ad15488cd4ff7a25c74bf070f163ec/CONTRIBUTING.md) documentation for plugin policy.



```text
Billy2011 <kschmidt2007@googlemail.com> (3):
      streamlink.plugins: replace global http session by self.session.http (#1925)
      stream.hls_playlist: fix some regex pattern & code optimization (#1918)
      plugins.filmon: fix NoPluginError, if channel is not an ID (#2005)

David Bell <me@geordish.org> (1):
      Update ine.py (#2171)

Forrest <forrest.alvarez@protonmail.com> (2):
      Remove bountysource from donation page, update flattr
      Add a note about specifying the full player path

Forrest <gravyboat@users.noreply.github.com> (2):
      Feature/plugin request policy update (#1838)
      Add icon, modify installer, update docs (#2165)

Hubcapp <walnut.alligator@gmail.com> (1):
      Window Titles = Stream Titles + Other Attributes (#1576)

Jani Ollikainen <bestis@cd.purkki.org> (1):
      Added support for viafree.fi

Lukas <keydon@gmail.com> (1):
      plugins.zdf_mediathek: use ptmd-template api path (#2233)

Maxwell Cody <maxwellcody@riseup.net> (1):
      Add ability to specify custom key URI override for HLS streams (#2139)

Mohamed El Morabity <melmorabity@users.noreply.github.com> (1):
      plugins.pluzz: fixes and francetvinfo.fr support (#2119)

Nick Gal <nickgal@me.com> (1):
      Update steam plugin to work with steam.tv urls

Petar Kukolj <petarkukolj3@yahoo.com> (5):
      plugins.cubetv: support for live streams on cubetv.sg
      plugins.ok_live: Changed URL regex to support VoDs
      plugins.bilibili: Fix plugin after API change
      plugins.twitch: Add support for {title}, {author} and {category}
      plugins.skai: Fix plugin after site update

Roman <w.romankornev@gmail.com> (2):
      [FIX] Debug log arguments string
      [FIX] Debug log arguments cross-platform

Roman Kornev <w.romankornev@gmail.com> (1):
      [FIX] Message duplicate

Sebastian Meyer <mail@bastimeyer.de> (1):
      Reword+reformat issue templates for consistency (#1966)

Stefan de Konink <stefan@konink.de> (1):
      Update the documentation with comments for playing YouTube Live Streams (#2156)

Søren Fuglede Jørgensen <s@fuglede.dk> (1):
      Update and reactivate plugin for dr.dk

Twilight0 <twilight@freemail.gr> (1):
      plugins.ssh101: Fixed plugin (#1916)

Vincent Rozenberg <vincentrozenberg@gmail.com> (1):
      Update npo.py

Vinny <vincent.aceto@gmail.com> (1):
      docs: Added documentation for the Funimation plugin (#2091)

Visatouch Deeying <xerodotc@gmail.com> (1):
      Fix crash on missing output.record when using player-continous-http

back-to <backto@protonmail.ch> (48):
      plugins.EuropaPlusTV: Fix for "No connection adapters were found"
      utils.args: Moved streamlink_cli utils.args into streamlink package
      tests.plugins: Test that each plugin has a test file (#1885)
      plugins.zattoo: session update and allow muxed hls / dash streams (#1902)
      plugins.tv4play: Fix for updated website
      debug: Added Session Language code as a debug message
      tests: run Python 3.7 tests on AppVeyor and Travis-CI (#1928)
      plugins.rtve: Fixed AttributeError 'ZTNRClient' has no 'session'
      plugins.twitch: Fixed AttributeError and Flake8
      plugins.filmon: Fixed AttributeError
      plugins.crunchyroll: Fixed AttributeError and Flake8
      tests.localization: use en_CA instead of en_US for test_equivalent
      plugins.younow: Fix for session error and plugin cleanup
      plugins.media_ccc_de: removed plugin
      plugins.pixiv: use API for the stream URL and cache login cookies
      plugins.youtube: Added support for {author} and {title} (#1944)
      docs-CLI: Fix for sort and prog issue
      plugins.ceskatelevize: Fix for https issues
      plugins.mjunoon: use a User-Agent
      api.useragents: use newer and more common User-Agent's
      script.makeinstaller: use a more recent version of Python and Pycryptodome
      Removed old Livestreamer deprecations and API references
      plugins.sportal: Removed old RTMP streams, use HLS
      plugins.twitch: new video URL regex
      Removed old or unwanted Streamlink Plugins
      tests: use unittest instead of pytest for itertags error (#1999)
      utils.parse_xml: allow a tab for ignore_ns
      plugins.afreeca: ignore new preloading urls
      plugins.filmon: use the same cdn for a playlist url (#2074)
      plugins.teleclubzoom: New plugin for teleclubzoom.ch
      plugins.oldlivestream: remove plugin, service not available anymore (#2081)
      travis: increase git clone depth
      stream.dash_manifest: Fixed bug for dynamic playlists when parent.id is None
      plugins.ustreamtv: use Desktop instead of Mobile streams (#2082)
      plugins.youtube: Added support for embedded livestream urls
      versioneer: always use 7 characters
      plugins.stv: New Plugin for https://player.stv.tv/live
      plugins.sbscokr: New Plugin for http://play.sbs.co.kr/onair/pc/index.html
      plugins.vtvgo: New plugin for https://vtvgo.vn/
      travis-ci: Fixed Python 3.8 error's
      plugins.cdnbg: Update for extra channels (#2186)
      api.useragents: update User-Agent list
      plugins.afreeca: use Referer for every connection (#2204)
      plugins.trt: Added support for https url, fixed logger error
      plugins.turkuvaz: Added support for channel 'apara'
      plugins.tvrby: Fixed broken plugin.
      plugins.youtube: replace "gaming" with "www" subdomain
      plugins.kanal7: Fixed iframe_re/stream_re, added new domain

bastimeyer <mail@bastimeyer.de> (6):
      Fix bug report template
      Move/rename issue templates
      Update generic issue template
      plugins.euronews: fix live stream API URL scheme
      Fix installer by moving additional files
      feature: {best,worst}-unfiltered stream synonyms

beardypig <beardypig@protonmail.com> (23):
      plugins.live_russia_tv: fix for live streams, and support for VOD
      plugin args: if args are suppressed, ignore them
      plugin.tvtoya: refactor, add tests, plugin docs, etc.
      stream.dash: fix bug where timeline_segments.t can be None
      stream.hls: only include audio/video streams in MuxedHLSStreams
      stream.hls: if the primary video stream has audio then include it
      plugins.facebook: support for videos in posts
      plugins.steam: api requests now require a session id
      test for rounding dash stream bitrate
      stream.dash: make the bitrate name for videos more human friendly
      plugins.schoolism: add support for assignment feedback videos
      plugins.senategov: support for hearing streams on senate.gov
      plugins.stadium: support for live stream on watchstadium.com
      plugins.funimationnow: workaround for #1899, see #2088
      cli: make the HH part of HH:MM:SS options optional
      plugins.bbciplayer: change in the mediator info in the page layout
      plugins.btsports: fix for change in login flow
      plugins.filmon: fix for live tv URLs that start with channel
      plugin.powerapp: support for "tvs" URLs
      setup: update requests to latest version and set urllib3 to match
      CI: make sure all the dev dependencies are up to date
      plugins.tf1: update to support new DASH streams
      plugins.tf1: re-add support for HLS with the new API

beardypig <git@beardypig.com> (7):
      Test coverage increase (#1646)
      Handle unicode log message in Python 2 (#1886)
      Update method for finding YouTube videoIds (#1888)
      stream.dash: prefer audio streams based on the user's locale (#1927)
      plugins.openrectv: update to match site changes and title support (#1968)
      URL builder utils (#1675)
      cli: disable progress output for -o when no tty is available (#2090)

fozzy <fozzy@fozzy.co> (1):
      update regex to support new pattern

fozzy <fozzysec@gmail.com> (1):
      plugins.egame: new plugin for egame.qq.com (#2070)

jackyzy823 <jackyzy823@gmail.com> (2):
      Plugin Request: new plugin for Abema.tv (#1949)
      Improve terminal progress display for  wide characters (#2032)

mp107 <mp107@users.noreply.github.com> (1):
      plugins.ltvlmslv: new Plugin for Latvian live TV channels on ltv.lsm.lv (#1986)

qkolj <qkolj@users.noreply.github.com> (5):
      plugins.tamago: support for live streams on player.tamago.live (#2108)
      plugins.huomao: Fix plugin after website changes (#2134)
      plugins.metube: Add support for live streams and  VoDs on www.metube.id (#2112)
      plugins.tvibo: Add support for livestreams on player.tvibo.com (#2130)
      Fix recording added in #920 (#2152)

remek30 <remek30@users.noreply.github.com> (1):
      plugins.toya: support for tvtoya.pl

skulblakka <pascal.romahn@mailbox.org> (1):
      [picarto.tv] Fix regarding changed URL (#1935)

yoya3312 <40212627+yoya3312@users.noreply.github.com> (1):
      plugins.youtube: use new "hlsManifestUrl" for Livestreams (#2238)
```


## streamlink 0.14.2 (2018-06-28)

Just a few small fixes in this release. 

- Fixed Twitch OAuth request flow (https://github.com/streamlink/streamlink/pull/1856)
- Fix the tv3cat and vk plugins (https://github.com/streamlink/streamlink/pull/1851, https://github.com/streamlink/streamlink/pull/1874)
- VOD supported added to atresplayer plugin (https://github.com/streamlink/streamlink/pull/1852, https://github.com/streamlink/streamlink/pull/1853)
- Removed tv8cati and nineanime plugins (https://github.com/streamlink/streamlink/pull/1860, https://github.com/streamlink/streamlink/pull/1863)
- Added mjunoon.tv plugin (https://github.com/streamlink/streamlink/pull/1857)

```text
NyanKiyoshi <NyanKiyoshi@users.noreply.github.com> (1):
      Fix 404 error on oauth authorize url

back-to <backto@protonmail.ch> (1):
      plugins.vk: _url_re update, allow embedded content, plugin cleanup (#1874)

beardypig <beardypig@protonmail.com> (10):
      plugins.t3cat: update validation rule, refactor plugin a little bit
      plugins.atresplayer: update to support VOD streams
      stream.dash: support for SegmentList streams with ranged segments
      plugins.mjunoon: support for live and vod streams on mjunoon.tv
      release: fix release notes manual install url
      plugins.tv8cat: plugin removed - the live broadcast is no longer available
      plugins.nineanime: no longer supported
      release: set the date of the release for UTC time
      plugin: support stream weights returned by DASHStream.parse_manifest
```


## streamlink 0.14.0 (2018-06-26)

Here are the changes to this months release!

- Multiple plugin fixes
- Bug fixes for DASH streams (https://github.com/streamlink/streamlink/pull/1846)
- Updated API call for api.utils hours_minutes_seconds (https://github.com/streamlink/streamlink/pull/1804)
- Updated documentation (https://github.com/streamlink/streamlink/pull/1826)
- Dict structures fix (https://github.com/streamlink/streamlink/pull/1792)
- Reformated help menu (https://github.com/streamlink/streamlink/pull/1754)
- Logger fix (https://github.com/streamlink/streamlink/pull/1773)

```text
Alexis Murzeau <amubtdx@gmail.com> (3):
      sdist: include tests resources (#1785)
      tests: freezegun: use object instead of lambda (#1787)
      rtlxl: use raw string to fix escape sequences (#1786)

BZHDeveloper <39899575+BZHDeveloper@users.noreply.github.com> (1):
      plugins.cnews : separate CNEWS data from CanalPlus plugin. (#1782)

MasterofJOKers <joker@someserver.de> (1):
      plugins.sportschau: Fix "No schema supplied" error

Mohamed El Morabity <melmorabity@fedoraproject.com> (2):
      plugins.pluzz: support for DASH streams
      plugins.pluzz: fix HDS streams

Mohamed El Morabity <melmorabity@users.noreply.github.com> (1):
      [plugins.rtbf] Fix radio streams + DASH support (#1771)

Sebastian Meyer <mail@bastimeyer.de> (1):
      Move docs version selection to sidebar (#1802)

Twilight0 <twilight@freemail.gr> (2):
      Convert literal comprehensive dicts to dict contructs
      Add arguments to __init__ - super to work on Python 2.7.X (#1796)

back-to <backto@protonmail.ch> (9):
      plugins: marked or removed broken plugins
      plugins.earthcam: Fixed hls_url - No schema supplied.
      plugins.rte: allow https
      plugins.VinhLongTV: New plugin for livestreams of thvli.vn
      docs.thirdparty: Added LiveProxy
      plugins.tlctr: New Plugin for tlctv.com.tr/canli-izle
      plugins.bigo: Fix for new channelnames and plugin cleanup (#1797)
      docs: removed some notes, updated some urls
      utils.times: hours_minutes_seconds update, twitch automate time offset

beardypig <beardypig@protonmail.com> (15):
      help: reformat all the help text so that it is <80 chars
      plugins.bbciplayer: fix bug is DASH for VOD
      sdist and wheel release fixes (#1758)
      plugin.youtube: find video id in page, fall back to API (#1746)
      logging: rename logger for main back to 'cli'
      plugins.vaughnlive: support for the HTML flv player
      plugins.yupptv: support for yupptv with login support
      plugins.nos: update for new page layout for live and VOD
      plugins.lrt: add support for Lithuanian National Television
      plugins.delfi: support for delfi.lt web portal
      plugins.vrtbe: update to new page layout/API
      plugins.itvplayer: update to new HTML5 API
      plugins.atresplayer: support new layout/API
      stream.dash: use the ID and mime-type to identify a representation
      plugins.mitele: sometimes ogn is null, html5 pdata endpoint works better

beardypig <git@beardypig.com> (5):
      plugins.crunchyroll: refactoring and updated API calls (#1820)
      Suppress/fix deprecated warnings for Python 3 (#1833)
      API for plugins to request input from the user (#1827)
      Steam Broadcast Plugin (#1717)
      USTV Now (#1840)

fozzy <fozzy@fozzy.co> (1):
      fix bug caused by indentation and add support for url pattern like 'xingxiu.panda.tv'
```


## streamlink 0.13.0 (2018-06-06)

Massive release this month!

Here are the changes:
 - Initial MPEG DASH support has been added! (https://github.com/streamlink/streamlink/pull/1637) Many thanks to @beardypig
 - As always, a *ton* of plugin updates
 - Updates to our documentation (https://github.com/streamlink/streamlink/pull/1673)
 - Updates to our logging (https://github.com/streamlink/streamlink/pull/1752) as well as log --quiet options (https://github.com/streamlink/streamlink/pull/1744) (https://github.com/streamlink/streamlink/pull/1720)
 - Our release script has been updated (https://github.com/streamlink/streamlink/pull/1711)
 - Support for livestreams when using the `--hls-duration` option (https://github.com/streamlink/streamlink/pull/1710)
 - Allow streamlink to exit faster when using Ctrl+C (https://github.com/streamlink/streamlink/pull/1658)
 - Added an OpenCV Face Detection example (https://github.com/streamlink/streamlink/pull/1689)

```text
BZHDeveloper <inizan.yannick@gmail.com> (1):
      plugins.bfmtv : Update regular expression (#1703)

Billy <kschmidt2007@googlemail.com> (1):
      plugins.ok_live: fix <hlsurl> extraction

Billy2011 <kschmidt2007@googlemail.com> (2):
      stream.dash: fix stuttering streams & maybe high CPU load (#1718)
      stream.akamaihd: fix some log.debug... issues (#1729)

Hsiao-Ting Yu <sst.dreams@gmail.com> (1):
      Add plugin for www.kingkong.com.tw (#1666)

LoneFox78 <lonefox@kapsi.fi> (1):
      plugins.tvcatchup: support for https URLs

back-to <backto@protonmail.ch> (3):
      plugins.chaturbate: only open a stream if the url is not empty
      stream.hls_playlist: removed int check from PROGRAM-ID (#1707)
      docs: PotPlayer Stdin Pipe

beardypig <beardypig@protonmail.com> (30):
      plugins.bbciplayer: enable HD for some channels and speed up start-up
      plugins.goodgame: update for change in page layout
      tests: test to ensure each plugin listed in the plugin matrix exists
      plugins.goodgame: fix bug with streamkey extraction
      plugins.onetv: add support for 1tv.ru and a few other related sites
      plugins.rtve: fix for m3u8 stream url formatting
      example: added an opencv face detection example
      plugins.europaplus: support for the europaplustv stream
      plugins.goltelevision: support for the live stream
      plugins.tvcatchup: add URL tests
      plugin.ustvnow: plugin to support ustvnow.com
      hls: support for live streams when using --hls-duration
      release: update to release script
      win-installer: add missing isodate module
      plugins.onetv: fix issues with ctc channels and add DASH support
      plugins.dailymotion: fix error logging for stream errors
      logging: set the log level once the plugin config files have been loaded
      logging: fixed issue with logging from plugins using logging module
      plugins.onetv: fixed tests
      plugins.reshet: support for reshet.tv live and VOD streams
      dash: fix for manifest reload - should be more reliable
      tests: coverage on src instead of the modules
      plugins.crunchyroll: switch method of obtaining session id
      plugins.facebook: remove debugging code
      plugins: store cookies between sessions (#1724)
      plugins.facebook: sd_src|hd_src can contain non-dash streams
      plugins.funimationnow: login support and bug fixes (#1721)
      logging: do not log when using quiet options (--json, --quiet, etc)
      dash: fix --json for dash streams and allow custom headers (#1748)
      logging: when using the trace level, log the timestamp

beardypig <beardypig@users.noreply.github.com> (21):
      plugins.filmon: more robust channel_id extraction
      build: use versioneer to set the build number (#1413)
      plugins.btsports: add plugin bt sports
      Allow streamlink to exit faster when using Ctrl-C
      plugins.tf1: add lci url to the main tf1 domain (#1660)
      plugins.ine: support for updated site layout
      docs: add a note about socks4 and socks5 vs socks4a and socks5h (#1655)
      plugins.gardenersworld: updated page layout
      plugins.vidio: update to support new layout
      plugins.btsports: add missing plugin matrix entry and tests
      plugins.vidio: py2 vs. py3 unicode fix
      tests: test to ensure that all plugins are listed in the plugin matrix
      build: use _ instead of + in the Windows installer exe filename
      Plugin Arguments API (#1638)
      Change log as markdown refactor (#1667)
      Add the README file to the Python package (#1665)
      build: build and sign sdist in travis using an RSA sign-only key (#1701)
      logging: refactor to use python logging module (#1690)
      MPEG DASH Support (initial) (#1637)
      plugins.bbciplayer: add dash support
      plugins.facebook: support for DASH streams (#1727)

hoilc <hoilc@foxmail.com> (1):
      fix checking live status

jshir <github.caqomfw25@GadgetScope.com> (1):
      Fix bug 1730, vaughnlive port change

yhel <yhel@users.noreply.github.com> (1):
      Feature/france.tv sport (#1700)
```


## streamlink 0.12.1 (2018-05-07)

Streamlink 0.12.1

Small release to fix a pip / Windows.exe generation bug!

```text
Charlie Drage <charlie@charliedrage.com> (1):
      0.12.0 Release
```


## streamlink 0.12.0 (2018-05-07)

Streamlink 0.12.0

Thanks for all the contributors to this month's release!

New updates:

  - A *ton* of plugin updates (like always! see below for a list of updates)
  - Ignoring a bunch of useless files when developing (https://github.com/streamlink/streamlink/pull/1570)
  - A new option to limit the number of fetch retries (https://github.com/streamlink/streamlink/pull/1375)
  - YouTube has been updated to not use MuxedStream for livestreams (https://github.com/streamlink/streamlink/pull/1556)
  - Bug fix with ffmpegmux (https://github.com/streamlink/streamlink/pull/1502)
  - Removed dead plugins and deprecated options (https://github.com/streamlink/streamlink/pull/1546)

```text
Alexis Murzeau <amubtdx@gmail.com> (2):
      Avoid use of non-ASCII in dogan plugin
      Fix test_plugins.py encoding errors in containerized environment (#1582)

BZHDeveloper <inizan.yannick@gmail.com> (1):
      [TF1] Fix plugin (Fixes #1579) (#1606)

Charlie Drage <charlie@charliedrage.com> (4):
      Add OpenCollective message to release script
      Manually update CHANGELOG.rst
      Remove livestream.patch
      Update release script

Igor Piddubnyi <igor.piddubnyi@gmail.com> (3):
      Plugin implementation for live.russia.tv
      Fix review coments
      Correctly exit on error

James Prance <jpts@users.noreply.github.com> (1):
      Small tweaks to fix ITV player. Fixes #1622 (#1623)

Mattias Amnefelt <mattiasa@avm.se> (1):
      stream.hls: change --hls-audio-select to take a list and wildcard (#1591)

Mohamed El Morabity <melmorabity@fedoraproject.com> (1):
      Add support for international Play TV website

Mohamed El Morabity <melmorabity@fedoraproject.org> (1):
      Add support for RTBF

Mohamed El Morabity <melmorabity@users.noreply.github.com> (1):
      [dailymotion] Fix for new stream data API (#1543)

Sean Greenslade <sean@seangreenslade.com> (1):
      Added retry-max option to limit the number of fetch retries.

back-to <backto@protonmail.ch> (9):
      [ffmpegmux] Fixed bug of an invisible terminal
      [TVRPlus] Fix for hls_re and use headers for HLSStream
      [streann] Fixed broken plugin
      Removed some dead plugins and some Deprecated options
      [youtube] Don't use MuxedStream for livestreams
      [pixiv] New plugin for sketch.pixiv.net (#1550)
      [TVP] New Plugin for Telewizja Polska S.A.
      [build] Fixed AppVeyor build pip10 error (#1605)
      [ABweb] New plugin for BIS Livestreams of french AB Groupe (#1595)

bastimeyer <mail@bastimeyer.de> (2):
      plugins.welt: add plugin
      Add OS + editor file/directory names to .gitignore

beardypig <beardypig@users.noreply.github.com> (7):
      plugins.rtve: add an option to parse_xml to try to fix invalid character entities
      plugins.vaughnlive: Updated server map
      plugins.brittv: fixed script layout change
      build/deploy: do not deploy streamlink-latest, and remove old nightlies (#1624)
      plugins.brittv: fix issue with stream url extraction, from 7018fc8 (#1625)
      plugins.raiplay: add user-agent header to stream redirect request
      plugins.dogan: update for page layout change

fozzy <fozzy@fozzy.co> (1):
      update plugin for longzhu.com to support new url pattern

steven7851 <steven7851@msn.com> (1):
      [app17] Fix HLS URL (#1600)
```


## streamlink 0.11.0 (2018-03-08)

Streamlink 0.11.0!

Here's what's new:

  - Fixed documentation (https://github.com/streamlink/streamlink/pull/1467 and https://github.com/streamlink/streamlink/pull/1468)
  - Current versions of the OS, Python, Streamlink and Requests are now shown with -l debug (https://github.com/streamlink/streamlink/pull/1374)
  - ok.ru/live plugin added (https://github.com/streamlink/streamlink/pull/1451)
  - New option --hls-segment-ignore-names (https://github.com/streamlink/streamlink/pull/1432)
  - AfreecaTV plugin updates (https://github.com/streamlink/streamlink/pull/1390)
  - Added support for zattoo recordings (https://github.com/streamlink/streamlink/pull/1480)
  - Bigo plugin updates (https://github.com/streamlink/streamlink/pull/1474)
  - Neulion plugin removed due to DMCA notice (https://github.com/streamlink/streamlink/pull/1497)
  - And many more updates to numerous other plugins!

```text
Alexis Murzeau <amubtdx@gmail.com> (3):
      Remove Debian directory
      docs/install: use sudo for Ubuntu and Solus
      docs/install: add Debian instructions (#1455)

Anton Tykhyy <atykhyy@gmail.com> (1):
      Add ok.ru/live plugin

BZHDeveloper <inizan.yannick@gmail.com> (1):
      [TF1] Fix plugin (#1457)

Bruno Ribeiro <offboard@users.noreply.github.com> (1):
      added cd streamlink

Drew J. Sonne <drewsonne@users.noreply.github.com> (1):
      [bbciplayer] Fix authentication failures (#1411)

Hannes Pétur Eggertsson <hannespetur@gmail.com> (1):
      Ruv plugin updated. Fixes #643. (#1486)

Mohamed El Morabity <melmorabity@fedoraproject.com> (1):
      Add support for IDF1

back-to <backto@protonmail.ch> (10):
      [cli-debug] Show current installed versions with -l debug
      [hls] New option --hls-segment-ignore-names
      [cli-debug] Renamed method and small template update
      [afreeca] Plugin update. - Login for +19 streams   --afreeca-username   --afreeca-password - Removed 15 sec countdown - Added some error messages - Removed old Global AfreecaTV plugin - Added url tests
      [zattoo] Added support for zattoo recordings
      [tests] Fixed metaclass on python 3
      [periscope] Fix for variant HLS streams
      [facebook] mark as broken, they use dash now.
      Removed furstream: dead website and file was wrong formated UTF8-BOM
      [codecov] use pytest and upload all data

bastimeyer <mail@bastimeyer.de> (2):
      docs: fix table layout on the install page
      [neulion] Remove plugin. See #1493

beardypig <beardypig@users.noreply.github.com> (2):
      plugins.kanal7: fix for new streaming iframe
      plugins.foxtr: update regex to match new site layout

leshka <leshkajm@ya.ru> (1):
      [goodgame] Fixed url regexp for handling miscellaneous symbols in username.

schrobby <schrawby@gmail.com> (1):
      update from github comments

sqrt2 <sqrt2@users.noreply.github.com> (1):
      [orf_tvthek] Work around broken HTTP connection persistence (#1420)

unnutricious <unnutricious@protonmail.com> (1):
      [bigo] update video regex to match current website (#1412)
```


## streamlink 0.10.0 (2018-01-23)

Streamlink 0.10.0!

There's been a lot of activity since our November release.

Changes:

  - Multiple plugin updates (too many to list, see below for the plugin changes!)
  - HLS seeking support (https://github.com/streamlink/streamlink/pull/1303)
  - Changes to the Windows binary (docs: https://github.com/streamlink/streamlink/pull/1408 minor changes to install directory: https://github.com/streamlink/streamlink/pull/1407)

```text
Alexis Murzeau <amubtdx@gmail.com> (3):
      docs: remove flattr-badge.png image
      Fix various typos in comments and documentation
      Implement PKCS#7 padding decoding with AES-128 HLS

BZHDeveloper <inizan.yannick@gmail.com> (1):
      [canalplus] Update plugin according to website changes (#1378)

Mohamed El Morabity <melmorabity@fedoraproject.org> (1):
      [pluzz] Fix video ID regex for France 3 Régions streams

RosadinTV <rosadintv@outlook.com> (1):
      Welcome 2018 (#1410)

Sean Greenslade <sean@seangreenslade.com> (4):
      Reworked picarto.tv plugin to deal with website changes. (#1359)
      Tweaked tigerdile URL regex to allow missing trailing slash.
      Added tigerdile HLS support and proper API poll for offline streams.
      Added basic URL tests for tigerdile.

back-to <back-to@users.noreply.github.com> (5):
      [zdf] apiToken update
      [camsoda] Fixed broken plugin
      [mixer] moved beam.py to mixer.py file requires two commits, for a proper commit history
      [mixer] replaced beam.pro with mixer.com
      [docs] Removed MPlayer2 - Domain expired - Not maintained anymore

back-to <backto@protonmail.ch> (13):
      [BTV] Fixed login return message
      [qq] New Plugin for live.qq.com
      [mlgtv] Fixed broken Plugin streamlink/streamlink#1362
      [viasat] Added support for urls without a stream_id - removed dead domains from _url_re - added a error message for geo blocking - new regex for stream_id from image url - Removed old embed plugin - try to find an iframe if no stream_id was found. - added tests
      [streann] Added headers for post request
      [Dailymotion] Fixed livestream id from channelpage
      [neulion] renamed ufctv.py to neulion.py
      [neulion] Updated the ufctv plugin to make it useable for other domains
      [youtube] added Audio m4a itag 256 and 258
      [hls] Don't try to skip a stream if the offset is 0, don't raise KeyError if the m3u8 file is empty this allows the file to reload.
      [zengatv] New Plugin for zengatv.com
      [mitele] Update for different api response - fallback if not hls_url was found, just the suffix. - added url tests
      [youtube] New params for get_video_info (#1423)

bastimeyer <mail@bastimeyer.de> (2):
      nsis: restore old install dir, keep multiuser
      docs: rewrite Windows binaries install section

beardypig <beardypig@users.noreply.github.com> (12):
      plugins.vaughnlive: try to guess the stream ID from the channel name
      plugins.vaughnlive: updated rtmp server map
      Update server map
      stream.hls: add options to skip some time at the start/end of VOD streams
      stream.hls: add option to restart live stream, if possible
      stream.hls: remove the end offset and replace with duration
      hls: add absolute start offset and duration options to the HLStream API
      duratio bug
      Fix bug with hls start offset = 0
      EOL Python 3.3
      plugins.kanal7: update to stream player URL config
      plugins.huya: fix stream URL scheme prefix

fozzy <fozzy@fozzy.co> (1):
      fix plugin for bilibili to adapt the new API

hicrop <35128217+hicrop@users.noreply.github.com> (1):
      PEP8 (#1427)

steven7851 <steven7851@msn.com> (1):
      [Douyutv] fix API

xela722 <alex0722@comcast.net> (1):
      Add plugin for olympicchannel.com (#1353)
```


## streamlink 0.9.0 (2017-11-14)

Streamlink 0.9.0 has been released!

This release is mostly code refactoring as well as module inclusion.

Features:

  - Updates to multiple plugins (electrecetv, tvplayer, Teve2, cnnturk, kanald)
  - SOCKS module being included in the Streamlink installer (PySocks)

Many thanks to those who've contributed in this release!


```text
Alexis Murzeau <amubtdx@outlook.fr> (2):
      docs: add new line before codeblock to fix them
      Fix sphinx warning on Directive class

Charlie Drage <charlie@charliedrage.com> (1):
      Update the release script

Emrah Er <emraher@users.noreply.github.com> (1):
      plugins.canlitv: fix URLs (#1281)

Jake Robertson <jake@faltro.com> (3):
      exit with code 130 after a KeyboardInterrupt
      refactor error code determination
      unify sys.exit() calls

RosadinTV <rosadintv@outlook.com> (5):
      Update eltrecetv.py
      Update eltrecetv.py
      Update plugin_matrix.rst
      Add webcast_india_gov.py
      Add test_webcast_india_gov.py

back-to <back-to@users.noreply.github.com> (3):
      [zattoo] It won't work with None in Python 3.6, set always a default date instead of None.
      [liveme] API update (#1298)
      Ignore WinError 10053 / WSAECONNABORTED

beardypig <beardypig@users.noreply.github.com> (10):
      plugins.tvplayer: extract the channel id when logged in as a subscriber
      installer: include the socks proxy modules
      plugins.kanal7: update for page layout change and referrer check
      plugins.turkuvaz: fix some turkuvaz sites and add support for anews
      plugins.cinergroup: support for different showtv url
      plugins.dogus/startv: fix dogus sites
      plugins.dogan: fix for teve2 and cnnturk
      plugins.dogan: fix for kanald
      plugins.tvcatchup: HLS source extraction update
      setup: fix PySocks module dependency

ficofabrid <31028711+ficofabrid@users.noreply.github.com> (1):
      Add a single newline at the end of the file. (#1235)

fozzy <fozzy@fozzy.co> (1):
      fix huya.com plugin

steven7851 <steven7851@msn.com> (1):
      plugins.pandatv: fix APIv3 (#1286)

wlerin <wlerin@gmail.com> (1):
      plugin.showroom: update to new api (#1311)
```


## Streamlink 0.8.1 (2017-09-12)

0.8.1 of Streamlink!

97 commits have occurred since the last release, including a large majority of plugin changes.

Here's the outline of what's new:

  - Multiple plugin fixes (twitch, vaughlive, hitbox, etc.)
  - Donations! We've gone ahead and joined the Open Collective at https://opencollective.com/streamlink
  - Multiple doc updates
  - Support for SOCKS proxies
  - Code refactoring

Many thanks to those who've contributed in this release!

```text
Benedikt Gollatz <ben@differentialschokolade.org> (1):
      Fix player URL extraction in bloomberg plugin

Forrest <gravyboat@users.noreply.github.com> (1):
      Update donation docs to note open collective (#1105)

Journey <timtag1190@gmail.com> (2):
      Update Arconaitv to new url
      fix arconai test plugin

Pascal Romahn <pascal.romahn@gmail.com> (1):
      The site always contains the text "does not exist". This should resolve issue https://github.com/streamlink/streamlink/issues/1193

RosadinTV <rosadintv@outlook.com> (2):
      Update Windows portable version documentation
      Fix documentation font-size

Sad Paladin <SadPaladin@users.noreply.github.com> (1):
      plugins.vk: add support for vk.com vod/livestreams

Xavier Damman <xdamman@gmail.com> (1):
      Added backers and sponsors on the README

back-to <back-to@users.noreply.github.com> (5):
      [zattoo] New plugin for zattoo.com / tvonline.ewe.de / nettv.netcologne.com (#1039)
      [vidio] Fixed Plugin, new Regex for HLS URL
      [arconai] Fixed plugin for new website
      [npo] Update for new website layout, Added HTTPStream support
      [liveme] url regex update

bastimeyer <mail@bastimeyer.de> (3):
      docs: add a third party applications list
      docs: add an official streamlink applications list
      Restructure README.md

beardypig <beardypig@users.noreply.github.com> (17):
      plugins.brittv: support for live streams on brittv.co.uk
      plugins.hitbox: fix bug when checking for hosted channels
      plugins.tvplayer: small update to channel id extraction
      plugins.vaughnlive: support for the new vaughnlive website layout
      plugins.vaughnlive: work around for a ssl websocket issue
      plugins.vaughnlive: drop HLS stream support for vaughnlive
      plugins.twitch: enable certificate verification for twitch api
      Resolve InsecurePlatformWarnings for older Python2.7 versions
      cli: remove the deprecation warnings for some of the http options
      plugins.vaughnlive: set a user agent for the initial page request
      plugins.adultswim: fix for some live streams
      plugins: separated the built-in plugins in to separate plugins
      cli: support for SOCKS proxies
      plugins.bbciplayer: fix for page formatting changes and login
      plugins.cdnbg: support for updated layout and extra channels
      plugins: add priority ordering to plugins
      plugins.bbciplayer: support for older VOD streams

fozzy <fozzy@fozzy.co> (10):
      remove unused code
      fix douyutv plugin by using new API
      update douyutv.py to support multiple rates by steven7851
      update HLS Stream name to 'live'
      update weights for streams
      fix stream name
      update stream name, middle and middle2 are of different quality
      Add support for skai.gr
      add eol
      remove unused importing

jgilf <james.gilfillan92@gmail.com> (2):
      Update ufctv.py
      Update ufctv.py

sdfwv <sdfwv@protonmail.ch> (1):
      [bongacams] replace RTMP with HLS Fixed streamlink/streamlink#1074

steven7851 <steven7851@msn.com> (8):
      plugins.douyutv: update post data
      plugins.app17: fix HLS url
      plugins.app17: RTMPStream is no longer used
      plugins.app17: return RTMPStream back
      plugins.douyutv: use douyu open API
      plugins.app17: new layout
      plugins.app17: use https
      plugins.app17: fix wansu cdn url

supergonkas <supergonkas@gmail.com> (1):
      Add support for RTP Play (#1051)

unnutricious <unnutricious@protonmail.com> (2):
      bigo: add support for hls streams
      bigo: improve plugin url regex
```


## streamlink 0.7.0 (2017-06-30)

0.7.0 of Streamlink!

Since our May release, we've incorporated quite a few changes!

Outlined are the major features in this month's release:

  - Stream types will now be sorted accordingly in terms of quality
  - TeamLiquid.net Plugin added
  - Numerous plugin & bug fixes
  - Updated HomeBrew package
  - Improved CLI documentation

Many thanks to those who've contributed in this release!

If you think that this application is helpful, please consider supporting the maintainers by [donating](https://streamlink.github.io/donate.html).


```text
Alex Shafer <shafer.alex@gmail.com> (1):
      Return sorted list of streams. (#731)

Alexandre Hitchcox <alexandre@hitchcox.me> (1):
      Allow live channel links without '/c/' prefix

Alexis Murzeau <amubtdx@outlook.fr> (1):
      docs: fix typo: specifiying, neverthless

CatKasha <CatKasha@users.noreply.github.com> (1):
      Add MPC-HC x64 in streamlinkrc

Forrest <gravyboat@users.noreply.github.com> (1):
      Add a few more examples to the player option (#896)

Jacob Malmberg <jacobma@kth.se> (3):
      Here's the plugin I wrote for teamliquid.net (w/ some help from https://github.com/back-to)
      Tests for teamliquid plugin
      Now with RE!

Mohamed El Morabity <melmorabity@fedoraproject.org> (9):
      Update for live API changes
      Add unit tests for Euronews plugin
      Drop pcyourfreetv plugin
      Add support for regional France 3 streams
      Add support for TV5Monde
      PEP8
      Add support for VOD/audio streams
      Add support for radio.net
      Ignore unreliable stream status returned by radio.net

Sebastian Meyer <mail@bastimeyer.de> (1):
      Homebrew package (#929)

back-to <back-to@users.noreply.github.com> (2):
      [dailymotion] fix for broken .f4m file that is a .m3u8 file (only livestreams)
      [arte] vod api url update & add new/missing languages

bastimeyer <mail@bastimeyer.de> (2):
      docs: fix parameters being linked in code blocks
      Improve CLI documentation

beardypig <beardypig@protonmail.com> (1):
      plugins.hitbox: add support for smashcast.tv

beardypig <beardypig@users.noreply.github.com> (21):
      plugins.bbciplayer: update to reflect slight site layout change
      plugins.bbciplayer: add option to login to a bbc account
      http_server: handle socket closed exception for Python 2.7
      docs: update Sphinx config to fix the rendering of --
      docs: pin sphinx to 1.6.+ so that no future changes affect the docs
      plugins.tvplayer: fix bug with some channels not loading
      plugins.hitbox: fix new VOD urls, and add support for hosted streams
      plugins.tvplayer: fix bug with some channels when not authenticated
      setup: exclude requests version 2.16 through 2.17.1
      win32: fix missing modules when using windows installer
      bbciplayer: fix for api changes to iplayer
      tvplayer: updated to match change token parameter name
      plugins.looch: support for live and vod streams on looch.tv
      plugins.webtv: decrypt the stream URL when applicable
      plugins.dogan: small api change for teve2.com.tr
      plugins.kanal7: fix for nested iframes
      win32: update the dependencies for the windows installer
      plugins.canlitv: simplified and fixed the m3u8 regex
      plugins.picarto: support for VOD
      plugins.ine: update to extract the relocated jwplayer config
      plugin.ufctv: support for free and premium vod/live streams

cirrus <nailzuk@gmail.com> (3):
      Create arconia.py
      Rename arconia.py to arconai.py
      Create plugin_matrix.rst

steven7851 <steven7851@msn.com> (4):
      plugins.app17: fix hls url and support UID page
      little change
      plugins.app17: change ROOM_URL
      [douyu] temporary fix by revert to previously commit (#1015)

whizzoo <grenardus@gmail.com> (2):
      Restore support for RTL XL
      plugin.rtlxl: Remove spaces from line 14

yhel <joel.delahayes@gmail.com> (1):
      Don't return an error when the stream is offline

yhel <yhelae@gmail.com> (1):
      Add capability of extracting current sport.francetv stream
```


## streamlink 0.6.0 (2017-05-11)

Another release of Streamlink!

We've updated more plugins, improved documentation, and moved out nightly builds to Bintray (S3 was costing *wayyyy* too much).

Again, many thanks for those who've contributed!

Thank you very much!

```text
Daniel Draper <Germandrummer92@users.noreply.github.com> (1):
      Will exit with exit code 1 if stream cannot be opened. (#785)

Forrest Alvarez <gravyboat@users.noreply.github.com> (3):
      Update readme so users are aware using Streamlink bypasses ads
      Forgot a )
      Make notice more agnostic

Mohamed El Morabity <melmorabity@fedoraproject.org> (18):
      Disable HDS streams which are no more available
      Add support for pc-yourfreetv.com
      Add support for BFMTV
      Add support for Cam4
      Disable HDS streams for live videos
      Add support for Bloomberg
      Add support for Bloomberg Radio live stream
      Add support for cnews.fr
      Fix unit tests for canalplus plugin
      Add authentication token to http queries
      Add rte.ie/player support
      Add support for HLS streams
      Update for new page layout
      Update for new new page layout
      Fix for new layout
      Pluzz platform replaced by new france.tv website
      Update documentation
      Always use token generator for streams from france.tv

Mohamed El Morabity <melmorabity@users.noreply.github.com> (1):
      plugins.brightcove: support for HLS stream URLs with query strings + RTMPE stream URLs (#790)

RosadinTV <rosadintv@outlook.com> (5):
      Update plugin_matrix.rst
      Add telefe.py
      Add test_plugin_telefe.py
      Update telefe.py
      Add support for ElTreceTV (VOD & Live) (#816)

Sebastian Meyer <mail@bastimeyer.de> (1):
      Improve contribution guidelines (#772)

back-to <back-to@users.noreply.github.com> (9):
      [chaturbate] New API for HLS url
      [chaturbate] Fixed python 3.5 bug and added regex tests
      [VRTbe] new plugin for vrt.be/vrtnu
      [oldlivestream] New regex for cdn subdomains and embeded streams
      [tv1channel.org] New Plugin for embeded streams on tv1channel.org
      [cyro] New plugin for embeded streams from cyro.se
      [Facebook] Added unittests
      [ArteTV] new regex, removed rtmp and better result for available streams
      [NRK.NO] fixed regex for _api_baseurl_re

beardypig <beardypig@protonmail.com> (15):
      travis: use pytest to run the tests for coverage
      Revert "stream.hds: ensure the live edge does not go past the latest fragment"
      plugins.azubutv: plugin removed
      plugins.ustreamtv: log timeout errors and adjust retries for polling
      appveyor: update config to fix builds on Python 3.3
      plugin.tvplayer: update to support new site layout
      plugin.tvplayer: update tests to match new plugin
      plugins.tvplayer: allow https stream URLs
      plugins.tvnbg: add support for live streams on tvn.bg
      plugins.apac: add ustream apac wrapper
      Deploy nightly builds to Bintray instead of S3
      plugins.streann: support for ott.streann.com
      utils.crypto: fix openssl_decrypt for py27
      build: update the bintray release notes for nightlies
      plugins.streamable: support for videos on streamable.com

beardypig <beardypig@users.noreply.github.com> (20):
      plugins.ustreamtv: support for the new ustream.tv API
      plugins.ustreamtv: add suppot for redirectLocked embedded streams
      plugins.livecodingtv: renamed to livedu, and updated for new site
      plugins.ustreamtv: continue to poll the ustream API when streaming
      plugins.ustreamtv: rename the plugin class back to UStreamTV
      docs: remove references to python-librtmp
      plugins.ustream: add some comments
      plugins.ustreamtv: support for password protected streams
      plugins.nbc: support vod from nbc.com
      plugins.nbcsports: add support for nbcsports.com via theplatform
      stream.hds: ensure the live edge does not go past the latest fragment
      Dailymotion feature video and backup stream fallback (#773)
      plugin.gardenersworld: support for VOD on gardenersworld.com
      plugins.twitch: support for pop-out player URLS and fixed clips
      tests: cmdline tests can fail if there are some config options set
      plugins.ustreamtv: fix moduleInfo retry loop
      cli: add --url option that can be used in config files to set a URL
      cli: clarification of the --url option
      cli: add wildcard to --stream-types option
      plugins.rtve: stop IOError bubbling up on 404 errors

wlerin <wlerin@gmail.com> (2):
      Send Referer and UserAgent headers
      Fix method decorator

zp@users.noreply.github.com <zp@users.noreply.github.com> (1):
      New plugin for Facebook 360p streams https://gist.github.com/zp/c461761565dba764c90548758ee5ae9f
```


## streamlink 0.5.0 (2017-04-04)

Streamlink 0.5.0!

Lot's of contributions since the last release. As always, lot's of updating to plugins!

One of the new features is the addition of Google Drive / Google Docs, you can now stream videos stored on Google Docs.

We've also gone ahead and removed dead plugins (sites which have gone down) as well as added pycrypto as a dependency for future plugins.

Again, many thanks for those who have contributed!

Thank you very much!

```text
CallMeJuf <CallMeJuf@users.noreply.github.com> (2):
      Aliez plugin now accepts any TLD (#696)
      New Periscope URL #748

Daniel Draper <Germandrummer92@gmail.com> (2):
      More robust url regex for bigo plugin.
      More robust url regex for bigo plugin, added unittest

Josip Ponjavic <josipponjavic@gmail.com> (4):
      fix vaugnlive info_url
      Update archlinux installation instructions and maintainer info
      setup: choose pycrypto as a dependency using an environment variable
      Add info about pycrypto and pycountry variables to install doc

Mohamed El Morabity <melmorabity@users.noreply.github.com> (1):
      plugins.pluzz: fix SWF player URL search to bring back HDS stream support (#679)

back-to <back-to@users.noreply.github.com> (5):
      plugins.camsoda Added support for camsoda.com
      plugins.canlitv - Added new plugin canlitv
      Removed dead plugins (#702)
      plugins.camsoda - Added tests and small update for the plugin
      plugins.garena - Added new plugin garena

beardypig <beardypig@users.noreply.github.com> (11):
      plugins.bbciplayer: add support for BBC iPlayer live and VOD
      plugins.vaughnlive: updated player version and info URL
      plugins.vaughnlive: search for player version, etc in the swf file
      plugins.beam: add support for VOD and HLS streams for live (#694)
      plugins.bbciplayer: add support for HLS streams
      utils.l10n: use default locale if the system returns an invalid locale
      plugins.dailymotion: play the featured video from channel pages
      plugins.rtve: support for avi/mov VOD streams
      plugins.googledocs: plugin to support playing videos stored on google docs
      plugins.googledocs: updated the url regex and added a status check
      plugins.googledrive: add googledrive support

steven7851 <steven7851@msn.com> (3):
      plugins.17media: Add support for HTTP stream
      plugins.17media: fix rtmp stream
      plugins.douyutv: support vod (#706)
```


## streamlink 0.4.0 (2017-03-09)

0.4.0 of Streamlink!

114 commits since the last release and *a lot* has changed.

In general, we've added some localization as well as an assortment of new plugins.

We've also introduced a change for Streamlink to *not* check for new updates each time Streamlink starts. We found this feature annoying as well as delaying the initial start of the stream. This feature can be re-enabled by the command line.

The major features of this release are:

  - New plugins added
  - Ongoing support to current plugins via bug fixes
  - Ensure retries to HLS streams
  - Disable update check

Many thanks to all contributors who have contributed in this release!

```text
406NotAcceptable <406NotAcceptable@somewhere> (2):
      plugins.afreecatv: API changes
      plugins.connectcast: API changes

BackTo <back-to@users.noreply.github.com> (1):
      plugins.zdf_mediathek Added missing headers for http.get (#653)

Charlie Drage <charlie@charliedrage.com> (7):
      Updating the release script.
      0.3.1 Release
      Update release script again to include sdist
      Fix underlining issue
      Fix the CHANGELOG.rst
      0.3.2 Release
      Update underscores title release script (#563)

Forrest <gravyboat@users.noreply.github.com> (3):
      Update license and debian copyright (#515)
      Add a donation page (#578)
      Fix up the donate docs (#672)

Forrest Alvarez <gravyboat@users.noreply.github.com> (1):
      Update license and debian copyright

John Smith <v2.0@protonmail.com> (1):
      plugins.bongacams: a few small changes (#429)

Mohamed El Morabity <melmorabity@fedoraproject.org> (1):
      Check whether videos are DRM-protected Add log messages when no stream is available

Mohamed El Morabity <melmorabity@users.noreply.github.com> (3):
      Add support for replay.gulli.fr (#468)
      plugins.pluzz: add support for ludo.fr and zouzous.fr (#536)
      Add subtitle support for pluzz plugins (#646)

Scott Buettner <buettner.scott@live.com> (1):
      Fix Crunchyroll string.format in Python 2.6 (#539)

Sven <sven@androd.se> (1):
      Adding Huomao plugin with possibility for different stream qualities.

Sven Anderzén <svenanderzen@users.noreply.github.com> (1):
      Huomao plugin tests (#566)

back-to <back-to@users.noreply.github.com> (2):
      [earthcam] Added HLS, Fixed live RTMP and changes some stuff
      plugins.ard_mediathek added mediathek.daserste.de support

beardypig <beardypig@users.noreply.github.com> (74):
      plugins.schoolism: add support for schoolism.com
      plugins.earthcam: added support for live and archive cam streams
      stream.hls_playlist: invalid durations in EXTINF lines are ignored
      plugins.livecoding: update to support the new domain: liveedu.tv
      plugins.srgssr: fix playlist reload auth issue
      Play twitch VOD stream from the beginning even if is still being recorded
      cli: wait for process to exit, not exit with non-0 error code
      Fix bug in customized Windows install
      add a general locale setting which can be used by plugins
      stream.hls: support external audio tracks
      plugins.turkuvaz: add referer to the secure token request
      localization: search for language codes in part2t+part2b+part3
      localization: invalid language/country codes are always inequivalent
      stream.hls: only support external audio tracks if ffmpeg is available
      installer: include the missing pkg_resources package
      Rewritten StreamProcess class (#441)
      plugins.dogus: fix for ntv streams not being found
      plugins.dogus: add support for eurostartv live stream
      plugins.twitch: update public API calls to use v5 API (#484)
      plugins.filmon: support for new site layout (#508)
      Support for Ceskatelevize streams (#520)
      Ensure retries with HLS Streams (#522)
      utils.l10n: add Country/Language classes, use pycountry is the iso modules are not available
      plugins.crunchyroll: added option to set the session id to a specific value
      CI: add pycountry for testing
      plugins.openrectv: add source quality for openrectv
      utils.l10n: default to en_US when an invalid locale is set
      fix some python2.6 issues
      allow failure for python2.6 in travis and update minimum supported python version to 2.7, as well as adding an annoying deprecation warning
      stream.hls: pick a better default stream language
      stream.hls: Retry HTTP requests to get the key for HLS streams
      plugins.openrectv: fixed broken vod support
      appveyor: use the build.cmd script to install streamlink, so that the sdk can be used if required
      stream.hls: last chance fallback audio
      stream: make Stream responsible for generating the stream_url
      utils.l10n: fix bug in iso3166 country lookup
      tests: speed up the cmdline tests
      Remove deprecation warning for invalid escape sequences
      tests: merged the Localization tests back in to one module
      plugins.foxtr: adjusted regex for slight site layout change
      plugins.ard_mediathek: update to support site change
      stream.hds: warn about streams being protected by DRM
      plugins.tvrplus: add support for tvrplus.ro live streams
      plugins.tvrby: support for live streams of Belarus national TV
      plugins.ovvatv: add support for ovva.tv live streams
      cli.utils.http_server: avoid "Address already in use" with --player-external-http
      setup: choose pycountry as a dependency using an environment variable
      plugins.ovvatv: fix b64decoding bug
      plugin.mitele: use the default plugin cache
      plugins.seetv: add support for seetv.tv live streams
      cli.utils.http_server: ignore errors with socket.shutdown
      plugins.daisuki: add support for VOD streams from daisuki.net (#609)
      plugins.daisuki: fix for truncated subtitles
      cli: disable automatic version checking by default
      plugins.rtve: update rtve plugin to support VOD (#628)
      plugins.rtve: return all the available qualities
      plugins.funimationnow: support for US and UK funimation|now streams (#629)
      cli: --no-version-check always disables the version check
      plugins.tvplayer: support for authenticated streams
      docs: updated the docs for built-in stream parameters
      utils.l10n: fix for some locales without an official name in pycountry
      plugins.wwenetwork: support for WWE Network streams
      plugins.trt: make the url test case insensitive and fix py3 bug
      plugins.tvplayer: automatically set postcode when required
      plugins.ard_live: updated to new site layout
      plugins.vidio: fix for regex, if the url is the english version
      plugins.animelab: added support for AnimeLab.com VOD
      plugin.npo: rewrite of plugin to use the new API (#642)
      plugins.goodgame: support for http URLs
      docs.donate: drop name headers to subsection level
      stream.hls: format string name input for parse_variant_playlist
      plugins.wwenetwork: use the resolution and bitrate in the stream name
      docs: make the nightly installer link more obvious
      stream.hls: option to select a specific, non-standard audio channel

fozzy <fozzy@fozzy.co> (4):
      update douyutv plugin, use new API
      update to support different quality
      fix typo and indent
      correct typo

fozzy <fozzysec@gmail.com> (3):
      Add support for Huya.com in issue #425 (#465)
      Fix issue #426 on plugins/tga.py (#456)
      fix douyutv issue #637 (#666)

intact <intact.devel@gmail.com> (1):
      Add Rtvs.sk Plugin

steven7851 <steven7851@msn.com> (4):
      plugins.douyutv: fix room id regex (#514)
      plugins.pandatv: use Pandatv API v3 (#410)
      Add plugin for 17app.co (#502)
      plugins.zhanqi: use new api (#498)

wlerin <wlerin@gmail.com> (1):
      plugins.showroom: add support for showroom-live.com live streams (#633)
```


## streamlink 0.3.2 (2017-02-10)

0.3.2 release of Streamlink!

A minor bug release of 0.3.2 to fix a few issues with stream providers.

Thanks to all whom have contributed to this (tiny) release!

```text
Charlie Drage <charlie@charliedrage.com> (3):
      Update release script again to include sdist
      Fix underlining issue
      Fix the CHANGELOG.rst

Sven <sven@androd.se> (1):
      Adding Huomao plugin with possibility for different stream qualities.

beardypig <beardypig@users.noreply.github.com> (7):
      Ensure retries with HLS Streams (#522)
      utils.l10n: add Country/Language classes, use pycountry is the iso modules are not available
      plugins.crunchyroll: added option to set the session id to a specific value
      CI: add pycountry for testing
      plugins.openrectv: add source quality for openrectv
      utils.l10n: default to en_US when an invalid locale is set
      stream.hls: pick a better default stream language

intact <intact.devel@gmail.com> (1):
      Add Rtvs.sk Plugin
```


## streamlink 0.3.1 (2017-02-03)

0.3.1 release of Streamlink

A *minor* release, we update our source code upload to *not* include the ffmpeg.exe binary as well as update a multitude of plugins.

Thanks again for all the contributions as well as updates!

```text
Charlie Drage <charlie@charliedrage.com> (1):
      Updating the release script.

Forrest <gravyboat@users.noreply.github.com> (1):
      Update license and debian copyright (#515)

Forrest Alvarez <gravyboat@users.noreply.github.com> (1):
      Update license and debian copyright

John Smith <v2.0@protonmail.com> (1):
      plugins.bongacams: a few small changes (#429)

Mohamed El Morabity <melmorabity@fedoraproject.org> (1):
      Check whether videos are DRM-protected Add log messages when no stream is available

Mohamed El Morabity <melmorabity@users.noreply.github.com> (1):
      Add support for replay.gulli.fr (#468)

beardypig <beardypig@users.noreply.github.com> (20):
      plugins.schoolism: add support for schoolism.com
      stream.hls_playlist: invalid durations in EXTINF lines are ignored
      plugins.livecoding: update to support the new domain: liveedu.tv
      plugins.srgssr: fix playlist reload auth issue
      Play twitch VOD stream from the beginning even if is still being recorded
      cli: wait for process to exit, not exit with non-0 error code
      Fix bug in customized Windows install
      add a general locale setting which can be used by plugins
      stream.hls: support external audio tracks
      plugins.turkuvaz: add referer to the secure token request
      localization: search for language codes in part2t+part2b+part3
      localization: invalid language/country codes are always inequivalent
      stream.hls: only support external audio tracks if ffmpeg is available
      installer: include the missing pkg_resources package
      Rewritten StreamProcess class (#441)
      plugins.dogus: fix for ntv streams not being found
      plugins.dogus: add support for eurostartv live stream
      plugins.twitch: update public API calls to use v5 API (#484)
      plugins.filmon: support for new site layout (#508)
      Support for Ceskatelevize streams (#520)

fozzy <fozzysec@gmail.com> (1):
      Add support for Huya.com in issue #425 (#465)

steven7851 <steven7851@msn.com> (1):
      plugins.douyutv: fix room id regex (#514)
```


## streamlink 0.3.0 (2017-01-24)

Release 0.3.0 of Streamlink!

A lot of updates to each plugin (thank you @beardypig !), automated Windows releases, PEP8 formatting throughout Streamlink are some of the few updates to this release as we near a stable 1.0.0 release.

Main features are:

  - Lot's of maintaining / updates to plugins
  - General bug and doc fixes
  - Major improvements to development (github issue templates, automatically created releases)

```text
Agustín Carrasco <asermax@gmail.com> (1):
      Links on crunchy's rss no longer contain the show name in the url (#379)

Brainzyy <Brainzyy@users.noreply.github.com> (1):
      Add basic tests for stream.me plugin (#391)

Javier Cantero <jcantero@escomposlinux.org> (2):
      plugins/twitch: use version v3 of the API
      plugins/twitch: use kraken URL

John Smith <v2.0@protonmail.com> (3):
      Added support for bongacams.com streams (#329)
      streamlink_cli.main: close stream_fd on exit (#427)
      streamlink_cli.utils.progress: write new line at finish (#442)

Max Riegler <rinukkusu@sub-r.de> (1):
      plugins.chaturbate: new regex (#457)

Michiel Sikma <michiel@wedemandhtml.com> (1):
      Update PLAYER_VERSION, as old one does not return data. Add ability to use streams with /embed/video in the URL, from embedded players. (#311)

Mohamed El Morabity <melmorabity@users.noreply.github.com> (6):
      Add support for pluzz.francetv.fr (#343)
      Fix ArteTV plugin (#385)
      Add support for Canal+ TV group channels (#416)
      Update installation instructions for Fedora (#443)
      Add support for Play TV (#439)
      Use token generator for HLS streams, as for HDS ones (#466)

RosadinTV <rosadintv@outlook.com> (1):
      --can-handle-url-no-redirect parameter added (#333)

Stefan Hanreich <stefanhani@gmail.com> (1):
      added chocolatey to the documentation (#380)

bastimeyer <mail@bastimeyer.de> (3):
      Automatically create Github releases
      Set changelog in automated github releases
      Add a github issue template

beardypig <beardypig@users.noreply.github.com> (55):
      plugins.tvcatchup: site layout changed, updated the stream regex to accommodate the change (#338)
      plugins.streamlive: streamlive.to have added some extra protection to their streams which currently prevents us from capturing them (#339)
      cli: add command line option to specific logging path for subprocess errorlog
      plugins.trtspor: added support for trtspor.com (#349)
      plugins.kanal7: fixed page change in kanal7 live stream (#348)
      plugins.picarto: Remove the unreliable rtmp stream (#353)
      packaging: removed the built in backports infavour of including them as dependencies when required (#355)
      Boost the test coverage a bit (#362)
      plugins: all regex string should be raw (#361)
      ci: build and test on Python 3.6 (+3.7 on travis, with allowed failure) (#360)
      packages.flashmedia: fix bug in AMFMessage (#359)
      tests: use mock from unittest when available otherwise fallback to mock (#358)
      stream.hls: try to retry stream segments (#357)
      tests: add codecov config file (#363)
      plugins.picarto: updated plugin to use tech_switch divs to find the stream parameters
      plugins.mitele: support for live streams on mitele.es
      docs: add a note about python-devel needing to be installed in some cases
      docs/release: generate the changelog as rst instead of md
      plugins.adultswim: support https urls
      use iso 8601 date format for the changelog
      plugins.tf1: added plugin to support tf1.fr and lci.fr
      plugins.raiplay: added plugin to support raiplay.it
      plugins.vaughnlive: updated player version and info URL (#383)
      plugins.tv8cat: added support for tv8.cat live stream (#390)
      Fix TF1.fr plugin (#389)
      plugins.stream: fix a default scheme handling for urls
      Add support for some Bulgarian live streams (#392)
      rtmp: fix bug in redirect for rtmp streams
      plugins.sportal: added support for the live stream on sportal.bg
      plugins.bnt: update the user agent string for the http requests
      plugins.ssh101: update to support new site layout
      Optionally use FFMPEG to mux separate video and audio streams (#224)
      Support for 4K videos in YouTube (#225)
      windows-installer: add the version info to the installer file
      include CHANGELOG.rst instead of .md in the egg
      stream.hls: output duplicate streams for HLS when multiple streams of the same quality are available
      stream.ffmpegmux: fix support for avconv, avconv will be used if ffmpeg is not found
      Adultswin VOD support (#406)
      Move streamlink_cli.utils.named_pipe in to streamlink.utils
      plugins.rtve: update plugin to support new streaming method
      stream.hds: omit HDS streams that are protected by DRM
      Adultswin VOD fix for live show replays (#418)
      plugins.rtve: add support for legacy stream URLs
      installer: remove the streamlink bin dir from %PATH% before installing
      plugins.twitch: only check hosted channels when playing a live stream
      docs: tweaks to docs and docs build process
      Fix iframe detection for BTN/cdn.bg streams (#437)
      fix some regex that give deprecation warnings in python 3.6
      plugins.adultswim: correct behaviour for archived streams
      plugins.nineanime: add scheme to grabber api url if not present
      session: add an option to disable Diffie Hellman key exchange
      plugins.srgssr: added support for srg ssr sites: srf, rts and rsi
      plugins.srgssr: fixed bug in api URL and fixed akamai urls with authparams
      cli: try to terminate the player process before killing it (if terminate takes too long)
      plugins.swisstxt: add support for the SRG SSR sites sports sections

fozzy <fozzysec@gmail.com> (1):
      Add plugin for huajiao.com and zhanqi.tv (#334)

sqrt2 <sqrt2@users.noreply.github.com> (1):
      Fix swf_url in livestream.com plugin (#428)

stepshal <nessento@openmailbox.org> (1):
      Remove trailing.

stepshal <stepshal@users.noreply.github.com> (2):
      Add blank line after class or function definition (#408)
      PEP8 (#414)
```


## streamlink 0.2.0 (2016-12-16)

Release 0.2.0 of Streamlink!

We've done numerous changes to plugins as well as fixed quite a few
which were originally failing. Among these changes are updated docs as
well as general UI/UX cleaning with console output.

The main features are:

 - Additional plugins added
 - Plugin fixes
 - Cleaned up console output
 - Additional documentation (contribution, installation instructions)

Again, thank you everyone whom contributed to this release! :D

```text
Beardypig <beardypig@users.noreply.github.com> (6):
      Turkish Streams Part III (#292)
      coverage: include streamlink_cli in the coverage, but exclude the vendored packages (#302)
      Windows command line parsing fix (#300)
      plugins.atresplayer: add support for live streams on atresplayer.com (#303)
      Turkish Streams IV (#305)
      Support for local files (#304)

Charlie Drage <charlie@charliedrage.com> (2):
      Spelling error in release script
      Fix issue with building installer

Fishscene <fishscene@gmail.com> (3):
      Updated homepage
      Updated README.md
      Fixed type in README.md.

Forrest <gravyboat@users.noreply.github.com> (3):
      Modify the browser redirect (#191)
      Update client ID (#241)
      Update requests version after bug fix (#239)

Josip Ponjavic <josipponjavic@gmail.com> (1):
      Add NixOS install instructions

Simon Bernier St-Pierre <sbernierstpierre@gmail.com> (1):
      add contributing guidelines

bastimeyer <mail@bastimeyer.de> (1):
      Add metadata to Windows installer

beardypig <beardypig@users.noreply.github.com> (25):
      plugins.nhkworld: update the plugin to use the new HLS streams
      plugins.picarto: updated the plugin to use the new javascript and support HLS streams
      add pycryptodome==3.4.3 to the setup.py dependencies
      plugins.nineanime: added a plugin to support 9anime.to
      plugins.nineanime: update the plugin matrix in the docs
      plugins.atv: add support for the live stream on atv.com.tr
      include omxplayer in the list of players in the documentation
      update the player docs with findings from @Junior1544 and @stevekmcc
      plugins.bigo: support for bigo.tv
      docs: move pycryptodome to the list of automatically installed libraries in the docs
      plugins.dingittv: add support for dingit.tv
      plugins.crunchyroll: support ultra quality for subscribers
      update URL for docs to point to the github.io page
      stream.hls: stream the HLS segments out to the player as they are downloaded, decrypting on the fly
      installer: install the required MS VC++ runtime files beside the python installation (see takluyver/pynsist/pull/87)
      plugins.bigo: FlashVars regex updated due to site change
      add some license notices for the bundled libraries
      plugins.youtube: support additional live urls
      add support for a few Turkish live streams
      plugins.foxtr: add support for turkish fox live streams
      plugins.kralmuzik: basic support for the HLS stream only
      stream.hds: added option to force akamai authentication plugins.startv: refactored in to a base class, to be used in other plugins that use the same hosting as StarTV plugins.kralmuzik: refactored to use StarTVBase plugins.ntv: added NTV support
      plugins.atv: add support for a2tv which is very similar to atv
      plugins.dogan: support for teve2, kanald, dreamtv, and ccnturk via the same plugin
      plugins.trt: added support for the live channels on trt.net.tr

che <che27012011@googlemail.com> (1):
      plugins.twitch: support for clips added

ioblank <iosonoblank@gmail.com> (1):
      Use ConsoleOutput for run-as-root warning

mmetak <mmetak@users.noreply.github.com> (3):
      Update install instruction (#257)
      Add links for windows portable version. (#299)
      Add package maintainers to docs. (#301)

thatlinuxfur <toss1@zootboy.com> (1):
      Added tigerdile.com support. (#221)
```


## streamlink 0.1.0 (2016-11-21)

A major update to Streamlink.

With this release, we include a Windows binary as well as numerous
plugin changes and fixes.

The main features are:

 -  Windows binary (and generation!) thanks to the fabulous work by
 @beardypig
 -  Multiple plugin fixes
 -  Remove unneeded run-as-root (no more warning you when you run as
   root, we trust that you know what you're doing)
 -  Fix stream quality naming issue

```text
Beardypig <beardypig@users.noreply.github.com> (13):
      fix stream quality naming issue with py2 vs. py3, fixing #89 (#96)
      updated connectcast plugin to support the new rtmp streams; fixes #93 (#95)
      Fix for erroneous escape coding the livecoding plugin. Fixes #106 (#121)
      TVPlayer.com: fix for 400 error, correctly set the platform parameter (#123)
      Added a method to automatically determine the encoding when parsing JSON, if no encoding is provided. (#122)
      when retry-streams and twitch-disable-hosting arguments are used the stream is retried until a non-hosted stream is found (#125)
      plugins.goodgame: Update for API change (#130)
      plugins.adultswim: added a new adultswim.com plugin (#139)
      plugins.goodgame: restored DDOS protection cookie support (#136)
      plugins.younow: update API url (#135)
      plugins.euronew: update to support the new site (#141)
      plugins.webtv: added a new plugin to support web.tv (#144)
      plugins.connectcast: fix regex issue with python 3 (#152)

Brainzyy <Brainzyy@users.noreply.github.com> (1):
      Add piczel.tv plugin (courtesy of @intact) (#114)

Charlie Drage <charlie@charliedrage.com> (1):
      Update release scripts

Erk- <Erk-@users.noreply.github.com> (1):
      Changed the twitch plugin to use https instead of http as discussed in #103 (#104)

Forrest <gravyboat@users.noreply.github.com> (2):
      Modify the changelog link (#107)
      Update cli to note a few windows issues (#108)

Simon Bernier St-Pierre <sbernierstpierre@gmail.com> (1):
      change icon

Simon Bernier St-Pierre <sbstp@users.noreply.github.com> (1):
      finish the installer (#98)

Stefan <stefan-github@yrden.de> (1):
      Debian packaging base (#80)

Stefan <stefanhani@gmail.com> (1):
      remove run-as-root option, reworded warning #85 (#109)

Weslly <weslly.honorato@gmail.com> (1):
      Fixed afreecatv.com url matching (#90)

bastimeyer <mail@bastimeyer.de> (2):
      Improve NSIS installer script
      Remove shortcut from previous releases on Windows

beardypig <beardypig@users.noreply.github.com> (8):
      plugins.cybergame: update to support changes to the live streams on the cybergame.tv website
      Use pycryptodome inplace of pyCrypto
      Automated build of the Windows NSIS installer
      support for relative paths for rtmpdump
      makeinstaller: install the streamlinkrc file in to the users %APPDATA% directory
      remove references to livestreamer in the win32 config template
      stream.rtmpdump: fixed the rtmpdump path issue, introduced in 6bf7fd7
      pin requests to <2.12.0 to avoid the strict IDNA2008 validation

ethanhlc <ethanhlc@users.noreply.github.com> (1):
      fixed instance of livestreamer (#99)

intact <intact.devel@gmail.com> (1):
      plugins.livestream: Support old player urls

mmetak <mmetak@users.noreply.github.com> (2):
      fix vaughnlive.tv info_url (#88)
      fix vaughnlive.tv info_url (yet again...) (#143)

skulblakka <pascal.romahn@mailbox.org> (1):
      Overworked Plugin for ZDF Mediathek (#154)

sqrt2 <sqrt2@users.noreply.github.com> (1):
      Fix ORF TVthek plugin (#113)

tam1m <tam1m@users.noreply.github.com> (1):
      Fix zdf_mediathek TypeError (#156)
```


## streamlink 0.0.2 (2016-10-12)

The second ever release of Streamlink!

In this release we've not only set the stepping stone for the further
development of Streamlink (documentation site updated, CI builds
working) but we're already fixing bugs and implementing features past
the initial fork of livestreamer.

The main features of this release are: - New windows build available and
generated via pyinstaller - Multiple provider bug fixes (twitch,
picarto, itvplayer, crunchyroll, periscope, douyutv) - Updated and
reformed documentation which also includes our site
https://streamlink.github.io

As always, below is a `git shortlog` of all changes from the previous
release of Streamlink (0.0.1) to now (0.0.2).

```text
Brainzyy <Brainzyy@users.noreply.github.com> (1):
      add stream.me to the docs

Charlie Drage <charlie@charliedrage.com> (9):
      Add script to generate authors list / update authors
      Add release script
      Get setup.py ready for a release.
      Revert "Latest fix to plugin from livestreamer"
      0.0.1 Release
      Update the README with installation notes
      Update copyright author
      Update plugin description on README
      It's now 2016

Forrest <gravyboat@users.noreply.github.com> (1):
      Add a coverage file (#54)

Forrest Alvarez <forrest.alvarez@gmail.com> (4):
      Modify release for streamlink
      Remove faraday from travis run
      Remove tox
      Add the code coverage badge

Latent Logic <lat.logic@gmail.com> (1):
      Picarto plugin: multistream workaround (fixes #50)

Maschmi <Maschmi@users.noreply.github.com> (1):
      added travis build status badge fixes #74 (#76)

Randy Taylor <tehgecKozzz@gmail.com> (1):
      Fix typo in issues docs and improve wording (#61)

Simon Bernier St-Pierre <sbernierstpierre@gmail.com> (8):
      add script to build & copy the docs
      move makedocs.sh to script/
      Automated docs updates via travis-ci
      prevent the build from hanging
      fix automated commit message
      add streamboat to the docs
      disable docs on pull requests
      twitch.tv: add option to disable hosting

Simon Bernier St-Pierre <sbstp@users.noreply.github.com> (2):
      Don't delete everything if docs build fail (#62)
      Create install script for pynsist (#27)

beardypig <beardypig@users.noreply.github.com> (3):
      TVPlayer plugin supports the latest version of the website
      crunchyroll: decide if to parse the stream links as HLS variant playlist or plain old HLS stream (fixes #70)
      itvplayer: updated the productionId extraction method

boda2004 <boda2004@gmail.com> (1):
      fixed periscope live streaming and allowed url re (#79)

ethanhlc <sakithree@gmail.com> (1):
      fixed instances of chrippa/streamlink to streamlink/streamlink

scottbernstein <scott_bernstein@hotmail.com> (1):
      Latest fix to plugin from livestreamer

steven7851 <steven7851@msn.com> (1):
      Update plugin.douyutv
```


## streamlink 0.0.1 (2016-09-23)

The first release of Streamlink!

This is the first release from the initial fork of Livestreamer. We aim
to have a concise, fast review process and progress in terms of
development and future releases.

Below is a `git shortlog` of all commits since the last change within
Livestream (hash ab80dbd6560f6f9835865b2fc9f9c6015aee5658). This will
serve as a base-point as we continue development of "Streamlink".

New releases will include a list of changes as we add new features /
code refactors to the existing code-base.

```text
Agustin Carrasco <asermax@gmail.com> (2):
      plugins.crunchyroll: added support for locale selection
      plugins.crunchyroll: use locale parameter on the header's user-agent as well

Alan Love <alan@cattes.us> (3):
      added support for livecoding.tv
      removed printing
      updated plugin matrix

Alexander <AleXoundOS@users.noreply.github.com> (1):
      channel info url change in afreeca plugin

Andreas Streichardt <andreas.streichardt@gmail.com> (1):
      Add Sportschau

Anton <anton9121@gmail.com> (2):
      goodgame ddos validation
      add stream_id with words

Benedikt Gollatz <ben@differentialschokolade.org> (1):
      Add support for ORF TVthek livestreams and VOD segments

Benoit Dien <benoit.dien@gmail.com> (1):
      Meerkat plugin

Brainzyy <Brainzyy@users.noreply.github.com> (1):
      fix azubu.tv plugin

Charlie Drage <charlie@charliedrage.com> (9):
      Update the README
      Fix travis
      Rename instances of "livestreamer" to "streamlink"
      Fix travis
      Add script to generate authors list / update authors
      Get setup.py ready for a release.
      Add release script
      Revert "Latest fix to plugin from livestreamer"
      0.0.0 Release

Charmander <~@charmander.me> (1):
      plugins.picarto: Update for API and URL change

Chris-Werner Reimer <creimer@betaworx.eu> (1):
      fix vaughnlive plugin #897

Christopher Rosell <chrippa@tanuki.se> (7):
      plugins.twitch: Handle subdomains with dash in them, e.g. en-gb.
      cli: Close output on exit.
      Show a brief usage when no option is specified.
      cli: Fix typo.
      travis: Use new artifacts tool.
      docs: Fix readthedocs build.
      travis: Build installer exe aswell.

Daniel Meißner <daniel@3st.be> (2):
      plugin: added media_ccc_de api and protocol changes
      docs/plugin_matrix: removed needless characters

Dominik Sokal <dominiksokal@gmail.com> (1):
      plugins.afreeca: fix stream

Ed Holohan <edmund@holohan.us> (1):
      Quick hack to handle Picarto changes

Emil Stahl <emil@emilstahl.dk> (1):
      Add support for viafree.dk

Erik G <aposymbiosis@gmail.com> (7):
      Added plugin for Dplay.
      Added plugin for Dplay and removed sbsdiscovery plugin.
      Add HLS support, adjust API schema, no SSL verify
      Add pvswf parameter to HDS stream parser
      Fix Video ID matching, add .no & .dk support, add error handling
      Match new URL, add HDS support, handle incorrect geolocation
      Add API support

Fat Deer <fatdeer@foxmail.com> (1):
      Update pandatv.py

Forrest Alvarez <forrest.alvarez@gmail.com> (3):
      Add some python releases
      Add coveralls to after_success
      Remove artifacts

Guillaume Depardon <guillaume.depardon@outlook.com> (1):
      Now catching socket errors on send

Javier Cantero <jcantero@escomposlinux.org> (1):
      Add new parameter to Twitch usher URL

Jeremy Symon <jtsymon@gmail.com> (2):
      Sort list of streams by quality
      Avoid sorting streams twice

Jon Bergli Heier <snakebite@jvnv.net> (2):
      plugins.nrk: Updated for webpage changes.
      plugins.nrk: Fixed _id_re regex not matching series URLs.

Kari Hänninen <lonefox@kapsi.fi> (7):
      Use client ID for twitch.tv API calls
      Revert "update INFO_URL for VaughnLive"
      Remove spurious print statement that made the plugin incompatible with python 3.
      livecoding.tv: fix breakage ("TypeError: cannot use a string pattern on a bytes-like object")
      sportschau: Fix breakage ("TypeError: a bytes-like object is required, not 'str'"). Also remove debug output.
      Update the plugin matrix
      Bump version to 1.14.0-rc1

Marcus Soll <Superschlumpf@web.de> (2):
      Added plugin for blip.tv VOD
      Updated blip.tv plugin

Mateusz Starzak <mstarzak@gmail.com> (1):
      Update periscope.py

Michael Copland <mjbcopland@gmail.com> (1):
      Fixed weighting of Twitch stream names

Michael Hoang <enzime@users.noreply.github.com> (1):
      Add OPENREC.tv plugin and chmod 2 files

Michiel <msvos@liacs.nl> (1):
      Support for Tour de France stream

Paul LaMendola <paulguy119@gmail.com> (2):
      Maybe fixed ustream validation failure.
      More strict test for weird stream.

Pavlos Touboulidis <pav@pav.gr> (2):
      Add antenna.gr plugin
      Update plugin matrix for antenna

Robin Schroer <sulami@peerwire.org> (1):
      azubutv: set video_player to None if stream is offline

Seth Creech <sethaaroncreech@gmail.com> (1):
      Added logic to support host mode

Simon Bernier St-Pierre <sbernierstpierre@gmail.com> (5):
      update the streamup.com plugin
      support virtualenv
      update references to livestreamer
      add stream.me plugin
      add streamboat plugin

Summon528 <cody880528@hotmail.com> (1):
      add support to afreecatv.com.tw

Swirt <swirt.ac@gmail.com> (2):
      Picarto plugin: update RTMPStream-settings
      Picarto plugin: update RTMPStream-settings

Tang <sugar1987cn@gmail.com> (1):
      New provider: live.bilibili.com

Warnar Boekkooi <warnar@boekkooi.net> (1):
      NPO token fix

WeinerRinkler <drachenlord@8chan.co> (2):
      First version
      Error fixed when streamer offline or invalid

blxd <blxd@users.noreply.github.com> (5):
      fixed tvcatchup.com plugin, the website layout changed and the method to find the stream URLs needed to be updated.
      tvcatchup now returns a variant playlist
      tvplayer.com only works with a browser user agent
      not all channels return hlsvariant playlists
      add user agent header to the tvcatchup plugin

chvrn <chev@protonmail.com> (4):
      added expressen plugin
      added expressen plugin
      update() => assign with subscript
      added entry for expressen

e00E <vakevk+git@gmail.com> (1):
      Fix Twitch plugin not working because bandwith was parsed as an int when it is really a float

fat deer <fatdeer@foxmail.com> (1):
      Add Panda.tv Plugin.

fcicq <fcicq@fcicq.net> (1):
      add afreecatv.jp support

hannespetur <hannespetur@gmail.com> (8):
      plugin for Ruv - the Icelandic national television - was added
      removed print statements and started to use quality key as audio if the url extensions is mp3
      the plugin added to the plugin matrix
      removed unused import
      alphabetical order is hard
      removed redundant assignments of best/worst quality
      HLS support added for the Ruv plugin
      Ruv plugin: returning generators instead of a dict

int3l <int3l@users.noreply.github.com> (1):
      Refactoring and update for the VOD support

intact <intact.devel@gmail.com> (21):
      plugins.artetv: Update json regex
      Updated douyutv.com plugin
      Added plugin for streamup.com
      plugins.streamupcom: Check live status
      plugins.streamupcom: Update for API change
      plugins.streamupcom: Update for API change
      plugins.dailymotion: Add HLS streams support
      plugins.npo: Fix Python 3 compatibility
      plugins.livestream: Prefer standard SWF players
      plugins.tga: Support more streams
      plugins.tga: Fix offline streams
      plugins.vaughnlive: Fix INFO_URL
      Added plugin for vidio.com
      plugins.vaughnlive: Update for API change
      plugins.vaughnlive: Fix app for some ingest servers
      plugins.vaughnlive: Remove debug print
      plugins.vaughnlive: Lowercase channel name
      plugins.vaughnlive: Update for API change
      plugins.vaughnlive: Update for API change
      plugins.livestream: Tolerate missing swf player URL
      plugins.livestream: Fix player URL

jkieberk <jkieberking@gmail.com> (1):
      Change Fedora Package Manager from Yum  to Dnf

kviktor <kviktor@cloud.bme.hu> (2):
      plugins: mediaklikk.hu stream and video support
      update mediaklikk plugin

livescope <livescope@users.noreply.github.com> (1):
      Add VOD/replay support for periscope.tv

liz1rgin <waiphereme@gmail.com> (2):
      Fix goodgame find Streame
      Update goodgame.py

maop <me@marcoalfonso.net> (1):
      Add Beam.pro plugin.

mindhalt <mindhalt@gmail.com> (1):
      Update redirect URI after successful twitch auth

neutric <ah0703@googlemail.com> (1):
      Update issues.rst

nitpicker <daniel@localhost> (2):
      I doesn't sign the term of services, so I doesnt violate!
      update INFO_URL for VaughnLive

oyvindln <mail@example.com> (1):
      Allow https urls for nrk.no.

ph0o <ph0o@users.noreply.github.com> (1):
      Create servustv.py

pulviscriptor <pulviscriptor@gmail.com> (1):
      GoodGame URL parse fix

scottbernstein <scott_bernstein@hotmail.com> (1):
      Latest fix to plugin from livestreamer

steven7851 <steven7851@msn.com> (16):
      plugins.douyutv: Use new api.
      update douyu
      fix cdn..
      fix for Python 3.x..
      use mobile api for reducing code
      fix for non number channel
      add middle and low quality
      fix quality
      fix room id regex
      make did by UUID module
      fix channel on event
      more retries for redirection
      remove useless lib
      try to support event page
      use https protocol
      Update plugin.douyutv

trocknet <trocknet@github> (1):
      plugins.afreeca: Fix HLS stream.

whizzoo <grenardus@gmail.com> (2):
      Add RTLXL plugin
      Add RTLXL plugin

wolftankk <wolftankk@gmail.com> (3):
      get azubu live status from api
      use new api get stream info
      fix video_player error
```
