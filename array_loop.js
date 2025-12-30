let arr1 = [1,93,5,6,88];
for(i = 0; i < arr1.length ; i++)
{
    // console.log(arr1[i],"\n");
    const value = arr1[i];
    console.log(value);
}
const new_arr = (arr) =>
{
  const element = arr.map((a)=>(a**2))
  return element;
}
console.log(new_arr(arr1));

const key = arr1.map(a => a**5);
console.log(key);

const key1 = arr1.reduce((result,value)=> result + value);
console.log(key1)

obj = {
    'harry':90,
    'laksh':88,
    'nimish':87
}
const keyarr = Array.from(Object.values(obj), value => value >88);
console.log(keyarr);
let reult = []
arr1.forEach((value, index,arr)=>
{
 if(value>88)
 {
    reult.push(value)
 }
});
console.log(reult);