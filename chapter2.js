//1.
// let age = parseInt(prompt("Enter your age:"));
// if(age>10 && age<20) {
//     console.log("You are a teenager.");
// }
// else if(age>=20) {
//     console.log("You are an adult.");
// }
// else {
//     console.log("You are a child.");
// }

// prompt return string 
// if you type 10 it will store as "10"
// let a = parseInt(prompt("enter the first element"));
//2.
// let a = parseInt(prompt("enter the first element"));
// let b = parseInt(prompt("enter the second element"));
// let c = 0;
// console.log("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division");
// let choice = parseInt(prompt("enter your choice 1/2/3/4"));
// switch(choice){
//     case 1:
//         c = a + b;
//         console.log("Addition is: " + c);
//         break;
//     case 2:
//         c = a - b;
//         console.log("Subtraction is: " + c);
//         break;
//     case 3:
//         c = a * b;
//         console.log("Multiplication is: " + c);
//         break;
//     case 4:
//         c = a / b;
//         console.log("Division is: " + c);
//         break;
//     default:
//         console.log("Invalid choice");
// }
// console.log(typeof(a),typeof(b),typeof(c),typeof(choice));
//3.
// let n = parseInt(prompt("enter the number"));
// while(n>=0)
// {
//     if(n%2==0 && n%3==0)
//     {
//         console.log(n + " is divisible by both 2 and 3");
//     }
//      n--;
// }

//4.
let n = parseInt(prompt("enter the number"));
// if(n%2==0 ||n%3==0)
// {
//     console.log(n + " is divisible by either 2 or 3");
// }
// else{
//     console.log(n + " is not divisible by either 2 or 3");
// }

// if(n%2==0)
// {
//     console.log(n + " is divisible by 2");
// }
// else if(n%3==0)
// {
//     console.log(n + " is divisible by 3");
// }
// else
// {
//     console.log(n + " is not divisible by either 2 or 3");
// }

//5.
// age = parseInt(prompt("Enter your age:"));
// (age < 0) ? console.log("invalid age"):(age < 18) ? console.log("You cannot drive") : (age > 18 && age < 60)? console.log("you can drive but slowly not to fast") :(age>60)? console.log("you are old please takecare of yourself..."):console.log("stop");