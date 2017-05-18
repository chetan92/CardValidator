import re

def is_hipercard(n):
    """Checks if credit card number fits the visa format."""
    n, length = str(n), len(str(n))

    if length >= 13 and length <= 19:
        if re.match('^606282|3841\d{2}',''.join(n[:6])):
            return True
    return False

def is_dankort(n):
    """Checks if credit card number fits the visa format."""
    n, length = str(n), len(str(n))

    if length >= 13 and length <= 19:
        if re.match('^(5019)\d+$',n):
            return True
    return False

def is_bcglobal(n):
    """Checks if credit card number fits the visa format."""
    n, length = str(n), len(str(n))

    if length >= 13 and length <= 19:
        if re.match('^(6541|6556)[0-9]{12}$',n):
            return True
    return False

def is_koreancard(n):
    """Checks if credit card number fits the visa format."""
    n, length = str(n), len(str(n))

    if length >= 13 and length <= 19:
        if re.match('^9[0-9]{15}$',n):
            return True
    return False

def is_carteblanche(n):
    """Checks if credit card number fits the visa format."""
    n, length = str(n), len(str(n))

    if length >= 13 and length <= 19:
        if re.match('^389[0-9]{11}$',n):
            return True
    return False

def is_instapayment(n):
    """Checks if credit card number fits the visa format."""
    n, length = str(n), len(str(n))

    if length >= 16 and length <= 19:
        if re.match('^(6360)\d+$',n) or re.match('^63[7-9][0-9]{13}$',n):
            return True
    return False

def is_laser(n):
    """Checks if credit card number fits the visa format."""
    n, length = str(n), len(str(n))
    form = ['6706','6709','6771']
    if length >= 16 and length <= 19:
        if ''.join(n[:4]) in form or re.match('^(6304|6706|6709|6771)[0-9]{12,15}$',n):
            return True
    return False


def is_bcmc(n):
    """Checks if credit card number fits the visa format."""
    n, length = str(n), len(str(n))
    form = ['6703']
    if length >= 13 and length <= 19:
        if ''.join(n[:4]) in form:
            return True
    return False

def is_solo(n):
    """Checks if credit card number fits the visa format."""
    n, length = str(n), len(str(n))
    form = ['6334','6767']
    if length >= 16 and length <= 19:
        if ''.join(n[:4]) in form or re.match('^(6334|6767)[0-9]{12}|(6334|6767)[0-9]{14}|(6334|6767)[0-9]{15}$',n):
            return True
    return False

def is_switch(n):
    """Checks if credit card number fits the visa format."""
    n, length = str(n), len(str(n))
    form = ['633110','633312','633304','633303','633301','633300']
    if length >= 16 and length <= 19:
        if ''.join(n[:6]) in form or re.match('^(4903|4905|4911|4936|6333|6759)[0-9]{12}|(4903|4905|4911|4936|6333|6759)[0-9]{14}|(4903|4905|4911|4936|6333|6759)[0-9]{15}|564182[0-9]{10}|564182[0-9]{12}|564182[0-9]{13}|633110[0-9]{10}|633110[0-9]{12}|633110[0-9]{13}$',n):
            return True
    return False

def is_jcb(n):
    """Checks if credit card number fits the visa format."""
    n, length = str(n), len(str(n))

    if length == 16:
        if ''.join(n[:4]) in strings_between(3528, 3589)or re.match('^(?:2131|1800|35\d{3})\d{11}$',n):
            return True
    return False

def is_unionpay(n):
    """Checks if credit card number fits the visa format."""
    n, length = str(n), len(str(n))

    if length >= 12 and length <= 19:
        if re.match('^(62|88)\d+$',n) or re.match('^(62[0-9]{14,17})$',n):
            return True
    return False

def is_visa(n):
    """Checks if credit card number fits the visa format."""
    n, length = str(n), len(str(n))

    if length >= 13 and length <= 16:
        if n[0] == '4':
            if(re.match('^4[0-9]{12}(?:[0-9]{3})?$',n)):
                return True
    return False

def is_dinersclub(n):
    """Checks if credit card number fits the visa format."""
    n, length = str(n), len(str(n))
    form = ['30','36']
    if length >= 13 and length <= 19:
        if ''.join(n[:2]) in form or (re.match('^3(?:0[0-5]|[68][0-9])[0-9]{11}$',n)):
            return True
    return False

