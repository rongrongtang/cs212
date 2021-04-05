import re

def parse(start_symbol, text, grammar):
    """Example call: parse('Exp', '3*x + b', G).
    Returns a (tree, remainder) pair. If remainder is '', it parsed the whole
    string. Failure iff remainder is None. This is a deterministic PEG parser,
    so rule order (left-to-right) matters. Do 'E => T op E | T', putting the
    longest parse first; don't do 'E => T | T op E'
    Also, no left recursion allowed: don't do 'E => E op T'"""

    tokenizer = grammar[' '] + '(%s)'

    def parse_sequence(sequence, text):
        result = []
        for atom in sequence:
            tree, text = parse_atom(atom, text)
            if text is None: return Fail
            result.append(tree)
        return result, text

    def parse_atom(atom, text):
        if atom in grammar:  # Non-Terminal: tuple of alternatives
            for alternative in grammar[atom]:
                tree, rem = parse_sequence(alternative, text)
                if rem is not None: return [atom]+tree, rem
            return Fail
        else:  # Terminal: match characters against start of text
            m = re.match(tokenizer%atom, text)                
            return Fail if (not m) else (m.group(1), text[m.end():])

    # Body of parse:
    return parse_atom(start_symbol, text)

def grammar(description,whitespace='\s*'):
    G={' ':whitespace}
    description=description.replace('\t','')
    for line in description.split('\n'):
        lhs,rhs=line.split('=>',1)        
        alternatives=rhs.split('|')
        G[lhs]=tuple(map(str.split,alternatives))
    return G


JSON=grammar(r"""object=>{ }|{ members }
members=>pair , members|pair
pair=>string : value
array=>[[] []]|[[] elements []]
elements=>value , elements| value
value=>string|number|object|array|true|false|null
string=>"[^"]*"
number=>int frac exp|int frac|int exp|int
int=>-?[1-9]+[0-9]*|0
frac=>[.][0-9]+
exp=>[eE][-+]?[0-9]+""")

def json_parse(text):
    return parse('value',text,JSON)

def json_test():
    for e in examples:
        print(e,'==',parse('value',e,JSON))
Fail=(None,None)


examples=['["testing",1,2,3]','-123.456e+789','{"age":21,"state":"CO","occupation":"rides the rodeo"}','[]','0','0.1']

print(JSON)
json_test()
