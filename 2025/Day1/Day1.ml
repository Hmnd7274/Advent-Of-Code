(* let input = "ex.txt" |> open_in |> In_channel.input_lines *)
let input = "ex.txt" |> open_in |> In_channel.input_lines |> Array.of_list

(* let x = "R23" *)
let nb str = String.sub str 1 (String.length str -1)
(* let leftOrRight str = if str.[0] = 'R' *)

let rotate arr =
  let x = ref 50 in
  let ans = ref 0 in
  for i=0 to Array.length arr -1 do
    let el = arr.(i) in
    if String.contains el 'R' then
      x := !x + int_of_string (nb el);
    if String.contains el 'L' then
      x := !x - int_of_string (nb el);
    if !x > 100 then
      x := !x - 100;
    if !x < 0 then
      x := !x + 100;
    if !x = 0 then
      ans := !ans + 1
  done;
  !x

print_int (rotate input)



  (* match list with
  |[t] ->
    if t.[0] = 'R' then
      if x + int_of_string (nb t) > 100 :
        x + int_of_string (nb t) -100
    else if t.[0] = 'L' then
      if x - int_of_string (nb t) < 0 :
        x + int_of_string (nb t) -100
      x - int_of_string (nb t) *)
