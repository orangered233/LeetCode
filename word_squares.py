from typing import List


class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        self.words = words
        self.n = len(words[0])
        self.solutions = []
        self.build_hashtable()
        # self.build_trie()
        for i in range(len(words)):
            self.traverse([words[i]])
        return self.solutions

    def build_trie(self):
        self.trie = {}
        for i, word in enumerate(self.words):
            node = self.trie
            for char in word:
                if char in node:
                    node[char]['#'].append(i)
                    node = node[char]
                else:
                    new_node = {'#': [i]}
                    node[char] = new_node
                    node = new_node

    def build_hashtable(self):
        self.hashtable = {}
        for word in self.words:
            for prefix in (word[:i] for i in range(1, len(word))):
                self.hashtable.setdefault(prefix, set()).add(word)

    def get_next_words_hashtable(self, prefix):
        return self.hashtable.get(prefix, [])

    def get_next_words_trie(self, prefix):
        node = self.trie
        for char in prefix:
            if char not in node:
                return []
            else:
                node = node[char]
        return [self.words[i] for i in node['#']]

    def traverse(self, words: List[str]):
        if len(words) == self.n:
            self.solutions.append(words)
        else:
            words_len = len(words)
            prefix = "".join([word[words_len] for word in words])
            next_words = self.get_next_words_hashtable(prefix)
            for next_word in next_words:
                new_words = words + [next_word]
                self.traverse(new_words)