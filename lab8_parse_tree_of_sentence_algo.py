class ParseTreeNode:
    def __init__(self, symbol):
        self.symbol = symbol
        self.children = []


def parse_sentence(sentence, grammar):
    tokens = sentence.split()  # Tokenize the input sentence
    return parse_non_terminal(grammar["S"], tokens, grammar)


def parse_non_terminal(non_terminal, tokens, grammar):
    node = ParseTreeNode(non_terminal)

    for production in grammar[non_terminal]:
        if all(
            part in grammar.keys() or part == token
            for part, token in zip(production, tokens)
        ):
            children = []
            remaining_tokens = tokens
            for part in production:
                if part in grammar:
                    child, remaining_tokens = parse_non_terminal(
                        part, remaining_tokens, grammar
                    )
                    children.append(child)
                else:
                    children.append(ParseTreeNode(part))
                    remaining_tokens = remaining_tokens[1:]
            node.children = children
            return node, remaining_tokens

    return None, tokens


# Example usage:
grammar = {
    "S": [("NP", "VP")],
    "NP": [("Det", "N")],
    "VP": [("V", "NP")],
    "Det": ["the", "a"],
    "N": ["man", "dog", "ball"],
    "V": ["hit", "threw"],
}


sentence = "the man hit the dog"
parse_tree, remaining_tokens = parse_sentence(sentence, grammar)
if parse_tree:
    print(parse_tree)
else:
    print("Parsing failed. Remaining tokens:", remaining_tokens)
