<?php
// Function to encrypt the string
function encrypt($s) {
    $n = strlen($s);
    $encrypted = '';
    $count = 1;

    // Count consecutive identical characters
    for ($i = 0; $i < $n; $i++) {
        if ($i < $n - 1 && $s[$i] == $s[$i + 1]) {
            $count++;
        } else {
            $encrypted .= $count . $s[$i];
            $count = 1;
        }
    }

    // Reverse the transformed string
    return strrev($encrypted);
}

// Function to decrypt the string
function decrypt($s) {
    $reversed = strrev($s);
    $decrypted = '';
    $n = strlen($reversed);
    $count = '';

    // Decrypt by parsing the reversed string
    for ($i = 0; $i < $n; $i++) {
        if (is_numeric($reversed[$i])) {
            $count .= $reversed[$i];
        } else {
            $decrypted .= str_repeat($reversed[$i], intval($count));
            $count = '';
        }
    }

    return $decrypted;
}


    // Test cases
    $input1 = "aaaaaaaaaaa";
    $encrypted1 = encrypt($input1);
    $decrypted1 = decrypt($encrypted1);
    echo "Input: $input1 <br/>";
    echo "Encrypted: $encrypted1 <br/>"; // Output: 11a
    echo "Decrypted: $decrypted1<br/>"; // Output: aaaaaaaaaaa
    
    echo "<br/>";
    $input2 = "ostad";
    $encrypted2 = encrypt($input2);
    $decrypted2 = decrypt($encrypted2);
    echo "\nInput: $input2<br/>";
    echo "Encrypted: $encrypted2<br/>"; // Output: 1d1a1t1s1o
    echo "Decrypted: $decrypted2\n"; // Output: ostad
?>
