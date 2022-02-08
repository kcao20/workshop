// The Adjective Nouns :: Noakai Aronesty, Kevin Cao
// SoftDev pd2
// K27 -- Basic functions in JavaScript
// 2022-02-04
// --------------------------------------------------


// as a duo...
// pair programming style,
// implement a fact and fib fxn


//Do whatever you think is needed. Think: S I M P L E.   Think: S M A R T

function fact(n) {
  if (n > 2) {
    return fact(n - 1) * n
  } else {
    return n
  }
}

function fib(n) {
  if (n < 2) {
    return n
  } else {
    return fib(n - 1) + fib(n - 2)
  }
}

function gcd(a, b) {
  if (a == b) {
    return a
  } else {
    if (a > b) {
      return gcd((a - b), b)
    } else {
      return gcd(a, (b - a))
    }
  }
}
