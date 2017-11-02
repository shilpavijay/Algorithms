function checkNum(n) {
    return n== 9999;
}

function steamrollArray(arr) {
  type = typeof(arr[0]);
  if (type === 'number'){
    inter = (arr.join().replace('[object Object]','9999').split(',').filter(Number).map(Number));
    if (inter.find(checkNum)) {
      inter[inter.indexOf(9999)] = {};
      result = inter;
    }
    result = inter;
  }
  else {
    result = (arr.join().split(',').map(String));
  }
  return result;
}

steamrollArray([1, [2], [3, [[4]]]]);