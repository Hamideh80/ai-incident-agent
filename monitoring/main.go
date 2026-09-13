package main

import (
	"fmt"
	"log"
	"net/http"
)

func main() {
	log.Println("Starting monitoring service...")

	http.HandleFunc("/incident", func(w http.ResponseWriter, r *http.Request) {
		w.WriteHeader(http.StatusOK)
		fmt.Fprintln(w, "incident received")
	})
	log.Println("Monitoring service is running on port 8080")
	log.Fatal(http.ListenAndServe(":8080", nil))
}