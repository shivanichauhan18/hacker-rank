var readline = require('readline-sync');

function replaceAllDigitsRegExp(input) {
  var space=" ";
  var str="";
  for (var i=0; i<input.length; i++){
    var data=input[i];
    if (data === space){
      str=str+space
      }else if(isNaN(input[i])){
         str=str+input[i]
        }else{
          var g="#"
        str=str+g 
        }
    }return str
  
  

}
const name = readline.question("What is your name?");

console.log(replaceAllDigitsRegExp(name))