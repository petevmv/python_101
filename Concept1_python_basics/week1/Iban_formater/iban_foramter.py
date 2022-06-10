def iban_formater(iban):
    result = []
    iban = iban.replace(' ', '')
    for idx, num in enumerate(iban):
        if (idx) % 4 == 0:
            result.append(' ')
        
        result.append(num)
    return ''.join(result).lstrip()
    

