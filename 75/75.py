# Given that L is the length of the wire,
# for how many values of L <= 1,500,000
# can exactly one integer sided right angle triangle be formed?

# as per Berggren (1934), all primitive Pythagorean triples can be generated from the (3, 4, 5) triangle.
# then we can use the fact that ka, kb, kc with constant k will generate all triangles.
from collections import defaultdict, deque

# functions
def T1(trip):
	a = trip[0]
	b = trip[1]
	c = trip[2]
	return((a-2*b+2*c, 2*a-b+2*c, 2*a-2*b+3*c))

def T2(trip):
	a = trip[0]
	b = trip[1]
	c = trip[2]
	return((a+2*b+2*c, 2*a+b+2*c, 2*a+2*b+3*c))

def T3(trip):
	a = trip[0]
	b = trip[1]
	c = trip[2]
	return((-a+2*b+2*c, -2*a+b+2*c, -2*a+2*b+3*c))

def build_tree(L, queue, tree, node):
	queue.append(node)

	while queue:
		s = queue.popleft()

	        # add valid nodes
		for candidate in [T1(s), T2(s), T3(s)]:
			if sum(candidate) < L:
				tree[s].append(candidate)
				tree[candidate] = []
		
		for neighbor in tree[s]:
			queue.append(neighbor)	
	return(tree)

# settting up things
L = 15*10**5
stump = (3,4,5)
queue = deque()
tree = {
        (3,4,5) : []
}
results_dict = defaultdict(int)

# RUN!
full_tree = build_tree(L, queue, tree, stump)
for node in full_tree.keys():
	k = 1
	new = tuple([x*k for x in node])
	while sum(new) < L:
		results_dict[sum(new)] += 1
		k += 1
		new = tuple([x*k for x in node])

answer = 0
for k,v in results_dict.items():
	if v == 1:
		answer += 1

print(answer)
