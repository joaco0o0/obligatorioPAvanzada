
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ADD_COLUMN ALTER_TABLE AND BETWEEN CAST COMMA COUNT CREATE_TABLE DEFAULT DELETE_FROM DISTINCT DROP_COLUMN DROP_TABLE EQUALS EXISTS FOREIGN_KEY FROM GREATER GREATEREQUAL GROUP_BY HAVING IDENTIFIER IN INSERT_INTO IS_NULL JOIN LESS LESSEQUAL LIKE LIMIT NOTEQUAL NOT_NULL NUMBER ON ORDER_BY PRIMARY_KEY SELECT SEMICOLON SET STAR STRING UNIQUE UPDATE VALUES WHEREquery : SELECT columns FROM table WHERE conditioncolumns : IDENTIFIER\n                   | STARtable : IDENTIFIERcondition : IDENTIFIER EQUALS value\n                     | IDENTIFIER GREATER value\n                     | IDENTIFIER LESS value\n                     | IDENTIFIER GREATEREQUAL value\n                     | IDENTIFIER LESSEQUAL value\n                     | IDENTIFIER NOTEQUAL valuevalue : NUMBER\n                 | IDENTIFIER\n                 | STRING'
    
_lr_action_items = {'SELECT':([0,],[2,]),'$end':([1,10,18,19,20,21,22,23,24,25,26,],[0,-1,-12,-5,-11,-13,-6,-7,-8,-9,-10,]),'IDENTIFIER':([2,6,9,12,13,14,15,16,17,],[4,8,11,18,18,18,18,18,18,]),'STAR':([2,],[5,]),'FROM':([3,4,5,],[6,-2,-3,]),'WHERE':([7,8,],[9,-4,]),'EQUALS':([11,],[12,]),'GREATER':([11,],[13,]),'LESS':([11,],[14,]),'GREATEREQUAL':([11,],[15,]),'LESSEQUAL':([11,],[16,]),'NOTEQUAL':([11,],[17,]),'NUMBER':([12,13,14,15,16,17,],[20,20,20,20,20,20,]),'STRING':([12,13,14,15,16,17,],[21,21,21,21,21,21,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'query':([0,],[1,]),'columns':([2,],[3,]),'table':([6,],[7,]),'condition':([9,],[10,]),'value':([12,13,14,15,16,17,],[19,22,23,24,25,26,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> query","S'",1,None,None,None),
  ('query -> SELECT columns FROM table WHERE condition','query',6,'p_query_select','Traductor.py',283),
  ('columns -> IDENTIFIER','columns',1,'p_columns','Traductor.py',288),
  ('columns -> STAR','columns',1,'p_columns','Traductor.py',289),
  ('table -> IDENTIFIER','table',1,'p_table','Traductor.py',294),
  ('condition -> IDENTIFIER EQUALS value','condition',3,'p_condition','Traductor.py',299),
  ('condition -> IDENTIFIER GREATER value','condition',3,'p_condition','Traductor.py',300),
  ('condition -> IDENTIFIER LESS value','condition',3,'p_condition','Traductor.py',301),
  ('condition -> IDENTIFIER GREATEREQUAL value','condition',3,'p_condition','Traductor.py',302),
  ('condition -> IDENTIFIER LESSEQUAL value','condition',3,'p_condition','Traductor.py',303),
  ('condition -> IDENTIFIER NOTEQUAL value','condition',3,'p_condition','Traductor.py',304),
  ('value -> NUMBER','value',1,'p_value','Traductor.py',309),
  ('value -> IDENTIFIER','value',1,'p_value','Traductor.py',310),
  ('value -> STRING','value',1,'p_value','Traductor.py',311),
]
