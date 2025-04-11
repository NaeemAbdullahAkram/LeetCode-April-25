
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        # mapping level: List[nodes]
        nodes_on_level = {}
        # node 2 level mapping as val:level
        n2l = {}

        def dfs(node, lvl):
            if not node:
                return lvl-1
            
            n2l[node.val]=lvl  # we need to know level of each node for fast lookup
            max_depth_of_children = max(dfs(node.left, lvl+1), dfs(node.right, lvl+1))            
            if not lvl in nodes_on_level:
                nodes_on_level[lvl] = {}
            nodes_on_level[lvl][node.val]=max_depth_of_children
            
            return max_depth_of_children
        
        dfs(root,1)

        # sort all this crazieness
        for lvl in nodes_on_level.keys():
            nodes_on_level[lvl] = sorted(nodes_on_level[lvl].items(), key = lambda x:x[1]) # sort by depth
              
        ret = []
        # answer queries
        for q in queries:            
            on_level = nodes_on_level[n2l[q]]
            if on_level[-1][0] == q:  # we cut most deepest branch
                if len(on_level) == 1:
                    ret.append(n2l[q]-2)
                else:
                    ret.append(on_level[-2][1] -1)
            else:
                ret.append(on_level[-1][1] -1)

        return ret
        