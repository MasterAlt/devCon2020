package main

import (
	"fmt"
	"log"
	"net/http"
)

func handler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintln(w, "Welcome to Devcon 2020 \nThis is the 2nd version of the application")
}

func main() {
	http.HandleFunc("/", handler)
	log.Fatal(http.ListenAndServe(":5464", nil))
}

func Sum(x int, y int) int {
    // Add 2 variables
    return x + y
}

func Add10(x int) int {
    // Implicit addition with 10
    var1 := 10
    return x + var1
}

func Add20(x int) int {
    // Implicit addition with 20
    var1 := 20
    return x + var1
}

func Add30(x int) int {
    // Implicit addition with 30
    var1 := 30
    return x + var1
}
