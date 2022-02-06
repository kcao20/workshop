#lang racket
(define fact
  (lambda(n)
    (if (> n 2)
        (* (fact(- n 1)) n)
        n
     )
   )
)

(define fib
  (lambda(n)
    (if (< n 2)
        n
        (+ (fib(- n 1)) (fib (- n 2)))
    )
  )
)