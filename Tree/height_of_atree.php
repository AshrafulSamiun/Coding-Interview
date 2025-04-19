<?php
function computeHeight($n, $parent) {
    $children = array_fill(0, $n, []);
    $root = -1;

    // Build children array
    for ($i = 0; $i < $n; $i++) {
        if ($parent[$i] == -1) {
            $root = $i; // Found root
        } else {
            $children[$parent[$i]][] = $i; // Add i as child of parent[i]
        }
    }

    // DFS function to compute height
    function dfs($node, $children) {
        if (empty($children[$node])) return 1; // Leaf node
        $maxHeight = 0;
        foreach ($children[$node] as $child) {
            $maxHeight = max($maxHeight, dfs($child, $children));
        }
        return $maxHeight + 1;
    }

    return dfs($root, $children);
}

//     "5 -1 5 2 2"
//original input (5 -1 5 2 2), but that input is not valid if n = 5, because it references node 5 (which doesn’t exist)

// lets try for 1 -1 1 2 2
$n=intval(trim(fgets(STDIN)));
$parent=array_map('intval',explode(' ',trim(fgets(STDIN))));
// print_r($parent);die;
echo computeHeight($n, $parent) . PHP_EOL;
