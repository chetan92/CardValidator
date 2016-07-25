import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from cardvalidator import formatter


class TestFormatter(unittest.TestCase):
    def test_visa_number(self):
        """should identify a visa card numbers."""
        visa_number = 4024007183310266
        self.assertTrue(formatter.is_visa(visa_number))

    def test_visa_number_string(self):
        """should identify a visa card number strings."""
        visa_string = '4024007183310266'
        self.assertTrue(formatter.is_visa(visa_string))

    def test_visa_electron_number(self):
        """should identify visa electron card numbers."""
        visa_electron_number = 4175004688713760
        self.assertTrue(formatter.is_visa_electron(visa_electron_number))

    def test_visa_electron_number_string(self):
        """should identify visa electron card number strings."""
        visa_electron_string = '4175004688713760'
        self.assertTrue(formatter.is_visa_electron(visa_electron_string))

    def test_mastercard_number(self):
        """should identify mastercard card numbers."""
        mastercard_number = 5409219472999830
        self.assertTrue(formatter.is_mastercard(mastercard_number))

    def test_mastercard_number_string(self):
        """should identify mastercard card number strings."""
        mastercard_string = '5409219472999830'
        self.assertTrue(formatter.is_mastercard(mastercard_string))

    def test_amex_number(self):
        """should identify american express card numbers."""
        amex_number = 374619657687666
        self.assertTrue(formatter.is_amex(amex_number))

    def test_amex_number_string(self):
        """should identify american express card number strings."""
        amex_string = '374619657687666'
        self.assertTrue(formatter.is_amex(amex_string))

    def test_maestro_number(self):
        """should identify maestro card numbers."""
        maestro_number = 6304236404755563
        self.assertTrue(formatter.is_maestro(maestro_number))

    def test_maestro_number_string(self):
        """should identify maestro card number strings."""
        maestro_string = '6304236404755563'
        self.assertTrue(formatter.is_maestro(maestro_string))

    def test_discover_number(self):
        """should identify discovery card numbers."""
        discover_number = 6011359876556543
        self.assertTrue(formatter.is_discover(discover_number))

    def test_discover_number_string(self):
        """should identify discovery card number strings."""
        discover_string = '6011359876556543'
        self.assertTrue(formatter.is_discover(discover_string))

    def test_dankort_number(self):
        """should identify dankort card numbers."""
        dankort_number = 5019717010103742
        self.assertTrue(formatter.is_dankort(dankort_number))

    def test_dankort_number_string(self):
        """should identify dankort card number strings."""
        dankort_string = '5019717010103742'
        self.assertTrue(formatter.is_dankort(dankort_string))

    def test_cartebancaire_number(self):
        """should identify cartebancaire card numbers."""
        cartebancaire_number = 4035501000000008
        self.assertTrue(formatter.is_cartebancaire(cartebancaire_number))

    def test_cartebancaire_number_string(self):
        """should identify cartebancaire card number strings."""
        cartebancaire_string = '4035501000000008'
        self.assertTrue(formatter.is_cartebancaire(cartebancaire_string))

    def test_jcb_number(self):
        """should identify jcb card numbers."""
        jcb_number = 3541599999092431
        self.assertTrue(formatter.is_jcb(jcb_number))

    def test_jcb_number_string(self):
        """should identify jcb card number strings."""
        jcb_string = '3541599999092431'
        self.assertTrue(formatter.is_jcb(jcb_string))

    def test_hipercard_number(self):
        """should identify hipercard card numbers."""
        hipercard_number = 6062828888666688
        self.assertTrue(formatter.is_hipercard(hipercard_number))

    def test_hipercard_number_string(self):
        """should identify hipercard card number strings."""
        hipercard_string = '6062828888666688'
        self.assertTrue(formatter.is_hipercard(hipercard_string))

    def test_dinersclub_number(self):
        """should identify dinersclub card numbers."""
        dinersclub_number = 36961903000009
        self.assertTrue(formatter.is_dinersclub(dinersclub_number))

    def test_dinersclub_number_string(self):
        """should identify dinersclub card number strings."""
        dinersclub_string = '36961903000009'
        self.assertTrue(formatter.is_dinersclub(dinersclub_string))

    def test_vpay_number(self):
        """should identify vpay card numbers."""
        vpay_number = 4822000000000000003
        self.assertTrue(formatter.is_vpay(vpay_number))

    def test_vpay_number_string(self):
        """should identify vpay card number strings."""
        vpay_string = '4822000000000000003'
        self.assertTrue(formatter.is_vpay(vpay_string))

    def test_solo_number(self):
        """should identify solo card numbers."""
        solo_number = 6334101999990016
        self.assertTrue(formatter.is_solo(solo_number))

    def test_solo_number_string(self):
        """should identify solo card number strings."""
        solo_string = '6334101999990016'
        self.assertTrue(formatter.is_solo(solo_string))

    def test_switch_number(self):
        """should identify switch card numbers."""
        switch_number = 6331101999990016
        self.assertTrue(formatter.is_switch(switch_number))

    def test_switch_number_string(self):
        """should identify switch card number strings."""
        switch_string = '6331101999990016'
        self.assertTrue(formatter.is_switch(switch_string))

    def test_bcmc_number(self):
        """should identify bcmc card numbers."""
        bcmc_number = 67039902990000011
        self.assertTrue(formatter.is_bcmc(bcmc_number))

    def test_bcmc_number_string(self):
        """should identify bcmc card number strings."""
        bcmc_string = '67039902990000011'
        self.assertTrue(formatter.is_bcmc(bcmc_string))

    def test_elo_number(self):
        """should identify elo card numbers."""
        elo_number = 5066991111111118
        self.assertTrue(formatter.is_elo(elo_number))

    def test_elo_number_string(self):
        """should identify elo card number strings."""
        elo_string = '5066991111111118'
        self.assertTrue(formatter.is_elo(elo_string))
        
    def test_unknown_formats(self):
        """should return none for unknown card formats."""
        unknown = 1234567890
        self.assertEqual(formatter.get_format(unknown), [])

    def test_single_format_of_number(self):
        """should get the format of a card number."""
        number = 5409219472999830
        self.assertEqual(formatter.get_format(number), ['mastercard'])

    def test_dual_formats_of_number(self):
        """should get multiple formats of a card number."""
        number = 4508077077058854
        self.assertEqual(formatter.get_format(number), ['visa', 'visa electron'])
