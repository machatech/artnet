class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

def build_tree():
    nodes = {}  
    while True:
        try:
            num_nodes = int(input("Enter the number of nodes (<= 50): "))
            if num_nodes <= 0 or num_nodes > 50:
                print("Please enter a positive integer less than or equal to 50.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
    
    print("Enter the node value and the child nodes , if no children the enter ' - ' : ")
    for _ in range(num_nodes):
        value = input(" ").strip()
        value = value.split()

        #for the +ve input part
        if not value[0].isdigit() or int(value[0]) <= 0:
            print(f"Invalid node value: {value[0]}. Node values must be positive integers.")
            continue
        if value[0] not in nodes:
            nodes[value[0]] = TreeNode(value[0])

        if value[1] == '-':
            continue

        for c_v in value[1:]:
            #child +ve values check
            if not c_v.isdigit() or int(c_v) <= 0:
                print(f"Invalid child value: {c_v}. Child values must be positive integers.")
                continue

        for c_v in value[1:]:
            if c_v not in  nodes:
                nodes[c_v] = TreeNode(c_v)
                nodes[value[0]].children.append(nodes[c_v])

    return nodes[next(iter(nodes))],nodes

def dfs(root, target_value, path=None,traversal = None):
    if path is None:
        path = []
    if traversal is None:
        traversal =[]
    path.append(root.value)
    traversal.append(root.value)
    if root.value == target_value:
        return path,traversal
    for child in root.children:
        result , result_traversal = dfs(child, target_value, path.copy(),traversal)
        if result:
            return result ,result_traversal
    path.pop()
    return None,traversal

def generate_arr(root, nodes, arr=None, index=0):
    if arr is None:
        arr = []
        arr.append(root.value)
        # print(root.value)
    if not root.children:
        arr.append('-')
        arr.append('-')
    else:
   
        child_values = [child.value for child in root.children]
        if len(child_values) == 1:
            arr.extend(child_values)
            arr.append('-')
        else:
            arr.extend(child_values)


    index += 1
    if index < len(arr):  
        if arr[index] in nodes:
            # print('yes', arr[index])
            ar_val = arr[index]
            generate_arr(nodes[ar_val], nodes, arr, index)
    return arr

# def tree_printer(arr, num_lvl):
#     total_nodes = 2 ** (num_lvl + 1) - 1
#     current_level = 0
#     index = 0  
    
#     while current_level <= num_lvl:
#         nodes_at_level = 2 ** current_level
#         if current_level == 0:
#             spaces_between_nodes = 0
#             leading_trailing_spaces = 2 ** (num_lvl + 1)
#         elif current_level == num_lvl:
#             leading_trailing_spaces = 2
#             spaces_between_nodes = 0            
#         else:
#             leading_trailing_spaces = 2 ** (num_lvl - current_level + 1)
#             spaces_between_nodes = (2 ** (num_lvl - current_level + 1)) - 2
        
#         line = ''
        
      
#         for _ in range(nodes_at_level):
#             if index < len(arr):
#                 # print(_)
#                 # if _ == 0:
#                 if str(arr[index]) == '-' and (index + 1 < len(arr) and str(arr[index + 1]) == '-'):
#                     spaces_between_nodes = 1
#                     leading_trailing_spaces = 2
#                 line += ' ' * leading_trailing_spaces + str(arr[index]) 
#                 index += 1
                
#                 if _ < nodes_at_level - 1:
#                     line += ' ' * spaces_between_nodes 
#                 if current_level == num_lvl and _ == 1:
#                     leading_trailing_spaces = 1
#                 elif current_level == num_lvl and _ > 1:
#                     leading_trailing_spaces = 2
                
#             # else:
#             #     line += ' ' * (leading_trailing_spaces )
        
#         print(line)
#         print()
        
#         current_level += 1
def find_depth(root):
    if root is None:
        return -1

    if not root.children:
        return 0
    child_depths = [find_depth(child) for child in root.children]
    
    return 1 + max(child_depths)
def main():
    root , nodes = build_tree()
    if not root:
        return

    arr = generate_arr(root,nodes)
    target_value = input("Enter the value to search for: ")
    path,traver_path = dfs(root, target_value)
    
    if path:
        print(f"Path = {' -> '.join(path)}")
        print("Node found")
        print(f"Traversal Path = {' -> '.join(traver_path)}")
    else:
        print("Value not found in the tree.")
        print(f"Path = {' -> '.join(traver_path)}")

    # tree_depth = find_depth(root)
    # tree_printer(arr, tree_depth)


if __name__ == "__main__":
    main()
