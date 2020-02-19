package main

import "testing"

func TestSum(t *testing.T) {
    total := Sum(5, 5)
    if total != 10 {
       t.Errorf("Sum was incorrect, got: %d, want: %d.", total, 10)
    }
}

func TestAdd20(t *testing.T) {
    total := Add20(10)
    if total != 30 {
       t.Errorf("Sum was incorrect, got: %d, want: %d.", total, 30)
    }
}

func TestAdd10(t *testing.T) {
    total := Add10(10)
    if total != 20 {
       t.Errorf("Sum was incorrect, got: %d, want: %d.", total, 20)
    }
}

func TestAdd30(t *testing.T) {
    total := Add30(0)
    if total != 30 {
       t.Errorf("Sum was incorrect, got: %d, want: %d.", total, 30)
    }
}
