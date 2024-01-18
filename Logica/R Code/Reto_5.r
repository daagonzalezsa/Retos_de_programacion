library("tidyverse")

Area_polygon = function(Figure, L1, L2) {
    if (!is.character(Figure)) {
        print("Figure debe ser String")
    } else if (!(tolower(Figure) %in% c("square", "rectangle", "triangle"))) {
       print("Figure debe ser Square, Rectangle o Triangle")
    } else if (tolower(Figure) == "square") {
       print(paste("El área del cuadrado es ", L1^2, sep = ""))
    } else if (tolower(Figure) == "rectangle") {
       print(paste("El área del Rectangulo es ", L1*L2, sep = ""))
    } else {
       print(paste("El área del Triangulo es ", L1*L2/2, sep = ""))
    }
}

Area_polygon("Triangle", 2, 2)
