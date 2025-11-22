import csv
from bst_avl import *
from graph_algorithms import Graph
from expression_tree import *

print("\n=== LOADING DATA ===")

# ---------------- LOAD BUILDING DATA ----------------
bst_root = None
avl_root = None

with open("data/buildings.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        node = Node(int(row["BuildingID"]), row["BuildingName"], row["LocationDetails"])
        bst_root = insert_bst(bst_root, node)
        avl_root = insert_avl(avl_root, node)

print("BST Inorder:", inorder(bst_root))
print("AVL Inorder:", inorder(avl_root))

# ---------------- LOAD GRAPH ----------------
graph = Graph()
with open("data/graph_edges.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        graph.add_edge(int(row["FromID"]), int(row["ToID"]), int(row["Distance"]))

print("\nBFS from 1:", graph.bfs(1))
print("DFS from 1:", graph.dfs(1))
print("Dijkstra (from 1):", graph.dijkstra(1))
print("Kruskal MST:", graph.kruskal())

# ---------------- EXPRESSION TREE ----------------
with open("data/energy_expression.csv") as f:
    expr = next(csv.DictReader(f))["Expression"]

tree = build_expression_tree(expr)
print("\nEnergy Bill Expression:", expr)
print("Result:", evaluate(tree))
