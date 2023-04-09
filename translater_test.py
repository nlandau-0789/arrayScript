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
                    'call',
                    'operator_add',
                    [
                        (
                            'simple_slice',
                            ('var', 'nom'),
                            [('const', 5)],
                            [('const', 9)],
                        ),
                        ('call', 'operator_pow', [('const', 90), ('const', 2)]),
                    ],
                ),
            ),
            ('return', ('const', 'Null')),
        ],
    ),
    (
        'assign',
        [('var', 'a')],
        (
            'call',
            'operator_add',
            [
                ('const', 1),
                (
                    'call',
                    'operator_mul',
                    [
                        ('const', 3),
                        (
                            'call',
                            'operator_add',
                            [
                                ('const', 5),
                                (
                                    'call',
                                    'operator_compose',
                                    [('var', 'input'), ('call', 'input', [])],
                                ),
                            ],
                        ),
                    ],
                ),
            ],
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
                (
                    'call',
                    'operator_compose',
                    [('var', 'make_num'), ('call', 'input', [])],
                ),
            ),
            (
                'assign',
                [('var', 'R')],
                (
                    'call',
                    'operator_compose',
                    [('var', 'make_num'), ('call', 'input', [])],
                ),
            ),
            (
                'assign',
                [('var', 'sections')],
                ('call', 'tuple', [('var', 'N'), ('var', 'make_num')]),
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
                            'call',
                            'operator_over',
                            [
                                ('var', 'make_num'),
                                (
                                    'call',
                                    'operator_compose',
                                    [('var', 'split'), ('call', 'input', [])],
                                ),
                            ],
                        ),
                    ),
                    (
                        'call',
                        'operator_decr',
                        [('item', ('var', 'sections'), [('var', 'I')])],
                    ),
                    (
                        'call',
                        'operator_incr',
                        [('item', ('var', 'sections'), [('var', 'J')])],
                    ),
                ],
            ),
            (
                'assign',
                [('var', 'sections')],
                (
                    'call',
                    'operator_scan',
                    [('var', 'operator_add'), ('var', 'sections')],
                ),
            ),
            (
                'call',
                'output',
                [
                    (
                        'call',
                        'operator_join',
                        [
                            ('const', '" "'),
                            (
                                'call',
                                'operator_over',
                                [('var', 'make_str'), ('var', 'sections')],
                            ),
                        ],
                    ),
                ],
            ),
            (
                'call',
                'output',
                [
                    (
                        'call',
                        'operator_goodname',
                        [
                            ('var', 'a'),
                            ('call', 'operator_goodname2', [('var', 'b')]),
                        ],
                    ),
                ],
            ),
            (
                'call',
                'operator_s_combinator_2',
                [
                    ('var', 'operator_add'),
                    ('var', 'operator_sub'),
                    ('var', 'aze'),
                ],
            ),
        ],
    ),
    ('call', 'output', [('const', 123)]),
    ('call', 'operator_apply', [('var', 'input'), ('call', 'output', [])]),
    (
        'assign',
        [('var', 'I'), ('var', 'J')],
        (
            'call',
            'operator_over',
            [
                ('var', 'make_num'),
                (
                    'call',
                    'operator_compose',
                    [('var', 'split'), ('call', 'input', [])],
                ),
            ],
        ),
    ),
]

from Utils.array_functions import flatten
# import json

def translate(stmt, indent = 0):
    if stmt[0] == "struct":
        return "\t"*indent + "struct "+ stmt[1][1] +" {\n" + "\t"*(indent+1) + (";\n"+"\t"*(indent+1)).join(flatten([translate(i, indent+1) for i in stmt[2]]))+ "\n" + "\t"*indent + "};"
    if stmt[0] == "declaration":
        type_ = stmt[1][1]
        return [type_+" "+name[1] for name in stmt[2]]
    if stmt[0] == "call":
        # return "\t"*indent + stmt[1] + "(" + ", ".join(flatten([translate(i, indent+1) for i in stmt[2]])) + ")"
        if stmt[1] == "operator_apply":
            stmt[2][1][2].insert(0, stmt[2][0])
            return translate(stmt[2][1])
        return stmt[1] + "(" + ", ".join(flatten([translate(i, indent+1) for i in stmt[2]])) + ")"
    if stmt[0] == "const":
        return str(stmt[1])
    if stmt[0] == "assign":
        if len(stmt[1]) == 1:
            return "auto " + translate(stmt[1][0], indent+1) + " = " + translate(stmt[2], indent+1)
        return "auto tmp = " + translate(stmt[2], indent+1) + "; auto " + "; auto ".join(translate(i, indent+1)+" = temp["+ str(idx) +"]" for idx, i in enumerate(stmt[1]))
    if stmt[0] == "var":
        return stmt[1]
    if stmt[0] == "return":
        return "return "+translate(stmt[1], indent+1)
    if stmt[0] == "func":
        return "\t"*indent+"auto " + stmt[1] + "("+ (", ").join(flatten([translate(i, indent+1) for i in stmt[2]])) +"){\n"+"\t"*(indent+1)+(";\n"+"\t"*(indent+1)).join(flatten([translate(i, indent+1) for i in stmt[3]]))+";\n"+"\t"*indent+"}"
    # if stmt[0] == "operator":
    #     return stmt[1]
    return ""
    


def run(p):
    # print(p)
    program = "#include <arrs.cpp>\n\nusing namespace arrs;\nusing namespace operators;\nusing namespace types;\nusing namespace funcs;\n\n"
    for i in p:
        program += translate(i)
        program += ";"*(not program[-1] in '};') 
        program += "\n\n"
    print(program)

run(p)