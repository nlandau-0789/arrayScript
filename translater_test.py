p = [
    (
        'struct',
        ('type', 'bad_struct'),
        [
            ('declaration', ('type', 'num'), [('var', 'a'), ('var', 'b')]),
            ('declaration', ('type', 'list'), [('var', 'c')]),
        ],
    ),
    (
        'struct',
        ('type', 'bad_struct2'),
        [
            ('declaration', ('type', 'num'), [('var', 'a'), ('var', 'b')]),
            ('declaration', ('type', 'list'), [('var', 'c')]),
        ],
    ),
    (
        'operator',
        [
            ('const', '"op"'),
            ('const', '"goodname"'),
            ('const', 5),
            ('const', '"{a} op {b}"'),
        ],
        [('return', ('const', 'Null'))],
    ),
    (
        'operator',
        [
            ('const', '"S"'),
            ('const', '"s_combinator"'),
            ('const', 0),
            ('const', '"S {f} {g} {x}"'),
        ],
        [
            (
                'return',
                (
                    'lambda',
                    [('var', 'x')],
                    ('call', 'f', [('var', 'x'), ('call', 'g', [('var', 'x')])]),
                ),
            ),
        ],
    ),
    (
        'operator',
        [
            ('const', '"S"'),
            ('const', '"s_combinator_2"'),
            ('const', 0),
            ('const', '"S §{f} §{g} {x}"'),
        ],
        [
            (
                'return',
                (
                    'lambda',
                    [('var', 'x')],
                    ('call', 'f', [('var', 'x'), ('call', 'g', [('var', 'x')])]),
                ),
            ),
        ],
    ),
    (
        'operator',
        [
            ('const', '"op2"'),
            ('const', '"goodname2"'),
            ('const', 9.7),
            ('const', '"op2 {a}"'),
        ],
        [('return', ('const', 'Null'))],
    ),
    (
        'func',
        'dummy',
        [('declaration', ('type', 'num'), [('var', 'a')])],
        [('return', ('const', 'Null'))],
    ),
    (
        'func',
        'dummy2',
        [
            ('declaration', ('type', 'num'), [('var', 'a'), ('var', 'b')]),
            ('declaration', ('type', 'list'), [('var', 'c')]),
        ],
        [
            (
                'assign',
                [('var', 'variable')],
                (
                    'operator_add',
                    (
                        'simple_slice',
                        ('var', 'nom'),
                        [('const', 5)],
                        [('const', 9)],
                    ),
                    ('operator_pow', ('const', 90), ('const', 2)),
                ),
            ),
            ('return', ('const', 'Null')),
        ],
    ),
    (
        'assign',
        [('var', 'a')],
        (
            'operator_add',
            ('const', 1),
            (
                'operator_mul',
                ('const', 3),
                (
                    'operator_add',
                    ('const', 5),
                    (
                        'operator_compose',
                        ('var', 'input'),
                        ('call', 'input', []),
                    ),
                ),
            ),
        ),
    ),
    (
        'func',
        'main',
        [],
        [
            (
                'assign',
                [('var', 'N')],
                ('operator_compose', ('type', 'num'), ('call', 'input', [])),
            ),
            (
                'struct',
                ('type', 'bad_struct3'),
                [
                    ('declaration', ('type', 'num'), [('var', 'a'), ('var', 'b')]),
                    ('declaration', ('type', 'list'), [('var', 'c')]),
                ],
            ),
            (
                'assign',
                [('var', 'R')],
                ('operator_compose', ('type', 'num'), ('call', 'input', [])),
            ),
            (
                'assign',
                [('var', 'sections')],
                ('call', 'tuple', [('var', 'N'), ('type', 'num')]),
            ),
            (
                'for',
                [('var', 'i')],
                ('call', 'range', [('var', 'R')]),
                [
                    (
                        'assign',
                        [('var', 'I'), ('var', 'J')],
                        (
                            'operator_over',
                            ('type', 'num'),
                            (
                                'operator_compose',
                                ('var', 'split'),
                                ('call', 'input', []),
                            ),
                        ),
                    ),
                    (
                        'operator_decr',
                        ('item', ('var', 'sections'), [('var', 'I')]),
                    ),
                    (
                        'operator_incr',
                        ('item', ('var', 'sections'), [('var', 'J')]),
                    ),
                ],
            ),
            (
                'assign',
                [('var', 'sections')],
                ('operator_scan', ('operator', '+'), ('var', 'sections')),
            ),
            (
                'call',
                'output',
                [
                    (
                        'operator_join',
                        ('const', '" "'),
                        ('operator_over', ('type', 'str'), ('var', 'sections')),
                    ),
                ],
            ),
            (
                'call',
                'output',
                [
                    (
                        'operator_goodname',
                        ('var', 'a'),
                        ('operator_goodname2', ('var', 'b')),
                    ),
                ],
            ),
            (
                'operator_s_combinator_2',
                ('operator', '+'),
                ('operator', '-'),
                ('var', 'aze'),
            ),
        ],
    ),
]

from Utils.array_functions import flatten

def translate(stmt, indent = 0):
    if stmt[0] == "struct":
        return "\t"*indent + "struct "+ stmt[1][1] +" {\n" + "\t"*(indent+1) + ("; \n"+"\t"*(indent+1)).join(flatten([translate(i, indent+1) for i in stmt[2]]))+ "\n" + "\t"*indent + "}; \n\n"
    if stmt[0] == "declaration":
        type_ = stmt[1][1]
        return [type_+" "+name[1] for name in stmt[2]]
    if stmt[0] == "call":
        return "\t"*indent + stmt[1] + "(" + ", ".join(flatten([translate(i, indent+1) for i in stmt[2]])) + ")"
    return ""
    


def run(p):
    # print(p)
    program = "#include <arrs.cpp>\n\n"
    for i in p:
        program += translate(i)
    print(program)

run(p)