def is_cartebancaire(n):
    """Checks if credit card number fits the visa format."""
    n, length = str(n), len(str(n))
    form = ['4035','4360']
    if length >= 13 and length <= 19:
        if ''.join(n[:4]) in form:
            return True
    return False

def is_vpay(n):
    """Checks if credit card number fits the visa format."""
    n, length = str(n), len(str(n))
    form = ['4370','482']
    if length >= 13 and length <= 19:
        if ''.join(n[:4]) in form or ''.join(n[:3]) in form:
            return True
    return False

def is_visa_electron(n):
    """Checks if credit card number fits the visa electron format."""
    n, length = str(n), len(str(n))
    form = ['026', '508', '844', '913', '917','405']

    if length == 16:
        if n[0] == '4':
            if ''.join(n[1:4]) in form or ''.join(n[1:6]) == '17500':
                return True
    return False


def is_mastercard(n):
    """Checks if credit card number fits the mastercard format."""
    n, length = str(n), len(str(n))

    if length >= 16 and length <= 19:
        if ''.join(n[:2]) in strings_between(50, 56) or (re.match('^5[1-5][0-9]{14}$',n)):
            return True
    return False

def is_rupay(n):
    """Checks if credit card number fits the mastercard format."""
    n, length = str(n), len(str(n))
    if length >= 13 and length <= 19:
        if ''.join(n[:6]) in strings_between(508500, 508999) or ''.join(n[:6]) in strings_between(606985, 607984) or ''.join(n[:6]) in strings_between(608001, 608500) or ''.join(n[:6]) in strings_between(652150, 653149):
            return True
    return False


def is_elo(n):
    """Checks if credit card number fits the mastercard format."""
    n, length = str(n), len(str(n))
    form = ['5066']
    if length >= 16 and length <= 19:
        if ''.join(n[:4]) in form:
            return True
    return False

def is_amex(n):
    """Checks if credit card number fits the american express format."""
    n, length = str(n), len(str(n))
    if length == 15:
        if n[0] == '3' and (n[1] == '4' or n[1] == '7'):
            if(re.match('^3[47][0-9]{13}$',n)):
                return True
            else:
                return False
    return False


def is_maestro(n):
    """Checks if credit card number fits the maestro format."""
    n, length = str(n), len(str(n))
    form = ['5018', '5020', '5038', '5893', '6304',
                    '6759', '6761', '6762', '6763','6731',
            '06','6779','677','678','679']

    if length >= 12 and length <= 19:
        if ''.join(n[:4]) in form:
            return True
        elif ''.join(n[:3]) in form:
            return True;
        elif ''.join(n[:2]) in form:
            return True;
    return False


def is_discover(n):
    """Checks if credit card number fits the discover card format."""
    n, length = str(n), len(str(n))

    if length == 16:
        if n[0] == '6':
            if ''.join(n[1:4]) == '011' or n[1] == '5':
                return True
            elif n[1] == '4' and n[2] in strings_between(4, 10):
                return True
            elif ''.join(n[1:6]) in strings_between(22126, 22926):
                return True
    return False


def get_format(n):
    """Gets a list of the formats a credit card number fits."""
    formats = []

    if is_visa(n):
        formats.append('visa')
    if is_visa_electron(n):
        formats.append('visa electron')
    if is_mastercard(n):
        formats.append('mastercard')
    if is_amex(n):
        formats.append('amex')
    if is_maestro(n):
        formats.append('maestro')
    if is_discover(n):
        formats.append('discover')
    if is_rupay(n):
        formats.append('rupay')
    if is_hipercard(n):
        formats.append('hipercard')
    if is_dankort(n):
        formats.append('dankort')
    if is_instapayment(n):
        formats.append('instapayment')
    if is_laser(n):
        formats.append('laser')
    if is_bcmc(n):
        formats.append('bcmc')
    if is_jcb(n):
        formats.append('jcb')
    if is_unionpay(n):
        formats.append('unionpay')
    if is_solo(n):
        formats.append('solo')
    if is_dinersclub(n):
        formats.append('dinersclub')
    if is_cartebancaire(n):
        formats.append('cartebancaire')
    if is_elo(n):
        formats.append('elo')
    if is_vpay(n):
        formats.append('vpay')
    if is_switch(n):
        formats.append('switch')
    if is_carteblanche(n):
        formats.append('carteblanche')
    if is_bcglobal(n):
        formats.append('bcglobal')
    if is_koreancard(n):
        formats.append('koreancard')
    return formats


def strings_between(a, b):
    """Generates a list of strings between a and b."""
    return list(map(str, range(a, b)))
