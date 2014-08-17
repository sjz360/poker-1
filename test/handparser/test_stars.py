from decimal import Decimal
from datetime import datetime
from collections import namedtuple
import pytz
import pytest
from poker.handhistory import HandHistoryPlayer
from poker.room.pokerstars import PokerStarsHandHistory
from poker.card import Card
from poker.hand import Combo
from . import stars_hands


ET = pytz.timezone('US/Eastern')


@pytest.fixture
def hand(request):
    """Parse handhistory defined in hand_text class attribute and returns a PokerStarsHandHistory instance."""
    return PokerStarsHandHistory(request.instance.hand_text)


@pytest.fixture
def hand_header(request):
    """Parse hand history header only defined in hand_text and returns a PokerStarsHandHistory instance."""
    h = PokerStarsHandHistory(request.instance.hand_text, parse=False)
    h.parse_header()
    return h


class TestHandWithFlopOnly:
    hand_text = stars_hands.HAND1
    # in py.test 2.4 it is recommended to use string like "attribute,expected",
    # but with tuple, it works in both 2.3.5 and 2.4
    @pytest.mark.parametrize(('attribute', 'expected_value'),
                             [('poker_room', 'STARS'),
                              ('ident', '105024000105'),
                              ('game_type', 'TOUR'),
                              ('tournament_ident', '797469411'),
                              ('tournament_level', 'I'),
                              ('currency', 'USD'),
                              ('buyin', Decimal('3.19')),
                              ('rake', Decimal('0.31')),
                              ('game', 'HOLDEM'),
                              ('limit', 'NL'),
                              ('sb', Decimal(10)),
                              ('bb', Decimal(20)),
                              ('date', ET.localize(datetime(2013, 10, 4, 13, 53, 27)))
                             ])
    def test_values_after_header_parsed(self, hand_header, attribute, expected_value):
        assert getattr(hand_header, attribute) == expected_value

    @pytest.mark.parametrize(('attribute', 'expected_value'),
                             [('table_name', '797469411 15'),
                              ('max_players', 9),
                              ('button_seat', 1),
                              ('button', HandHistoryPlayer(name='flettl2', stack=1500, seat=1,
                                                           combo=None)
                              ),
                              ('hero', HandHistoryPlayer(
                                        name='W2lkm2n', stack=3000, seat=5, combo=Combo('AcJh')),
                              ),
                              ('players', [
                               HandHistoryPlayer(name='flettl2', stack=1500, seat=1, combo=None),
                               HandHistoryPlayer(name='santy312', stack=3000, seat=2, combo=None),
                               HandHistoryPlayer(name='flavio766', stack=3000, seat=3, combo=None),
                               HandHistoryPlayer(name='strongi82', stack=3000, seat=4, combo=None),
                               HandHistoryPlayer(name='W2lkm2n', stack=3000, seat=5, combo=Combo('AcJh')),
                               HandHistoryPlayer(name='MISTRPerfect', stack=3000, seat=6, combo=None),
                               HandHistoryPlayer(name='blak_douglas', stack=3000, seat=7, combo=None),
                               HandHistoryPlayer(name='sinus91', stack=1500, seat=8, combo=None),
                               HandHistoryPlayer(name='STBIJUJA', stack=1500, seat=9, combo=None),
                               ]),
                              ('flop', (Card('2s'), Card('6d'), Card('6h'))),
                              ('turn', None),
                              ('river', None),
                              ('board', (Card('2s'), Card('6d'), Card('6h'))),
                              ('preflop_actions', ("strongi82: folds",
                                                   "W2lkm2n: raises 40 to 60",
                                                   "MISTRPerfect: calls 60",
                                                   "blak_douglas: folds",
                                                   "sinus91: folds",
                                                   "STBIJUJA: folds",
                                                   "flettl2: folds",
                                                   "santy312: folds",
                                                   "flavio766: folds")),
                              ('flop_actions', ('W2lkm2n: bets 80',
                                                'MISTRPerfect: folds',
                                                'Uncalled bet (80) returned to W2lkm2n',
                                                'W2lkm2n collected 150 from pot',
                                                "W2lkm2n: doesn't show hand")),
                              ('turn_actions', None),
                              ('river_actions', None),
                              ('total_pot', Decimal(150)),
                              ('show_down', False),
                              ('winners', ('W2lkm2n',)),
                              ])
    def test_body(self, hand, attribute, expected_value):
        assert getattr(hand, attribute) == expected_value


