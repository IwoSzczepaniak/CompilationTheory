
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "left+-DOTADDDOTSUBleft*/DOTMULDOTDIVright=ADDASSIGNSUBASSIGNMULASSIGNDIVASSIGNnonassocLTGTEQNEGELEnonassocIFELSErightUMINUS'ADDASSIGN BREAK CONTINUE DIVASSIGN DOTADD DOTDIV DOTMUL DOTSUB ELSE EQ EYE FLOAT FOR GE GT ID IF INTNUM LE LT MULASSIGN NE ONES PRINT RETURN STRING SUBASSIGN UMINUS WHILE ZEROSinstructions : instruction\n                    | instruction instructionsinstruction : block\n                   | conditional\n                   | loop\n                   | statement ';'\n                   | error ';'statement : assignment\n                 | flow_keyword\n                 | return\n                 | printflow_keyword : BREAK\n                    | CONTINUEexpression : comparison_expression\n                  | numeric_expressionblock : '{' instructions '}'\n             | '{' error '}'print : PRINT print_bodyprint_body : string\n                  | expression\n                  | string ',' print_body\n                  | expression ',' print_bodyreturn : RETURN expression\n              | RETURNstring : STRINGvector : '[' vector_body ']'\n              | '[' ']'vector_body : numeric_expression\n                   | vector_body ',' numeric_expressionmatrix : '[' matrix_body ']'\n              | '[' ']'matrix_body : vector\n                   | matrix_body ',' vectorarray_range : var '[' expression ',' expression ']'fun : fun_name '(' numeric_expression ')'\n           | fun_name '(' error ')'fun_name : ZEROS\n                | ONES\n                | EYEloop : while\n            | forwhile : WHILE '(' expression ')' instructionfor : FOR ID '=' numeric_expression ':' numeric_expression instructionconditional : IF '(' expression ')' instruction %prec IF\n                   | IF '(' expression ')' instruction ELSE instructionassignment_lhs : var\n                      | array_rangeassignment : assignment_lhs assignment_operator expression\n                  | assignment_lhs '=' stringassignment_operator : '='\n                           | ADDASSIGN\n                           | SUBASSIGN\n                           | MULASSIGN\n                           | DIVASSIGNvar : ID\n           | var '[' numeric_expression ']'num : INTNUM\n           | FLOAT\n           | varunary_op : negation\n                | transpositionnegation : '-' numeric_expression %prec UMINUStransposition : numeric_expression '\\''numeric_expression : num\n                          | matrix\n                          | unary_op\n                          | fun\n                          | '(' numeric_expression ')'numeric_expression : numeric_expression '+' numeric_expression\n                          | numeric_expression '-' numeric_expression\n                          | numeric_expression '*' numeric_expression\n                          | numeric_expression '/' numeric_expression\n                          | numeric_expression DOTADD numeric_expression\n                          | numeric_expression DOTSUB numeric_expression\n                          | numeric_expression DOTMUL numeric_expression\n                          | numeric_expression DOTDIV numeric_expressioncomparison_expression : numeric_expression LT numeric_expression\n           | numeric_expression GT numeric_expression\n           | numeric_expression EQ numeric_expression\n           | numeric_expression NE numeric_expression\n           | numeric_expression GE numeric_expression\n           | numeric_expression LE numeric_expression\n           | '(' comparison_expression ')'"
    
