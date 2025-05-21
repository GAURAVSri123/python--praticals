##11111111111111111111111111111111
class SET:
    def __init__(self, u_set):
        self.u_set = set(u_set)

    def is_member(self, element):
        return "Element Found" if element in self.u_set else "Element Not Found"

    def powerset(self):
        powerset_list = []
        length = len(self.u_set)
        u_set_list = list(self.u_set)

        for i in range(1 << length):  # from 0 to 2^n - 1
            subset = set()
            for j in range(length):
                if i & (1 << j):  # check if j-th bit is set
                    subset.add(u_set_list[j])
            powerset_list.append(subset)

        print("Your Required Powerset Is:")
        for s in powerset_list:
            print(s)

    def subset(self, subset_set):
        if set(subset_set.u_set).issubset(self.u_set):
            return "This is a subset"
        else:
            return "This is not a subset"

    def union_intersection(self, set2):
        print("Union of sets:\n", self.u_set.union(set2.u_set))
        print("Intersection of sets:\n", self.u_set.intersection(set2.u_set))

    def complement(self, complement_set):
        print("Complement of set:\n", self.u_set - complement_set.u_set)

    def difference_and_symmetric_difference(self, set2):
        print("Difference of sets:\n", self.u_set.difference(set2.u_set))
        print("Symmetric Difference of sets:\n", self.u_set.symmetric_difference(set2.u_set))

    def cartesian_product(self, set2):
        cartesian_product = {(x, y) for x in self.u_set for y in set2.u_set}
        print("Cartesian Product of sets:\n", cartesian_product)


# Function outside the class to take input
def create_set(name="Set"):
    u_set = set(map(int, input(f"Enter elements of {name} separated by space: ").split()))
    print(f"Your {name} is: {u_set}")
    return u_set


# Menu-Driven Code (outside the class)
for _ in range(8):  # Run 8 times
    choice = input("""\nMain Menu:
1. Check whether an element belongs to the set or not
2. List all elements of the power set
3. Check if one set is a subset of another
4. Find union and intersection of two sets
5. Find complement of a set
6. Find difference and symmetric difference between two sets
7. Find Cartesian product of two sets
Enter your choice (1-7): """)

    if choice == '1':
        set1 = SET(create_set())
        element = int(input("Enter your element: "))
        print(set1.is_member(element))

    elif choice == '2':
        set1 = SET(create_set())
        set1.powerset()

    elif choice == '3':
        universal_set = SET(create_set("Universal Set"))
        subset_set = SET(create_set("Another Set"))
        print(universal_set.subset(subset_set))

    elif choice == '4':
        set1 = SET(create_set("First Set"))
        set2 = SET(create_set("Second Set"))
        set1.union_intersection(set2)

    elif choice == '5':
        universal_set = SET(create_set("Universal Set"))
        subset = SET(create_set("Subset"))
        universal_set.complement(subset)

    elif choice == '6':
        set1 = SET(create_set("First Set"))
        set2 = SET(create_set("Second Set"))
        set1.difference_and_symmetric_difference(set2)

    elif choice == '7':
        set1 = SET(create_set("First Set"))
        set2 = SET(create_set("Second Set"))
        set1.cartesian_product(set2)

    else:
        print("Invalid choice. Try again.")


## 22222222222222222222
from numpy import array

class RELATION:
    def __init__(self, matrix):
        self.matrix = matrix
        self.length = len(matrix)

    def reflexive(self):
        for i in range(self.length):
            if not self.matrix[i][i]:
                return False
        return True

    def symmetric(self):
        for i in range(self.length):
            for j in range(self.length):
                if self.matrix[i][j] != self.matrix[j][i]:
                    return False
        return True

    def transitive(self):
        for i in range(self.length):
            for j in range(self.length):
                for k in range(self.length):
                    if self.matrix[i][j] and self.matrix[j][k] and not self.matrix[i][k]:
                        return False
        return True

    def antisymmetric(self):
        for i in range(self.length):
            for j in range(self.length): 
                if i != j and self.matrix[i][j] and self.matrix[j][i]:
                    return False
        return True

# Function to enter matrix (outside the class, not inside)
def enter_matrix():
    list1 = list(map(int, input("Enter all elements of the relation matrix (space-separated): ").split()))
    row = int(input("Enter number of rows (same as columns, since it's a square matrix): "))
    matrix = array(list1).reshape(row, row)
    print("The relation matrix is:\n", matrix)
    return matrix

# Main function (also outside the class)
def main():
    matrix = enter_matrix()
    rel = RELATION(matrix)
    
    if rel.reflexive() and rel.symmetric() and rel.transitive():
        print("✅ The relation is an **Equivalence Relation**")
    elif rel.reflexive() and rel.antisymmetric() and rel.transitive():
        print("✅ The relation is a **Partial Order Relation**")
    else:
        print("❌ The relation is **Neither Equivalence nor Partial Order**")

