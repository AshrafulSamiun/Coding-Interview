<?php

    function find_character($k){
        $word="a";
        
        
        while(strlen($word)<$k){
            $new_word="";
            for($i=0;$i<strlen($word);$i++){
                //echo chr((ord($word[$i])-ord('a')+1)%26+ord('a'));die;

               // echo chr((ord($word[$i])-ord('a')+1)%26)+ord('a');
                $new_word=$new_word."".chr((ord($word[$i])-ord('a')+1)%26+ord('a'));
            }
            $word.=$new_word;
        }
        return $word[$k-1];
    }

   echo  find_character(5);
   echo "<br/>";
   echo  find_character(10);
