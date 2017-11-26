
# _parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'B_FOLD_END B_FOLD_START B_LITERAL_END B_LITERAL_START B_MAP_COMPACT_KEY B_MAP_COMPACT_VALUE B_MAP_KEY B_MAP_VALUE B_SEQUENCE_COMPACT_START B_SEQUENCE_START CAST_TYPE DEDENT DOC_END DOC_START DOUBLEQUOTE_END DOUBLEQUOTE_START F_MAP_END F_MAP_KEY F_MAP_START F_SEP F_SEQUENCE_END F_SEQUENCE_START INDENT SCALAR SINGLEQUOTE_END SINGLEQUOTE_START\n        docs    : doc\n                | doc DOC_END\n        \n        docs    : docs doc\n        \n        doc : DOC_START doc DOC_END\n            | DOC_START doc\n            | INDENT doc DEDENT\n        \n        doc : collection\n            | scalar\n        \n        scalar      : ignore_indent_dedent  scalar\n        \n        collection  : sequence\n                    | map\n                    | flow_collection\n        \n        map : map_item\n        \n        map : map map_item\n        \n        map_item    : map_item_key map_item_value\n        \n        map_item    : B_MAP_COMPACT_KEY scalar B_MAP_VALUE scalar DEDENT\n        \n        map_item_key    : B_MAP_KEY         scalar\n        \n        map_item_key    : scalar\n        \n        map_item_key    :  B_MAP_KEY    INDENT collection DEDENT\n        map_item_value  :  B_MAP_VALUE  INDENT collection DEDENT\n        \n        map_item_value  :  B_MAP_VALUE flow_collection\n        \n        map_item_value  : B_MAP_VALUE scalar\n        \n        map_item_value  : B_MAP_VALUE INDENT scalar DEDENT\n        \n        map_item_value  : B_MAP_VALUE sequence\n        \n        sequence    : sequence_item\n        \n        sequence    : sequence sequence_item\n        \n        sequence_item   : B_SEQUENCE_START scalar\n        \n        sequence_item   : B_SEQUENCE_START INDENT collection DEDENT\n        \n        map_item_key    : B_MAP_COMPACT_KEY         collection DEDENT\n        map_item_value  : B_MAP_COMPACT_VALUE       collection DEDENT\n        sequence_item   : B_SEQUENCE_COMPACT_START  collection DEDENT\n        \n        sequence_item   : B_SEQUENCE_START flow_collection\n        \n        scalar  : DOUBLEQUOTE_START SCALAR DOUBLEQUOTE_END\n        \n        scalar  : SINGLEQUOTE_START SCALAR SINGLEQUOTE_END\n        \n        scalar  : DOUBLEQUOTE_START DOUBLEQUOTE_END\n                | SINGLEQUOTE_START SINGLEQUOTE_END\n        \n        scalar  : CAST_TYPE scalar\n        \n        scalar  : SCALAR\n        \n        scalar  : B_LITERAL_START scalar_group B_LITERAL_END\n        \n        scalar  : B_FOLD_START scalar_group B_FOLD_END\n        \n        scalar  : INDENT scalar_group DEDENT\n        \n        scalar  : scalar INDENT SCALAR DEDENT\n        \n        scalar_group    : SCALAR\n                        | scalar_group SCALAR\n        \n        ignore_indent_dedent    : INDENT DEDENT\n        \n        flow_collection : F_SEQUENCE_START flow_sequence F_SEQUENCE_END\n                        | F_SEQUENCE_START flow_sequence F_SEP F_SEQUENCE_END\n                        | F_MAP_START flow_map F_MAP_END\n                        | F_MAP_START flow_map F_SEP F_MAP_END\n        \n        flow_sequence   : flow_sequence_item\n        \n        flow_sequence   : flow_sequence F_SEP flow_sequence_item\n        \n        flow_sequence_item  : scalar\n        \n        flow_map   : flow_map_item\n        \n        flow_map   : flow_map F_SEP flow_map_item\n        \n        flow_map_item  : flow_map_item_key flow_map_item_value\n        \n        flow_map_item_key   : scalar F_MAP_KEY\n        \n        flow_map_item_value    : scalar\n        '
    
