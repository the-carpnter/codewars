DNA = {'A':'T', 'C':'G', 'T':'A', 'G':'C'}
def reverse_complement(dna):
    try:
        return ''.join(map(lambda x: DNA[x], dna.upper()))[::-1]
    except KeyError:
        return 'Invalid sequence'
