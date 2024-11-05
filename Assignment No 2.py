class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ''  # Huffman code placeholder

# Function to print the nodes in the Huffman tree
def printNodes(node, val=''):
    newVal = val + str(node.huff)
    
    if node.left:
        printNodes(node.left, newVal)
    if node.right:
        printNodes(node.right, newVal)
    
    # Print the character and its code when it's a leaf node
    if not node.left and not node.right:
        print(f"{node.symbol} -> {newVal}")

# Characters for Huffman tree
chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# Frequencies of the characters
freq = [4, 7, 12, 14, 17, 43, 54]

# List containing nodes
nodes = []

# Converting characters and frequencies into Huffman tree nodes
for x in range(len(chars)):
    nodes.append(Node(freq[x], chars[x]))

# Building the Huffman tree
while len(nodes) > 1:
    # Sort nodes in ascending order based on frequency
    nodes = sorted(nodes, key=lambda x: x.freq)
    
    # Pick two smallest nodes
    left = nodes[0]
    right = nodes[1]
    
    # Assign binary codes (0 and 1) to these nodes
    left.huff = 0
    right.huff = 1
    
    # Combine the two smallest nodes to create a new parent node
    newNode = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)
    
    # Remove the two smallest nodes and add the new parent node
    nodes.remove(left)
    nodes.remove(right)
    nodes.append(newNode)

# Print the Huffman codes by traversing the tree
printNodes(nodes[0])
