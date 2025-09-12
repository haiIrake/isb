import java.io.FileWriter;
import java.io.IOException;
import java.util.Random;

public class RandomGenerator {

    /**
    * Generates a random binary sequence of 128 bit
    * 
    * @return Generated binary sequence as a string
    */
    public static String generate_seq() {
        Random rand = new Random();
        StringBuilder sequence = new StringBuilder();
        
        for (int i = 0; i < 128; ++i) {
            sequence.append(rand.nextInt(2));
        }
        
        return sequence.toString();
    }
    
    /**
    * Saves a sequence to the specified file
    * 
    * @param filename Path to the file to save
    * @param sequence Sequence to save
    */
    public static void save_seq(String filename, String sequence) {
        try (FileWriter writer = new FileWriter(filename)) {
            writer.write(sequence + "\n");
        }
        catch (IOException e) {
            System.err.println(e.getMessage());
        }
    }
    
    /**
    * Main method of the program
    * 
    * @param args Command line arguments (not used)
    */
    public static void main(String[] args) {
        String sequence = generate_seq();
        save_seq("sequence_java.txt", sequence);
    }
}
