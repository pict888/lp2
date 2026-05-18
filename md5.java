import java.security.MessageDigest;
import java.util.Scanner;

class Block {

    int num;
    long nonce = 0;

    String data;
    String prevHash;
    String hash;

    // Constructor
    Block(int num, String data, String prevHash, int difficulty) {
        this.num = num;
        this.data = data;
        this.prevHash = prevHash;
        mine(difficulty);
    }

    // Generate MD5 Hash
    String calculateHash() {

        try {

            String input = num + data + prevHash + nonce;
            MessageDigest md = MessageDigest.getInstance("MD5");
            byte[] hashBytes = md.digest(input.getBytes());
            StringBuilder sb = new StringBuilder();
            for(byte b : hashBytes) {
                sb.append(String.format("%02x", b));
            }
            return sb.toString();
        } catch(Exception e) {
            return "";
        }
    }

    // Mining
    void mine(int difficulty) {
    // String target = "";

    // for(int i = 0; i < difficulty; i++) {
    //     target += "0";
    // }
        String target = "0".repeat(difficulty);
        while(true) {
            hash = calculateHash();
            if(hash.startsWith(target)) {
                System.out.println("\nBlock Mined!");
                System.out.println("Nonce : " + nonce);
                System.out.println("Hash  : " + hash);
                break;
            }
            nonce++;
        }
    }

    // Display Block
    void display() {
        System.out.println("\nBlock Number : " + num);
        System.out.println("Data         : " + data);
        System.out.println("Previous Hash: " + prevHash);
        System.out.println("Nonce        : " + nonce);
        System.out.println("Hash         : " + hash);
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of blocks: ");
        int n = sc.nextInt();

        System.out.print("Enter difficulty: ");
        int difficulty = sc.nextInt();
        sc.nextLine();

        Block[] blockchain = new Block[n];
        String prevHash = "00000000000000000000000000000000";

        for(int i = 0; i < n; i++) {
            System.out.print("\nEnter data for Block " + (i+1) + ": ");
            String data = sc.nextLine();
            blockchain[i] = new Block(i + 1, data, prevHash, difficulty);
            prevHash = blockchain[i].hash;
        }

        System.out.println("\n===== BLOCKCHAIN =====");
        for(Block b : blockchain) {
            b.display();
        }

        sc.close();
    }
}
