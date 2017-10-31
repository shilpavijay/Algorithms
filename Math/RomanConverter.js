function prodAndRem(div,divisor) {
  prod = Math.floor(div/divisor)
  rem = div%divisor
  return [prod,rem] 
}

function convertToRoman(num) {
  RomanDict = {1000: 'M', 500: 'D',100: 'C',50: 'L',10: 'X',5: 'V',1: 'I'};
  Dec = [1000,500,100,50,10,5,1];
  Rom = ['M','D','C','L','X','V','I'];
  decArr = [];
  roman = [];
  divisor = 1000;
  //Construct the num Array:
  while (num > 0 && divisor > 0){
    par = prodAndRem(num,divisor);
    console.log(par);
    decArr.push(par[0]*divisor);
    num = par[1];
    divisor/=10;
    }
    
  console.log(decArr)
  
  for(i=0;i<decArr.length;i++){
    p = Math.pow(10,(decArr.length - i-1));
    console.log(p);
    par = prodAndRem(decArr[i],p);
    console.log(par);
    if (par[0] < 4 && par[0] > 0){
      roman.push(RomanDict[p]);
        while(par[0] > 1){
          roman.push(RomanDict[p]);
          par[0]--;
        }
    }
    else if(par[0] !== 0 && (p[0] == 4  || p[0] == 5)) {
      console.log('mid else')
      actnum = p * par[0];
      num = actnum;
      while (Dec.indexOf(num) < 0){
        num += 1;
      }
      roman.push(RomanDict[num - actnum]);
      idx = Dec.indexOf(num);
      console.log(Rom[idx]);
      roman.push(Rom[idx]);
    }
    else if(par[0] !== 0) {
      console.log('last else')
      actnum = p * par[0];
      num = actnum;
      while (Dec.indexOf(num) < 0){
        num -= 1;
      }
      idx = Dec.indexOf(num);
      console.log(idx)
      console.log(Rom[idx]);
      roman.push(Rom[idx]);
      roman.push(RomanDict[actnum - num]);
     
    }
  }  
  return roman.join('');
}

convertToRoman(4);
