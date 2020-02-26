#!/usr/bin/env python3

""" AD1459, an IRC Client

  Copyright ©2019-2020 by Gaven Royer

  Permission to use, copy, modify, and/or distribute this software for any
  purpose with or without fee is hereby granted, provided that the above
  copyright notice and this permission notice appear in all copies.

  THE SOFTWARE IS PROVIDED "AS IS" AND ISC DISCLAIMS ALL WARRANTIES WITH REGARD
  TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND
  FITNESS. IN NO EVENT SHALL ISC BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR
  CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE,
  DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS
  ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS
  SOFTWARE.

  The IRC client object.
"""

import asyncio
import logging
import time
import datetime
import random

class TestClient():
    """ This is the actual IRC Client. 

    Most of this functionality is provided by Pydle.
    """

    channels = {
        '##Bestnext': {
            'users': {
                'AnIowathetogumbsai',
                'Rehiinvasive',
                'Hispumpjack',
                'Vaccinate',
                'Aptsallows',
                'Arpnerhooyah',
                'Xisleastfoul',
                'VisalTheapodalilkars',
                'Yougroined',
                'Ayegoldarnit',
                'AckErie',
                'Libyanhalest',
                'Uffdaheresy_',
                'Intangibly',
                'Allsimoleans',
                'Fryless',
                'Extemporised',
                'Hobpaparabic',
                'Mesathecults',
                'Hobpaparabic|cloud_',
                'ChanServ',
                'Uglilybigowt',
                'Shejudders',
                'Hobandeye',
                'Mehandskylit-',
                'Nextandacest',
                'Esquired',
                'Compoesedly',
                'Runandgibbed',
                'Awwharumph',
                'Whygackadieu',
                'Whaddayawant',
            },
            'modes': {
                'o': ['ChanServ'],
                'C': True,
                'c': True,
                'i': True,
                'n': True,
                's': True,
            },
            'topic': 'It caught him off guard that space smelled of seared steak.',
            'topic_by': 'Hispumpjack',
            'topic_set': datetime.datetime(2019, 12, 11, 14, 46, 32),
            'created': datetime.datetime(2015, 3, 11, 18, 10, 39),
            'password': None,
            'banlist': None,
            'public': False,
            'exceptlist': None,
            'inviteexceptlist': None,
        },
        '##Akehighly': {
            'users': {
                'Yourperiwigs',
                'AnIowathetogumbsai',
                'Yourpus',
                'Awklabilenet',
                'Rehiinvasive',
                'TogoLaosnoir',
                'Hispumpjack',
                'Thesticklers',
                'Ourrelishes',
                'Niuebothgyps',
                'Bingokick',
                'Youintrust[m]',
                'Weerandsurer',
                'SagydeafUtah',
                'SineDeviance',
                'Aptsallows',
                'Vaccinate',
                'Thekeffiyehs',
                'Xisleastfoul',
                'Leastandmost',
                'VisalTheapodalilkars',
                'Yougroined',
                'Iranforplute',
                'Ayegoldarnit',
                'AckErie',
                'Hitandmobbed',
                'Howtoovainly',
                'Libyanhalest',
                'Wootright-oh',
                'Yup',
                'Uffdaheresy_',
                'Kapow',
                'Yourwideness',
                'Themostpurls',
                'Allsimoleans',
                'Allweervangs',
                'Yourton',
                'Extemporised',
                'Hobpaparabic',
                'Fryless',
                'Fobtoy',
                'Hobpaparabic|cloud_',
                'Mostnextmost^2',
                'Youbaggsed',
                'Shejudders',
                'Anymostgists',
                'Hobandeye',
                'Bothoks',
                'Utahallcrops',
                'Peopledurged[m]',
                'Mehandskylit-',
                'Woahgrrmyass',
                'Theyembayed',
                'PulAlgeria',
                'Guest49835',
                'Okshetrotund',
                'Compoesedly',
                'Herlastshoat',
                'Youparqueted',
                'Whaddayawant',
                'Boweddyed',
                'Indecently',
                'Runandgibbed',
                'Woahgrrmyass_work',
                'Ourbestbleep',
                'Theyaxe',
                'FlagQatarfar',
                'Awwharumph',
                'Herlastzoa',
                'Mostdot',
                'Theybay',
                'Theyaddeemed',
                'Volaranddang',
                'Urigreediest',
                'Anytinierres',
            },
            'modes': {
                'c': True,
                'g': True,
                'n': True,
                't': True,
            },
            'topic': 'He had a hidden stash underneath the floorboards in the back room of the house.',
            'topic_by': 'Awwharumph',
            'topic_set': datetime.datetime(2016, 6, 21, 10, 51, 29),
            'created': datetime.datetime(2013, 9, 6, 11, 49, 28),
            'password': None,
            'banlist': None,
            'public': True,
            'exceptlist': None,
            'inviteexceptlist': None,
        },
        '##Bestmostlast': {
            'users': {
                'TexasNamibia',
                'Lessdoped',
                'Allmostdolls',
                'Achyweeds',
                'Hapandhugs',
                'Acericier',
                'Anypawpaw',
                'Allsassydahs',
                'Deing',
                'Anylycees',
                'Utahandseers',
                'Shepsalmed',
                'Enchanted',
                'Bowserinator',
                'Hisdirestfee1',
                'Pithierdors',
                'Anaglyphic',
                'Berksacer',
                'ChanServ',
                'Obiandpayola',
                'Atiltwhy',
                'Yetbrusquely',
                'Yourpolyol',
                'Barairbagpap',
                'Leastandlast',
                'Getnogprose',
                'Compoesedly',
                'Bothovations',
                'Prodsmore',
                'Yousensitize',
                'Boothsfreest',
                'PopplipOman',
                'Lycianummary',
                'Toonieatt',
                'Bestmostlast',
                'Yeuchhee-',
            },
            'modes': {
                'o': [
                    'Toonieatt',
                    'Anypawpaw',
                    'Berksacer',
                    'ChanServ',
                    'Shepsalmed',
                    'Bestmostlast',
                    'Yousensitize',
                    'Bothovations',
                    'PopplipOman',
                    'Obiandpayola',
                    'Pithierdors',
                    'Atiltwhy',
                    'Yourpolyol',
                    'Leastandlast',
                    'Yeuchhee-',
                    'Lessdoped',
                    'Allsassydahs',
                    'Hisdirestfee1',
                    'Yetbrusquely',
                    'Boothsfreest',
                    'Utahandseers',
                    'Deing',
                    'Anaglyphic',
                    'Prodsmore',
                    'Achyweeds',
                    'Getnogprose',
                    'TexasNamibia',
                    'Allmostdolls',
                    'Enchanted',
                ],
                'g': True,
                'n': True,
                'p': True,
                'r': True,
                's': True,
                't': True,
            },
            'topic': "Welcome to ##Bestmostlast where everyone says they love nature until they realize how dangerous she can be.",
            'topic_by': 'Bestmostlast',
            'topic_set': datetime.datetime(2020, 1, 22, 17, 56, 56),
            'created': datetime.datetime(2013, 5, 20, 19, 1, 53),
            'password': None,
            'banlist': None,
            'public': False,
            'exceptlist': None,
            'inviteexceptlist': None,
        },
        '##Kobcloser': {
            'users': {
                'Anylastvet',
                'Lessdoped',
                'Allmostdolls',
                'Nexttaffy',
                'Acericier',
                'Allsassydahs',
                'Shepsalmed',
                'Ta-da',
                'OurAfrica',
                'Anaglyphic',
                'Berksacer',
                'ChanServ',
                'Atiltwhy',
                'Yetbrusquely',
                'Yourpolyol',
                'Theykindle',
                'Leastandlast',
                'Compoesedly',
                'Boweddyed',
                'Anytipi',
                'PopplipOman',
                'Bestmostlast',
            },
            'modes': {
                'o': [
                    'Berksacer',
                    'Ta-da',
                    'ChanServ',
                    'Shepsalmed',
                    'Anylastvet',
                    'Theykindle',
                    'Bestmostlast',
                    'Anytipi',
                    'PopplipOman',
                    'Atiltwhy',
                    'Boweddyed',
                    'Yourpolyol',
                    'Leastandlast',
                    'Allsassydahs',
                    'Yetbrusquely',
                    'Anaglyphic',
                    'Allmostdolls',
                    'Nexttaffy',
                ],
                'v': ['Lessdoped'],
                's': True,
            },
            'topic': "Someone I know recently combined Maple Syrup & buttered Popcorn thinking it would taste like caramel popcorn. It didn’t and they don’t recommend anyone else do it either. | ❤️🧡💛💚💙💜 | 💛⚪💜🖤 | 💜🌸💛💚",
            'topic_by': 'Boweddyed',
            'topic_set': datetime.datetime(2019, 6, 23, 21, 18, 8),
            'created': datetime.datetime(2012, 2, 24, 0, 23, 27),
            'password': None,
            'banlist': None,
            'public': False,
            'exceptlist': None,
            'inviteexceptlist': None,
        },
        '##Corerpeddler': {
            'users': {
                'Lastleast',
                'Xismilder',
                'Sheundercuts',
                'Taxfaster',
                'Liedset',
                'Vapidly[m]',
                'Allobi',
                'Thexerox',
                'Anythink',
                'Theyscut',
                'Anyjoki',
                'Shekeeps',
                'Waheyhoo',
                'Soxacest',
                'HooFargo',
                'Hollasox',
                'Libyaova',
                'Weeracer',
                'Nilegray',
                'Uneasily',
                'Yourworkings',
                'YuckKiribati',
                'Kif',
                'Acertapeworm',
                'Yepsnakily',
                'Newermorefey',
                'Wetandsnuffy',
                'Themostpurls',
                'Coronatheegg',
                'Yetlongtoday',
                'ShuckDenmark',
                'Laosbayirony',
                'Epigyneshymn',
                'Shelevels',
                'Yourstrake',
                'Fastheyoorah',
                'Weergrenades',
                'Weaponless',
                'Zoagrabbiest',
                'Dismayinject',
                'Thesoftersai',
                'Cuzdartingly',
                'Anylastvet',
                'Anaesthetize',
                'Lessawedweer',
                'Shegis',
                'Ourevocators',
                'Geez',
                'Chadfortowns',
                'Theouthouse',
                'DueWacoChina',
                'Ardlipfringe[]',
                'Yourweersops',
                'ChanServ',
                'Sherated',
                'Sheclagged',
                'Perudam',
                'Gutandcoital-IRC',
                'Compoesedly',
                'Anotherlure',
                'Sherecants',
                'Theyessayed',
                'Youknowburrs',
                'LaosandFiji',
                'Setbestirred',
                'Sheculched',
                'Resandyakalo',
                'EthandBurma',
                'Youshinned[m]2',
                'Corerpeddler',
                'Laterandless',
                'Oversea',
                'Tollsnippier',
                'Agalspilalux',
                'Ohiofromuri',
                'Anyboxiersap',
                'Sheburdens',
                'Acerdankness',
                'Allteethers',
                'Uglilybigowt',
                'Erieforjunks',
                'Moreandhuger',
                'Barairbagpap',
                'Houndedeaten',
                'Anyscuppers',
                'EmoapoGuyana',
                'Cagyandnyc',
                'Erieallbinds',
                'Zaphuzzashit',
            },
            'modes': {
                'v': [
                    'LaosandFiji',
                    'Thexerox',
                    'Weergrenades',
                    'Sheundercuts',
                    'Libyaova',
                    'Anythink',
                    'Dismayinject',
                    'ChanServ',
                    'ShuckDenmark',
                    'Sheclagged',
                    'DueWacoChina',
                    'Anylastvet',
                    'Erieforjunks',
                    'Uneasily',
                    'Taxfaster',
                    'Shelevels',
                    'Theyessayed',
                    'Geez',
                    'Resandyakalo',
                    'Sherecants',
                    'Corerpeddler',
                    'EthandBurma',
                    'Themostpurls',
                    'Laosbayirony',
                    'Waheyhoo',
                    'Zoagrabbiest',
                    'Anyjoki',
                    'Newermorefey',
                    'Epigyneshymn',
                    'Agalspilalux',
                    'Youshinned[m]2',
                    'Weeracer',
                    'Chadfortowns',
                    'Yourstrake',
                    'Anyscuppers',
                    'Yetlongtoday',
                    'EmoapoGuyana',
                    'Soxacest',
                    'Anaesthetize',
                    'Ardlipfringe[]',
                    'Anotherlure',
                    'Cagyandnyc',
                    'Erieallbinds',
                    'Theouthouse',
                    'Shegis',
                    'Vapidly[m]',
                    'Lastleast',
                    'Sherated',
                    'Kif',
                    'Coronatheegg',
                    'Allobi',
                    'Tollsnippier',
                    'Compoesedly',
                    'Lessawedweer',
                    'Shekeeps',
                    'Sheculched',
                    'Barairbagpap',
                    'Ohiofromuri',
                    'Anyboxiersap',
                    'Wetandsnuffy',
                    'Cuzdartingly',
                    'Moreandhuger',
                    'Uglilybigowt',
                    'Liedset',
                    'Fastheyoorah',
                    'Weaponless',
                    'Nilegray',
                    'Acertapeworm',
                    'Ourevocators',
                    'Zaphuzzashit',
                    'Gutandcoital-IRC',
                    'Xismilder',
                    'Allteethers',
                    'Setbestirred',
                    'Laterandless',
                    'HooFargo',
                    'Oversea',
                    'Yourweersops',
                    'Yourworkings',
                    'Theyscut',
                    'Thesoftersai',
                    'Hollasox',
                    'Perudam',
                    'Sheburdens',
                    'Yepsnakily',
                    'Houndedeaten',
                    'YuckKiribati',
                    'Acerdankness',
                ],
                'o': [
                    'ChanServ',
                    'Geez',
                    'Corerpeddler',
                    'Yourstrake',
                    'Ohiofromuri',
                    'Youknowburrs',
                    'Nilegray',
                ],
                'C': True,
                'g': True,
                'n': True,
                's': True,
                't': True,
            },
            'topic': 'Tuesdays are free if you bring a gnome costume.',
            'topic_by': 'Corerpeddler',
            'topic_set': datetime.datetime(2020, 1, 21, 22, 35, 57),
            'created': datetime.datetime(2017, 2, 5, 18, 7, 51),
            'password': None,
            'banlist': None,
            'public': False,
            'exceptlist': None,
            'inviteexceptlist': None,
        },
        '##Consyen': {
            'users': {
                'Trickortreat',
                'Vimstwinjets',
                'Anymoreknife',
                'Omananyclegg',
                'Sheundercuts',
                'Thelaw',
                'Yourbumatt',
                'Lastandworst',
                'Acerbedstead',
                'Bothbesttens',
                'Hisdirestfee2',
                'Hisdirestfee1',
                'Annexandsop',
                'Sleekbadwhat',
                'Anaglyphic',
                'Obiandpayola',
                'Redshadowily',
                'Anyeneclann',
                'Leguminous',
                'Laoslynagger',
                'CaYoushinneddfrets',
                'Zapmartlets',
                'Yeehacoats',
                'Boothsfreest',
                'PopplipOman',
                'Chadjammed',
                'TexasNamibia',
                'Samoaanyvug',
                'Cubaforteddy',
                'Oftloudlynrn',
                'Peacefully',
                'Uhuhabrasion',
                'Achyweeds',
                'Cupandangels',
                'Erieforgriot',
                'Bothliponyms',
                'Hissloops`',
                'Acerandacer',
                'Newermorefey',
                'Cerebralised',
                'Anyrumcircle',
                'Hisgadfly',
                'Pithierdors',
                'Keesbossiest',
                'Heracersurds',
                'Yetbrusquely',
                'Iowathetog',
                'Yourpolyol',
                'Leastandlast',
                'Getnogprose',
                'Powoopshurry',
                'Anotherlupin',
                'Egyptwithpul',
                'Pssst',
                'Yeuchhee-',
                'Tzarinanog',
                'Pewgrowler',
                'Erieanyarson',
                'TinfaderTogo',
                'Theydisleave',
                'Hapandhugs',
                'Yourdalmatic',
                'Theirmen',
                'Anothertole',
                'Allsassydahs',
                'Anylycees',
                'Worstonset',
                'Yourweersops',
                'Sherated',
                'Atiltwhy',
                'Ouricedbarbs',
                'QatarandGuam',
                'Perspiculate',
                'Theykindle',
                'lykos',
                'Compoesedly',
                'Pisandmagnum',
                'Bothovations',
                'Yousensitize',
                'Wacooddcrisp',
                'Next',
                'Awwcalfskin',
                'Theyessayed',
                'Bosniaandfry',
                'Iraqthemoans',
                'Hit',
                'Allmostdolls',
                'Palauanyxis',
                'Deing',
                'Hisgoatfish',
                'Bestleastpop',
                'Utahandseers',
                'Shepsalmed',
                'Lessandtamer',
                'DorandIsrael',
                'CaYoushinnedyearls',
                'Parentally',
                'AnIowathetogexttulip',
                'Acerdankness',
                'Anytime',
                'Kidbadmazdas',
                'Congratsouch',
                'Lagdymbanian-1',
                'Ickhuzza',
                'Theirnature',
                'Kipandcareen',
                'Barairbagpap',
                'Great',
                'Ourcringers',
                'Idahowithwiz',
                'Uriwonukases',
                'Miscibly',
                'Boweddyed',
                'Acermoreless',
                'Anyslowness',
                'Woogackpeace',
                'Lycianummary',
                'Theapodalilk',
                'Hislastferes',
                'Ghanathissex',
                'Bestmostlast',
            },
            'modes': {
                'o': ['lykos'],
                'C': True,
                'j': '5:10',
                'n': True,
                'r': True,
                't': True,
            },
            'topic': 'The irony of the situation wasn\'t lost on anyone in the room.',
            'topic_by': 'Oftloudlynrn',
            'topic_set': datetime.datetime(2019, 12, 31, 15, 38, 38),
            'created': datetime.datetime(2011, 4, 3, 22, 49, 18),
            'password': None,
            'banlist': None,
            'public': True,
            'exceptlist': None,
            'inviteexceptlist': None,
        },
        '#ad1459': {
            'users': {
                'ChanServ',
                'LordYoushinned',
                'Compoesedly',
            },
            'modes': {
                'o': ['ChanServ'],
                'n': True,
                't': True,
            },
            'topic': 'AD1459 is an open-source (ISC) IRC client Sleekbadwhatten in Python and GTK3. | This channel is for discussion and questions about AD1459 | https://pypi.org/project/ad1459/ | https://github.com/g4vr0che/ad1459',
            'topic_by': 'Compoesedly',
            'topic_set': datetime.datetime(2020, 1, 20, 9, 36, 55),
            'created': datetime.datetime(2020, 1, 6, 12, 13, 11),
            'password': None,
            'banlist': None,
            'public': True,
            'exceptlist': None,
            'inviteexceptlist': None,
        },
        '#Connaffer': {
            'users': {
                'AnIowathetogumbsai',
                'Rehiinvasive',
                'Paxandtagger',
                'Shut',
                'Hispumpjack',
                'Laoslilyukky',
                'Weerandsurer',
                'Aptsallows',
                'Xisleastfoul',
                'Thereps',
                'EbbBhutan',
                'Iranforplute',
                'Herlipoicmug',
                'Oururi',
                'Ayegoldarnit',
                'Intangibly',
                'Allsimoleans',
                'Hobpaparabic',
                'Mesathecults',
                'Hobpaparabic|cloud_',
                'ChanServ',
                'Shejudders',
                'AttanHerlipoicmugovels',
                'Mehandskylit-',
                'Theyembayed',
                'Compoesedly',
                'Sherefused',
                'Awwharumph',
                'Whygackadieu',
                'Whaddayawant',
            },
            'modes': {
                'o': ['ChanServ'],
                'c': True,
                'g': True,
                'n': True,
            },
            'topic': 'Sometimes I stare at a door or a wall and I wonder what is this reality, why am I alive, and what is this all about?',
            'topic_by': 'Rehiinvasive',
            'topic_set': datetime.datetime(2020, 1, 21, 21, 53, 36),
            'created': datetime.datetime(2009, 2, 22, 21, 38, 51),
            'password': None,
            'banlist': None,
            'public': True,
            'exceptlist': None,
            'inviteexceptlist': None,
        },
        '##Yereither': {
            'users': {
                'Hobpaparabic',
                'Bothovations',
                'Hobpaparabic|cloud_',
                'KinmehMekong',
                'Allbestviews',
                'Allsassydahs',
                'Compoesedly',
            },
            'modes': {
                'g': True,
                'n': True,
            },
            'topic': "Girl, we got a good thing. And I don't see this ending. Do you want to fly? Do you want to flee? Do you want to get away with me? Do you want to face the great unknown?",
            'topic_by': 'Compoesedly',
            'topic_set': datetime.datetime(2017, 9, 11, 22, 38 ,27),
            'created': datetime.datetime(2015, 9, 20, 12, 21, 44),
            'password': None,
            'banlist': None,
            'public': True,
            'exceptlist': None,
            'inviteexceptlist': None,
        },
    }

    connected = True

    def __init__(self, nick, network, sasl_username=None, sasl_password=None, **kwargs):
        self.log = logging.getLogger('ad1459.testclient')
        self.nick = nick
        self.network_ = network
        self.log.debug('Created client for network %s', self.network_.name)
        self.bouncer = False
        self.eventloop = asyncio.get_event_loop()
    
    def run(self, *args, **kwargs):
        """ Connect and run bot in event loop. """
        self.eventloop.run_until_complete(self.connect(*args, **kwargs))
        try:
            self.eventloop.run_forever()
        finally:
            self.eventloop.stop()
    
    async def connect(self, hostname=None, password=None, **kwargs):
        self.log.debug('Client initiating connection to %s', hostname)
        
    
    async def on_connect(self):
        self.log.info('Connected to %s', self.network_.name)
        
        await self.network_.on_connected()

    
    async def on_raw(self, message):
        if message.command == ('CAP' or 'cap' or 'Cap'):
            if 'znc.in/' in " ".join(message.params):
                self.log.debug('Server appears to be a ZNC Bouncer')
                self.bouncer = True
        
        
    
    async def on_nick_change(self, old, new):
        self.log.debug('User %s is now %s', old, new)
        await self.network_.on_nick_change(old, new)
    
    async def set_nickname(self, nickname):
        self.log.debug('Got set_nickname in testing')
        await self.network_.on_nick_change(self.nick, nickname)
        self.nick = nickname
        
    
    async def on_join(self, channel, user):
        self.log.debug(f'User {user} joined {channel} on {self.network_.name}')
        await self.network_.on_join(channel, user)
    
    async def join(self, channel, password=None):
        self.log.debug('Got join in testing')
        await self.network_.on_join(channel, self.nick)
        
    
    async def on_part(self, channel, user, message=None):
        self.log.debug(f'User {user} parted {channel} on {self.network_.name}')
        await self.network_.on_part(channel, user, message=message)
    
    async def part(self, channel, message=None):
        self.log.debug('Got part in testing')
        await self.network_.on_part(channel, self.nick, message=message)
    
    async def on_kick(self, channel, target, by, reason=None):
        self.log.debug('%s was kicked from %s by %s (%s)', target, channel, by, reason)
        await self.network_.on_kick(channel, target, by, reason=reason)
        
    
    async def on_quit(self, user, message=None):
        self.log.debug(f'User {user} has quit {self.network_.name}')
        await self.network_.on_quit(user, message=message)
        
    
    async def on_kill(self, target, by, reason):
        self.log.debug('%s was killed by %s, (%s)', target, by, reason)
        await self.network_.on_kill(target, by, reason=reason)
        

    async def on_message(self, target, source, message):
        self.log.debug('New message in %s from %s: %s', target, source, message)
        await self.network_.on_message(target, source, message)
    
    async def message(self, target, message):
        self.log.debug('Got message in testing')
        nick = random.sample(self.channels[target]['users'], 1)[0]
        self.log.debug('Sending message from %s to %s', nick, target)
        await self.network_.on_message(target, nick, message)
        
    
    async def on_notice(self, target, by, message):
        self.log.debug('Received notice to %s from %s', target, by)
        await self.network_.on_notice(target, by, message)
    
    async def notice(self, target, message):
        self.log.debug('Got notice in testing')

        await self.network_.on_notice(target, self.nick, message)
    
    async def on_private_message(self, target, by, message):
        self.log.debug('New private message to %s from %s: %s', target, by, message)
        await self.network_.on_private_message(target, by, message)
        
    
    async def on_private_notice(self, target, by, message):
        self.log.debug('Received private notice to %s from %s', target, by)
        await self.network_.on_private_notice(target, by, message)
        
    
    async def on_mode_change(self, channel, modes, by):
        self.log.debug('%s set modes %s in %s', by, modes, channel)
        await self.network_.on_mode_change(channel, modes, by)
        
    
    async def on_topic_change(self, channel, message, by):
        self.log.debug('Topic in %s set to "%s" by %s', channel, message, by)
        await self.network_.on_topic_change(channel, message, by)
    
    async def set_topic (self, channel, topic):
        self.log.debug('Got set_topic in testing')
        await self.network_.on_topic_change(channel, topic, self.nick)
    
    async def on_user_invite(self, target, channel, by):
        self.log.debug('%s was invited to %s by %s', target, channel, by)
        await self.network_.on_user_invite(target, channel, by)
        

    async def on_invite(self, channel, by):
        self.log.debug('Invited to %s by %s', channel, by)
        await self.network_.on_invite(channel, by)
        
    
    # CTCP Support

    async def on_ctcp(self, by, target, what, contents):
        self.log.debug('%s received CTCP %s from %s: %s', target, what, by, contents)
        
    
    async def on_ctcp_reply(self, by, target, what, contents):
        self.log.debug('%s received REPLY CTCP %s from %s: %s', target, what, by, contents)
        

    async def on_ctcp_action(self, by, target, contents):
        await self.network_.on_ctcp_action(target, by, contents)