class TestAllinPreflopHand:
    hand_text = stars_hands.HAND2

    @pytest.mark.parametrize(('attribute', 'expected_value'),
                             [('poker_room', 'STARS'),
                              ('ident', '105034215446'),
                              ('game_type', 'TOUR'),
                              ('tournament_ident', '797536898'),
                              ('tournament_level', 'XI'),
                              ('currency', 'USD'),
                              ('buyin', Decimal('3.19')),
                              ('rake', Decimal('0.31')),
                              ('game', 'HOLDEM'),
                              ('limit', 'NL'),
                              ('sb', Decimal(400)),
                              ('bb', Decimal(800)),
                              ('date', ET.localize(datetime(2013, 10, 4, 17, 22, 20))),
                              ])
    def test_values_after_header_parsed(self, hand_header, attribute, expected_value):
        assert getattr(hand_header, attribute) == expected_value

    @pytest.mark.parametrize(('attribute', 'expected_value'),
                             [('table_name', '797536898 9'),
                              ('max_players', 9),
                              ('button_seat', 2),
                              ('button', HandHistoryPlayer(name='W2lkm2n', stack=11815, seat=2,
                                            combo=Combo('JdJs'))
                              ),
                              ('hero', HandHistoryPlayer(name='W2lkm2n', stack=11815, seat=2,
                                    combo=Combo('JdJs'))
                              ),
                              ('players', [
                               HandHistoryPlayer(name='RichFatWhale', stack=12910, seat=1, combo=None),
                               HandHistoryPlayer(name='W2lkm2n', stack=11815, seat=2, combo=Combo('JdJs')),
                               HandHistoryPlayer(name='Labahra', stack=7395, seat=3, combo=None),
                               HandHistoryPlayer(name='Lean Abadia', stack=7765, seat=4, combo=None),
                               HandHistoryPlayer(name='lkenny44', stack=10080, seat=5, combo=None),
                               HandHistoryPlayer(name='Newfie_187', stack=1030, seat=6, combo=None),
                               HandHistoryPlayer(name='Hokolix', stack=13175, seat=7, combo=None),
                               HandHistoryPlayer(name='pmmr', stack=2415, seat=8, combo=None),
                               HandHistoryPlayer(name='costamar', stack=13070, seat=9, combo=None),
                               ]),
                              ('flop', (Card('3c'), Card('6s'), Card('9d'))),
                              ('turn', Card('8d')),
                              ('river', Card('Ks')),
                              ('board', (Card('3c'), Card('6s'), Card('9d'), Card('8d'), Card('Ks'))),
                              ('preflop_actions', ("lkenny44: folds",
                                                   "Newfie_187: raises 155 to 955 and is all-in",
                                                   "Hokolix: folds",
                                                   "pmmr: folds",
                                                   "costamar: raises 12040 to 12995 and is all-in",
                                                   "RichFatWhale: folds",
                                                   "W2lkm2n: calls 11740 and is all-in",
                                                   "Labahra: folds",
                                                   "Lean Abadia: folds",
                                                   "Uncalled bet (1255) returned to costamar")),
                              ('flop_actions', None),
                              ('turn_actions', None),
                              ('river_actions', None),
                              ('total_pot', Decimal(26310)),
                              ('show_down', True),
                              ('winners', ('costamar',)),
                              ])
    def test_body(self, hand, attribute, expected_value):
        assert getattr(hand, attribute) == expected_value


