"""
141 Tree Lab - Derp the Interpreter

The Derp interpreter parses and evaluates prefix integer expressions 
containing basic arithmetic operators (*,//,-,+). It performs arithmetic with
integer operands that are either literals or variables (read from a 
symbol table).  It dumps the symbol table, prints the infix expression with 
parentheses to denote order of operation, and evaluates the expression to
print the result.

Author: CS@RIT.EDU

Author: Ryan Nowak
"""

from derp_types import *        # dataclasses for the Derp interpreter


def make_table(name):
    """
    Reads a txt file into a dictionary of variables with assigned values
    :param name: Name of txt file to open
    :return: dictionary of variables with assigned values
    """
    table = dict()
    for line in open(name):
        line = line.split()
        table[line[0]] = int(line[1])

    print('Derping the symbol table (variable name -> integer value)...')
    for key in table.keys():
        print(key, '->', table[key])

    return table

##############################################################################
# parse
############################################################################## 
    
def parse(tokens):
    """parse: list(String) -> Node
    From a prefix stream of tokens, construct and return the tree,
    as a collection of Nodes, that represent the expression.
    precondition: tokens is a non-empty list of strings
    """
    var = tokens.pop(0)
    if var.isnumeric():
        return LiteralNode(int(var))
    elif var.isidentifier():
        return VariableNode(var)
    else:
        return MathNode(parse(tokens), var, parse(tokens))
            
##############################################################################
# infix
##############################################################################
        
def infix(node):
    """infix: Node -> String 
    Perform an inorder traversal of the node and return a string that
    represents the infix expression.
    precondition: node is a valid derp tree node
    """
    if isinstance(node, MathNode):
        return '(' + infix(node.left) + ' ' + node.operator \
               + ' ' + infix(node.right) + ')'
    elif isinstance(node, LiteralNode):
        return str(node.val)
    elif isinstance(node, VariableNode):
        return node.name
 
##############################################################################
# evaluate
##############################################################################    
      
def evaluate(node, sym_tbl):
    """evaluate: Node * dict(key=String, value=int) -> int 
    Return the result of evaluating the expression represented by node.
    Precondition: all variable names must exist in sym_tbl
    precondition: node is a valid derp tree node
    """
    if isinstance(node, MathNode):
        if node.operator == '+':
            return evaluate(node.left, sym_tbl) \
                   + evaluate(node.right, sym_tbl)
        elif node.operator == '-':
            return evaluate(node.left, sym_tbl) \
                   - evaluate(node.right, sym_tbl)
        elif node.operator == '*':
            return evaluate(node.left, sym_tbl) \
                   * evaluate(node.right, sym_tbl)
        elif node.operator == '//':
            return evaluate(node.left, sym_tbl) \
                   // evaluate(node.right, sym_tbl)
    elif isinstance(node, LiteralNode):
        return node.val
    else:
        return sym_tbl[node.name]

    
##############################################################################
# main
##############################################################################
                     
def main():
    """main: None -> None
    The main program prompts for the symbol table file, and a prefix 
    expression.  It produces the infix expression, and the integer result of
    evaluating the expression"""
    
    print("Hello Herp, welcome to Derp v1.0 :)")
    
    in_file = input("Herp, enter symbol table file: ")
    
    # STUDENT: CONSTRUCT AND DISPLAY THE SYMBOL TABLE HERE
    table = make_table(in_file)

    print("Herp, enter prefix expressions, e.g.: + 10 20 (ENTER to quit)...")
    
    # input loop prompts for prefix expressions and produces infix version
    # along with its evaluation
    while True:
        prefix_exp = input("derp> ")
        if prefix_exp == "":
            break
            
        # STUDENT: GENERATE A LIST OF TOKENS FROM THE PREFIX EXPRESSION
        tokens = prefix_exp.split()
        
        # STUDENT: CALL parse WITH THE LIST OF TOKENS AND SAVE THE ROOT OF 
        # THE PARSE TREE.
        root_tr = parse(tokens)
            
        # STUDENT: GENERATE THE INFIX EXPRESSION BY CALLING infix AND SAVING
        # THE STRING.
        infix_exp = infix(root_tr)

        # STUDENT: MODIFY THE print STATEMENT TO INCLUDE RESULT.    
        print("Derping the infix expression:", infix_exp)
        
        # STUDENT: EVALUTE THE PARSE TREE BY CALLING evaluate AND SAVING THE
        # INTEGER RESULT.
        value = evaluate(root_tr, table)

        # STUDENT: MODIFY THE print STATEMENT TO INCLUDE RESULT.
        print("Derping the evaluation:", value)
         
    print("Goodbye Herp :(")
    
if __name__ == "__main__":
    main()
