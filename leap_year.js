var readline = require('readline-sync');

const year = readline.question("What is your year?");
var leap = false

if (year%4==0 || year%100==0 && year%400==0){
    leap = true
    console.log(leap)
}else{
    console.log(leap)
}
