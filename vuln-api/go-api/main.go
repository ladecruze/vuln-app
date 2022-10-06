package main

import (
    "fmt"
    "log"
    "net/http"
    "database/sql"
    _ "github.com/go-sql-driver/mysql"
)

func main() {

    type Todo struct {
        ID   int    `json:"id"`
        Todo string `json:"todo"`
        User string `json:"user"`
        Date string `json:"date"`
    }

    db, err := sql.Open("mysql", "root:root@tcp(127.0.0.1:3306)/vulnapi")

    if err != nil {
        panic(err.Error())
    }

    defer db.Close()

    http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
        fmt.Fprintf(w, "<h1> Welcome to the Practical DevSecOps Vulnerable API</h1>")
    })

    http.HandleFunc("/api/v1/resources/todos/", func(w http.ResponseWriter, r *http.Request) {
        // Execute the query
        results, err := db.Query("SELECT * FROM todos where id=3")

        if err != nil {
            panic(err.Error()) // proper error handling instead of panic in your app
        }

        for results.Next() {
            var todo Todo
            // for each row, scan the result into our todo composite object
            err = results.Scan(&todo.ID, &todo.Todo, &todo.User, &todo.Date)
            if err != nil {
                panic(err.Error()) // proper error handling instead of panic in your app
            }
            log.Printf(todo.Todo)
        }
    })



    log.Fatal(http.ListenAndServe(":8081", nil))

}

