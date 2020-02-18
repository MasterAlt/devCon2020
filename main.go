package main

import (
	"fmt"
	"log"
	"net/http"
)

func handler(w http.ResponseWriter, r *http.Request) {
    addition := Sum(5, 5)
	fmt.Fprintln(w, "This is the version 1 of the application \nIn Sum Module the sample value is",addition)
}

func main() {
	http.HandleFunc("/", handler)
	log.Fatal(http.ListenAndServe(":5464", nil))
}

func Sum(x int, y int) int {
    // Add 2 variables
    return x + y
}

func Addition(x int) int {
    // Implicit addition with 10
    var1 := 10
    return x + var1
}

func Add(x int) int {
    // Implicit addition with 20
    var1 := 20
    return x + 20
}

func Merge(x int) int {
    // Implicit addition with 30
    var1 := 30
    return x + 30
}
