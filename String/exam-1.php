<?php

function isKOstad($str1, $str2, $k) {
    $len1 = strlen($str1);
    $len2 = strlen($str2);
    
    // If the difference in length is greater than k, they can't be K-Ostad
    if (abs($len1 - $len2) > $k) {
        return "No";
    }

    // Count character frequencies
    $count1 = array_count_values(str_split($str1));
    $count2 = array_count_values(str_split($str2));

    // Calculate the number of modifications required
    $modifications = 0;
    
    // Check extra or changed characters in str1
    foreach ($count1 as $char => $freq) {
        if (isset($count2[$char])) {
            $modifications += abs($freq - $count2[$char]);
        } else {
            $modifications += $freq;
        }
    }

    // Check extra characters in str2
    foreach ($count2 as $char => $freq) {
        if (!isset($count1[$char])) {
            $modifications += $freq;
        }
    }
    
    // If modifications required are less than or equal to k, they are K-Ostad
    return ($modifications / 2 <= $k) ? "Yes" : "No";
}

    // Test cases
    echo isKOstad("anagram", "grammar", 3) . "\n"; 
    echo isKOstad("ostad", "boss", 1) . "\n";      
?>
