let arr = [1,2,3,4,5];
console.log(arr.length);
console.log(arr);
console.log(arr[0]);
console.log(arr[2]);
//push,pop
arr.pop();
console.log(arr);
arr.push(10);
arr.push(10);
// shift -> starting ,does not take any argument
//unshift -> starting , it take 1or more argument
// push unshift are bhai bhai ,it take 1or more argument
// pop shift are bhai bhai, does not take any argument
arr.shift();
console.log(arr);
arr.unshift(15,20);
console.log(arr);
// arr.join("-");
// console.log(arr.join("-"));
// console.log(arr.toString());
// let arr2 = [5,10,15,20,25];
// console.log(arr.concat(arr2));
//splice -> we can and remove element using splice 
// 1. for remove -> giving index position next how elements you want to remove
// 2. for add -> giving index position where you want to start , then how elements you want to remove,giving values that you want add 
arr.splice(1,3)
console.log(arr);
console.log(arr.slice(0,2));
let arr1 = [10,1,2,3,4,5];
arr1.slice(1,4);
console.log(arr1.slice(1,4));
let arr3 = [70,23,1,90,5,8];
//compare function
arr3.sort((a,b) => a - b);
console.log(arr3);
let arr4 = ['jasmin','roy','laksh','arahan','neinesh']
arr4.sort();
console.log(arr4);
arr.sort((a,b)=>a -b);
console.log(arr);
let add = (a,b)=>
{
    let result = a-b;
    return result;
}
console.log(add(50,20));
arr3.reverse();
console.log(arr3)