_lr_action_items = {'error':([0,2,3,4,5,8,10,11,18,27,28,44,45,46,47,49,50,51,53,54,64,65,85,88,93,95,101,102,110,111,112,113,114,115,116,117,119,125,131,134,135,140,141,143,144,147,148,],[7,7,-3,-4,-5,30,-40,-41,-55,-6,-7,-64,-65,-66,-67,-57,-58,-59,-60,-61,-16,-17,-63,-62,-31,128,7,7,-69,-70,-71,-72,-73,-74,-75,-76,-68,-30,-56,-44,-42,-35,-36,7,7,-45,-43,]),'{':([0,2,3,4,5,8,10,11,18,27,28,44,45,46,47,49,50,51,53,54,64,65,85,88,93,101,102,110,111,112,113,114,115,116,117,119,125,131,134,135,140,141,143,144,147,148,],[8,8,-3,-4,-5,8,-40,-41,-55,-6,-7,-64,-65,-66,-67,-57,-58,-59,-60,-61,-16,-17,-63,-62,-31,8,8,-69,-70,-71,-72,-73,-74,-75,-76,-68,-30,-56,-44,-42,-35,-36,8,8,-45,-43,]),'IF':([0,2,3,4,5,8,10,11,18,27,28,44,45,46,47,49,50,51,53,54,64,65,85,88,93,101,102,110,111,112,113,114,115,116,117,119,125,131,134,135,140,141,143,144,147,148,],[9,9,-3,-4,-5,9,-40,-41,-55,-6,-7,-64,-65,-66,-67,-57,-58,-59,-60,-61,-16,-17,-63,-62,-31,9,9,-69,-70,-71,-72,-73,-74,-75,-76,-68,-30,-56,-44,-42,-35,-36,9,9,-45,-43,]),'WHILE':([0,2,3,4,5,8,10,11,18,27,28,44,45,46,47,49,50,51,53,54,64,65,85,88,93,101,102,110,111,112,113,114,115,116,117,119,125,131,134,135,140,141,143,144,147,148,],[16,16,-3,-4,-5,16,-40,-41,-55,-6,-7,-64,-65,-66,-67,-57,-58,-59,-60,-61,-16,-17,-63,-62,-31,16,16,-69,-70,-71,-72,-73,-74,-75,-76,-68,-30,-56,-44,-42,-35,-36,16,16,-45,-43,]),'FOR':([0,2,3,4,5,8,10,11,18,27,28,44,45,46,47,49,50,51,53,54,64,65,85,88,93,101,102,110,111,112,113,114,115,116,117,119,125,131,134,135,140,141,143,144,147,148,],[17,17,-3,-4,-5,17,-40,-41,-55,-6,-7,-64,-65,-66,-67,-57,-58,-59,-60,-61,-16,-17,-63,-62,-31,17,17,-69,-70,-71,-72,-73,-74,-75,-76,-68,-30,-56,-44,-42,-35,-36,17,17,-45,-43,]),'BREAK':([0,2,3,4,5,8,10,11,18,27,28,44,45,46,47,49,50,51,53,54,64,65,85,88,93,101,102,110,111,112,113,114,115,116,117,119,125,131,134,135,140,141,143,144,147,148,],[20,20,-3,-4,-5,20,-40,-41,-55,-6,-7,-64,-65,-66,-67,-57,-58,-59,-60,-61,-16,-17,-63,-62,-31,20,20,-69,-70,-71,-72,-73,-74,-75,-76,-68,-30,-56,-44,-42,-35,-36,20,20,-45,-43,]),'CONTINUE':([0,2,3,4,5,8,10,11,18,27,28,44,45,46,47,49,50,51,53,54,64,65,85,88,93,101,102,110,111,112,113,114,115,116,117,119,125,131,134,135,140,141,143,144,147,148,],[21,21,-3,-4,-5,21,-40,-41,-55,-6,-7,-64,-65,-66,-67,-57,-58,-59,-60,-61,-16,-17,-63,-62,-31,21,21,-69,-70,-71,-72,-73,-74,-75,-76,-68,-30,-56,-44,-42,-35,-36,21,21,-45,-43,]),'RETURN':([0,2,3,4,5,8,10,11,18,27,28,44,45,46,47,49,50,51,53,54,64,65,85,88,93,101,102,110,111,112,113,114,115,116,117,119,125,131,134,135,140,141,143,144,147,148,],[22,22,-3,-4,-5,22,-40,-41,-55,-6,-7,-64,-65,-66,-67,-57,-58,-59,-60,-61,-16,-17,-63,-62,-31,22,22,-69,-70,-71,-72,-73,-74,-75,-76,-68,-30,-56,-44,-42,-35,-36,22,22,-45,-43,]),'PRINT':([0,2,3,4,5,8,10,11,18,27,28,44,45,46,47,49,50,51,53,54,64,65,85,88,93,101,102,110,111,112,113,114,115,116,117,119,125,131,134,135,140,141,143,144,147,148,],[23,23,-3,-4,-5,23,-40,-41,-55,-6,-7,-64,-65,-66,-67,-57,-58,-59,-60,-61,-16,-17,-63,-62,-31,23,23,-69,-70,-71,-72,-73,-74,-75,-76,-68,-30,-56,-44,-42,-35,-36,23,23,-45,-43,]),'ID':([0,2,3,4,5,8,10,11,17,18,22,23,27,28,31,32,34,35,36,37,38,39,43,44,45,46,47,48,49,50,51,53,54,63,64,65,68,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,88,89,90,91,93,95,96,97,100,101,102,110,111,112,113,114,115,116,117,119,125,131,132,134,135,136,138,140,141,143,144,147,148,],[18,18,-3,-4,-5,18,-40,-41,33,-55,18,18,-6,-7,18,18,18,-50,-51,-52,-53,-54,18,-64,-65,-66,-67,18,-57,-58,-59,-60,-61,18,-16,-17,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,-63,-62,18,18,18,-31,18,18,18,18,18,18,-69,-70,-71,-72,-73,-74,-75,-76,-68,-30,-56,18,-44,-42,18,18,-35,-36,18,18,-45,-43,]),'$end':([1,2,3,4,5,10,11,26,27,28,64,65,134,135,147,148,],[0,-1,-3,-4,-5,-40,-41,-2,-6,-7,-16,-17,-44,-42,-45,-43,]),'}':([2,3,4,5,10,11,26,27,28,29,30,64,65,134,135,147,148,],[-1,-3,-4,-5,-40,-41,-2,-6,-7,64,65,-16,-17,-44,-42,-45,-43,]),'ELSE':([3,4,5,10,11,27,28,64,65,134,135,147,148,],[-3,-4,-5,-40,-41,-6,-7,-16,-17,None,-42,-45,-43,]),';':([6,7,12,13,14,15,18,20,21,22,30,40,41,42,44,45,46,47,49,50,51,53,54,59,60,61,62,69,70,85,88,93,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,125,129,130,131,140,141,],[27,28,-8,-9,-10,-11,-55,-12,-13,-24,28,-23,-14,-15,-64,-65,-66,-67,-57,-58,-59,-60,-61,-18,-19,-20,-25,-48,-49,-63,-62,-31,-77,-78,-79,-80,-81,-82,-69,-70,-71,-72,-73,-74,-75,-76,-83,-68,-30,-21,-22,-56,-35,-36,]),'(':([9,16,22,23,31,32,34,35,36,37,38,39,43,48,55,56,57,58,63,68,71,72,73,74,75,76,77,78,79,80,81,82,83,84,89,90,91,95,96,97,100,132,136,138,],[31,32,43,43,43,43,43,-50,-51,-52,-53,-54,43,89,95,-37,-38,-39,100,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,43,43,100,43,89,89,]),'[':([18,22,23,24,31,32,34,35,36,37,38,39,43,48,51,52,63,68,71,72,73,74,75,76,77,78,79,80,81,82,83,84,89,90,91,95,96,97,100,126,131,132,136,138,],[-55,52,52,63,52,52,52,-50,-51,-52,-53,-54,52,52,90,91,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,91,-56,52,52,52,]),'=':([18,19,24,25,33,131,146,],[-55,35,-46,-47,68,-56,-34,]),'ADDASSIGN':([18,19,24,25,131,146,],[-55,36,-46,-47,-56,-34,]),'SUBASSIGN':([18,19,24,25,131,146,],[-55,37,-46,-47,-56,-34,]),'MULASSIGN':([18,19,24,25,131,146,],[-55,38,-46,-47,-56,-34,]),'DIVASSIGN':([18,19,24,25,131,146,],[-55,39,-46,-47,-56,-34,]),'LT':([18,42,44,45,46,47,49,50,51,53,54,85,87,88,93,98,110,111,112,113,114,115,116,117,119,125,131,133,140,141,],[-55,71,-64,-65,-66,-67,-57,-58,-59,-60,-61,-63,71,-62,-31,71,-69,-70,-71,-72,-73,-74,-75,-76,-68,-30,-56,71,-35,-36,]),'GT':([18,42,44,45,46,47,49,50,51,53,54,85,87,88,93,98,110,111,112,113,114,115,116,117,119,125,131,133,140,141,],[-55,72,-64,-65,-66,-67,-57,-58,-59,-60,-61,-63,72,-62,-31,72,-69,-70,-71,-72,-73,-74,-75,-76,-68,-30,-56,72,-35,-36,]),'EQ':([18,42,44,45,46,47,49,50,51,53,54,85,87,88,93,98,110,111,112,113,114,115,116,117,119,125,131,133,140,141,],[-55,73,-64,-65,-66,-67,-57,-58,-59,-60,-61,-63,73,-62,-31,73,-69,-70,-71,-72,-73,-74,-75,-76,-68,-30,-56,73,-35,-36,]),'NE':([18,42,44,45,46,47,49,50,51,53,54,85,87,88,93,98,110,111,112,113,114,115,116,117,119,125,131,133,140,141,],[-55,74,-64,-65,-66,-67,-57,-58,-59,-60,-61,-63,74,-62,-31,74,-69,-70,-71,-72,-73,-74,-75,-76,-68,-30,-56,74,-35,-36,]),'GE':([18,42,44,45,46,47,49,50,51,53,54,85,87,88,93,98,110,111,112,113,114,115,116,117,119,125,131,133,140,141,],[-55,75,-64,-65,-66,-67,-57,-58,-59,-60,-61,-63,75,-62,-31,75,-69,-70,-71,-72,-73,-74,-75,-76,-68,-30,-56,75,-35,-36,]),'LE':([18,42,44,45,46,47,49,50,51,53,54,85,87,88,93,98,110,111,112,113,114,115,116,117,119,125,131,133,140,141,],[-55,76,-64,-65,-66,-67,-57,-58,-59,-60,-61,-63,76,-62,-31,76,-69,-70,-71,-72,-73,-74,-75,-76,-68,-30,-56,76,-35,-36,]),'+':([18,42,44,45,46,47,49,50,51,53,54,85,87,88,93,98,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,119,120,121,124,125,127,131,133,140,141,144,145,],[-55,77,-64,-65,-66,-67,-57,-58,-59,-60,-61,-63,77,-62,-31,77,77,77,77,77,77,77,77,-69,-70,-71,-72,-73,-74,-75,-76,-68,77,77,77,-30,77,-56,77,-35,-36,77,77,]),'-':([18,22,23,31,32,34,35,36,37,38,39,42,43,44,45,46,47,48,49,50,51,53,54,63,68,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,87,88,89,90,91,93,95,96,97,98,100,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,119,120,121,124,125,127,131,132,133,136,138,140,141,144,145,],[-55,48,48,48,48,48,-50,-51,-52,-53,-54,78,48,-64,-65,-66,-67,48,-57,-58,-59,-60,-61,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,-63,78,-62,48,48,48,-31,48,48,48,78,48,78,78,78,78,78,78,78,-69,-70,-71,-72,-73,-74,-75,-76,-68,78,78,78,-30,78,-56,48,78,48,48,-35,-36,78,78,]),'*':([18,42,44,45,46,47,49,50,51,53,54,85,87,88,93,98,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,119,120,121,124,125,127,131,133,140,141,144,145,],[-55,79,-64,-65,-66,-67,-57,-58,-59,-60,-61,-63,79,-62,-31,79,79,79,79,79,79,79,79,79,79,-71,-72,79,79,-75,-76,-68,79,79,79,-30,79,-56,79,-35,-36,79,79,]),'/':([18,42,44,45,46,47,49,50,51,53,54,85,87,88,93,98,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,119,120,121,124,125,127,131,133,140,141,144,145,],[-55,80,-64,-65,-66,-67,-57,-58,-59,-60,-61,-63,80,-62,-31,80,80,80,80,80,80,80,80,80,80,-71,-72,80,80,-75,-76,-68,80,80,80,-30,80,-56,80,-35,-36,80,80,]),'DOTADD':([18,42,44,45,46,47,49,50,51,53,54,85,87,88,93,98,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,119,120,121,124,125,127,131,133,140,141,144,145,],[-55,81,-64,-65,-66,-67,-57,-58,-59,-60,-61,-63,81,-62,-31,81,81,81,81,81,81,81,81,-69,-70,-71,-72,-73,-74,-75,-76,-68,81,81,81,-30,81,-56,81,-35,-36,81,81,]),'DOTSUB':([18,42,44,45,46,47,49,50,51,53,54,85,87,88,93,98,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,119,120,121,124,125,127,131,133,140,141,144,145,],[-55,82,-64,-65,-66,-67,-57,-58,-59,-60,-61,-63,82,-62,-31,82,82,82,82,82,82,82,82,-69,-70,-71,-72,-73,-74,-75,-76,-68,82,82,82,-30,82,-56,82,-35,-36,82,82,]),'DOTMUL':([18,42,44,45,46,47,49,50,51,53,54,85,87,88,93,98,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,119,120,121,124,125,127,131,133,140,141,144,145,],[-55,83,-64,-65,-66,-67,-57,-58,-59,-60,-61,-63,83,-62,-31,83,83,83,83,83,83,83,83,83,83,-71,-72,83,83,-75,-76,-68,83,83,83,-30,83,-56,83,-35,-36,83,83,]),'DOTDIV':([18,42,44,45,46,47,49,50,51,53,54,85,87,88,93,98,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,119,120,121,124,125,127,131,133,140,141,144,145,],[-55,84,-64,-65,-66,-67,-57,-58,-59,-60,-61,-63,84,-62,-31,84,84,84,84,84,84,84,84,84,84,-71,-72,84,84,-75,-76,-68,84,84,84,-30,84,-56,84,-35,-36,84,84,]),"'":([18,42,44,45,46,47,49,50,51,53,54,85,87,88,93,98,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,119,120,121,124,125,127,131,133,140,141,144,145,],[-55,85,-64,-65,-66,-67,-57,-58,-59,-60,-61,-63,85,85,-31,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,85,-68,85,85,85,-30,85,-56,85,-35,-36,85,85,]),',':([18,41,42,44,45,46,47,49,50,51,53,54,60,61,62,85,88,92,93,94,98,99,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,122,123,124,125,131,137,139,140,141,145,],[-55,-14,-15,-64,-65,-66,-67,-57,-58,-59,-60,-61,96,97,-25,-63,-62,126,-31,-32,-15,132,-77,-78,-79,-80,-81,-82,-69,-70,-71,-72,-73,-74,-75,-76,-83,-68,138,-27,-28,-30,-56,-26,-33,-35,-36,-29,]),')':([18,41,42,44,45,46,47,49,50,51,53,54,66,67,85,86,87,88,93,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,125,127,128,131,133,140,141,],[-55,-14,-15,-64,-65,-66,-67,-57,-58,-59,-60,-61,101,102,-63,118,119,-62,-31,-77,-78,-79,-80,-81,-82,-69,-70,-71,-72,-73,-74,-75,-76,-83,-68,119,-30,140,141,-56,119,-35,-36,]),']':([18,41,42,44,45,46,47,49,50,51,52,53,54,85,88,91,92,93,94,98,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,121,122,123,124,125,131,137,139,140,141,142,145,],[-55,-14,-15,-64,-65,-66,-67,-57,-58,-59,93,-60,-61,-63,-62,123,125,-31,-32,131,-77,-78,-79,-80,-81,-82,-69,-70,-71,-72,-73,-74,-75,-76,-83,-68,131,137,-27,-28,-30,-56,-26,-33,-35,-36,146,-29,]),':':([18,44,45,46,47,49,50,51,53,54,85,88,93,103,110,111,112,113,114,115,116,117,119,125,131,140,141,],[-55,-64,-65,-66,-67,-57,-58,-59,-60,-61,-63,-62,-31,136,-69,-70,-71,-72,-73,-74,-75,-76,-68,-30,-56,-35,-36,]),'INTNUM':([22,23,31,32,34,35,36,37,38,39,43,48,63,68,71,72,73,74,75,76,77,78,79,80,81,82,83,84,89,90,91,95,96,97,100,132,136,138,],[49,49,49,49,49,-50,-51,-52,-53,-54,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,]),'FLOAT':([22,23,31,32,34,35,36,37,38,39,43,48,63,68,71,72,73,74,75,76,77,78,79,80,81,82,83,84,89,90,91,95,96,97,100,132,136,138,],[50,50,50,50,50,-50,-51,-52,-53,-54,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,]),'ZEROS':([22,23,31,32,34,35,36,37,38,39,43,48,63,68,71,72,73,74,75,76,77,78,79,80,81,82,83,84,89,90,91,95,96,97,100,132,136,138,],[56,56,56,56,56,-50,-51,-52,-53,-54,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,]),'ONES':([22,23,31,32,34,35,36,37,38,39,43,48,63,68,71,72,73,74,75,76,77,78,79,80,81,82,83,84,89,90,91,95,96,97,100,132,136,138,],[57,57,57,57,57,-50,-51,-52,-53,-54,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,]),'EYE':([22,23,31,32,34,35,36,37,38,39,43,48,63,68,71,72,73,74,75,76,77,78,79,80,81,82,83,84,89,90,91,95,96,97,100,132,136,138,],[58,58,58,58,58,-50,-51,-52,-53,-54,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,]),'STRING':([23,35,96,97,],[62,62,62,62,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'instructions':([0,2,8,],[1,26,29,]),'instruction':([0,2,8,101,102,143,144,],[2,2,2,134,135,147,148,]),'block':([0,2,8,101,102,143,144,],[3,3,3,3,3,3,3,]),'conditional':([0,2,8,101,102,143,144,],[4,4,4,4,4,4,4,]),'loop':([0,2,8,101,102,143,144,],[5,5,5,5,5,5,5,]),'statement':([0,2,8,101,102,143,144,],[6,6,6,6,6,6,6,]),'while':([0,2,8,101,102,143,144,],[10,10,10,10,10,10,10,]),'for':([0,2,8,101,102,143,144,],[11,11,11,11,11,11,11,]),'assignment':([0,2,8,101,102,143,144,],[12,12,12,12,12,12,12,]),'flow_keyword':([0,2,8,101,102,143,144,],[13,13,13,13,13,13,13,]),'return':([0,2,8,101,102,143,144,],[14,14,14,14,14,14,14,]),'print':([0,2,8,101,102,143,144,],[15,15,15,15,15,15,15,]),'assignment_lhs':([0,2,8,101,102,143,144,],[19,19,19,19,19,19,19,]),'var':([0,2,8,22,23,31,32,34,43,48,63,68,71,72,73,74,75,76,77,78,79,80,81,82,83,84,89,90,91,95,96,97,100,101,102,132,136,138,143,144,],[24,24,24,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,24,24,51,51,51,24,24,]),'array_range':([0,2,8,101,102,143,144,],[25,25,25,25,25,25,25,]),'assignment_operator':([19,],[34,]),'expression':([22,23,31,32,34,63,96,97,132,],[40,61,66,67,69,99,61,61,142,]),'comparison_expression':([22,23,31,32,34,43,63,96,97,100,132,],[41,41,41,41,41,86,41,41,41,86,41,]),'numeric_expression':([22,23,31,32,34,43,48,63,68,71,72,73,74,75,76,77,78,79,80,81,82,83,84,89,90,91,95,96,97,100,132,136,138,],[42,42,42,42,42,87,88,98,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,120,121,124,127,42,42,133,42,144,145,]),'num':([22,23,31,32,34,43,48,63,68,71,72,73,74,75,76,77,78,79,80,81,82,83,84,89,90,91,95,96,97,100,132,136,138,],[44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'matrix':([22,23,31,32,34,43,48,63,68,71,72,73,74,75,76,77,78,79,80,81,82,83,84,89,90,91,95,96,97,100,132,136,138,],[45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,]),'unary_op':([22,23,31,32,34,43,48,63,68,71,72,73,74,75,76,77,78,79,80,81,82,83,84,89,90,91,95,96,97,100,132,136,138,],[46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,]),'fun':([22,23,31,32,34,43,48,63,68,71,72,73,74,75,76,77,78,79,80,81,82,83,84,89,90,91,95,96,97,100,132,136,138,],[47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,]),'negation':([22,23,31,32,34,43,48,63,68,71,72,73,74,75,76,77,78,79,80,81,82,83,84,89,90,91,95,96,97,100,132,136,138,],[53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,]),'transposition':([22,23,31,32,34,43,48,63,68,71,72,73,74,75,76,77,78,79,80,81,82,83,84,89,90,91,95,96,97,100,132,136,138,],[54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,]),'fun_name':([22,23,31,32,34,43,48,63,68,71,72,73,74,75,76,77,78,79,80,81,82,83,84,89,90,91,95,96,97,100,132,136,138,],[55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,]),'print_body':([23,96,97,],[59,129,130,]),'string':([23,35,96,97,],[60,70,60,60,]),'matrix_body':([52,],[92,]),'vector':([52,126,],[94,139,]),'vector_body':([91,],[122,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> instructions","S'",1,None,None,None),
  ('instructions -> instruction','instructions',1,'p_instructions','MyParser.py',31),
  ('instructions -> instruction instructions','instructions',2,'p_instructions','MyParser.py',32),
  ('instruction -> block','instruction',1,'p_instruction','MyParser.py',36),
  ('instruction -> conditional','instruction',1,'p_instruction','MyParser.py',37),
  ('instruction -> loop','instruction',1,'p_instruction','MyParser.py',38),
  ('instruction -> statement ;','instruction',2,'p_instruction','MyParser.py',39),
  ('instruction -> error ;','instruction',2,'p_instruction','MyParser.py',40),
  ('statement -> assignment','statement',1,'p_statement','MyParser.py',44),
  ('statement -> flow_keyword','statement',1,'p_statement','MyParser.py',45),
  ('statement -> return','statement',1,'p_statement','MyParser.py',46),
  ('statement -> print','statement',1,'p_statement','MyParser.py',47),
  ('flow_keyword -> BREAK','flow_keyword',1,'p_flow_keyword','MyParser.py',51),
  ('flow_keyword -> CONTINUE','flow_keyword',1,'p_flow_keyword','MyParser.py',52),
  ('expression -> comparison_expression','expression',1,'p_expression','MyParser.py',56),
  ('expression -> numeric_expression','expression',1,'p_expression','MyParser.py',57),
  ('block -> { instructions }','block',3,'p_block','MyParser.py',61),
  ('block -> { error }','block',3,'p_block','MyParser.py',62),
  ('print -> PRINT print_body','print',2,'p_print','MyParser.py',66),
  ('print_body -> string','print_body',1,'p_print_body','MyParser.py',70),
  ('print_body -> expression','print_body',1,'p_print_body','MyParser.py',71),
  ('print_body -> string , print_body','print_body',3,'p_print_body','MyParser.py',72),
  ('print_body -> expression , print_body','print_body',3,'p_print_body','MyParser.py',73),
  ('return -> RETURN expression','return',2,'p_return','MyParser.py',77),
  ('return -> RETURN','return',1,'p_return','MyParser.py',78),
  ('string -> STRING','string',1,'p_string','MyParser.py',82),
  ('vector -> [ vector_body ]','vector',3,'p_vector','MyParser.py',90),
  ('vector -> [ ]','vector',2,'p_vector','MyParser.py',91),
  ('vector_body -> numeric_expression','vector_body',1,'p_vector_body','MyParser.py',95),
  ('vector_body -> vector_body , numeric_expression','vector_body',3,'p_vector_body','MyParser.py',96),
  ('matrix -> [ matrix_body ]','matrix',3,'p_matrix','MyParser.py',100),
  ('matrix -> [ ]','matrix',2,'p_matrix','MyParser.py',101),
  ('matrix_body -> vector','matrix_body',1,'p_matrix_body','MyParser.py',105),
  ('matrix_body -> matrix_body , vector','matrix_body',3,'p_matrix_body','MyParser.py',106),
  ('array_range -> var [ expression , expression ]','array_range',6,'p_array_range','MyParser.py',114),
  ('fun -> fun_name ( numeric_expression )','fun',4,'p_fun','MyParser.py',122),
  ('fun -> fun_name ( error )','fun',4,'p_fun','MyParser.py',123),
  ('fun_name -> ZEROS','fun_name',1,'p_fun_name','MyParser.py',127),
  ('fun_name -> ONES','fun_name',1,'p_fun_name','MyParser.py',128),
  ('fun_name -> EYE','fun_name',1,'p_fun_name','MyParser.py',129),
  ('loop -> while','loop',1,'p_loop','MyParser.py',137),
  ('loop -> for','loop',1,'p_loop','MyParser.py',138),
  ('while -> WHILE ( expression ) instruction','while',5,'p_while','MyParser.py',142),
  ('for -> FOR ID = numeric_expression : numeric_expression instruction','for',7,'p_for','MyParser.py',146),
  ('conditional -> IF ( expression ) instruction','conditional',5,'p_conditional','MyParser.py',154),
  ('conditional -> IF ( expression ) instruction ELSE instruction','conditional',7,'p_conditional','MyParser.py',155),
  ('assignment_lhs -> var','assignment_lhs',1,'p_assignment_lhs','MyParser.py',163),
  ('assignment_lhs -> array_range','assignment_lhs',1,'p_assignment_lhs','MyParser.py',164),
  ('assignment -> assignment_lhs assignment_operator expression','assignment',3,'p_assignment','MyParser.py',168),
  ('assignment -> assignment_lhs = string','assignment',3,'p_assignment','MyParser.py',169),
  ('assignment_operator -> =','assignment_operator',1,'p_assignment_operator','MyParser.py',173),
  ('assignment_operator -> ADDASSIGN','assignment_operator',1,'p_assignment_operator','MyParser.py',174),
  ('assignment_operator -> SUBASSIGN','assignment_operator',1,'p_assignment_operator','MyParser.py',175),
  ('assignment_operator -> MULASSIGN','assignment_operator',1,'p_assignment_operator','MyParser.py',176),
  ('assignment_operator -> DIVASSIGN','assignment_operator',1,'p_assignment_operator','MyParser.py',177),
  ('var -> ID','var',1,'p_var','MyParser.py',185),
  ('var -> var [ numeric_expression ]','var',4,'p_var','MyParser.py',186),
  ('num -> INTNUM','num',1,'p_num','MyParser.py',190),
  ('num -> FLOAT','num',1,'p_num','MyParser.py',191),
  ('num -> var','num',1,'p_num','MyParser.py',192),
  ('unary_op -> negation','unary_op',1,'p_unary_op','MyParser.py',200),
  ('unary_op -> transposition','unary_op',1,'p_unary_op','MyParser.py',201),
  ('negation -> - numeric_expression','negation',2,'p_neg','MyParser.py',205),
  ("transposition -> numeric_expression '",'transposition',2,'p_transposition','MyParser.py',209),
  ('numeric_expression -> num','numeric_expression',1,'p_numeric_expression','MyParser.py',213),
  ('numeric_expression -> matrix','numeric_expression',1,'p_numeric_expression','MyParser.py',214),
  ('numeric_expression -> unary_op','numeric_expression',1,'p_numeric_expression','MyParser.py',215),
  ('numeric_expression -> fun','numeric_expression',1,'p_numeric_expression','MyParser.py',216),
  ('numeric_expression -> ( numeric_expression )','numeric_expression',3,'p_numeric_expression','MyParser.py',217),
  ('numeric_expression -> numeric_expression + numeric_expression','numeric_expression',3,'p_bin_numeric_expression','MyParser.py',221),
  ('numeric_expression -> numeric_expression - numeric_expression','numeric_expression',3,'p_bin_numeric_expression','MyParser.py',222),
  ('numeric_expression -> numeric_expression * numeric_expression','numeric_expression',3,'p_bin_numeric_expression','MyParser.py',223),
  ('numeric_expression -> numeric_expression / numeric_expression','numeric_expression',3,'p_bin_numeric_expression','MyParser.py',224),
  ('numeric_expression -> numeric_expression DOTADD numeric_expression','numeric_expression',3,'p_bin_numeric_expression','MyParser.py',225),
  ('numeric_expression -> numeric_expression DOTSUB numeric_expression','numeric_expression',3,'p_bin_numeric_expression','MyParser.py',226),
  ('numeric_expression -> numeric_expression DOTMUL numeric_expression','numeric_expression',3,'p_bin_numeric_expression','MyParser.py',227),
  ('numeric_expression -> numeric_expression DOTDIV numeric_expression','numeric_expression',3,'p_bin_numeric_expression','MyParser.py',228),
  ('comparison_expression -> numeric_expression LT numeric_expression','comparison_expression',3,'p_comparison_expression','MyParser.py',236),
  ('comparison_expression -> numeric_expression GT numeric_expression','comparison_expression',3,'p_comparison_expression','MyParser.py',237),
  ('comparison_expression -> numeric_expression EQ numeric_expression','comparison_expression',3,'p_comparison_expression','MyParser.py',238),
  ('comparison_expression -> numeric_expression NE numeric_expression','comparison_expression',3,'p_comparison_expression','MyParser.py',239),
  ('comparison_expression -> numeric_expression GE numeric_expression','comparison_expression',3,'p_comparison_expression','MyParser.py',240),
  ('comparison_expression -> numeric_expression LE numeric_expression','comparison_expression',3,'p_comparison_expression','MyParser.py',241),
  ('comparison_expression -> ( comparison_expression )','comparison_expression',3,'p_comparison_expression','MyParser.py',242),
]