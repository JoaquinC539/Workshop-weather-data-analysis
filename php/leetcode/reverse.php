<?php
/* Complete the function that accepts a string parameter, and reverses each word in the string.
 All spaces in the string should be retained.

Examples
"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps" */

function reverseWords($str) {

    $words=explode(" ",$str);
    $results="";

    for($i=0; $i < count($words); $i++) {        
        $word = str_split($words[$i]);
        $reversed_word = '';

        for($j=count($word)-1;$j>=0;$j--){           
            $reversed_word .= $word[$j];
        }

        $results .= $reversed_word ." ";

    }

    // rtrim($string, ",");
    return rtrim($results);
  }
  

  print_r(reverseWords("This is an example!"));