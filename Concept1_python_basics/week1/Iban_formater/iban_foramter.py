def iban_formater(iban):
    for i in iban:
        if i == ' ':
            return iban
    return (iban[:4] + " " + iban[4:8] + " " + iban[8:12] + " " + iban[12:16] + " " + iban[16:20] + " " + iban[20:])
