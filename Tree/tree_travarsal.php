<?php

// Read number of nodes

$n = intval(trim(fgets(STDIN)));

$tree=[];

for($i=0;$i<$n;$i++){
    [$val,$left,$right]=array_map('intval',explode(" ",trim(fgets(STDIN))));

    $tree[$i]=['val'=>$val, 'left'=>$left, 'right'=>$right];
}

$inorder = [];
$preorder = [];
$postorder = [];

function inOrder($index,$tree,&$result){
    if($index===-1) return ;
    inOrder($tree[$index]['left'],$tree,$result);
    $result[]=$tree[$index]['val'];
    inOrder($tree[$index]['right'],$tree,$result);
}

function preOrder($index,$tree,&$result){
    if($index===-1) return ;
    $result[]=$tree[$index]['val'];
    preOrder($tree[$index]['left'],$tree,$result);
    preOrder($tree[$index]['right'],$tree,$result);
}


function postOrder($index,$tree,&$result){
    if($index===-1) return ;
    postOrder($tree[$index]['left'],$tree,$result);
    postOrder($tree[$index]['right'],$tree,$result);
    $result[]=$tree[$index]['val'];
}

inOrder(0, $tree, $inorder);
preOrder(0, $tree, $preorder);
postOrder(0, $tree, $postorder);

//print_r($inorder);die;

echo implode(' ', $inorder) . PHP_EOL;
echo implode(' ', $preorder) . PHP_EOL;
echo implode(' ', $postorder) . PHP_EOL;

?>