if __name__ == "__main__":
    main()


#33333333333333333333333
from itertools import permutations, product

def generate_permutation(Set, repetition):
    if repetition:
        return list(product(Set, repeat=len(Set)))  # With repetition
    else:
        return list(permutations(Set))  # Without repetition

if __name__ == "__main__":
    Set = list(map(int, input("Enter the elements with space: ").split()))
    
    with_repetition = generate_permutation(Set, repetition=True)
    without_repetition = generate_permutation(Set, repetition=False)

    print("\nPermutations WITH repetition:")
    for perm in with_repetition:
        print(perm)

    print("\nPermutations WITHOUT repetition:")
    for perm in without_repetition:
        print(perm)

    print(f"\nTotal with repetition: {len(with_repetition)}")
    print(f"Total without repetition: {len(without_repetition)}")




## 444444444444444
from itertools import product

def find_solutions(n, C):
    solutions = []
    # Generate all n-tuples with values from 0 to C (inclusive)
    for combo in product(range(C+1), repeat=n):
        if sum(combo) == C:
            solutions.append(combo)
    
    return solutions

if __name__ == "__main__":
    n = int(input("Enter number of variables (n): "))
    C = int(input("Enter constant value (C ≤ 10): "))
    
    if C > 10 or C < 0:
        print("C must be between 0 and 10 (inclusive).")
    else:
        solutions = find_solutions(n, C)
        print(f"\nAll solutions for x1 + x2 + ... + x{n} = {C} are:")
        for sol in solutions:
            print(sol)
        print(f"\nTotal solutions found: {len(solutions)}")


##555555555555555555555555
def solve_function():
    func = list(map(int, input("Enter the coefficients of the function (highest to lowest power), separated by space: ").split()))
    num = int(input("Enter value of variable: "))
    
    value = 0
    degree = len(func) - 1
    
    for i in range(len(func)):
        value += func[i] * (num ** (degree - i))
    
    return value

# Call the function and print the result
print("Value of the function is:", solve_function())



##6666666666666666666
def is_complete_graph(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if i == j:
                if matrix[i][j] != 0:  # No self-loop
                    return False
            else:
                if matrix[i][j] != 1:  # All distinct pairs must be connected
                    return False
    return True

def main():
    n = int(input("Enter the number of vertices in the graph: "))
    print("Enter the adjacency matrix row by row (space-separated):")

    matrix = []
    for i in range(n):
        row = list(map(int, input(f"Row {i+1}: ").split()))
        if len(row) != n:
            print("Invalid row length. Matrix must be square.")
            return
        matrix.append(row)

    print("\nAdjacency Matrix:")
    for row in matrix:
        print(row)

    if is_complete_graph(matrix):
        print("\nThe graph is a COMPLETE graph.")
    else:
        print("\nThe graph is NOT a complete graph.")

if __name__ == "__main__":
    main()


##7777777777777777777777777777
def is_complete_graph(adj_list):
    n = len(adj_list)
    for vertex, neighbors in adj_list.items():
        if len(neighbors) != n - 1:
            return False
    return True

def main():
    n = int(input("Enter the number of vertices: "))
    adj_list = {}

    print("Enter the adjacency list for each vertex:")
    for i in range(n):
        neighbors = list(map(int, input(f"Enter neighbors of vertex {i} (space-separated): ").split()))
        adj_list[i] = neighbors

    print("\nAdjacency List:")
    for vertex in adj_list:
        print(f"{vertex}: {adj_list[vertex]}")

    if is_complete_graph(adj_list):
        print("\nThe graph is a COMPLETE graph.")
    else:
        print("\nThe graph is NOT a complete graph.")

if __name__ == "__main__":
    main()



##8888888888888888888
class DirectedGraph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        # Add a directed edge from u to v
        self.adj_list[u].append(v)

    def compute_degrees(self):
        in_degree = [0] * self.vertices
        out_degree = [0] * self.vertices

        for u in range(self.vertices):
            out_degree[u] = len(self.adj_list[u])  # Count of outgoing edges
            for v in self.adj_list[u]:
                in_degree[v] += 1  # Count of incoming edges

        print("\nVertex\tIn-Degree\tOut-Degree")
        for i in range(self.vertices):
            print(f"{i}\t{in_degree[i]}\t\t{out_degree[i]}")

    def print_adj_list(self):
        print("\nAdjacency List:")
        for i in range(self.vertices):
            print(f"{i}: {self.adj_list[i]}")


# Main program
if __name__ == "__main__":
    n = int(input("Enter number of vertices: "))
    e = int(input("Enter number of directed edges: "))

    graph = DirectedGraph(n)

    for i in range(e):
        u, v = map(int, input(f"Enter edge {i+1} (from to): ").split())
        graph.add_edge(u, v)

    graph.print_adj_list()
    graph.compute_degrees()
