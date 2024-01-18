Prime = unlist(list())
for (i in 1:100) {
    Divisors = unlist(list())
  for (j in 1:100) {
    if (i>=j) {
        if (i %% j == 0) {
            Divisors = append(Divisors, j)
        }
    }
  }
  if (length(Divisors) <= 2) {
    Prime = append(Prime, i)
  }
}

Prime
