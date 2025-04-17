# What is a Trie?
Trie (pronounced Try) is a prefix tree which stores a dynamic set of strings. Each node in a trie represents a single character of a string and paths from the root to a node represent prefixes of the stored strings.

```text
(root)
 ├── a
 │   └── p
 │       └── p
 │           ├── (end)          ← "app"
 │           └── l
 │               └── e
 │                   └── (end)  ← "apple"
 │       └── e
 │           └── x
 │               └── (end)      ← "apex"
 └── b
     └── a
         ├── t
         │   └── (end)          ← "bat"
         └── d
             └── (end)          ← "bad"
```

## When do you use Trie?
You use Trie when you need fast prefix-based lookup or efficient storage of strings with shared prefixes.
Trie is used for applications such as: 
* IP Routing (Routers use prefixes (like 192.168.\*.\*) to forward packets.)
* Autocomplete
* Prefix search
* Spell checker

## ⏱️ Time and 🧠 Space Complexity
Let:
- `n` = number of words
- `m` = average length of a word

### Time Complexity

| Operation        | Time Complexity | Description |
|------------------|------------------|-------------|
| **Insert**       | O(m)             | One node per character |
| **Search**       | O(m)             | Traverse characters until found or failed |
| **Prefix Search**| O(m)             | Same as search, but don't check for end of word |
| **Delete**       | O(m)             | May require cleanup of nodes |

### Space Complexity

| Scenario                     | Space Complexity | Description |
|------------------------------|------------------|-------------|
| **Worst case**               | O(n * m)         | All words are unique (no shared prefixes) |
| **Best case**                | Closer to O(m)   | All words share common prefixes |
| **Per node (hash map)**      | O(1) avg.        | One entry per unique child |
| **Per node (fixed alphabet)**| O(σ), e.g., O(26) | Fixed-size array for alphabet (like 'a'–'z') |

> **Note:**  
> Tries trade **space** for **speed**, especially in prefix-heavy datasets. In cases where space is a concern, a [radix tree (compressed trie)](https://en.wikipedia.org/wiki/Radix_tree) may be preferred.


## What are the PROs / CONs of Tries?
Pros:
* Fast prefix-based search

* Can be more space-efficient than a hash map of strings, especially with shared prefixes

Cons:
* Can use more memory in worst cases due to the number of nodes
