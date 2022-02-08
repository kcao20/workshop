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

(define gcd
  (lambda(a b)
    (if (= a b)
        a
        (if (> a b)
            (gcd (- a b) b)
            (gcd a (- b a))
        )
    )
  )
)
