<?php
   echo "Coding Interview with array: Maximum Gab<br/><br/>";
    function maximum_gap($nums){
        $n=count($nums);
        sort($nums);
        if($n==1) return 0;
        
        $max_diff=0;
        for($i=0;$i<$n-1;$i++)
        {
            $diff=$nums[$i+1]-$nums[$i];
            
            if($diff>$max_diff) $max_diff=$diff;
        }
        return $max_diff;
    }

    $number_arr=[3,6,9,1];
    $result=maximum_gap($number_arr);
    echo $result;