DEFAULT_OPTIONS = {
    'remove_comments': True,
    'strip_lines': True
}

# Replace without regex
replace_simple = [
    ['\\ds\\','\\displaystyle\\'],
    ['$\\C$', '\\mathcal{C}'],
    ['\\e^', '\\text{e}^'],
    ['\\mathscr', '\\mathcal'],
    ['\n$$', '\n$$\n'],
    ['$$\n', '\n$$\n'],
    [r'\[', '\n$$\n'],
    [r'\]', '\n$$\n'],
    ['\\begin', '\n\\begin'],
    ['\\begin{center}', ''],
    ['\\end{center}', ''],
    ['\\begin{solution}', ':::startsolution\n'],
    ['\\end{solution}', '\n\n:::endsolution']
]


# Deleted with TexSoup
del_commands = ['vspace',
                'Bareme',
                'cornouaille',
                'renewcommand',
                'setbar',
                'esp',
                'encadre',
                'ref',
                'arraycolsep',
                'label',
                'renewcommand',
                'hspace',
                'parindent',
                'raisebox',
                'rhead',
                'lhead',
                'lfoot',
                'rfoot',
                'addtolength',
                'pagestyle',
                'thispagestyle',
                'marginpar',
                'newpage',
                'hfill',
                'medskip',
                'bigskip',
                'smallskip',
                'setlength',
                'decofourleft',
                'footrulewidth',
                'decofourright'
                ]

del_environnements = [r'\begin{center}', r'\end{center}']

del_blocks = ['center']

replace_commands = [['chapter', '# S_T_R'],
                    ['section', '## S_T_R'],
                    ['subsection', '### S_T_R'],
                    ['textbf', '**S_T_R**'],
                    ['textsc', 'S_T_R'],
                    ['emph', '_S_T_R_']
                    ]

math_sub = [[r"\\np\{((?P<arg>.*?))\}", r'\1'],
            [r"\\nombre\{((?P<arg>.*?))\}", r'\1'],
            #[r"\\section\{((?P<arg>.*?))\}", r':::section \1'],
            [r"\\textsf\{((?P<arg>.*?))\}", r'\1'],
            [r"\\Large(\{(?P<arg>.*?)\})?", r'\1'],
            [r"\\parbox\{((?P<arg>.*?))\}", ''],
            [r"\\end\{((?P<arg>.*?))\}", r'\\end{\1}\n'],
            [r"\\Oijk",
             r"$\\left(\\text{O};~\\vect{i},~\\vect{j},~\\vect{k}\\right)$"],
            [r"\\Ouv", r"$\\left(\\text{O};~\\vect{u},~\\vect{v}\\right)$"],
            [r"\\Oij", r"$\\left(\\text{O};~\\vect{i},~\\vect{j}\\right)$"],
            [r"\\vect\{((?P<arg>.*?))\}", r"\\overrightarrow{\1}"],
            [r"\\e(\W)", r'\1']]


postpandoc = [
    [r"\\textsf\{((?P<arg>.*?))\}", r'\1'],
    [r"\\Large(\{(?P<arg>.*?)\})?", r'\1'],
    [r"\\parbox\{((?P<arg>.*?))\}", ''],
    [r"\\end\{((?P<arg>.*?))\}", r'\\end{\1}\n'],
    [r"\\Oijk",
     r"$\\left(\\text{O};~\\vect{i},~\\vect{j},~\\vect{k}\\right)$"],
    [r"\\Ouv", r"$\\left(\\text{O};~\\vect{u},~\\vect{v}\\right)$"],
    [r"\\Oij", r"$\\left(\\text{O};~\\vect{i},~\\vect{j}\\right)$"],
    [r"\\vect\{((?P<arg>.*?))\}", r"\\overrightarrow{\1}"],
    [r"\\e(\W)", r'\1']]
