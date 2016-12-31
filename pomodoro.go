package main   

import (
    "fmt"
    "time"
    "math/rand"
  )

// run in terminal: $ go run pomodoro.go 
func main() {
  // TODO add a way to dynamically populate array
  exercises := [10]string {
    "Wall sits",
    "Sit ups",
    "Push ups",
    "Hand Stand",
    "Air squats",
    "Plank",
    "Supine twist",
    "Pigeon pose",
    "Runners stretch",
    "Forward hang",
  }

  // TODO integrate start button (web or native app)
  on := true
  // TODO add support for changing work/break
  // time periods
  var work time.Duration
  var br time.Duration
  work = 25
  br = 5

  // swap between work and breaks
  // print excercise after work period
  for on == true {
    // TODO print time
    timer := time.NewTimer(time.Minute * work)
    <- timer.C
    println("Work Time\n")

    timer = time.NewTimer(time.Minute * br)
    <- timer.C
    n := rand.Intn(10)
    // bell sound
    fmt.Print("\x07")
    println("Break\n")
    fmt.Printf("%v\n", exercises[n])
  }
}