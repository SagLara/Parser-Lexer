
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'DIVISION MINUS NUMBER PLUS TIMESexpression : expression expression PLUSexpression : expression expression MINUSexpression : termterm : expression expression TIMESterm : expression expression DIVISIONterm : factorfactor : NUMBER'
    
_lr_action_items = {'DIVISION':([1,2,3,5,6,7,8,9,],[-3,-7,-6,6,-5,-4,-1,-2,]),'NUMBER':([0,1,2,3,4,5,6,7,8,9,],[2,-3,-7,-6,2,2,-5,-4,-1,-2,]),'TIMES':([1,2,3,5,6,7,8,9,],[-3,-7,-6,7,-5,-4,-1,-2,]),'PLUS':([1,2,3,5,6,7,8,9,],[-3,-7,-6,8,-5,-4,-1,-2,]),'MINUS':([1,2,3,5,6,7,8,9,],[-3,-7,-6,9,-5,-4,-1,-2,]),'$end':([1,2,3,4,6,7,8,9,],[-3,-7,-6,0,-5,-4,-1,-2,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'term':([0,4,5,],[1,1,1,]),'expression':([0,4,5,],[4,5,5,]),'factor':([0,4,5,],[3,3,3,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> expression expression PLUS','expression',3,'p_expression_plus','parser_rules.py',5),
  ('expression -> expression expression MINUS','expression',3,'p_expression_minus','parser_rules.py',9),
  ('expression -> term','expression',1,'p_expression_term','parser_rules.py',13),
  ('term -> expression expression TIMES','term',3,'p_term_times','parser_rules.py',17),
  ('term -> expression expression DIVISION','term',3,'p_term_division','parser_rules.py',21),
  ('term -> factor','term',1,'p_term_factor','parser_rules.py',25),
  ('factor -> NUMBER','factor',1,'p_factor_num','parser_rules.py',29),
]
