# Given that L is the length of the wire,
# for how many values of L <= 1,500,000
# can exactly one integer sided right angle triangle be formed?

# as per Berggren (1934), all primitive Pythagorean triples can be generated from the (3, 4, 5) triangle.
# then we can use the fact that ka, kb, kc with constant k will generate all triangles.

# so we use Berggren to generate all primitives, then for a given primitive iterate over K till L > 1.5*10**6 then move to next primitive.

# yee haw
