<?php
   echo "Coding Interview with array: Pascal's Triangle<br/><br/>";

    function pascal_triangle($rows){
        $triangle=[];
        for($i=0;$i<$rows; $i++)
        {
            $row = array_fill(0, $i + 1, 1);
            
            for($j=1;$j<$i;$j++){
                $row[$j]=$triangle[$i-1][$j-1]+$triangle[$i-1][$j];
            }
     
            
            $triangle[]=$row;
           
           // return $triangle;
           
        }

        return $triangle;
    }

    $result=pascal_triangle(10);
    var_dump($result);
