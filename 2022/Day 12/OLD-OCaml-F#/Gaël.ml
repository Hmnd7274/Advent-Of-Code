
let map f = function
    | Some x -> Some (f x)
    | None -> None

type shape =
    | Circle of int
    | Square of int
    | Rect of int * int

let ma_shape = Rect (42, 69)
let area shape =
    match shape with
    | Circle radius -> ()
    | Square cote -> ()
    | Rect (l, l''''''') -> ()

let toto (a: (int, string) result) =
    match a with
    | Ok valeur -> ()
    | Error error -> 