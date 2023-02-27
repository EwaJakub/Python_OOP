import unittest
from unittest.mock import patch, call

import exercise


class TraderTestCase(unittest.TestCase):
    def test_wallet_does_not_change_if_waiting_using_c_or_czekaj_or_empty(self):
        with patch('exercise.input') as inp, patch('exercise.print') as prt:
            inp.side_effect = ['c', 'czekaj', '', '', '']
            exercise.main([5, 5, 5, 5, 5])

    def test_wallet_buying_using_kup(self):
        with patch('exercise.input') as inp, patch('exercise.print') as prt:
            inp.side_effect = ['c', 'c', 'kup', '', '']
            exercise.main([2, 2, 5, 2, 3])
        prt.assert_called_with('Twój wynik: 60.0zł!')

    def test_wallet_buying_using_k(self):
        with patch('exercise.input') as inp, patch('exercise.print') as prt:
            inp.side_effect = ['', '', 'k', '', '']
            exercise.main([2, 2, 5, 2, 3])
        prt.assert_called_with('Twój wynik: 60.0zł!')

    def test_wallet_selling_using_sprzedaj(self):
        with patch('exercise.input') as inp, patch('exercise.print') as prt:
            inp.side_effect = ['c', 'c', 'k', 'sprzedaj', '']
            exercise.main([2, 2, 5, 2, 3])
        prt.assert_called_with('Twój wynik: 40.0zł!')

    def test_wallet_selling_using_s(self):
        with patch('exercise.input') as inp, patch('exercise.print') as prt:
            inp.side_effect = ['c', 'c', 'k', 's', '']
            exercise.main([2, 2, 5, 2, 3])
        prt.assert_called_with('Twój wynik: 40.0zł!')

    def test_asking_again_for_correct_command(self):
        with patch('exercise.input') as inp, patch('exercise.print') as prt:
            inp.side_effect = ['c', 'c', 'Počkejte', 'c', 'k', 's']
            exercise.main([2, 2, 2, 4, 8])
        prt.assert_has_calls(
            [call('Niepoprawny wybór: Počkejte'), call('Twój wynik: 200.0zł!')],
            any_order=True
        )

    def test_selling_with_no_usd_does_not_change_wallet(self):
        with patch('exercise.input') as inp, patch('exercise.print') as prt:
            inp.side_effect = ['c', 'c', 's', 's', '']
            exercise.main([2, 3, 4, 5, 6])
        prt.assert_called_with('Twój wynik: 100.0zł!')

    def test_buying_with_no_pln_does_not_change_wallet(self):
        with patch('exercise.input') as inp, patch('exercise.print') as prt:
            inp.side_effect = ['c', 'k', 'k', 'k', 's']
            exercise.main([3, 4, 5, 6, 7])
        prt.assert_called_with('Twój wynik: 175.0zł!')
