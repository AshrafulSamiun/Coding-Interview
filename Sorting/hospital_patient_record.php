<?php 

    


    // $n = intval(trim(fgets(STDIN)));

    // // Initialize patient list
    // $patient_list = [];
    
    // // Read patient details
    // for ($i = 0; $i < $n; $i++) {
    //     $input = explode(" ", trim(fgets(STDIN)));
    //     $patient_list[] = [
    //         "id" => intval($input[0]),
    //         "name" => $input[1],
    //         "age" => intval($input[2]),
    //         "severity" => intval($input[3])
    //     ];
    // }

    $n=5;
    $input_arr[]="101 Alice 30 5";
    $input_arr[]="102 Bob 25 8";
    $input_arr[]="103 Charlie 40 8";
    $input_arr[]="104 David 35 6";
    $input_arr[]="105 Eve 28 5";
     // Read patient details
    for ($i = 0; $i < $n; $i++) {
        $input = explode(" ", $input_arr[$i]);
        $patient_list[] = [
            "id" => intval($input[0]),
            "name" => $input[1],
            "age" => intval($input[2]),
            "severity" => intval($input[3])
        ];
    }

    usort($patient_list, function ($a, $b) {
        if ($b['severity'] == $a['severity']) {
            return $a['age'] <=> $b['age']; // Ascending order for Age
        }
        return $b['severity'] <=> $a['severity']; // Descending order for Severity
    });

   
    foreach ($patient_list as $patient) {
        echo "{$patient['id']} {$patient['name']} {$patient['age']} {$patient['severity']}"."</br>";
    }

      
    
      
    
     
    



    // $n = (int)trim(fgets(STDIN));

// // Initialize an empty array to store patient list
// $patient_list = array();

// // Loop to read patient details
// for ($i = 0; $i < $n; $i++) {
//     // Read a line of input, split it by space, and store it in the patient list
//     $patient = explode(" ", trim(fgets(STDIN)));
//     array_push($patient_list, $patient);
// }

// // Optionally, print the patient list to verify
// print_r($patient_list);

















?>