class TestBodyMissingPlayerNoBoard:
    hand_text = stars_hands.HAND3

    @pytest.mark.parametrize(('attribute', 'expected_value'),
                             [('poker_room', 'STARS'),
                              ('ident', '105026771696'),
                              ('game_type', 'TOUR'),
                              ('tournament_ident', '797469411'),
                              ('tournament_level', 'X'),
                              ('currency', 'USD'),
                              ('buyin', Decimal('3.19')),
                              ('rake', Decimal('0.31')),
                              ('game', 'HOLDEM'),
                              ('limit', 'NL'),
                              ('sb', Decimal(300)),
                              ('bb', Decimal(600)),
                              ('date', ET.localize(datetime(2013, 10, 4, 14, 50, 56)))
                             ])
    def test_values_after_header_parsed(self, hand_header, attribute, expected_value):
        assert getattr(hand_header, attribute) == expected_value

    @pytest.mark.parametrize(('attribute', 'expected_value'),
                             [('table_name', '797469411 11'),
                              ('max_players', 9),
                              ('button_seat', 8),
                              ('button', HandHistoryPlayer(name='W2lkm2n', stack=10714, seat=8, combo=Combo('6d8d'))),
                              ('hero', HandHistoryPlayer(name='W2lkm2n', stack=10714, seat=8, combo=Combo('6d8d'))),
                              ('players', [
                               HandHistoryPlayer(name='Empty Seat 1', stack=0, seat=1, combo=None),
                               HandHistoryPlayer(name='snelle_jel', stack=4295, seat=2, combo=None),
                               HandHistoryPlayer(name='EuSh0wTelm0', stack=11501, seat=3, combo=None),
                               HandHistoryPlayer(name='panost3', stack=7014, seat=4, combo=None),
                               HandHistoryPlayer(name='Samovlyblen', stack=7620, seat=5, combo=None),
                               HandHistoryPlayer(name='Theralion', stack=4378, seat=6, combo=None),
                               HandHistoryPlayer(name='wrsport1015', stack=9880, seat=7, combo=None),
                               HandHistoryPlayer(name='W2lkm2n', stack=10714, seat=8, combo=Combo('6d8d')),
                               HandHistoryPlayer(name='fischero68', stack=8724, seat=9, combo=None),
                               ]),
                              ('flop', None),
                              ('turn', None),
                              ('river', None),
                              ('board', None),
                              ('preflop_actions', ('EuSh0wTelm0: folds',
                                                   'panost3: folds',
                                                   'Samovlyblen: folds',
                                                   'Theralion: raises 600 to 1200',
                                                   'wrsport1015: folds',
                                                   'W2lkm2n: folds',
                                                   'fischero68: folds',
                                                   'snelle_jel: folds',
                                                   'Uncalled bet (600) returned to Theralion',
                                                   'Theralion collected 1900 from pot',
                                                   "Theralion: doesn't show hand")),
                              ('flop_actions', None),
                              ('turn_actions', None),
                              ('river_actions', None),
                              ('total_pot', Decimal(1900)),
                              ('show_down', False),
                              ('winners', ('Theralion',)),
                              ])
    def test_body(self, hand, attribute, expected_value):
        assert getattr(hand, attribute) == expected_value


