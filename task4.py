import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  
        self.id = str(uuid.uuid4())  

class BinaryHeap:
    def __init__(self, heap_type='min'):
        self.heap = []
        self.heap_type = heap_type  

    def push(self, val):
        node = Node(val)
        self.heap.append(node)
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def _heapify_up(self, idx):
        parent_idx = (idx - 1) // 2
        if idx > 0 and self._compare(self.heap[idx].val, self.heap[parent_idx].val):
            self.heap[idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx]
            self._heapify_up(parent_idx)

    def _heapify_down(self, idx):
        left_idx = 2 * idx + 1
        right_idx = 2 * idx + 2
        smallest_or_largest = idx

        if left_idx < len(self.heap) and self._compare(self.heap[left_idx].val, self.heap[smallest_or_largest].val):
            smallest_or_largest = left_idx
        if right_idx < len(self.heap) and self._compare(self.heap[right_idx].val, self.heap[smallest_or_largest].val):
            smallest_or_largest = right_idx

        if smallest_or_largest != idx:
            self.heap[idx], self.heap[smallest_or_largest] = self.heap[smallest_or_largest], self.heap[idx]
            self._heapify_down(smallest_or_largest)

    def _compare(self, child_val, parent_val):
        if self.heap_type == 'min':
            return child_val < parent_val
        else:
            return child_val > parent_val

    def build_tree(self):
        if not self.heap:
            return None
        root = self.heap[0]
        self._build_tree(root, 0)
        return root

    def _build_tree(self, node, idx):
        left_idx = 2 * idx + 1
        right_idx = 2 * idx + 2
        if left_idx < len(self.heap):
            node.left = self.heap[left_idx]
            self._build_tree(node.left, left_idx)
        if right_idx < len(self.heap):
            node.right = self.heap[right_idx]
            self._build_tree(node.right, right_idx)

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_heap(heap_root):
    tree = nx.DiGraph()
    pos = {heap_root.id: (0, 0)}
    tree = add_edges(tree, heap_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

heap = BinaryHeap(heap_type='min')
heap.push(10)
heap.push(5)
heap.push(20)
heap.push(15)
heap.push(30)

root = heap.build_tree()

draw_heap(root)
