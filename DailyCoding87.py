
# Cool problem! After considering and rejecting a SAT-based approach (anologous to build a knowledge base: Will work 100%, but huge overhead), I found a quite similar solution that I like more tho:
# # (Simplified problem statement with only N-E-S-W instead of the mixed cardinal directions, but they should not pose a problem).
# # Have 4 directed graphs, one for each cardinal direction.
# # Do the following for all rules: If, say, A N B is encountered, add a edge from B to A in the North graph and a edge from A to B in the South graph.
# # Check every graph for cycles. Iff every graph is cycle-free, then there is no contradiction in the rule.
# # I like this approach more because now finding the answer is purely graph-based and has a better worst time complexity: O(|E| + |V|) with Tarjan's strongly connected components algorithm
# # E: Thanks to /u/FalconTaterz : It is possible to do with only two directed graphs, for example for directions N and E. If B S A would be encountered then, this would be considered as if A N B was encounterals form a vector space, only two unit vectors are needed.ed. What a nice observation which puts us closer to the truth: If the four cardin
