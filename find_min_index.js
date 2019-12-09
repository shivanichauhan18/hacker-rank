function arrayMinimumIndex(inputArray) {
    var min_index=0
    var i=0
    var min = inputArray[i]
    while(i<inputArray.length){    
            if(min>inputArray[i]){
            min=inputArray[i];
            min_index=i
            
        }i++;       
    }return min_index

}
var inputArray = [19, 32, 11, 23]
console.log(arrayMinimumIndex(inputArray))
