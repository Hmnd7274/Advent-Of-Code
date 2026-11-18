//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
//public static class Tuple<A, B> {
//    public final A i;
//    public final B y;
//
//    public Tuple(A i, B y) {
//        this.i = i;
//        this.y = y;
//    }
//}

public void print(Object str) {
    System.out.println(str);
}

public List<Tuple> getSymbolsList(List<String> puzzleList){
    var ans = new ArrayList<Tuple>();
    int i = 0;
    for (var line : puzzleList) {
        for (int y = 0; y < puzzleList.get(i).length(); y++) {
            if (line.charAt(y) == '*') {
                ans.add(new Tuple(i, y));
            }
        }
        i++;
    }
    return ans;
}

public Tuple findNumber(String line, int index) {
    String ans = String.valueOf(line.charAt(index));
    System.out.println("ENORME BITE" + ans);
    int i = index - 1;
    int min;
    System.out.println("line = " + line + " ;  index = " + index);
    while (i >= 0 && Character.isDigit(line.charAt(i))) { // De l'elem exclu à tout à gauche
        ans = line.charAt(i) + ans;
        System.out.println(ans);
        i--;
        System.out.println("i = " + i);
    }
    min = i + 1;
    i = index + 1;
    while (i < line.length() && Character.isDigit(line.charAt(i))) { // De l'elem exclu à tout à droite
        ans += line.charAt(i);
        i++;
    }
    System.out.println("findNumber : " + ans + " ; start index : " + min);
    return new Tuple(min, Integer.parseInt(ans));
}

public List<List<Integer>> getNumbersList(List<String> puzzleInput){
    List<List<Integer>> ans = new ArrayList<>();
    
    for (var tuple : getSymbolsList(puzzleInput)) {
        int puzzleIndex = tuple.i;
        int lineIndex = tuple.y;
        System.out.println("puzzleIndex = " + puzzleIndex + " ; lineIndex = " + lineIndex + '\n');
        
        List<Tuple> tempNumbers = new ArrayList<>();
        for (var relativePos : getRelativePositions()) {
            int newPuzzleIndex = puzzleIndex + relativePos.i;
            int newLineIndex = lineIndex + relativePos.y;
            ;
//            String test = puzzleInput.get(newPuzzleIndex);
//            String test8 = String.valueOf(puzzleInput.get(newPuzzleIndex).charAt(newLineIndex));
//            Character test2 = test.charAt(newLineIndex);
//            boolean test3 = newPuzzleIndex >= 0;
//            boolean test4 = newLineIndex >= 0;
//            boolean test5 = Character.isDigit(puzzleInput.get(newPuzzleIndex).charAt(newLineIndex));

            
            if (newPuzzleIndex < 0 || lineIndex < 0) continue;
            
            if (!Character.isDigit(puzzleInput.get(newPuzzleIndex).charAt(newLineIndex))) continue;
            
            if (tempNumbers.contains(findNumber(puzzleInput.get(newPuzzleIndex), newLineIndex))) continue;
            
            tempNumbers.add(findNumber(puzzleInput.get(newPuzzleIndex), newLineIndex));
            System.out.println(findNumber(puzzleInput.get(newPuzzleIndex), newLineIndex));
        }

        if (tempNumbers.size() >= 2) ans.add(List.of(tempNumbers.getFirst().y, tempNumbers.getLast().y));

        System.out.println("getNumberList = " + tempNumbers.size());
        
//        // Above
//        if (puzzleIndex > 0) {
//            for (int upperLineIndex = -1; upperLineIndex < 2; upperLineIndex++) {
//                if (lineIndex + upperLineIndex >= 0) {
//                    
//                    char upperElement = puzzleList.get(puzzleIndex - 1).charAt(lineIndex + upperLineIndex);
//                    
//                    if (Character.isDigit(upperElement)) {
//                        ans.add(findNumber(puzzleList.get(puzzleIndex - 1), lineIndex + upperLineIndex));
//                    }
//                }
//            }
//        if (puzzleIndex > 1)break;
        System.out.println("\n\n");
    }
    return ans;
//    for (var line : puzzleList) {
//        for (int y = 0; y < puzzleList.get(i).length(); y++) {
//            if ()
//        }
//        i++;
//    }
}

public List<Tuple> getRelativePositions(){
    var ans = new ArrayList<Tuple>();
    for (int i = -1; i < 2; i++) {
        for (int y = -1; y < 2; y++) {
            ans.add(new Tuple(i, y));
        }
    }
    return ans;
}

void main() {
    List<String> puzzleInput = new ArrayList<>();
    try (BufferedReader br = new BufferedReader(new FileReader("puzzle.txt"))) {
        String line;
        while ((line = br.readLine()) != null) {
            puzzleInput.add(line);
        }
        for (var lines : puzzleInput) {
            System.out.println(lines);
        }
            System.out.println(" ");
        
        
        
//        for (var el : getSymbolsList(puzzleInput)) {
//            System.out.println(el.i + " " + el.y);
//        }

        System.out.println("main" + " bite");
        var list = getNumbersList(puzzleInput);
        System.out.println("main" + list);
        int answer = 0;
        for (var el : list) {
            int x = 1;
            for (var val : el) {
                x *= val;
            }
            answer += x;
        }
        print(answer);
        
    } catch (IOException e) {
        e.printStackTrace();
    }
}

public record Tuple(int i, int y){}