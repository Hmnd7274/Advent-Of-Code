(* let rec goIn list n = match n with | 0 -> List.hd list | t -> goIn (List.tl list) (t-1) *)
(* let printL list = for i = 0 to (List.length list - 1) do
    print_string (goIn list i); print_newline ()
done *)

(* let () = printL input *)

(* let transformToArray list : string array = let newArray = Array.make (List.length input) "" in
    let rec recTransform laListe index = match laListe with
        | [] -> newArray
        | line::w -> newArray.(index) <- line ; recTransform w (index+1) in
    recTransform list 0 *)

    (* Array.find_mapi (fun lineIndex line ->
        let index_of_S = String.index_opt line 'S' in
        match index_of_S with
        | None -> None
        | Some idx -> Some (lineIndex, idx)
        (* |> Option.map (fun idx -> lineIndex, idx) *)
    ) *)
    (* let ans = ref 'r' in
    for x = 0 to Array.length inputArr -1 do
        let currentLine = inputArr.(x) in
        for y = 0 to String.length inputArr.(x) -1 do
            print_char (String.get currentLine y);
            if (String.get currentLine y) = 'S' then
                String.get currentLine y
        done
    done *)


(* Array.iter (fun a -> print_int (int_of_float (distance a ePos)); print_newline ()) (getClosestArr (0, 0)) *)

let input = "ex.txt" |> open_in |> In_channel.input_lines |> Array.of_list
let printArr = Array.iter print_string

let findChar arr char =
    arr |> Array.find_mapi (fun lineIndex element -> 
        let w = String.index_opt element char in match w with
        | None -> None
        | Some value -> Some (lineIndex, value)
        )

let sPos = Option.get (findChar input 'S')
let xSPos, ySPos = sPos
(* let ePos = (10, 10) *)
let ePos = Option.get (findChar input 'E')

let xEPos, yEPos = ePos
let relativePos = [|(-1, 0); (0, -1); (1, 0); (0, 1)|]

let filterArr f arr = let newList = ref [] in for i = 0 to Array.length arr - 1 do print_string (string_of_int i) ; print_newline () ; if f arr.(i) <= 1 then newList := arr.(i)::!newList done; Array.of_list !newList

let getHeight (x, y) = int_of_char input.(x).[y]

let printPos (a, b) = print_int a; print_string " ; "; print_int b; print_newline ()

let distance (x, y) (w, z) = (sqrt ((float_of_int (abs (x - w)) ** 2.) +. (float_of_int (abs (y - z)) ** 2.)))

let compareDistances firstEl secondEl = int_of_float ((distance firstEl ePos) -. (distance secondEl ePos))

let heightDiff firstEl secondEl = (getHeight secondEl) - (getHeight firstEl) 

let getClosestArr (x, y) = let newPoses = Array.map (fun el -> let relx, rely = el in (relx + x, rely + y)) relativePos in Array.sort compareDistances newPoses; newPoses

let rec findPath (x, y) count =
    let closestArr = filterArr (heightDiff (x, y)) (getClosestArr (x, y)) in
    match (x, y) with
    | (w, z) when (w, z) = ePos -> print_int count; print_newline ()
    | (w, z) -> Array.iter (fun el -> findPath el (count+1)) closestArr

findPath sPos 0