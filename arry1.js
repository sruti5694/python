let array = [10,20,30,40,50,9]
const new_Arr = array.reduce((result,cvalue ) => result + cvalue);
console.log(new_Arr);
array.forEach((element, index, array)=>{
    console.log(`index :${index} value:${element}`)
});
let array1 = [3,5,7,9,11];
const new_Arr1 = array1.map((a) => {
    let result = 1;
    for(let i = 1;i <= a;i++)
    {
        result *=i;
    }
   return result;
});
 console.log(new_Arr1);
const new_Arr2 = array1.filter(a => a>7);
console.log(new_Arr2);

const new_Arr3 = ((a)=>{
 if (a%2==0)
 {
    return true;
 }
 else
 {
    return false;
 }
});
console.log(array.filter(new_Arr3)) // keeps those valuse which return true

const new_Arr4 = a =>(a >= 5);
console.log(array1.filter(new_Arr4));