open Vector
type ('key, 'prio) t = {
  priorities : 'prio Vector.t;
  keys : 'key Vector.t;
  mapping : ('key, int) Hashtbl.t
}

let length q = Vector.length q.priorities

let create () =
  {priorities = Vector.create ();
   keys = Vector.create ();
   mapping = Hashtbl.create 10}

let mem q x =
  Hashtbl.mem q.mapping x

let swap t i j =
  let tmp = Vector.get t i in
  Vector.set t i (Vector.get t j);
  Vector.set t j tmp

let full_swap q i j =
  swap q.keys i j;
  swap q.priorities i j;
  Hashtbl.replace q.mapping (Vector.get q.keys i) i;
  Hashtbl.replace q.mapping (Vector.get q.keys j) j

let get_min q =
  if length q = 0 then None
  else Some (Vector.get q.keys 0, Vector.get q.priorities 0)

let left i = 2 * i + 1

let right i = 2 * i + 2

let parent i = (i - 1) / 2

let rec sift_up q i =
  let j = parent i in
  if i > 0 && Vector.get q.priorities i < Vector.get q.priorities j then
    begin
      full_swap q i j;
      sift_up q j
    end

let insert q (x, prio) =
  Vector.push q.keys x;
  Vector.push q.priorities prio;
  Hashtbl.add q.mapping x (length q - 1);
  sift_up q (length q - 1)

let rec sift_down q i =
  let prio j = Vector.get q.priorities j in
  let smallest = ref i in
  if left i < length q && prio (left i) < prio i then
    smallest := left i;
  if right i < length q && prio (right i) < prio !smallest then
    smallest := right i;
  if !smallest <> i then
    begin
      full_swap q i !smallest;
      sift_down q !smallest
    end

let extract_min q =
  if length q = 0 then
    None
  else
    begin
      let key = Vector.get q.keys 0 in
      let prio = Vector.get q.priorities 0 in
      full_swap q 0 (length q - 1);
      Hashtbl.remove q.mapping key;
      ignore (Vector.pop q.priorities);
      ignore (Vector.pop q.keys);
      sift_down q 0;
      Some (key, prio)
    end

let decrease_priority q (x, prio) =
  let i = Hashtbl.find q.mapping x in
  assert (prio <= Vector.get q.priorities i);
  Vector.set q.priorities i prio;
  sift_up q i

let insert_or_decrease q (x, prio) =
  if mem q x then decrease_priority q (x, prio)
  else insert q (x, prio)






let input = "2022/Day 12/ex.txt" |> open_in |> In_channel.input_lines |> Array.of_list
let length = Array.length input
let wide = String.length input.(0)
let startHeight = Char.code 'a'
let finishHeight = Char.code 'z'
let height c =
  match c with
  |'S' -> startHeight
  |'E' -> finishHeight
  |_ -> Char.code c
let findAvailable (i,j) =
  let currHeight = height input.(i).[j] in
  let answer = ref [] in
  if j > 0 then (
    (* print_newline (); print_string "left: "; print_int (i); print_string ","; print_int (j-1); print_newline (); *)
    let left = height input.(i).[j-1] in
    if currHeight - left |> abs < 2 then 
      answer := (i,j-1)::!answer;
  );
  if i > 0 then (
    (* print_newline (); print_string "up: "; print_int (i-1); print_string ","; print_int (j); print_newline (); *)
    let up = height input.(i-1).[j] in
    if currHeight - up |> abs < 2 then 
      answer := (i-1,j)::!answer;
  );
  if j < wide - 1 then (
    let right = height input.(i).[j+1] in
    (* print_newline (); print_string "right: "; print_int (i); print_string ","; print_int (j+1); print_newline (); *)
    if currHeight - right |> abs < 2 then 
      answer := (i,j+1)::!answer
  );
  print_newline (); print_string "down: "; print_int (i);
  if i < length - 1 then (
    (* print_newline (); print_string "down: "; print_int (i+1); print_string ","; print_int (j); print_newline (); *)
    let down = height input.(i+1).[j] in
    if currHeight - down |> abs < 2 then 
      answer := (i+1,j)::!answer;
  );
  List.sort (fun (x,y) (w,z) -> height input.(x).[y] - height input.(w).[z]) !answer

let calc start =
  let vue = Array.make_matrix length wide false in
  let file = create () in
  Queue.add start file;
  let rec travel steps =
    let (i,j) = Queue.pop file in
    print_newline (); print_int (i); print_string ","; print_int (j); print_newline ();
    if height input.(i).[j] = finishHeight then (
      print_newline (); print_int steps; print_string " JGAGNE";
    )
    else ( 
    List.iter (fun (x,y) -> if not vue.(x).(y) then (Queue.add (x,y) file; vue.(x).(y) <- true)) (findAvailable (i,j));
    if not (Queue.is_empty file) then
      travel (steps+1)
    )
  in
  travel 0



let _ =
  let start = ref (-1,-1) in
  Array.iteri (fun i x -> String.iteri (fun j c -> if c = 'S' then start := (i,j)) x) input;
  print_newline (); print_int (fst !start); print_string ","; print_int (snd !start); print_newline ();
  calc !start

let _ = findAvailable (0,0)
let _ = height 'E'
let _ = startHeight - 97 |> abs