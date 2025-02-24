<?php


function pow_of_five($n){
    if($n==0){
        return false;
    }
    if($n==1){
        return true;
    }

    if($n<0){
        return pow_of_five($n);
    }
   
    if($n%5!=0){
        return false;
    }

    return pow_of_five($n/5);
}

$n=4;
$result=pow_of_five($n);
//var_dump($result);die;
if($result) echo "True";
else  echo "No";
