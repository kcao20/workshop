// BSGE :: Kevin Cao, Eliza Knapp
// SoftDev pd2
// K29 -- DOMfoolery++
// 2022-02-10
// --------------------------------------------------


//send diagnostic output to console
//(Ctrl-Shift-K in Firefox to reveal console)
console.log("AYO");

var i = "hello";
var j = 20;

//assign an anonymous fxn to a var
var f = function (x) {
  var j = 30;
  return j + x;
};

//instantiate an object
var o = {
  'name': 'Thluffy',
  age: 15,
  items: [10, 20, 30, 40],
  morestuff: { a: 1, b: 'ayo' },
  func: function (x) {
    return x + 30;
  }
};

// add text to end of list
var addItem = function (text) {
  var list = document.getElementById("thelist");
  var newitem = document.createElement("li");
  newitem.innerHTML = text;
  list.appendChild(newitem);
};

// remove item n from list
var removeItem = function (n) {
  var listitems = document.getElementsByTagName('li');
  listitems[n].remove();
};

// turns all li to red, doesn't override existing class with color
var red = function () {
  var items = document.getElementsByTagName("li");
  for (var i = 0; i < items.length; i++) {
    items[i].classList.add('red');
  }
};

// add stripes to list, only visible on li without class -> doesn't override
var stripe = function () {
  var items = document.getElementsByTagName("li");
  for (var i = 0; i < items.length; i++) {
    if (i % 2 == 0) {
      items[i].classList.add('red');
    } else {
      items[i].classList.add('blue');
    }
  }
};

//insert your implementations here for...
// FIB
let fib = function (n) {
  let a = 0, b = 1, temp
  for (let i = 0; i < n; i++) {
    temp = a + b
    a = b, b = temp
  }
  return a
}

// FAC
let fact = function (n) {
  if (n > 2) {
    return fact(n - 1) * n
  } else {
    return n
  }
}

// GCD
let gcd = function (a, b) {
  if (b) {
    return gcd(b, a % b)
  } else {
    return Math.abs(a)
  }
}

const fact_click = function () {
  let n = prompt("Enter n");
  addItem("Factorial of " + n + " is " + fact(n))
}

const fib_click = function () {
  let n = prompt("Enter n");
  addItem("The " + n + "th number of the fib sequence is " + fib(n))
}

let c = document.getElementById("gcd");
c.addEventListener('click', gcd_click)

function gcd_click () {
  console.log("working")
  let x = prompt("Enter the first number");
  let y = prompt("Enter the second number");
  addItem("The greatest common denominator of " + x + " and " + y + " is " + gcd(x, y))
}

let a = document.getElementById("fact");
a.addEventListener('click', fact_click)

let b = document.getElementById("fib");
b.addEventListener('click', fib_click)
