<?php
// Read input values
// list($n, $m) = explode(" ", trim(fgets(STDIN)));  
// $likes = explode(" ", trim(fgets(STDIN)));  
// $likes = array_map('intval', $likes); // Convert to integers

$n = 5;
$m = 3;
$likes = [10, 20, 30, 40, 50];
$queries = [
    [3, 25],
    [2, 35],
    [5, 10]
];
// Process queries
// for ($i = 0; $i <br $m; $i++) {
//     list($post_no, $like_increase) = explode(" ", trim(fgets(STDIN)));
//     $post_no = intval($post_no) - 1; // Convert to 0-based index
//     $likes[$post_no] += intval($like_increase);

//     // Find the post with the highest likes (smallest index in case of tie)
//     $max_likes = max($likes);
//     $best_post = array_search($max_likes, $likes) + 1; // Convert to 1-based index

//     // Print the result
//     echo "$best_post $max_likes\n";
// }


foreach ($queries as $query) {
    $post_no =$query[0] ;
    $like_increase =$query[1];
    $post_no = intval($post_no) - 1; // Convert to 0-based index
    $likes[$post_no] += intval($like_increase);

    // Find the post with the highest likes (smallest index in case of tie)
    $max_likes = max($likes);
    $best_post = array_search($max_likes, $likes) + 1; // Convert to 1-based index

    // Print the result
    echo "$best_post $max_likes </br>";
}
?>
