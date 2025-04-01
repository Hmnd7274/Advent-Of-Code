open System
open System.IO

let lines =
    File.ReadLines "puzzleInput.txt"
printfn "toto: %A" lines

let mutable list1 = []
let mutable list2 = []
for line in lines do
    let lin = line.Split(" ", StringSplitOptions.RemoveEmptyEntries)
    list1 <- List.append list1 [ lin[0] ]
    list2 <- List.append list2 [ lin[1] ]
let mutable smscore = 0

for e in list1 do
    let x =
        list2
        |> List.filter (fun x -> x = e) 
        |> List.length

    smscore <- smscore + (int e * x)
printfn "%A" smscore