package main

import "testing"

func TestSum(t *testing.T) {
    total := Sum(5, 5)
    if total != 10 {
       t.Errorf("Sum was incorrect, got: %d, want: %d.", total, 10)
    }
}

func TestAdd(t *testing.T) {
    total := Add(10)
    if total != 30 {
       t.Errorf("Sum was incorrect, got: %d, want: %d.", total, 30)
    }
}

func TestAddition(t *testing.T) {
    total := Addition(10)
    if total != 20 {
       t.Errorf("Sum was incorrect, got: %d, want: %d.", total, 20)
    }
}

func TestMerge(t *testing.T) {
    total := Merge(0)
    if total != 30 {
       t.Errorf("Sum was incorrect, got: %d, want: %d.", total, 30)
    }
}
