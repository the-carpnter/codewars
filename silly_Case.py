def sillycase(silly):
    mid = len(silly) // 2 + len(silly) % 2 
    return silly[:mid].lower() + silly[mid:].upper()