class TestBodyEveryStreet:
    hand_text = stars_hands.HAND4

    @pytest.mark.parametrize(('attribute', 'expected_value'),
                             [('poker_room', 'STARS'),
                              ('ident', '105025168298'),
                              ('game_type', 'TOUR'),
                              ('tournament_ident', '797469411'),
                              ('tournament_level', 'IV'),
                              ('currency', 'USD'),
                              ('buyin', Decimal('3.19')),
                              ('rake', Decimal('0.31')),
                              ('game', 'HOLDEM'),
                              ('limit', 'NL'),
                              ('sb', Decimal(50)),
                              ('bb', Decimal(100)),
                              ('date', ET.localize(datetime(2013, 10, 4, 14, 19, 17)))
                             ])
    def test_values_after_header_parsed(self, hand_header, attribute, expected_value):
        assert getattr(hand_header, attribute) == expected_value

    @pytest.mark.parametrize(('attribute', 'expected_value'),
                             [('table_name', '797469411 15'),
                              ('max_players', 9),
                              ('button_seat', 5),
                              ('button', HandHistoryPlayer(name='W2lkm2n', stack=5145, seat=5, combo=Combo('Jc5c'))),
                              ('hero', HandHistoryPlayer(name='W2lkm2n', stack=5145, seat=5, combo=Combo('Jc5c'))),
                              ('players', [
                               HandHistoryPlayer(name='flettl2', stack=3000, seat=1, combo=None),
                               HandHistoryPlayer(name='santy312', stack=5890, seat=2, combo=None),
                               HandHistoryPlayer(name='flavio766', stack=11010, seat=3, combo=None),
                               HandHistoryPlayer(name='strongi82', stack=2855, seat=4, combo=None),
                               HandHistoryPlayer(name='W2lkm2n', stack=5145, seat=5, combo=Combo('Jc5c')),
                               HandHistoryPlayer(name='MISTRPerfect', stack=2395, seat=6, combo=None),
                               HandHistoryPlayer(name='blak_douglas', stack=3000, seat=7, combo=None),
                               HandHistoryPlayer(name='sinus91', stack=3000, seat=8, combo=None),
                               HandHistoryPlayer(name='STBIJUJA', stack=1205, seat=9, combo=None),
                               ]),
                              ('flop', (Card('6s'), Card('4d'), Card('3s'))),
                              ('turn', Card('8c')),
                              ('river', Card('Kd')),
                              ('board', (Card('6s'), Card('4d'), Card('3s'), Card('8c'), Card('Kd'))),
                              ('preflop_actions', ('sinus91: folds',
                                                   'STBIJUJA: folds',
                                                   'flettl2: raises 125 to 225',
                                                   'santy312: folds',
                                                   'flavio766: folds',
                                                   'strongi82: folds',
                                                   'W2lkm2n: folds',
                                                   'MISTRPerfect: folds',
                                                   'blak_douglas: calls 125')),
                              ('flop_actions', ('blak_douglas: checks',
                                                'flettl2: bets 150',
                                                'blak_douglas: calls 150')),
                              ('turn_actions', ('blak_douglas: checks',
                                                'flettl2: bets 250',
                                                'blak_douglas: calls 250')),
                              ('river_actions', ('blak_douglas: checks',
                                                 'flettl2: bets 1300',
                                                 'blak_douglas: folds',
                                                 'Uncalled bet (1300) returned to flettl2',
                                                 'flettl2 collected 1300 from pot',
                                                 "flettl2: doesn't show hand")),
                              ('total_pot', Decimal(1300)),
                              ('show_down', False),
                              ('winners', ('flettl2',)),
                              ])
    def test_body(self, hand, attribute, expected_value):
        assert getattr(hand, attribute) == expected_value


class TestClassRepresentation:
    hand_text = stars_hands.HAND1

    def test_unicode(self, hand_header):
        assert u'<PokerStarsHandHistory: STARS hand #105024000105>' == str(hand_header)

    def test_str(self, hand_header):
        assert '<PokerStarsHandHistory: STARS hand #105024000105>' == str(hand_header)


class TestPlayerNameWithDot:
    hand_text = stars_hands.HAND5

    def test_player_is_in_player_list(self, hand):
        assert '.prestige.U$' in [p.name for p in hand.players]

    def test_player_stack(self, hand):
        player_names = [p.name for p in hand.players]
        player_index = player_names.index('.prestige.U$')
        assert hand.players[player_index].stack == 3000
