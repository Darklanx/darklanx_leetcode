# d-e-f
# a-b-c
# add e/b => e/b = e/f * f/a * a/b, f/a = e/b * b/a * f/e
# a/d? a/e?
# e/c?

class Node:
    def __init__(self, name):
        self.name = name
        self.parent = self
        self.next = None
        self.transition_val = 1
        
    def get_root(self):
        node = self
        while node.parent != node:
            node = node.parent
        return node
    
class Graph:
    def __init__(self, equations, values):
        self.nodes = {}
        for eq, val in zip(equations, values):
            name1, name2 = eq[0], eq[1]
            if name1 not in self.nodes:
                self.nodes[name1] = Node(name1)
            if name2 not in self.nodes:
                self.nodes[name2] = Node(name2)
            
            self.merge(name1, name2, val)
                
            
    def merge(self, denominator, nominator, val):
        if self.nodes[denominator].get_root() == self.nodes[nominator].get_root():
            return
        node_denom = self.nodes[denominator]
        
        last1 = self.get_last_in_chain(denominator)
        root2 = self.nodes[nominator].get_root()
        
        # connect two chain
        last1.next = root2
        root2.parent = last1.parent
        
        # calculate the trainsition last1/root2,
        # last1/root2 => denominator/nominator * 
        cur_node = node_denom
        while(cur_node.name != nominator):
            val /= cur_node.transition_val
            cur_node = cur_node.next
        last1.transition_val = val

    
    def get_last_in_chain(self, name):
        node = self.nodes[name]
        while node.next is not None:
            node = node.next
        return node
    
    def query(self, denominator, nominator):
        if denominator not in self.nodes or nominator not in self.nodes:
            return -1.0
        val = 1.0
        node = self.nodes[denominator]
        failed = False
        while node.name != nominator:
            val *= node.transition_val
            if node.next is None:
                failed = True
                break
            node = node.next
        if not failed:
            return val
        
        val = 1.0
        node = self.nodes[nominator]
        failed = False
        while node.name != denominator:
            if node.next is None:
                failed = True
                break
            val *= node.transition_val
            node = node.next
            
        
        if failed:
            return -1.0
            
        return 1.0 / val
        
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = Graph(equations, values)

        ans = []
        for q in queries:
            ans.append(graph.query(q[0], q[1]))
        return ans
            
        