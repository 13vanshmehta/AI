class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.val = value

def inorder(root):
    result = []
    if root:
        # Traverse left
        result.extend(inorder(root.left))
        # Traverse root
        result.append(root.val)
        # Traverse right
        result.extend(inorder(root.right))
    return result

def preorder(root):
    result = []
    if root:
        # Traverse root
        result.append(root.val)
        # Traverse left
        result.extend(preorder(root.left))
        # Traverse right
        result.extend(preorder(root.right))
    return result

def postorder(root):
    result = []
    if root:
        # Traverse left
        result.extend(postorder(root.left))
        # Traverse right
        result.extend(postorder(root.right))
        # Traverse root
        result.append(root.val)
    return result

def build_tree():
    print("Building a binary tree")
    
    # Get number of nodes
    while True:
        try:
            n = int(input("Enter number of nodes: "))
            if n > 0:
                break
            print("Please enter a positive number")
        except ValueError:
            print("Please enter a valid number")
    
    nodes = {}
    root = None
    
    print("\nEnter node pairs (format: 'node1 node2'):")
    
    for i in range(n):
        pair = input(f"Edge {i+1}: ").strip().split()
        
        if len(pair) != 2:
            print("Invalid format. Please enter two values separated by space.")
            continue
        
        parent_val, child_val = pair
        
        # Create parent node if it doesn't exist
        if parent_val not in nodes:
            nodes[parent_val] = Node(parent_val)
        
        # Set root to first parent if not set yet
        if root is None:
            root = nodes[parent_val]
        
        # Create child node if it doesn't exist
        if child_val not in nodes:
            nodes[child_val] = Node(child_val)
        
        # Connect parent to child
        parent_node = nodes[parent_val]
        if parent_node.left is None:
            parent_node.left = nodes[child_val]
        elif parent_node.right is None:
            parent_node.right = nodes[child_val]
        else:
            print(f"Warning: Node {parent_val} already has two children. Ignoring {child_val}.")
            i -= 1
    
    return root

def main():
    print("Binary Tree Traversal Implementation")
    
    # Build tree from user input
    root = build_tree()
    
    while True:
        print("\nSelect traversal method:")
        print("1. Inorder traversal (Left -> Root -> Right)")
        print("2. Preorder traversal (Root -> Left -> Right)")
        print("3. Postorder traversal (Left -> Right -> Root)")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            result = inorder(root)
            print("\nInorder traversal:")
            print(" -> ".join(result))
        
        elif choice == '2':
            result = preorder(root)
            print("\nPreorder traversal:")
            print(" -> ".join(result))
        
        elif choice == '3':
            result = postorder(root)
            print("\nPostorder traversal:")
            print(" -> ".join(result))
        
        elif choice == '4':
            print("Exiting program...")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()