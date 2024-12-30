def get_dosage_text(dosage, weight):
    dosage_rules = dosage.split(',')[::-1]  # Reverse the list
    for rule in dosage_rules:
        parts = rule.split(':')
        w = float(parts[0].strip())
        text = parts[1].strip()
        if w <= weight:
            return text
    return None