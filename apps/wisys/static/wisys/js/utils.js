
function merge(array1,array2) {
  for(item in array1) {
    array2[item] = array1[item];
  }
  return array2;
}

function isDefined( value ){
    if( isNaN(value)  || typeof(value) == "undefined" || value == "" )
        return false;
    else
        return true;

}

