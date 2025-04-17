class TrieNode:

    def __init__(self):
        # stores the Child nodes for a given parent node
        self.children = {}
        self.is_end_of_word = False

class Trie(object):

    def __init__(self):
        self.root = TrieNode()


    def insert(self, word):
        """
        Inserts the string word into the trie.
        :type word: str
        :rtype: None
        """
        current_node = self.root
        for chr in word:
            if chr not in current_node.children:
                current_node.children[chr] = TrieNode()
            current_node = current_node.children[chr]
        current_node.is_end_of_word = True


    def search(self, word):
        """
        Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
        :type word: str
        :rtype: bool
        """
        current_node = self.root
        for chr in word:
            if chr not in current_node.children:
                return False
            current_node = current_node.children[chr]
        return current_node.is_end_of_word
        

    def startsWith(self, prefix):
        """
        Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
        :type prefix: str
        :rtype: bool
        """
        current_node = self.root
        for chr in prefix:
            if chr not in current_node.children:
                return False
            current_node = current_node.children[chr]
        return True

def print_trie(node, prefix=''):
    for char, child_node in node.children.items():
        end_marker = ' (end)' if child_node.is_end_of_word else ''
        print(f"{prefix}└── {char}{end_marker}")
        print_trie(child_node, prefix + '    ')

if __name__ == "__main__":
    trie = Trie()

    trie.insert('apple')
    print_trie(trie.root)
    print(trie.search('apple'))
    print(trie.search('aple'))
    print(trie.search('app'))
    print(trie.startsWith("app"))