_lr_action_items = {'B_SEQUENCE_COMPACT_START':([0,1,4,5,6,9,10,11,14,15,17,18,19,21,23,29,30,36,43,44,46,50,51,52,53,55,56,60,62,63,64,65,67,69,70,73,76,77,78,82,83,84,85,88,89,93,95,99,100,102,103,104,105,],[1,1,1,1,-25,1,-11,-38,1,-7,1,-13,-8,-1,-12,-37,1,-3,-5,-14,-36,1,1,-15,-26,-9,-2,-35,1,-27,-32,-31,-41,-6,-40,-48,-4,-39,-34,1,1,-22,-21,-46,-33,-49,-30,-42,-47,-28,-16,-20,-23,]),'F_SEP':([11,29,39,41,46,55,57,58,59,60,67,70,74,75,77,78,89,92,99,101,],[-38,-37,-53,72,-36,-9,-52,-50,87,-35,-41,-40,-57,-55,-39,-34,-33,-54,-42,-51,]),'DOC_END':([6,10,11,15,17,18,19,21,23,29,43,44,46,52,53,55,60,63,64,65,67,69,70,73,76,77,78,83,84,85,88,89,93,95,99,100,102,103,104,105,],[-25,-11,-38,-7,-10,-13,-8,56,-12,-37,76,-14,-36,-15,-26,-9,-35,-27,-32,-31,-41,-6,-40,-48,-4,-39,-34,-24,-22,-21,-46,-33,-49,-30,-42,-47,-28,-16,-20,-23,]),'F_MAP_KEY':([11,29,40,46,55,60,67,70,77,78,89,99,],[-38,-37,71,-36,-9,-35,-41,-40,-39,-34,-33,-42,]),'CAST_TYPE':([0,1,2,3,4,5,6,8,9,10,11,14,15,17,18,19,20,21,22,23,25,29,30,35,36,42,43,44,46,50,51,52,53,55,56,60,62,63,64,65,67,69,70,71,72,73,76,77,78,80,82,83,84,85,87,88,89,93,95,99,100,102,103,104,105,],[2,2,2,2,2,2,-25,2,2,2,-38,2,-7,-10,-13,-8,2,-1,2,-12,2,-37,2,-45,-3,2,-5,-14,-36,2,2,-15,-26,-9,-2,-35,2,-27,-32,-31,-41,-6,-40,-56,2,-48,-4,-39,-34,2,2,-24,-22,-21,2,-46,-33,-49,-30,-42,-47,-28,-16,-20,-23,]),'B_MAP_KEY':([0,1,4,5,6,9,10,11,14,15,17,18,19,21,23,29,30,36,43,44,46,50,52,53,55,56,60,62,63,64,65,67,69,70,73,76,77,78,82,83,84,85,88,89,93,95,99,100,102,103,104,105,],[3,3,3,3,-25,3,3,-38,3,-7,-10,-13,-8,-1,-12,-37,3,-3,-5,-14,-36,3,-15,-26,-9,-2,-35,3,-27,-32,-31,-41,-6,-40,-48,-4,-39,-34,3,-24,-22,-21,-46,-33,-49,-30,-42,-47,-28,-16,-20,-23,]),'F_SEQUENCE_END':([11,29,46,55,57,58,59,60,67,70,77,78,87,89,99,101,],[-38,-37,-36,-9,-52,-50,88,-35,-41,-40,-39,-34,100,-33,-42,-51,]),'INDENT':([0,1,2,3,4,5,6,8,9,10,11,14,15,17,18,19,20,21,22,23,25,28,29,30,31,32,35,36,40,42,43,44,46,49,50,51,52,53,55,56,57,60,62,63,64,65,67,69,70,71,72,73,74,76,77,78,80,82,83,84,85,87,88,89,93,94,95,96,98,99,100,102,103,104,105,],[4,26,26,30,4,4,-25,26,4,26,-38,26,-7,-10,-13,54,26,-1,26,-12,62,54,54,26,54,-38,-45,-3,54,26,-5,-14,-36,54,26,82,-15,-26,54,-2,54,-35,26,54,-32,-31,-41,-6,-40,-56,26,-48,54,-4,-39,-34,26,26,-24,54,-21,26,-46,-33,-49,54,-30,-38,54,-42,-47,-28,-16,-20,-23,]),'B_FOLD_START':([0,1,2,3,4,5,6,8,9,10,11,14,15,17,18,19,20,21,22,23,25,29,30,35,36,42,43,44,46,50,51,52,53,55,56,60,62,63,64,65,67,69,70,71,72,73,76,77,78,80,82,83,84,85,87,88,89,93,95,99,100,102,103,104,105,],[7,7,7,7,7,7,-25,7,7,7,-38,7,-7,-10,-13,-8,7,-1,7,-12,7,-37,7,-45,-3,7,-5,-14,-36,7,7,-15,-26,-9,-2,-35,7,-27,-32,-31,-41,-6,-40,-56,7,-48,-4,-39,-34,7,7,-24,-22,-21,7,-46,-33,-49,-30,-42,-47,-28,-16,-20,-23,]),'F_MAP_START':([0,1,4,5,6,9,10,11,14,15,17,18,19,21,23,25,29,30,36,43,44,46,50,51,52,53,55,56,60,62,63,64,65,67,69,70,73,76,77,78,82,83,84,85,88,89,93,95,99,100,102,103,104,105,],[8,8,8,8,-25,8,-11,-38,8,-7,-10,-13,-8,-1,-12,8,-37,8,-3,-5,-14,-36,8,8,-15,-26,-9,-2,-35,8,-27,-32,-31,-41,-6,-40,-48,-4,-39,-34,8,-24,-22,-21,-46,-33,-49,-30,-42,-47,-28,-16,-20,-23,]),'B_FOLD_END':([37,38,68,],[70,-43,-44,]),'DOUBLEQUOTE_END':([24,61,],[60,89,]),'DOC_START':([0,4,5,6,9,10,11,15,17,18,19,21,23,29,36,43,44,46,52,53,55,56,60,63,64,65,67,69,70,73,76,77,78,83,84,85,88,89,93,95,99,100,102,103,104,105,],[9,9,9,-25,9,-11,-38,-7,-10,-13,-8,-1,-12,-37,-3,-5,-14,-36,-15,-26,-9,-2,-35,-27,-32,-31,-41,-6,-40,-48,-4,-39,-34,-24,-22,-21,-46,-33,-49,-30,-42,-47,-28,-16,-20,-23,]),'SINGLEQUOTE_END':([13,47,],[46,78,]),'SCALAR':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,18,19,20,21,22,23,24,25,26,29,30,32,33,35,36,37,38,42,43,44,45,46,50,51,52,53,54,55,56,60,62,63,64,65,67,68,69,70,71,72,73,76,77,78,80,82,83,84,85,87,88,89,93,95,96,99,100,102,103,104,105,],[11,11,11,11,32,11,-25,38,11,11,11,-38,38,47,11,-7,-10,-13,-8,11,-1,11,-12,61,11,38,-37,32,-43,68,-45,-3,68,-43,11,-5,-14,68,-36,11,11,-15,-26,86,-9,-2,-35,32,-27,-32,-31,-41,-44,-6,-40,-56,11,-48,-4,-39,-34,11,96,-24,-22,-21,11,-46,-33,-49,-30,-43,-42,-47,-28,-16,-20,-23,]),'B_LITERAL_START':([0,1,2,3,4,5,6,8,9,10,11,14,15,17,18,19,20,21,22,23,25,29,30,35,36,42,43,44,46,50,51,52,53,55,56,60,62,63,64,65,67,69,70,71,72,73,76,77,78,80,82,83,84,85,87,88,89,93,95,99,100,102,103,104,105,],[12,12,12,12,12,12,-25,12,12,12,-38,12,-7,-10,-13,-8,12,-1,12,-12,12,-37,12,-45,-3,12,-5,-14,-36,12,12,-15,-26,-9,-2,-35,12,-27,-32,-31,-41,-6,-40,-56,12,-48,-4,-39,-34,12,12,-24,-22,-21,12,-46,-33,-49,-30,-42,-47,-28,-16,-20,-23,]),'SINGLEQUOTE_START':([0,1,2,3,4,5,6,8,9,10,11,14,15,17,18,19,20,21,22,23,25,29,30,35,36,42,43,44,46,50,51,52,53,55,56,60,62,63,64,65,67,69,70,71,72,73,76,77,78,80,82,83,84,85,87,88,89,93,95,99,100,102,103,104,105,],[13,13,13,13,13,13,-25,13,13,13,-38,13,-7,-10,-13,-8,13,-1,13,-12,13,-37,13,-45,-3,13,-5,-14,-36,13,13,-15,-26,-9,-2,-35,13,-27,-32,-31,-41,-6,-40,-56,13,-48,-4,-39,-34,13,13,-24,-22,-21,13,-46,-33,-49,-30,-42,-47,-28,-16,-20,-23,]),'B_MAP_COMPACT_KEY':([0,1,4,5,6,9,10,11,14,15,17,18,19,21,23,29,30,36,43,44,46,50,52,53,55,56,60,62,63,64,65,67,69,70,73,76,77,78,82,83,84,85,88,89,93,95,99,100,102,103,104,105,],[14,14,14,14,-25,14,14,-38,14,-7,-10,-13,-8,-1,-12,-37,14,-3,-5,-14,-36,14,-15,-26,-9,-2,-35,14,-27,-32,-31,-41,-6,-40,-48,-4,-39,-34,14,-24,-22,-21,-46,-33,-49,-30,-42,-47,-28,-16,-20,-23,]),'$end':([5,6,10,11,15,17,18,19,21,23,29,36,43,44,46,52,53,55,56,60,63,64,65,67,69,70,73,76,77,78,83,84,85,88,89,93,95,99,100,102,103,104,105,],[0,-25,-11,-38,-7,-10,-13,-8,-1,-12,-37,-3,-5,-14,-36,-15,-26,-9,-2,-35,-27,-32,-31,-41,-6,-40,-48,-4,-39,-34,-24,-22,-21,-46,-33,-49,-30,-42,-47,-28,-16,-20,-23,]),'B_MAP_COMPACT_VALUE':([11,16,19,28,29,31,32,46,49,55,60,67,70,77,78,79,89,91,96,98,99,],[-38,50,-18,-18,-37,-17,-38,-36,-18,-9,-35,-41,-40,-39,-34,-29,-33,-19,-38,-18,-42,]),'B_MAP_VALUE':([11,16,19,28,29,31,32,46,49,55,60,67,70,77,78,79,89,91,96,98,99,],[-38,51,-18,-18,-37,-17,-38,-36,80,-9,-35,-41,-40,-39,-34,-29,-33,-19,-38,-18,-42,]),'F_SEQUENCE_START':([0,1,4,5,6,9,10,11,14,15,17,18,19,21,23,25,29,30,36,43,44,46,50,51,52,53,55,56,60,62,63,64,65,67,69,70,73,76,77,78,82,83,84,85,88,89,93,95,99,100,102,103,104,105,],[22,22,22,22,-25,22,-11,-38,22,-7,-10,-13,-8,-1,-12,22,-37,22,-3,-5,-14,-36,22,22,-15,-26,-9,-2,-35,22,-27,-32,-31,-41,-6,-40,-48,-4,-39,-34,22,-24,-22,-21,-46,-33,-49,-30,-42,-47,-28,-16,-20,-23,]),'DOUBLEQUOTE_START':([0,1,2,3,4,5,6,8,9,10,11,14,15,17,18,19,20,21,22,23,25,29,30,35,36,42,43,44,46,50,51,52,53,55,56,60,62,63,64,65,67,69,70,71,72,73,76,77,78,80,82,83,84,85,87,88,89,93,95,99,100,102,103,104,105,],[24,24,24,24,24,24,-25,24,24,24,-38,24,-7,-10,-13,-8,24,-1,24,-12,24,-37,24,-45,-3,24,-5,-14,-36,24,24,-15,-26,-9,-2,-35,24,-27,-32,-31,-41,-6,-40,-56,24,-48,-4,-39,-34,24,24,-24,-22,-21,24,-46,-33,-49,-30,-42,-47,-28,-16,-20,-23,]),'F_MAP_END':([11,29,39,41,46,55,60,67,70,72,74,75,77,78,89,92,99,],[-38,-37,-53,73,-36,-9,-35,-41,-40,93,-57,-55,-39,-34,-33,-54,-42,]),'B_LITERAL_END':([38,45,68,],[-43,77,-44,]),'B_SEQUENCE_START':([0,1,4,5,6,9,10,11,14,15,17,18,19,21,23,29,30,36,43,44,46,50,51,52,53,55,56,60,62,63,64,65,67,69,70,73,76,77,78,82,83,84,85,88,89,93,95,99,100,102,103,104,105,],[25,25,25,25,-25,25,-11,-38,25,-7,25,-13,-8,-1,-12,-37,25,-3,-5,-14,-36,25,25,-15,-26,-9,-2,-35,25,-27,-32,-31,-41,-6,-40,-48,-4,-39,-34,25,25,-22,-21,-46,-33,-49,-30,-42,-47,-28,-16,-20,-23,]),'DEDENT':([4,6,10,11,15,17,18,19,23,26,27,29,30,32,33,34,38,43,44,46,48,52,53,55,60,62,63,64,65,66,67,68,69,70,73,76,77,78,81,82,83,84,85,86,88,89,90,93,94,95,96,97,98,99,100,102,103,104,105,],[35,-25,-11,-38,-7,-10,-13,-8,-12,35,65,-37,35,-38,67,69,-43,-5,-14,-36,79,-15,-26,-9,-35,35,-27,-32,-31,91,-41,-44,-6,-40,-48,-4,-39,-34,95,35,-24,-22,-21,99,-46,-33,102,-49,103,-30,-38,104,105,-42,-47,-28,-16,-20,-23,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'flow_map_item':([8,72,],[39,92,]),'scalar_group':([4,7,12,26,30,62,82,],[33,37,45,33,33,33,33,]),'collection':([0,1,4,5,9,14,30,50,62,82,],[15,27,15,15,15,48,66,81,90,97,]),'map_item_key':([0,1,4,5,9,10,14,30,50,62,82,],[16,16,16,16,16,16,16,16,16,16,16,]),'sequence':([0,1,4,5,9,14,30,50,51,62,82,],[17,17,17,17,17,17,17,17,83,17,17,]),'map_item':([0,1,4,5,9,10,14,30,50,62,82,],[18,18,18,18,18,44,18,18,18,18,18,]),'scalar':([0,1,2,3,4,5,8,9,10,14,20,22,25,30,42,50,51,62,72,80,82,87,],[19,28,29,31,19,19,40,19,28,49,55,57,63,28,74,28,84,28,40,94,98,57,]),'ignore_indent_dedent':([0,1,2,3,4,5,8,9,10,14,20,22,25,30,42,50,51,62,72,80,82,87,],[20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,]),'docs':([0,],[5,]),'sequence_item':([0,1,4,5,9,14,17,30,50,51,62,82,83,],[6,6,6,6,6,6,53,6,6,6,6,6,53,]),'flow_map':([8,],[41,]),'doc':([0,4,5,9,],[21,34,36,43,]),'flow_collection':([0,1,4,5,9,14,25,30,50,51,62,82,],[23,23,23,23,23,23,64,23,23,85,23,23,]),'flow_sequence_item':([22,87,],[58,101,]),'flow_map_item_value':([42,],[75,]),'map_item_value':([16,],[52,]),'flow_sequence':([22,],[59,]),'map':([0,1,4,5,9,14,30,50,62,82,],[10,10,10,10,10,10,10,10,10,10,]),'flow_map_item_key':([8,72,],[42,42,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> docs","S'",1,None,None,None),
  ('docs -> doc','docs',1,'p_docs__last','productions.py',19),
  ('docs -> doc DOC_END','docs',2,'p_docs__last','productions.py',20),
  ('docs -> docs doc','docs',2,'p_docs__init','productions.py',27),
  ('doc -> DOC_START doc DOC_END','doc',3,'p_doc__indent','productions.py',34),
  ('doc -> DOC_START doc','doc',2,'p_doc__indent','productions.py',35),
  ('doc -> INDENT doc DEDENT','doc',3,'p_doc__indent','productions.py',36),
  ('doc -> collection','doc',1,'p_doc','productions.py',43),
  ('doc -> scalar','doc',1,'p_doc','productions.py',44),
  ('scalar -> ignore_indent_dedent scalar','scalar',2,'p_doc_scalar_collection_ignore','productions.py',51),
  ('collection -> sequence','collection',1,'p_collection','productions.py',58),
  ('collection -> map','collection',1,'p_collection','productions.py',59),
  ('collection -> flow_collection','collection',1,'p_collection','productions.py',60),
  ('map -> map_item','map',1,'p_map__last','productions.py',67),
  ('map -> map map_item','map',2,'p_map__init','productions.py',74),
  ('map_item -> map_item_key map_item_value','map_item',2,'p_map_item','productions.py',81),
  ('map_item -> B_MAP_COMPACT_KEY scalar B_MAP_VALUE scalar DEDENT','map_item',5,'p_map_item__compact_scalar','productions.py',88),
  ('map_item_key -> B_MAP_KEY scalar','map_item_key',2,'p_map_item_key__complex_key_scalar','productions.py',95),
  ('map_item_key -> scalar','map_item_key',1,'p_map_item_key','productions.py',102),
  ('map_item_key -> B_MAP_KEY INDENT collection DEDENT','map_item_key',4,'p_map_item___key_value__collection','productions.py',109),
  ('map_item_value -> B_MAP_VALUE INDENT collection DEDENT','map_item_value',4,'p_map_item___key_value__collection','productions.py',110),
  ('map_item_value -> B_MAP_VALUE flow_collection','map_item_value',2,'p_map_item_value__flow_collection','productions.py',117),
  ('map_item_value -> B_MAP_VALUE scalar','map_item_value',2,'p_map_item_value__scalar','productions.py',124),
  ('map_item_value -> B_MAP_VALUE INDENT scalar DEDENT','map_item_value',4,'p_map_item_value__scalar_indented','productions.py',131),
  ('map_item_value -> B_MAP_VALUE sequence','map_item_value',2,'p_map_item_value__sequence_no_indent','productions.py',138),
  ('sequence -> sequence_item','sequence',1,'p_sequence__last','productions.py',152),
  ('sequence -> sequence sequence_item','sequence',2,'p_sequence__init','productions.py',159),
  ('sequence_item -> B_SEQUENCE_START scalar','sequence_item',2,'p_sequence_item__scalar','productions.py',166),
  ('sequence_item -> B_SEQUENCE_START INDENT collection DEDENT','sequence_item',4,'p_sequence_item__collection','productions.py',180),
  ('map_item_key -> B_MAP_COMPACT_KEY collection DEDENT','map_item_key',3,'p_map_item__key__map_item_value__sequence_item__compact_collection','productions.py',187),
  ('map_item_value -> B_MAP_COMPACT_VALUE collection DEDENT','map_item_value',3,'p_map_item__key__map_item_value__sequence_item__compact_collection','productions.py',188),
  ('sequence_item -> B_SEQUENCE_COMPACT_START collection DEDENT','sequence_item',3,'p_map_item__key__map_item_value__sequence_item__compact_collection','productions.py',189),
  ('sequence_item -> B_SEQUENCE_START flow_collection','sequence_item',2,'p_sequence_item__flow_collection','productions.py',196),
  ('scalar -> DOUBLEQUOTE_START SCALAR DOUBLEQUOTE_END','scalar',3,'p_scalar__doublequote','productions.py',203),
  ('scalar -> SINGLEQUOTE_START SCALAR SINGLEQUOTE_END','scalar',3,'p_scalar__singlequote','productions.py',212),
  ('scalar -> DOUBLEQUOTE_START DOUBLEQUOTE_END','scalar',2,'p_scalar__quote_empty','productions.py',219),
  ('scalar -> SINGLEQUOTE_START SINGLEQUOTE_END','scalar',2,'p_scalar__quote_empty','productions.py',220),
  ('scalar -> CAST_TYPE scalar','scalar',2,'p_scalar__explicit_cast','productions.py',227),
  ('scalar -> SCALAR','scalar',1,'p_scalar','productions.py',234),
  ('scalar -> B_LITERAL_START scalar_group B_LITERAL_END','scalar',3,'p_scalar__literal','productions.py',241),
  ('scalar -> B_FOLD_START scalar_group B_FOLD_END','scalar',3,'p_scalar__folded','productions.py',249),
  ('scalar -> INDENT scalar_group DEDENT','scalar',3,'p_scalar__indented_flow','productions.py',258),
  ('scalar -> scalar INDENT SCALAR DEDENT','scalar',4,'p_scalar__string_indented_multi_line','productions.py',267),
  ('scalar_group -> SCALAR','scalar_group',1,'p_scalar_group','productions.py',276),
  ('scalar_group -> scalar_group SCALAR','scalar_group',2,'p_scalar_group','productions.py',277),
  ('ignore_indent_dedent -> INDENT DEDENT','ignore_indent_dedent',2,'p_ignore_indent_dedent','productions.py',291),
  ('flow_collection -> F_SEQUENCE_START flow_sequence F_SEQUENCE_END','flow_collection',3,'p_flow_collection','productions.py',296),
  ('flow_collection -> F_SEQUENCE_START flow_sequence F_SEP F_SEQUENCE_END','flow_collection',4,'p_flow_collection','productions.py',297),
  ('flow_collection -> F_MAP_START flow_map F_MAP_END','flow_collection',3,'p_flow_collection','productions.py',298),
  ('flow_collection -> F_MAP_START flow_map F_SEP F_MAP_END','flow_collection',4,'p_flow_collection','productions.py',299),
  ('flow_sequence -> flow_sequence_item','flow_sequence',1,'p_flow_sequence__last','productions.py',306),
  ('flow_sequence -> flow_sequence F_SEP flow_sequence_item','flow_sequence',3,'p_flow_sequence__init','productions.py',313),
  ('flow_sequence_item -> scalar','flow_sequence_item',1,'p_flow_sequence_item','productions.py',320),
  ('flow_map -> flow_map_item','flow_map',1,'p_flow_map__last','productions.py',327),
  ('flow_map -> flow_map F_SEP flow_map_item','flow_map',3,'p_flow_map__init','productions.py',334),
  ('flow_map_item -> flow_map_item_key flow_map_item_value','flow_map_item',2,'p_flow_map_item','productions.py',341),
  ('flow_map_item_key -> scalar F_MAP_KEY','flow_map_item_key',2,'p_flow_map_item_key','productions.py',348),
  ('flow_map_item_value -> scalar','flow_map_item_value',1,'p_flow_map_item_value','productions.py',355),
]