library(tidyverse)

Anagrama = function(w1, w2) {
  w1 = tolower(w1)
  w2 = tolower(w2)
  if (w1 == w2) {
    return(FALSE)
  } else {
    paste(str_sort(unlist(strsplit(w1, ""))),
    collapse = "") == paste(str_sort(unlist(strsplit(w2, ""))), collapse = "")
  }
}