from pp import pformat
from pyperclip import copy, paste

ast = eval(paste())
copy(pformat(ast))